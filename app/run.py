from config import app
from model.product import Product
from model.user import User
from config import engine
from config import Base
from api.routes.product_routes import create_product
from api.routes.product_routes import product_by_code
from api.routes.product_routes import get_all_products
from sqlalchemy.orm import sessionmaker


Base.metadata.create_all(bind=engine)

app.route('/product', methods=['POST'])(create_product)
app.route('/product/<int:product_code>', methods=['GET'])(product_by_code)
app.route('/product', methods=['GET'])(get_all_products)
app.route('/product', methods=['DELETE'])(product_by_code)



if __name__ == "__main__":
    app.run(debug=True)
