from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_product_list():
    return [
    {"id": 1, "name": "Organic Coffee Beans", "price": 10.49},
    {"id": 2, "name": "Premium Green Tea", "price": 9.49},
    {"id": 3, "name": "Cereal Granola", "price": 6.29},
    {"id": 4, "name": "Masala Chai Mix", "price": 10.49},
    {"id": 5, "name": "Yerba Mate Loose Leaf", "price": 13.49},
    {"id": 6, "name": "Hot Chocolate Mix", "price": 8.29},
    {"id": 7, "name": "Earl Grey Tea", "price": 12.49},
    {"id": 8, "name": "Espresso Beans", "price": 17.99},
    {"id": 9, "name": "Chamomile Tea", "price": 7.49},
    {"id": 10, "name": "Matcha Green Tea Powder", "price": 21.99},
    {"id": 11, "name": "Decaf Coffee Beans", "price": 16.99},
    {"id": 12, "name": "Mint Tea", "price": 8.29},
    {"id": 13, "name": "Instant Coffee", "price": 12.49},
    {"id": 14, "name": "Rooibos Tea", "price": 9.99},
    {"id": 15, "name": "Cold Brew Concentrate", "price": 14.49},
    {"id": 16, "name": "Vanilla Latte Powder", "price": 11.99},
    {"id": 17, "name": "Almond Milk (1L)", "price": 3.99},
    {"id": 18, "name": "Hazelnut Coffee Creamer", "price": 4.49},
    {"id": 19, "name": "Coconut Sugar (500g)", "price": 6.99},
    {"id": 20, "name": "Organic Agave Syrup", "price": 5.49}
]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

