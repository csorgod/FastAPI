from sqlalchemy.orm import Session

from src.models.cat import Cat as CatModel
from src.schemas.cat import Cat as CatSchema

class CatService():

    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(CatModel).offset(skip).limit(limit).all()

    def get_by_id(db: Session, cat_id: int):
        return db.query(CatModel).filter(CatModel.cat_id == cat_id).first()

    def create_new(db: Session, cat: CatSchema):
        _cat = CatModel(cat.name, cat.age, cat.breed)
        db.add(_cat)
        db.commit()
        db.refresh(_cat)
        return _cat
