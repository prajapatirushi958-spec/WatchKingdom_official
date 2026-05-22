# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# APNI WATCHES KA DATA (MULTIPLE IMAGES KE SAATH)
WATCHES_DATA = [
    {
        'id': 1, 
        'name': 'Hublot Classic Fusion - Full Black', 
        'brand': 'Hublot', 
        'price': 1299,                      
        'desc': 'HIGH QUALITY | BEST RATE AVAILABLE | DATE WORKING',
        'specs': '42mm Dial | Automatic Caliber | Genuine Leather',
        # Pehli image main rahegi, baaki dono extra images thumbnails banengi
        'images': ['image1.jpeg', 'image2.jpeg', 'image3.jpeg'], 
        'category': 'Classic'
    },
    {
        'id': 2, 
        'name': 'Longines Conquest Chronograph', 
        'brand': 'Longines Conquest', 
        'price': 1699, 
        'desc': 'Premium luxury steel sports watch with an iconic octagonal bezel.',
        'specs': '41mm Dial | Automatic Movement | Stainless Steel',
        # Isme bhi extra images ke naam dalo (Mene example ke liye image4, 5, 6 likha hai)
        'images': ['image4.jpeg', 'image5.jpeg', 'image6.jpeg'], 
        'category': 'Sport'
    },
    {
        'id': 3, 
        'name': 'Omega Moon Watch ', 
        'brand': 'OMEGA', 
        'price': 1599, 
        'desc': 'Premium luxury steel sports watch with an iconic octagonal bezel.',
        'specs': '41mm Dial | Automatic Movement | Stainless Steel | Limted Edition | New Model | Uniqe',
        # Isme bhi extra images ke naam dalo (Mene example ke liye image4, 5, 6 likha hai)
        'images': ['omega1.jpeg', 'omega2.jpeg', 'omega3.jpeg','omega4.jpeg','omega5.jpeg','omega6.jpeg'], 
        'category': 'Sport'
    },
    {
        'id': 4, 
        'name': 'Michael Kors Bradshow ', 
        'brand': 'Michael Kors', 
        'price': 1499, 
        'desc': 'Premium luxury steel sports watch with an iconic octagonal bezel.',
        'specs': '41mm Dial | Automatic Movement | Stainless Steel | All Chrono Working | New Model | Womens Watch ',
        # Isme bhi extra images ke naam dalo (Mene example ke liye image4, 5, 6 likha hai)
        'images': ['mk1.jpeg', 'mk2.jpeg', 'mk3.jpeg','mk4.jpeg','mk5.jpeg'], 
        'category': 'Diver'
    },
    {
        'id':5 , 
        'name': 'Casio Edifice Chronograph ', 
        'brand': 'Casio Edifice', 
        'price': 1299, 
        'desc': 'Premium luxury steel sports watch with an iconic octagonal bezel.',
        'specs': '41mm Dial | Automatic Movement | Stainless Steel | All Chrono Working | New Model |  ',
        
        'images': ['casio1.jpeg', 'casio2.jpeg'], 
        'category': 'Sport'
    },
{
        'id':6 , 
        'name': 'Seiko 5 Sports Automatic ', 
        'brand': 'Seiko', 
        'price': 2199, 
        'desc': 'Premium luxury steel sports watch with an iconic octagonal bezel.',
        'specs': '41mm Dial | Automatic Movement | Strong Belt | All Chrono Working | New Model |  ',
        
        'images': ['seiko1.jpeg', 'seiko2.jpeg','seiko3.jpeg','seiko4.jpeg'], 
        'category': 'Sport'
    },
{
        'id':7 , 
        'name': 'Emporio Armani Classic ', 
        'brand': 'Emporio Armani', 
        'price': 1299, 
        'desc': 'Premium luxury steel sports watch with an iconic octagonal bezel.',
        'specs': '41mm Dial | Strong Build Quality | Stainless Steel | All Chrono Working | Classic Model |  ',
        
        'images': ['ea1.jpeg', 'ea2.jpeg','ea3.jpeg','ea4.jpeg'], 
        'category': 'Classic'
    },

    {
        'id':8, 
        'name': 'Omega Speedmaster Silver Snoopy ', 
        'brand': 'Omega', 
        'price': 1799, 
        'desc': 'Premium luxury steel sports watch with an iconic octagonal bezel.',
        'specs': '41mm Dial | Automatic Movement | Strong Belt | All Chrono Working | New Model |  ',
        
        'images': ['o1.jpeg', 'o2.jpeg','o3.jpeg','04.jpeg'], 
        'category': 'Sport'
    },
{
        'id':9 , 
        'name': 'MINI FOCUS ORIGINAL ', 
        'brand': 'MINI FOCUS', 
        'price': 2799, 
        'desc': 'Premium luxury steel Classic watch with Strong Belt.',
        'specs': '41mm Dial | Quartz Movement | Strong Belt | All Chrono Working | Japan Machine |  ',
        
        'images': ['m1.jpeg', 'm2.jpeg','m3.jpeg','m4.jpeg'], 
        'category': 'Classic'
    },
{
        'id':10 , 
        'name': 'NAVIFORCE - NF9243S ', 
        'brand': 'NAVIFORCE', 
        'price': 1899, 
        'desc': 'Premium luxury steel Classic watch with OG BOX & BAG .',
        'specs': '41mm Dial | Automatic Movement | Strong Belt | All Chrono Working | Naviforce Original  |  ',
        
        'images': ['n1.jpeg', 'n2.jpeg','n3.jpeg','n4.jpeg'], 
        'category': 'Classic'
    },
{
        'id':11 , 
        'name': 'Rado  HighTech Automatic ', 
        'brand': 'RADO', 
        'price': 1799, 
        'desc': 'Premium luxury steel Classic watch with Strong Belt .',
        'specs': '41mm Dial | Automatic Movement | Strong Belt | All Chrono Working | Silver |  ',
        
        'images': ['r1.jpeg', 'r2.jpeg','r3.jpeg'], 
        'category': 'Sport'
    },
{
        'id':12 , 
        'name': 'RADO QUARTZ ', 
        'brand': 'RADO', 
        'price': 1250, 
        'desc': 'Premium luxury steel Classic watch.',
        'specs':  | Automatic Movement | Strong Belt | All Chrono Working | Trending  |  ',
        
        'images': ['rado1.jpeg', 'rado2.jpeg'], 
        'category': 'Classic'
    },


]

USER_CART = {}

# 1. Homepage Route
@app.route('/')
def home():
    search_query = request.args.get('search', '').lower()
    category_filter = request.args.get('category', '')
    
    filtered_products = WATCHES_DATA
    if search_query:
        filtered_products = [w for w in filtered_products if search_query in w['name'].lower() or search_query in w['brand'].lower()]
    if category_filter:
        filtered_products = [w for w in filtered_products if w['category'] == category_filter]
        
    return render_template('index.html', products=filtered_products, selected_category=category_filter)

# 2. Product Detail Route (FIXED PATH)
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    watch = next((item for item in WATCHES_DATA if item['id'] == product_id), None)
    if watch:
        # Yeh line confirm karegi ki product.html page hi load ho
        return render_template('product.html', product=watch)
    return "Collection Item Not Found", 404

# 3. Cart APIs
@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    p_id = str(data.get('id'))
    watch = next((item for item in WATCHES_DATA if str(item['id']) == p_id), None)
    
    if watch:
        if p_id in USER_CART:
            USER_CART[p_id]['quantity'] += 1
        else:
            USER_CART[p_id] = {'name': watch['name'], 'price': watch['price'], 'quantity': 1}
        return jsonify({'success': True, 'cart_count': sum(item['quantity'] for item in USER_CART.values())})
    return jsonify({'success': False}), 400

@app.route('/api/cart/get', methods=['GET'])
def get_cart():
    total_price = sum(item['price'] * item['quantity'] for item in USER_CART.values())
    return jsonify({'items': list(USER_CART.values()), 'total': total_price})

if __name__ == '__main__':
    app.run(debug=True) 
