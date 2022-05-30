from fastapi import APIRouter
from src.endpoints import healthcheck, cat

router = APIRouter()
router.include_router(healthcheck.router)
router.include_router(cat.router)