from pydantic import BaseModel

class Signup(BaseModel):
    username: str
    usermail: str
    userpassword: int

class Login(BaseModel):
    email: str
    password: int
