from config import app
from model.product import Product
from model.user import User
from config import engine
from config import Base
from api.routes.product_routes import create_product
from api.routes.product_routes import product_by_code
from api.routes.product_routes import get_all_products
from api.routes.product_routes import delete_product
from api.routes.product_routes import process_csv_file
from api.routes.user_routes import get_all
from api.routes.user_routes import delete_user
from api.routes.user_routes import create_user


Base.metadata.create_all(bind=engine)

app.route("/api/product", methods=["POST"])(create_product)
app.route("/api/product/<int:product_code>", methods=["GET"])(product_by_code)
app.route("/api/product", methods=["GET"])(get_all_products)
app.route("/api/product/<int:product_code>", methods=["DELETE"])(delete_product)
app.route("/api/product/upload-csv", methods=["POST"])(process_csv_file)

app.route("/api/user", methods=["POST"])(create_user)
app.route("/api/user/<int:id>", methods=["DELETE"])(delete_user)
app.route("/api/user", methods=["GET"])(get_all)

if __name__ == "__main__":
    app.run(debug=True)
