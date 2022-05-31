from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from src.schemas.cat import Cat, CatResponse
from src.services.cat_service import CatService
from src.dependencies import database

router = APIRouter(
    prefix="/cats",
    tags=["Cats"],
    responses={
        404: {"message": "Not found"}
    },
)


@router.get("", response_model=List[CatResponse], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
async def get_all(skip=0, limit=10, db: Session = Depends(database.get_db)):
    return CatService.get_all(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=CatResponse, response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
async def get_by_id(id: int, db: Session = Depends(database.get_db)):
    return CatService.get_by_id(db, id)


@router.post("", status_code=status.HTTP_201_CREATED)
async def get_by_id(cat: Cat, db: Session = Depends(database.get_db)):
    return CatService.create_new(db, cat)
