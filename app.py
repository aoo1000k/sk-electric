from flask import Flask, render_template, request

app = Flask(__name__)

electrical_products = [
    {"name_th": "สายไฟ IEC01 (THW) 1x1.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Cable 1x1.5 sq.mm. (100m)", "price": "478", "img": "/static/thw15.jpg", "category": "wire"},
    {"name_th": "สายไฟ IEC01 (THW) 1x2.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Cable 1x2.5 sq.mm. (100m)", "price": "850", "img": "https://placehold.co", "category": "wire"},
    {"name_th": "สายไฟ VAF 2x1.5 sq.mm. (100 เมตร)", "name_en": "VAF Cable 2x1.5 sq.mm. (100m)", "price": "1,200", "img": "https://placehold.co", "category": "wire"},
    {"name_th": "สายไฟ VAF 2x2.5 sq.mm. (100 เมตร)", "name_en": "VAF Cable 2x2.5 sq.mm. (100m)", "price": "1,800", "img": "https://placehold.co", "category": "wire"},
    {"name_th": "สายไฟ NYY 1x1.5 sq.mm. (100 เมตร)", "name_en": "NYY Cable 1x1.5 sq.mm. (100m)", "price": "1,450", "img": "https://placehold.co", "category": "wire"},
    {"name_th": "สายไฟ NYY 4x10 sq.mm. (ตัดเมตร)", "name_en": "NYY Cable 4x10 sq.mm. (per meter)", "price": "280 / เมตร", "img": "https://placehold.co", "category": "wire"},
    {"name_th": "ท่อร้อยสายไฟ PVC ขนาด 1/2 นิ้ว (สีเหลือง)", "name_en": "PVC Conduit 1/2 inch (Yellow)", "price": "45", "img": "https://placehold.co", "category": "pipe"},
    {"name_th": "เบรกเกอร์ 2P 20A (ช้าง/Panasonic)", "price": "120", "name_en": "Circuit Breaker 2P 20A", "img": "https://placehold.co", "category": "breaker"}
]

@app.route('/')
def home():
    # 🌐 ระบบภาษาเริ่มต้น (ถ้าลูกค้าไม่เลือกจะเป็นภาษาไทย 'th')
    lang = request.args.get('lang', 'th')
    
    # 🔍 ระบบรับค่าจากช่องค้นหา
    search_query = request.args.get('search', '').strip().lower()
    
    # 🗂️ ระบบรับค่าตัวกรองหมวดหมู่
    selected_category = request.args.get('cat', 'all')
    
    # 1. กรองตามหมวดหมู่ก่อน
    if selected_category == 'all':
        filtered_products = electrical_products
    else:
        filtered_products = [p for p in electrical_products if p['category'] == selected_category]
        
    # 2. กรองตามคำค้นหา (พิมพ์ vaf หรือ ท่อ ก็จะค้นเจอทั้งคู่)
    if search_query:
        filtered_products = [
            p for p in filtered_products 
            if search_query in p['name_th'].lower() or search_query in p['name_en'].lower()
        ]
        
    return render_template(
        'index.html', 
        products=filtered_products, 
        current_cat=selected_category, 
        search_query=request.args.get('search', ''),
        lang=lang,
        shop_name="ร้านไฟฟ้าแสงคูณ" if lang == 'th' else "Saengkhoon Electric Shop"
    )

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
