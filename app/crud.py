from sqlalchemy.orm import Session
from app import models, schemas

# جلب كل المنتجات
def get_all_products(db: Session):
    products = db.query(models.DigitalProduct).all()
    # تحويل كل عنصر إلى Pydantic
    return [schemas.DigitalProductBase.from_orm(p) for p in products]

# إنشاء منتج جديد
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

# جلب منتج واحد
def get_product(db: Session, product_id: int):
    product = db.query(models.DigitalProduct).filter(models.DigitalProduct.id == product_id).first()
    return schemas.DigitalProductBase.from_orm(product) if product else None

# تحديث منتج
def update_product(db: Session, product_id: int, product_data: schemas.DigitalProductUpdate):
    product = db.query(models.DigitalProduct).filter(models.DigitalProduct.id == product_id).first()
    if not product:
        return None
    for key, value in product_data.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return schemas.DigitalProductBase.from_orm(product)

# حذف منتج
def delete_product(db: Session, product_id: int):
    product = db.query(models.DigitalProduct).filter(models.DigitalProduct.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product
