import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.infrastructure.api.route_employee import route_employee
from app.infrastructure.api.route_products import route_product

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

API_PREFIX = '/api'

fast_api_app.include_router(route_employee, prefix=f"{API_PREFIX}/employees", tags=["employees"])
fast_api_app.include_router(route_product, prefix=f"{API_PREFIX}/products", tags=["products"])


if __name__ == '__main__':
    uvicorn.run(fast_api_app)
