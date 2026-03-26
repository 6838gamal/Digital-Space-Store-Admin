from sqlalchemy.orm import Session
from app import models

# جلب كل المنتجات (كـ SQLAlchemy Objects)
def get_all_products(db: Session):
    return db.query(models.DigitalProduct).all()

# إضافة منتج
def create_product(db: Session, product_data):
    product = models.DigitalProduct(
        title=product_data.title,
        description=product_data.description,
        product_type=product_data.product_type,
        price=product_data.price,
        file_url=product_data.file_url
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
