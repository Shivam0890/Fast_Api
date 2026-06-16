from pydantic import BaseModel,EmailStr,AnyUrl ,Field
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
	name:str
	age:Annotated[int,Field(gt=0,lt=150 ,strict=True)]
	weight:float = Annotated[float,Field(gt=0,strict=True)]
	email: EmailStr
	linkedin_url: Annotated[Optional[AnyUrl] ,Field( default= None,title='linked In profile Url of the patient')]
	married:Annotated[bool ,Field(default= False,description='Marital Status of the patient')] # using = sets default values
	allergies:Optional[List[str]] = None
	contact_details:Dict[str,str]


def update_patient(patient:Patient):
	print(patient.name)
	print(patient.age)
	print(patient.married)
	print('Updated details')