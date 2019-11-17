from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Product

engine = create_engine('sqlite:///database.db', echo=True)

Session = sessionmaker(bind=engine)


def get_products():
    session = Session()
    db_products = session.query(Product).all()
    products = {
        product.name: product.price for product in db_products
    }
    session.close()
    return products
