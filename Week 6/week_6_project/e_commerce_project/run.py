# Import libraries 
import os
from dotenv import load_dotenv
from ecommerce_app import create_app ,db

# Load environment variables 
load_dotenv()

# Setup app environment
app_config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(app_config_name)

# Register CLI commands for database seeding
@app.cli.command('sample_db')
def sample_database():
    # Import models
    from ecommerce_app.models.user import User
    from ecommerce_app.models.product import Product, Category
    
    # Create sample admin
    existing_user = User.query.filter_by(email='admin@gmail.com').first()
    if not existing_user:
        admin = User(
            email = 'admin@gmail.com',
            first_name = 'Sharon',
            last_name = 'Akinjongula',
            role = 'admin'
            )

        admin.set_password('Admin123$')
        
        db.session.add(admin)
        db.session.commit()

    # Create sample categories
    category_data = [
        ("Pain Relief", "Analgesics and anti-inflammatory medications"),
        ("Antibiotics", "Prescription antibiotic medications"),
        ("Vitamins & Supplements", "Vitamins, minerals, and dietary supplements"),
        ("Allergy & Cold", "Antihistamines and cold medications"),
        ("Digestive Health", "Antacids, laxatives, and digestive aids"),
        ("Skin Care", "Topical creams, ointments, and skin treatments"),
        ("Diabetes Care", "Insulin, blood glucose monitors, and diabetes supplies"),
    ]

    category_objects = {}
    for name , description in category_data:
        existing_category = Category.query.filter_by(name=name).first()
        if not existing_category:
            cat = Category(name=name, description=description)
            db.session.commit(cat)
            db.session.flush()
            category_objects[name] = cat

        else:
            category_objects[name] = existing_category

    db.session.commit()

    # Create sample products
    products_data = [
        {
            "name": "Apple iPhone 14 Pro Max",
            "generic_name": "Smartphone",
            "brand_name": "Apple",
            "description": "6.7-inch Super Retina XDR display with ProMotion. A16 Bionic chip, 48MP main camera, and all-day battery life.",
            "requires_prescription": False,
            "color": "Deep Purple",
            "storage": "256GB",
            "price": 1199.99,
            "original_price": 1299.99,
            "stock_quantity": 45,
            "manufacturer": "Apple Inc.",
            "warranty": "1-year limited warranty",
            "category": "Electronics",
            "unit": "1 unit"
        },
        {
            "name": "Samsung 65\" Class QLED 4K TV",
            "generic_name": "Television",
            "brand_name": "Samsung",
            "description": "Quantum Processor 4K, 100% Color Volume with Quantum Dot, HDR, and Smart TV capabilities with voice control.",
            "requires_prescription": False,
            "screen_size": "65 inches",
            "resolution": "4K UHD",
            "price": 899.99,
            "original_price": 1199.99,
            "stock_quantity": 12,
            "manufacturer": "Samsung Electronics",
            "warranty": "2-year manufacturer warranty",
            "category": "Electronics",
            "unit": "1 unit"
        },
        {
            "name": "Sony WH-1000XM5 Headphones",
            "generic_name": "Wireless Headphones",
            "brand_name": "Sony",
            "description": "Industry-leading noise cancellation with Auto NC Optimizer. Crystal clear hands-free calling and 30-hour battery life.",
            "requires_prescription": False,
            "color": "Silver",
            "connectivity": "Bluetooth 5.2",
            "price": 348.99,
            "stock_quantity": 28,
            "manufacturer": "Sony Corporation",
            "warranty": "1-year warranty",
            "category": "Audio",
            "unit": "1 pair"
        },
        {
            "name": "Nike Air Max 270",
            "generic_name": "Athletic Shoes",
            "brand_name": "Nike",
            "description": "Men's running shoes with Max Air unit for ultra-soft comfort. Breathable mesh upper and durable rubber sole.",
            "requires_prescription": False,
            "color": "Black/White",
            "size": "10",
            "price": 149.99,
            "original_price": 169.99,
            "stock_quantity": 34,
            "manufacturer": "Nike Inc.",
            "category": "Footwear",
            "unit": "1 pair"
        },
        {
            "name": "Levi's 501 Original Jeans",
            "generic_name": "Jeans",
            "brand_name": "Levi's",
            "description": "Classic straight-fit jeans with signature button fly. 100% cotton denim that softens with wear.",
            "requires_prescription": False,
            "color": "Dark Wash",
            "size": "32x32",
            "price": 79.99,
            "stock_quantity": 56,
            "manufacturer": "Levi Strauss & Co.",
            "category": "Clothing",
            "unit": "1 pair"
        },
        {
            "name": "KitchenAid Stand Mixer",
            "generic_name": "Stand Mixer",
            "brand_name": "KitchenAid",
            "description": "5-quart tilt-head stand mixer with 10 speeds. Includes coated flat beater, dough hook, and wire whip.",
            "requires_prescription": False,
            "color": "Empire Red",
            "capacity": "5 quarts",
            "price": 399.99,
            "original_price": 449.99,
            "stock_quantity": 8,
            "low_stock_threshold": 10,
            "manufacturer": "KitchenAid",
            "warranty": "1-year warranty",
            "category": "Kitchen & Dining",
            "unit": "1 unit"
        },
        {
            "name": "Dyson V15 Detect Vacuum",
            "generic_name": "Cordless Vacuum",
            "brand_name": "Dyson",
            "description": "Powerful cordless vacuum with laser illumination to detect invisible dust. Intelligent vacuum cleaner with LCD screen.",
            "requires_prescription": False,
            "color": "Yellow/Nickel",
            "battery_life": "60 minutes",
            "price": 699.99,
            "stock_quantity": 5,
            "low_stock_threshold": 8,
            "manufacturer": "Dyson Ltd.",
            "warranty": "2-year warranty",
            "category": "Home Appliances",
            "unit": "1 unit"
        },
        {
            "name": "The Legend of Zelda: Tears of the Kingdom",
            "generic_name": "Video Game",
            "brand_name": "Nintendo",
            "description": "Action-adventure game for Nintendo Switch. Explore the vast lands of Hyrule in this epic sequel.",
            "requires_prescription": False,
            "platform": "Nintendo Switch",
            "genre": "Action-Adventure",
            "price": 59.99,
            "stock_quantity": 0,
            "manufacturer": "Nintendo",
            "category": "Video Games",
            "unit": "1 game"
        },
        {
            "name": "LEGO Star Wars Millennium Falcon",
            "generic_name": "Building Set",
            "brand_name": "LEGO",
            "description": "Detailed building set with 1,351 pieces. Includes 7 minifigures and buildable starship with interior.",
            "requires_prescription": False,
            "pieces": "1351",
            "age_range": "9-14 years",
            "price": 159.99,
            "original_price": 179.99,
            "stock_quantity": 23,
            "manufacturer": "LEGO Group",
            "category": "Toys & Games",
            "unit": "1 set"
        },
        {
            "name": "CeraVe Hydrating Facial Cleanser",
            "generic_name": "Facial Cleanser",
            "brand_name": "CeraVe",
            "description": "Non-foaming, hydrating facial cleanser with ceramides and hyaluronic acid. Fragrance-free and non-comedogenic.",
            "requires_prescription": False,
            "size": "16 fl oz",
            "skin_type": "Normal to Dry",
            "price": 14.99,
            "stock_quantity": 42,
            "manufacturer": "CeraVe",
            "category": "Beauty & Personal Care",
            "unit": "1 bottle"
        },
        {
            "name": "The Silent Patient by Alex Michaelides",
            "generic_name": "Hardcover Book",
            "brand_name": "Celadon Books",
            "description": "International bestselling psychological thriller about a woman's act of violence against her husband and the therapist obsessed with uncovering her motive.",
            "requires_prescription": False,
            "format": "Hardcover",
            "pages": "336",
            "price": 18.99,
            "original_price": 22.99,
            "stock_quantity": 67,
            "manufacturer": "Celadon Books",
            "category": "Books",
            "unit": "1 book"
        },
        {
            "name": "Stanley Quencher H2.0 Tumbler",
            "generic_name": "Insulated Tumbler",
            "brand_name": "Stanley",
            "description": "40oz insulated tumbler with handle and straw. Keeps drinks cold for hours. Dishwasher safe and BPA-free.",
            "requires_prescription": False,
            "color": "Rose Quartz",
            "capacity": "40 oz",
            "price": 45.00,
            "stock_quantity": 2,
            "low_stock_threshold": 5,
            "manufacturer": "Stanley",
            "category": "Kitchen & Dining",
            "unit": "1 tumbler"
        },
        {
            "name": "YETI Rambler 20 oz Tumbler",
            "generic_name": "Insulated Cup",
            "brand_name": "YETI",
            "description": "Stainless steel, vacuum-insulated tumbler that keeps drinks hot or cold for hours. MagSlider lid included.",
            "requires_prescription": False,
            "color": "Navy",
            "capacity": "20 oz",
            "price": 29.99,
            "stock_quantity": 15,
            "manufacturer": "YETI",
            "category": "Kitchen & Dining",
            "unit": "1 tumbler"
        },
        {
            "name": "Hydro Flask 32 oz Water Bottle",
            "generic_name": "Water Bottle",
            "brand_name": "Hydro Flask",
            "description": "Double-wall vacuum-insulated water bottle with Flex Cap. Keeps water cold for up to 24 hours.",
            "requires_prescription": False,
            "color": "White",
            "capacity": "32 oz",
            "price": 39.95,
            "stock_quantity": 28,
            "manufacturer": "Hydro Flask",
            "category": "Sports & Outdoors",
            "unit": "1 bottle"
        }
    ]

    for product_data in products_data:
        if Product.query.filter_by(name=product_data['name']).first():
            continue

        category_name = product_data.pop('category',None)
        category = category_objects.get(category_name)

        product = Product(**product_data, category_id=category.id if category else None)

        db.session.add(product)

    db.session.commit()

    print("\nDatabase seeded successfully!")
    print("\nTest accounts:")
    print("  Admin:    admin@pharmacy.com / Admin123$")
    print("  Customer: customer@test.com / Customer123$")

    # Create CLI command to create sample admin
    @app.cli.command('create-admin')
    def create_admin():
        # Get admin login details
        email= input('Admin email:\n')
        password= input('Admin password:\n')

        existing = User.query.filter_by(email=email).first()
        if not existing:
            admin = User(
                email=email,
                first_name='Sharon',
                last_name='Akinjogula',
                role='admin'
            )

            admin.set_password(password)

            db.session.add(admin)
            db.session.commit()
            print(f'Admin user created sucesssfully.{email}')


            # Run application
            if __name__ == 'main':
                app.run(DEBUG=True, host='0.0.0.0',port=5000)

