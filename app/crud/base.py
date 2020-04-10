from typing import Optional, Generic, TypeVar, Type

from pydantic import BaseModel

from app.database.postgresql import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateDtoType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateDtoType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateDtoType, UpdateDtoType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `dto`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, id: int) -> Optional[ModelType]:
        return self.model.filter(self.model.id == id).first()

