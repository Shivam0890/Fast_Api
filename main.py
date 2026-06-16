from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()


def laod_data():
	with open('patient.json','r') as f :
		data  =	json.load(f)
	return data

@app.get('/')
def home():
	return {'Welcome Page':"Hello Welcome to this side !"}

@app.get('/about/{user}')
def about(user:str ):
	return {'About Page':f"Hello How are you ? Are you okey {user} !! "}


@app.get('/view')
def view():
	data = laod_data()
	return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='ID of the patient',example='P001 ,P002 etc')):
	data = laod_data()

	if patient_id in data:
		return data[patient_id]
	
	raise HTTPException(status_code=404,detail="Patient not found")


@app.get('/sort')
def sort_patient(sort_by:str = Query(...,description='Give the information to sort according which ',example='height,bmi,weight,etc.'),order:str=Query(...,description='Tell the order of sorting',example="asc or desc")):
	value_field = ['height','weight','bmi']

	if sort_by not in value_field:
		raise HTTPException(status_code=404 , detail=f'Invaild field select from {value_field}')
	
	if order not in ['asc','desc']:
		raise HTTPException(status_code=404,detail='Invalid order of sorting give asc or desc order ')
	
	data = laod_data()

	sorted_order = True if order=='desc' else False

	sorted_data = sorted(data.values(),key=lambda x :x.get('height',0), reverse=sorted_order)

	return sorted_data