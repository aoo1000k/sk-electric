from flask import Flask, render_template, request

app = Flask(__name__)

# รายการสินค้า (รองรับแบบมีตัวเลือกย่อย variations)
electrical_products = [
    {
        "name": "ตู้คอนซูเมอร์ 4 ช่อง ยี่ห้อ BF", 
        "name_en": "BF Consumer Unit 4 Ways", 
        "category": "consumer_unit",
        "img": "/static/bf_consumer4.jpg",
        "has_variations": True,
        "variations": [
            {"name": "แบบธรรมดา (ไม่กันดูด)", "price": "480"},
            {"name": "แบบกันดูด (RCBO)", "price": "590"}
        ]
    },
    {
        "name": "แค้มใบเมทัลลิค", 
        "name_en": "Metallic Pipe Clip", 
        "category": "pipe",
        "img": "/static/metallic_clamp.jpg",
        "has_variations": True,
        "variations": [
            {"name": "แบบ 1 สกรู", "price": "45"},
            {"name": "แบบ 2 สกรู", "price": "98"}
        ]
    },
    # สินค้าแบบปกติที่มีราคาเดียว
    {"name": "สาย THW #1.5 ยี่ห้อ ICON", "name_en": "ICON THW Wire #1.5", "price": "350", "img": "/static/icon_thw15.jpg", "category": "wire", "has_variations": False},
    {"name": "สวิทช์ ยี่ห้อ zeberg", "name_en": "Zeberg Switch", "price": "35", "img": "/static/zeberg_switch.jpg", "category": "switch_outlet", "has_variations": False},
    {"name": "ปลั๊กเดี่ยว ยี่ห้อ zeberg", "name_en": "Zeberg Single Receptacle", "price": "40", "img": "/static/zeberg_single_outlet.jpg", "category": "switch_outlet", "has_variations": False},
    {"name": "ปลั๊กกราวด์เดี่ยว ยี่ห้อ zeberg", "name_en": "Zeberg Single Grounded Outlet", "price": "55", "img": "/static/zeberg_ground_single.jpg", "category": "switch_outlet", "has_variations": False},
    {"name": "ปลั๊กกราวด์คู่ยี่ห้อ Zeberg", "name_en": "Zeberg Duplex Grounded Outlet", "price": "85", "img": "/static/zeberg_ground_คู่.jpg", "category": "switch_outlet", "has_variations": False},
    {"name": "สายไฟ IEC01 (THW) 1x1.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Wire 1x1.5 sq.mm. (100m)", "price": "478", "img": "/static/thw15.jpg", "category": "wire", "has_variations": False},
    {"name": "สายไฟ IEC01 (THW) 1x2.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Wire 1x2.5 sq.mm. (100m)", "price": "850", "img": "/static/thw25.jpg", "category": "wire", "has_variations": False},
    {"name": "สายไฟ VAF 2x1.5 sq.mm. (100 เมตร)", "name_en": "VAF Wire 2x1.5 sq.mm. (100m)", "price": "1,200", "img": "/static/vaf15.jpg", "category": "wire", "has_variations": False},
    {"name": "สายไฟ VAF 2x2.5 sq.mm. (100 เมตร)", "name_en": "VAF Wire 2x2.5 sq.mm. (100m)", "price": "1,800", "img": "/static/vaf25.jpg", "category": "wire", "has_variations": False},
    {"name": "สายไฟ NYY 1x1.5 sq.mm. (100 เมตร)", "name_en": "NYY Wire 1x1.5 sq.mm. (100m)", "price": "1,450", "img": "/static/nyy15.jpg", "category": "wire", "has_variations": False},
    {"name": "สายไฟ NYY 4x10 sq.mm. (ตัดเมตร)", "name_en": "NYY Wire 4x10 sq.mm. (Per Meter)", "price": "280 / เมตร", "img": "/static/nyy410.jpg", "category": "wire", "has_variations": False},
    {"name": "ท่อร้อยสายไฟ PVC ขนาด 1/2 นิ้ว (สีเหลือง)", "name_en": "PVC Conduit 1/2 Inch (Yellow)", "price": "45", "img": "/static/pvc12.jpg", "category": "pipe", "has_variations": False},
    {"name": "เซอร์กิตเบรกเกอร์ ตราช้าง (CHANG) ขนาด 10A-30A", "name_en": "CHANG Safety Breaker 10A-30A", "price": "ถถ", "img": "/static/chang.jpg", "category": "breaker", "has_variations": False}
]

@app.route('/')
def home():
    lang = request.args.get('lang', 'th')
    search_query = request.args.get('search', '').strip().lower()
    selected_category = request.args.get('cat', 'all')
    
    if selected_category == 'all':
        filtered_products = electrical_products
    else:
        filtered_products = [p for p in electrical_products if p['category'] == selected_category]
        
    if search_query:
        filtered_products = [
            p for p in filtered_products 
            if search_query in p['name'].lower() or search_query in p['name_en'].lower()
        ]
        
    return render_template('index.html', products=filtered_products, current_cat=selected_category, current_lang=lang, search_query=search_query, shop_name="ร้านไฟฟ้าแสงคูณ")

@app.route('/product/<int:index>')
def product_detail(index):
    if 0 <= index < len(electrical_products):
        current_product = electrical_products[index]
        return render_template('product.html', product=current_product)
    else:
        return "ไม่พบสินค้าที่คุณต้องการ", 404

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
