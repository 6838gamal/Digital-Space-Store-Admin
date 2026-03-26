from pydantic import BaseModel

class DigitalProductBase(BaseModel):
    title: str
    description: str | None = None
    product_type: str
    price: float | None = None
    file_url: str | None = None

    class Config:
        from_attributes = True  # بديل orm_mode في Pydantic V2

# للإضافة
class DigitalProductCreate(DigitalProductBase):
    pass

# للتحديث
class DigitalProductUpdate(DigitalProductBase):
    pass
