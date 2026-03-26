from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app import models, crud, schemas
from app.database import engine, SessionLocal, Base

# إنشاء الجداول في قاعدة البيانات
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====== ROOT ======
@app.get("/")
def root():
    # إعادة التوجيه للوحة التحكم
    return RedirectResponse(url="/dashboard")

# ====== DASHBOARD ======
@app.get("/dashboard")
def dashboard(request: Request, db: Session = Depends(get_db)):
    products = crud.get_all_products(db)
    return templates.TemplateResponse("dashboard.html", {"request": request, "products": products})

# ====== ADD PRODUCT ======
@app.get("/products/add")
def add_product_form(request: Request):
    return templates.TemplateResponse("add_product.html", {"request": request})

@app.post("/products/add")
def add_product(
    request: Request,
    title: str = Form(...),
    description: str = Form(None),
    product_type: str = Form(...),
    price: float = Form(None),
    file_url: str = Form(None),
    db: Session = Depends(get_db)
):
    product = schemas.DigitalProductCreate(
        title=title,
        description=description,
        product_type=product_type,
        price=price,
        file_url=file_url
    )
    crud.create_product(db, product)
    return templates.TemplateResponse("add_product.html", {"request": request, "success": True})

# ====== VIEW PRODUCTS (Users) ======
@app.get("/products")
def view_products(request: Request, db: Session = Depends(get_db)):
    products = crud.get_all_products(db)
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

# ====== OPTIONAL: DELETE PRODUCT ======
@app.post("/products/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    crud.delete_product(db, product_id)
    return RedirectResponse(url="/dashboard", status_code=303)

# ====== OPTIONAL: UPDATE PRODUCT ======
@app.get("/products/edit/{product_id}")
def edit_product_form(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    return templates.TemplateResponse("add_product.html", {"request": request, "product": product})

@app.post("/products/edit/{product_id}")
def edit_product(
    product_id: int,
    request: Request,
    title: str = Form(...),
    description: str = Form(None),
    product_type: str = Form(...),
    price: float = Form(None),
    file_url: str = Form(None),
    db: Session = Depends(get_db)
):
    product_data = schemas.DigitalProductUpdate(
        title=title,
        description=description,
        product_type=product_type,
        price=price,
        file_url=file_url
    )
    crud.update_product(db, product_id, product_data)
    return RedirectResponse(url="/dashboard", status_code=303)
