from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
import os

app = FastAPI()

allowed_origins = os.getenv("ALLOWED_ORIGINS","http://localhost:3000").split(",")

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    # Create tables at startup. Wrap in try/except so app can still run if DB is unreachable.
    try:
        database_models.Base.metadata.create_all(bind=engine)
    except OperationalError as e:
        # Log the error to console; in production use proper logging
        print("Warning: could not create tables on startup:", e)


@app.get("/")
def func():
    return {"message": "Inventory Management System"}

# In-memory sample products (ids as ints to match Pydantic model)
products = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=699.99, quantity=25),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50),
    Product(id=4, name="Monitor", description="4K UHD Monitor", price=399.99, quantity=15),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    # what count is returing here


    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

    db.commit()

init_db()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    # Return in-memory list for now
    db_products = db.query(database_models.Product).all()
    return db_products


@app.get("/products/{product_id}")
def get_product(product_id: int,db:Session = Depends(get_db)):
    for p in products:
        if p.id == product_id:
            return db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    return {"error": "Product not found"}


@app.post("/products")
def create_product(product: Product,db:Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    print(db_product)
    db.add(db_product)
    db.commit() 
    return product


@app.put("/products/{id}")
def update_product(id: int, product: Product,db:Session = Depends(get_db)):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
            if db_product:
                db_product.name = product.name
                db_product.description = product.description
                db_product.price = product.price
                db_product.quantity = product.quantity
                db.commit()
            return product
    return {"error": "Product not found"}


@app.delete("/products/{id}")
def delete_product(id: int,db:Session = Depends(get_db)):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
            if db_product:
                db.delete(db_product)
                db.commit()
            return {"message": "Product deleted"}

    return {"error": "Product not found"}