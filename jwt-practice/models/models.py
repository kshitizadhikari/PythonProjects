from database.db import Base
from sqlalchemy import Column, Integer, Boolean, Text, String


class User(Base):
    """
    User model for storing user details.

    Attributes:
    -----------
    id : int
        Unique identifier for the user.
    username : str
        Unique username for the user.
    email : str
        Unique email address for the user.
    password : str
        Hashed password for the user.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    password = Column(Text, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
