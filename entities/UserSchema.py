from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):

    name: str
    username: str
    email: EmailStr
    phone_number: str
    password: str

    class Config:
        orm_mode = True
        title = "User"

class UserIDSchema(UserSchema):

    id: int