import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())
 
# условная база данных - набор объектов Person
people = [Person("Tom", 38), Person("Bob", 42), Person("Sam", 28)]
 
# для поиска пользователя в списке people
def find_person(id):
   for person in people: 
        if person.id == id:
           return person
   return None
 
app = FastAPI()
 
@app.get("/")
async def main():
    return FileResponse("public/index.html")
 
@app.get("/api/users")
def get_people():
    return people
 
@app.get("/api/users/{id}")
def get_person(id):
    # получаем пользователя по id
    person = find_person(id)
    print(person)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person==None:  
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    #если пользователь найден, отправляем его
    return person
 
 
@app.post("/api/users")
def create_person(data  = Body()):
    person = Person(data["name"], data["age"])
    # добавляем объект в список people
    people.append(person)
    return person
 
@app.put("/api/users")
def edit_person(data  = Body()):
  
    # получаем пользователя по id
    person = find_person(data["id"])
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None: 
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    return person
 
 
@app.delete("/api/users/{id}")
def delete_person(id):
    # получаем пользователя по id
    person = find_person(id)
  
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
  
    # если пользователь найден, удаляем его
    people.remove(person)
    return person


# import uuid
# from fastapi import FastAPI, Body, status
# from fastapi.responses import JSONResponse, FileResponse
# import json
# import flask

# import dbManager

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.id = str(uuid.uuid4())

# class Person_get:
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id


# # условная база данных - набор объектов Person
# people = [Person("Tom", 38), Person("Bob", 42), Person("Sam", 28)]

# # для поиска пользователя в списке people
# def find_person(id):
#    for person in people:
#         if person.id == id:
#            return person
#    return None

# app = FastAPI()


# @app.get("/")
# async def main():
#     return FileResponse("public/index.html")

# @app.get("/api/users")
# def get_people():
#     peoples = []
#     db = dbManager.dbManager.MemsDB()
#     people_db = db.get_all_data_from_db()
#     db.close_DB()

#     for people in people_db:
#         peoples.append(Person_get(name = people[0],age = people[1],id = people[2]))


#     return peoples
#     #return people

# @app.get("/api/users/{id}")
# def get_person(id):
#     # получаем пользователя по id

#     db = dbManager.dbManager.MemsDB()
#     #data = json.loads(data)

#     person =  db.get_data_from_db(id=id)
#  #добавляем объект в список peopl
#     #people.append(person)
#     db.close_DB()
#     #если пользователь найден, отправляем его
#     return Person_get(name=person[0][0], age=person[0][1], id = person[0][2])


# @app.post("/api/users")
# def create_person(data  = Body()):

#     db = dbManager.dbManager.MemsDB()
#     #data = json.loads(data)

#     person = Person(data["name"], data["age"])
#  #добавляем объект в список people
#     db.data_entry(name=str(person.name), age=int(person.age), id=str(person.id))
#     #people.append(person)
#     db.close_DB()
#     return person


# @app.put("/api/users")
# def edit_person(data  = Body()):
#     print(data)

#     db = dbManager.dbManager.MemsDB()
#     # получаем пользователя по id
#     person =  db.get_data_from_db(id=id)

#     db.update_data_from_db(name=data["name"], age=int(data["age"]), id = person[0][2])

#     #person.age = data["age"]
#     #person.name = data["name"]

#     db.close_DB()
#     return person


# @app.delete("/api/users/{id}")
# def delete_person(id):
#     # получаем пользователя по id
#     db = dbManager.dbManager.MemsDB()

#     person = db.get_data_from_db(id=id)
#     db.delete_data_from_db(id=id)

#     ret_person = Person_get(name = person[0][0], age = person[0][1], id= person[0][2])

#     db.close_DB()

#     #people.remove(person)
#     return ret_person
