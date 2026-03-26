from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime
from app.database import Base
import datetime

class DigitalProduct(Base):
    __tablename__ = "digital_products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)           # اسم المنتج
    description = Column(Text, nullable=True)            # وصف المنتج
    product_type = Column(String(50), nullable=False)    # script, short_book, automation_template, coloring_book, notebook
    price = Column(Float, nullable=True)                 # سعر المنتج
    file_url = Column(String(255), nullable=True)        # رابط التحميل
    is_active = Column(Boolean, default=True)            # حالة المنتج
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
