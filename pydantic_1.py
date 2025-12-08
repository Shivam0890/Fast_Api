from pydantic import BaseModel
from typing import List,Optional,Dict

class Patient(BaseModel):
	name:str
	age:int
	weight:float
	married:bool
	allergies:Optional[List[str]] = None
	contact_details : Dict[str,str]


def insert_patient_info(patient:Patient):
	print(patient.name)
	print(patient.age)
	print('Inserted')


def update_patient_info(patient:Patient):
	print(patient.name)
	print(patient.age)
	print(patient.allergies)
	print('Updated')



patient_info = {'name':'shivam','age':19,'weight':75.2,'married':True,'allergies':['Pollen','Dust'],'contact_details':{'email':'shivam@gmail.com','phone_no':'8452637910'}}

patient1 = Patient(**patient_info)

insert_patient_info(patient1)
update_patient_info(patient1)