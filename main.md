# @app.get("/num")
# def sum(a:int,b:int):
# 	return {"a":a,"b":b,"Sum":a+b}


# @app.get("/mul/{x}/{y}")
# def multiply(x: int, y: int):
#     return {"result": f"{x*y}"}


# @app.get("/home")
# def new():
# 	return "This is not a welcome page"


# @app.get('/home/{name}')
# def user(name:str):
# 	return f"Hello {name} to home page"


# @app.get('/square')
# def user(int:int):
# 	return {"square":int**2}

# @app.get('/welcome/{name}/{age}')
# def welcome(name:str,age:int):
# 	return {'message':f"Hello {name} are you {age} old"}


class User(BaseModel):
	name:str
	age:int

@app.post('/register')
def register(user:User):
	return "Okey"

@app.get("/")
def home():
	return {"Message":"Welcome page !!"}

@app.get('/sum/{a}/{b}')
def sum(a:int,b:int):
	return {"a":a,"b":b,"Sum":a+b}

class User(BaseModel):
	name:str
	age:int
	address:str

@app.post('/register')
def register(user:User):
	return {'message':'User Registered !','data':user}

class add(BaseModel):
	num1 : int
	num2 : int

@app.get('/add')
def addition(num1:int,num2:int):
	return f"The sum of these two digit {num1} & {num2} --->{num1+num2}"

@app.get('/greet')
def greet(name:str):
	return f"Welcome {name} to this pagination of virtual world"

class Product():
	p_id:int
	p_name:str
	price:int
	category:str
	
	
@app.product('/product/all')
def product(product:Product):
	return