from pydantic import BaseModel



class RegisterUserValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    city: str
    password: str


class EditUserValidator(BaseModel):
    user_id: int
    edit_type: str
    new_data: str