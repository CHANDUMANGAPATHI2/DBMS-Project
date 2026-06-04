# pydantic is used for form validation and pydantic is used only when fastapi is used
# like java we dont use "extends" keyword in python instead we use class Signinschema(BaseModel)
#  here BaseModel is parent and Signinschema is child class and we use all the properties of BaseModel in Signinschema and Signupschema and we can also add our own properties in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel
#  in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema 
# # and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema and we can also use the properties of BaseModel in Signinschema and Signupschema.  
from pydantic import BaseModel



class SignupSchema(BaseModel):
    fullname:str
    phone:str
    email: str
    password: str

class SigninSchema(BaseModel):
    
    username: str
    password: str

class UserSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str
    role: int
    status: int
class TasksSchema(BaseModel):
    title: str
    description: str
    createdby: int
    assignedto: int
    priority: int
    deadline: str
    status: int

