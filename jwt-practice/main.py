from fastapi import FastAPI
from routers.auth_router import auth_router
from routers.store_router import store_router

app = FastAPI(debug=True)

app.include_router(auth_router)
app.include_router(store_router)

@app.get("/")
def index():
    return {
        "data": "helloo successful person"
    }

