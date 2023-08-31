from pydantic import BaseModel, constr

class AuthRequestModel(BaseModel):
    username: constr(strict=True)   # Username for authentication, valid: admin
    password: constr(strict=True)   # Password for authentication, valid: password123

class AuthResponse(BaseModel):
    token: str