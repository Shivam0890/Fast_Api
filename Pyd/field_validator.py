from pydantic import BaseModel, EmailStr, field_validator , Field
from typing import List,Dict,Optional,Annotated
from fastapi import FastAPI,HTTPException


class Patient(BaseModel):

	name:str
	email:EmailStr
	age: int
	weight: float
	height: float
	married:bool
	allergies: Optional[List[str]]
	contact_details:Dict[str,str]

	@field_validator('email')
	@classmethod
	def email_validator(cls,value):
		valid_domain = ['hdfc.com','rbi.com']
		
		domain_name = value.split('@')[-1]

		if domain_name not in valid_domain:
			raise HTTPException(status_code=404,detail='Invaild Email Id of the patient')

		return value
	

def update_Patient_data(patient:Patient):
	print(patient.name)
	print(patient.age)
	print(patient.allergies)
	print(patient.married)
	print('Updated')


patient1_info = {'name':'shivam','email':'shivam@gmail.com','age':"30",'weight':'77','married':False,'contact_details':{'phone_no':'2334556789'}}

patient1 = Patient(**patient1_info)

update_Patient_data(patient1)
