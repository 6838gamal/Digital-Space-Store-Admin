from pydantic import BaseModel
from typing import Optional

class DigitalProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    product_type: str
    price: Optional[float] = None
    file_url: Optional[str] = None
    is_active: Optional[bool] = True

class DigitalProductCreate(DigitalProductBase):
    pass

class DigitalProductUpdate(DigitalProductBase):
    pass

class DigitalProduct(DigitalProductBase):
    id: int
    class Config:
        orm_mode = True
