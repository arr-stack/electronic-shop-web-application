from pydantic import BaseModel, Field

class UserLogin(BaseModel):
    id: int = Field()
    email: str = Field()
    username: str = Field(min_length=1)
    password: str = Field(min_length=8)


#country code (like +7 or +3) + 11 characters
class ConfirmForm(BaseModel):
    email: str = Field(min_length=1)
    username: str = Field(min_length=1)
    password: str = Field(min_length=8)

class ConfirmCode(BaseModel):
    input_code: str = Field(min_length=6, max_length=6)