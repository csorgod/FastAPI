from src.schemas.base_schema import BaseSchema as BaseModel

class Cat(BaseModel):
    cat_id: int
    name: str
    breed: str

class CatResponse(BaseModel):
    cat_id: int
    name: str
    breed: str