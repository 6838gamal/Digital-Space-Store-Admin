from sqlalchemy import Column, Integer, String, Float, Text
from app.database import Base

class DigitalProduct(Base):
    __tablename__ = "digital_products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    product_type = Column(String(100), nullable=False)  # كتب، سكربت، قالب، دفتر ملاحظات
    price = Column(Float, nullable=True)
    file_url = Column(String(255), nullable=True)
