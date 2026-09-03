from flask import Flask, render_template, request

app = Flask(__name__)

# เพิ่มหมวดหมู่ (category) ให้สินค้าแต่ละชิ้น เพื่อทำระบบตัวกรอง
electrical_products = [
    {"name": "สายไฟ THW 1x1.5 sq.mm. (100 เมตร)", "price": "478", "img": "/static/thw15.jpg", "category": "wire"},
    {"name": "สายไฟ THW 1x2.5 sq.mm. (100 เมตร)", "price": "850", "img": "https://placehold.co", "category": "wire"},
    {"name": "สายไฟ VAF 2x1.5 sq.mm. (100 เมตร)", "price": "1,200", "img": "https://placehold.co", "category": "wire"},
    {"name": "สายไฟ VAF 2x2.5 sq.mm. (100 เมตร)", "price": "1,800", "img": "https://placehold.co", "category": "wire"},
    {"name": "สายไฟ NYY 1x1.5 sq.mm. (100 เมตร)", "price": "1,450", "img": "https://placehold.co", "category": "wire"},
    {"name": "สายไฟ NYY 4x10 sq.mm. (ตัดเมตร)", "price": "280 / เมตร", "img": "https://placehold.co", "category": "wire"},
    {"name": "ท่อร้อยสายไฟ PVC ขนาด 1/2 นิ้ว (สีเหลือง)", "price": "45", "img": "https://placehold.co", "category": "pipe"},
    {"name": "เบรกเกอร์ 2P 20A (ช้าง/Panasonic)", "price": "120", "img": "https://placehold.co", "category": "breaker"}
]

@app.route('/')
def home():
    # ดึงค่าหมวดหมู่ที่ลูกค้ากดเลือกจากหน้าเว็บ (ถ้าไม่กดจะกลายเป็นดึงทั้งหมด)
    selected_category = request.args.get('cat', 'all')
    
    # ข้อ 4: ระบบกรองสินค้าตามหมวดหมู่
    if selected_category == 'all':
        filtered_products = electrical_products
    else:
        filtered_products = [p for p in electrical_products if p['category'] == selected_category]
        
    return render_template('index.html', products=filtered_products, current_cat=selected_category, shop_name="ร้านไฟฟ้าแสงคูณ")

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
