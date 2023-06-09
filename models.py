from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# orm models
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(15), unique=True, index=True)
    username = Column(String(20), unique=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    hashed_password = Column(String(200))
    is_active = Column(Boolean, default=True)
    # phone_number = Column(String)
    # address_id = Column(Integer, ForeignKey("address.id"), nullable=True) #is the foriegn key correct?

    todos = relationship("Todos", back_populates="owner")
    # address = relationship("Address", back_populates="user_address")

class Todos(Base):
    # this is where we define table name
    __tablename__ = "todos"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(20))
    description = Column(String(100))
    priority    = Column(Integer)
    complete    = Column(Boolean, default=False)
    owner_id    = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="todos")

# class Address(Base):
#     __tablename__="address"

#     id = Column(Integer, primary_key=True, index=True)
#     address1 = Column(String)
#     address2 = Column(String)
#     city = Column(String)
#     state = Column(String)
#     country = Column(String)
#     postalcode = Column(String)

#     user_address = relationship("Users", back_populates="address")