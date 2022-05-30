from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import db

class Cat(db):
    __tablename__ = "cats"

    cat_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    breed = Column(String)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
