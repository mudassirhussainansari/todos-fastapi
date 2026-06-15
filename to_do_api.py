from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    description: str
    is_complete: bool = False

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"todos created successfully",
        "Data":[item.model_dump() for item in todos]
    }
    
@app.get("/todos")
def get_todos():
    return {
        "message": "success",
        "data": todos
    }

@app.get("/todos/{id}")
def get_todo_id(id:int):
    for todo in todos:
        if todo.id == id:
            return {
                "message": "success",
                "data": todo
            }
    return {
        "error": "todo not found"
    }
    
@app.put("/todos/{id}")
def update_todo(id:int, update_todo: Todo):
    for index,todo in enumerate(todos):
        if todo.id == id:
            todos[index] = update_todo
            return {
                "message": "successfully updated",
                "data":update_todo
            }
        else:
            return {
                "error": "todo not found"
                }
            
@app.delete("/todos/{id}")
def delete_todo(id:int):
    for index,todo in enumerate(todos):
        if todo.id == id:
            todo.pop(index)
            return {
                "message": "successfully deleted"}
    return {"message": "todo not found"}


