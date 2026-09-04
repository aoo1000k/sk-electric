from flask import Flask, render_template, request

app = Flask(__name__)

# เพิ่มรายการสินค้าทั้งหมดรวมถึงเบรกเกอร์ตราช้าง (ดึงชื่อรูปตามในโฟลเดอร์ static)
electrical_products = [
    {"name": "สายไฟ IEC01 (THW) 1x1.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Wire 1x1.5 sq.mm. (100m)", "price": "478", "img": "/static/thw15.jpg", "category": "wire"},
    {"name": "สายไฟ IEC01 (THW) 1x2.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Wire 1x2.5 sq.mm. (100m)", "price": "850", "img": "/static/thw25.jpg", "category": "wire"},
    {"name": "สายไฟ VAF 2x1.5 sq.mm. (100 เมตร)", "name_en": "VAF Wire 2x1.5 sq.mm. (100m)", "price": "1,200", "img": "/static/vaf15.jpg", "category": "wire"},
    {"name": "สายไฟ VAF 2x2.5 sq.mm. (100 เมตร)", "name_en": "VAF Wire 2x2.5 sq.mm. (100m)", "price": "1,800", "img": "/static/vaf25.jpg", "category": "wire"},
    {"name": "สายไฟ NYY 1x1.5 sq.mm. (100 เมตร)", "name_en": "NYY Wire 1x1.5 sq.mm. (100m)", "price": "1,450", "img": "/static/nyy15.jpg", "category": "wire"},
    {"name": "สายไฟ NYY 4x10 sq.mm. (ตัดเมตร)", "name_en": "NYY Wire 4x10 sq.mm. (Per Meter)", "price": "280 / เมตร", "img": "/static/nyy410.jpg", "category": "wire"},
    {"name": "ท่อร้อยสายไฟ PVC ขนาด 1/2 นิ้ว (สีเหลือง)", "name_en": "PVC Conduit 1/2 Inch (Yellow)", "price": "45", "img": "/static/pvc12.jpg", "category": "pipe"},
    {"name": "เบรกเกอร์ 2P 20A (ช้าง/Panasonic)", "name_en": "Circuit Breaker 2P 20A", "price": "120", "img": "/static/breaker20.jpg", "category": "breaker"},
    {"name": "เซอร์กิตเบรกเกอร์ ตราช้าง (CHANG) ขนาด 10A-30A", "name_en": "CHANG Safety Breaker 10A-30A", "price": "120", "img": "/static/chang_breaker.jpg.heif", "category": "breaker"}
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
