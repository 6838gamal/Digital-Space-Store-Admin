from sqlalchemy.orm import Session
from app import models, schemas

def get_all_products(db: Session):
    return db.query(models.DigitalProduct).all()

def get_product(db: Session, product_id: int):
    return db.query(models.DigitalProduct).filter(models.DigitalProduct.id == product_id).first()

def create_product(db: Session, product: schemas.DigitalProductCreate):
    db_product = models.DigitalProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: schemas.DigitalProductUpdate):
    db_product = get_product(db, product_id)
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
