from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    """
    Pydantic model for user data.
    
    Attributes:
    -----------
    id : int
        Unique identifier for the user.
    username : str
        Unique username for the user.
    email : EmailStr
        Unique email address for the user.
    password : str
        Hashed password for the user.
    """
    username: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "johnyboy",
                "email": "john@gmail.com",
                "password": "john123",
            }
        }

class LoginModel(BaseModel):
    """
    Pydantic model for login data.
    
    Attributes:
    -----------
    username : str
        The username of the user attempting to log in.
    password : str
        The password of the user attempting to log in.
    """
    username: str
    password: str

class Token(BaseModel):
    """
    Pydantic model for token data.
    
    Attributes:
    -----------
    token : str
        The authentication token.
    token_type : str
        The type of the token (e.g., Bearer).
    """
    token: str
    token_type: str
