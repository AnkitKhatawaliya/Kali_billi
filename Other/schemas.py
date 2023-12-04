from pydantic import BaseModel


class User_Model(BaseModel):
    Name: str
    Email: str
    Username: str
    Password: str