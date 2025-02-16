from fastapi import FastAPI
from routes import order

app = FastAPI()

app.include_router(order.router, prefix="/api")

@app.get("/")
def home():
    return {"message": "SCM Backend Running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
