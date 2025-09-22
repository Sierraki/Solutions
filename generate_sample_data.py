import sqlite3
import random
from datetime import datetime, timedelta

def create_sample_tables():
    """
    创建示例表结构
    """
    # 连接到SQLite数据库
    conn = sqlite3.connect('s:/Code/Solutions/123.sqlite')
    cursor = conn.cursor()
    
    # 创建用户表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 创建产品表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 创建订单表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    ''')
    
    # 提交更改
    conn.commit()
    conn.close()
    print("表结构创建成功！")

def generate_sample_users(num_users=20):
    """
    生成示例用户数据
    """
    conn = sqlite3.connect('s:/Code/Solutions/123.sqlite')
    cursor = conn.cursor()
    
    # 常见用户名和邮箱域名
    first_names = ['张', '李', '王', '刘', '陈', '杨', '赵', '黄', '周', '吴']
    last_names = ['伟', '芳', '娜', '敏', '静', '丽', '强', '磊', '军', '洋', 
                  '勇', '艳', '杰', '娟', '涛', '明', '超', '秀英', '霞', '平']
    domains = ['example.com', 'test.com', 'demo.com', 'sample.org', 'fake.net']
    
    users = []
    for i in range(num_users):
        # 生成随机用户名和邮箱
        first = random.choice(first_names)
        last = random.choice(last_names)
        username = first + last + str(random.randint(1, 999))
        email = username.lower() + '@' + random.choice(domains)
        age = random.randint(18, 65)
        users.append((username, email, age))
    
    # 插入用户数据
    cursor.executemany('''
        INSERT OR IGNORE INTO users (username, email, age) 
        VALUES (?, ?, ?)
    ''', users)
    
    conn.commit()
    conn.close()
    print(f"生成 {len(users)} 个用户数据")

def generate_sample_products(num_products=15):
    """
    生成示例产品数据
    """
    conn = sqlite3.connect('s:/Code/Solutions/123.sqlite')
    cursor = conn.cursor()
    
    # 产品名称和类别
    product_names = ['笔记本电脑', '智能手机', '平板电脑', '耳机', '键盘', '鼠标', 
                     '显示器', '音响', '路由器', '充电器', '移动硬盘', 'U盘', 
                     '摄像头', '打印机', '扫描仪']
    categories = ['电子产品', '计算机配件', '网络设备', '办公用品']
    
    products = []
    for i in range(num_products):
        name = random.choice(product_names)
        price = round(random.uniform(50, 5000), 2)
        category = random.choice(categories)
        products.append((name, price, category))
    
    # 插入产品数据
    cursor.executemany('''
        INSERT OR IGNORE INTO products (name, price, category) 
        VALUES (?, ?, ?)
    ''', products)
    
    conn.commit()
    conn.close()
    print(f"生成 {len(products)} 个产品数据")

def generate_sample_orders(num_orders=50):
    """
    生成示例订单数据
    """
    conn = sqlite3.connect('s:/Code/Solutions/123.sqlite')
    cursor = conn.cursor()
    
    # 获取用户ID和产品ID
    cursor.execute('SELECT id FROM users')
    user_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute('SELECT id FROM products')
    product_ids = [row[0] for row in cursor.fetchall()]
    
    if not user_ids or not product_ids:
        print("请先生成用户和产品数据")
        conn.close()
        return
    
    orders = []
    # 生成随机订单
    for i in range(num_orders):
        user_id = random.choice(user_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        orders.append((user_id, product_id, quantity))
    
    # 插入订单数据
    cursor.executemany('''
        INSERT OR IGNORE INTO orders (user_id, product_id, quantity) 
        VALUES (?, ?, ?)
    ''', orders)
    
    conn.commit()
    conn.close()
    print(f"生成 {len(orders)} 个订单数据")

def query_sample_data():
    """
    查询示例数据
    """
    conn = sqlite3.connect('s:/Code/Solutions/123.sqlite')
    cursor = conn.cursor()
    
    print("\n=== 用户数据 ===")
    cursor.execute('SELECT * FROM users LIMIT 5')
    for row in cursor.fetchall():
        print(row)
    
    print("\n=== 产品数据 ===")
    cursor.execute('SELECT * FROM products LIMIT 5')
    for row in cursor.fetchall():
        print(row)
    
    print("\n=== 订单数据 ===")
    cursor.execute('''
        SELECT o.id, u.username, p.name, o.quantity, o.order_date 
        FROM orders o
        JOIN users u ON o.user_id = u.id
        JOIN products p ON o.product_id = p.id
        LIMIT 5
    ''')
    for row in cursor.fetchall():
        print(row)
    
    conn.close()

if __name__ == "__main__":
    # 创建表结构
    create_sample_tables()
    
    # 生成示例数据
    generate_sample_users()
    generate_sample_products()
    generate_sample_orders()
    
    # 查询并显示部分数据
    query_sample_data()
    
    print("\n数据生成完成！")