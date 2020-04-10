from typing import Optional
from app.models.user import User
from app.dtos.userDto import UserRequest, UserResponse
from app.crud.base import CRUDBase

from app.database.session import Session

session = Session()

class CRUDUser(CRUDBase[User, UserRequest, UserResponse]):
    def get_user_by_id(self, id: int) -> Optional[User]:
        result = session.query(User).filter(User.id == id).first()
        return result.__dict__

    def get_by_email(self, email: str) -> Optional[User]:
        return filter(User.email == email).first()

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)
