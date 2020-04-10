from sqlalchemy import Boolean, Column, Integer, String, PrimaryKeyConstraint
from app.database.postgresql import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    address = Column(String)
    phone = Column(Integer)
    active = Column(Boolean)
    role = Column(String, nullable = False)

    __table_args__ = (
        PrimaryKeyConstraint(email, address, role), {}
    )
