from flask import Flask, render_template, request

app = Flask(__name__)

# เพิ่มข้อมูลชื่อภาษาอังกฤษ (name_en) เพื่อรองรับระบบ 2 ภาษา
electrical_products = [
    {"name": "สายไฟ IEC01 (THW) 1x1.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Wire 1x1.5 sq.mm. (100m)", "price": "478", "img": "/static/thw15.jpg", "category": "wire"},
    {"name": "สายไฟ IEC01 (THW) 1x2.5 sq.mm. (100 เมตร)", "name_en": "IEC01 (THW) Wire 1x2.5 sq.mm. (100m)", "price": "850", "img": "/static/thw25.jpg", "category": "wire"},
    {"name": "สายไฟ VAF 2x1.5 sq.mm. (100 เมตร)", "name_en": "VAF Wire 2x1.5 sq.mm. (100m)", "price": "1,200", "img": "/static/vaf15.jpg", "category": "wire"},
    {"name": "สายไฟ VAF 2x2.5 sq.mm. (100 เมตร)", "name_en": "VAF Wire 2x2.5 sq.mm. (100m)", "price": "1,800", "img": "/static/vaf25.jpg", "category": "wire"},
    {"name": "สายไฟ NYY 1x1.5 sq.mm. (100 เมตร)", "name_en": "NYY Wire 1x1.5 sq.mm. (100m)", "price": "1,450", "img": "/static/nyy15.jpg", "category": "wire"},
    {"name": "สายไฟ NYY 4x10 sq.mm. (ตัดเมตร)", "name_en": "NYY Wire 4x10 sq.mm. (Per Meter)", "price": "280 / เมตร", "img": "/static/nyy410.jpg", "category": "wire"},
    {"name": "ท่อร้อยสายไฟ PVC ขนาด 1/2 นิ้ว (สีเหลือง)", "name_en": "PVC Conduit 1/2 Inch (Yellow)", "price": "45", "img": "/static/pvc12.jpg", "category": "pipe"},
    {"name": "เบรกเกอร์ 2P 20A (ช้าง/Panasonic)", "name_en": "Circuit Breaker 2P 20A", "price": "120", "img": "/static/breaker20.jpg", "category": "breaker"}
]

@app.route('/')
def home():
    # 1. ระบบเลือกภาษา (ดึงค่าจากปุ่มกด TH/EN ถ้าไม่เลือกจะตั้งเป็น th เริ่มต้น)
    lang = request.args.get('lang', 'th')
    
    # 2. ระบบค้นหา (ดึงข้อความจากช่อง Search ที่ลูกค้าพิมพ์เข้ามา)
    search_query = request.args.get('search', '').strip().lower()
    
    # 3. ระบบกรองหมวดหมู่เดิม
    selected_category = request.args.get('cat', 'all')
    
    # กรองหมวดหมู่สินค้าก่อน
    if selected_category == 'all':
        filtered_products = electrical_products
    else:
        filtered_products = [p for p in electrical_products if p['category'] == selected_category]
        
    # ระบบค้นหาอัจฉริยะ: ค้นหาคำค้นจากทั้งชื่อไทยและอังกฤษ (เช่น พิมพ์ vaf หรือ thw ก็เจอหมด)
    if search_query:
        filtered_products = [
            p for p in filtered_products 
            if search_query in p['name'].lower() or search_query in p['name_en'].lower()
        ]
        
    return render_template('index.html', products=filtered_products, current_cat=selected_category, current_lang=lang, search_query=search_query, shop_name="ร้านไฟฟ้าแสงคูณ")

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
