from sqlalchemy.orm import Session
from app import models, schemas

def get_all_products(db: Session):
    products = db.query(models.DigitalProduct).all()
    return [schemas.DigitalProductBase.from_orm(p) for p in products]

def create_product(db: Session, product: schemas.DigitalProductCreate):
    db_product = models.DigitalProduct(
        title=product.title,
        description=product.description,
        product_type=product.product_type,
        price=product.price,
        file_url=product.file_url
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
