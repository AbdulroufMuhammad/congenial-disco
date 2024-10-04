from pydantic import BaseModel


class UserCreate(BaseModel):
    FirstName : str
    LastName : str
    Email : str
    Password : str
    Confirm_password : str

    