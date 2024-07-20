import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.infrastructure.api.route_atuh import route_auth
from app.infrastructure.api.route_employee import route_employee
from app.infrastructure.api.route_products import route_product
from app.infrastructure.api.route_stores import route_stores

# load_dotenv('.env')

API_PREFIX = '/api'

fast_api_app = FastAPI()


@fast_api_app.get("/")
async def root():
    return {"message": "Hello World"}


fast_api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fast_api_app.include_router(route_auth, prefix=f"{API_PREFIX}/auth", tags=["auth"])
fast_api_app.include_router(route_employee, prefix=f"{API_PREFIX}/employees", tags=["employees"])
fast_api_app.include_router(route_product, prefix=f"{API_PREFIX}/products", tags=["products"])
fast_api_app.include_router(route_stores, prefix=f"{API_PREFIX}/stores", tags=["stores"])

if __name__ == '__main__':
    uvicorn.run(fast_api_app)
