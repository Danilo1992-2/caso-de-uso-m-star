from config import app
from model.product import Product
from model.user import User
from config import engine
from config import Base
from api.routes.product_routes import create_product
from api.routes.product_routes import product_by_code
from api.routes.product_routes import get_all_products
from api.routes.product_routes import delete_product
from api.routes.user_routes import get_all
from api.routes.user_routes import delete_user
from api.routes.user_routes import create_user

Base.metadata.create_all(bind=engine)

app.route('/product', methods=['POST'])(create_product)
app.route('/product/<int:product_code>', methods=['GET'])(product_by_code)
app.route('/product', methods=['GET'])(get_all_products)
app.route('/product/<int:product_code>', methods=['DELETE'])(delete_product)

app.route('/user', methods=['POST'])(create_user)
app.route('/user/<int:id>', methods=['DELETE'])(delete_user)
app.route('/user', methods=['GET'])(get_all)

if __name__ == "__main__":
    app.run(debug=True)
