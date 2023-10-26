from fastapi import FastAPI, HTTPException
from typing import List
from User import User, UpdateUser
import uvicorn
from uuid import uuid4, UUID


app = FastAPI()

# Create a simple data base:
db: List[User] = [
    User(
        id=uuid4(),
        name="Albert Einstein",
        age=76,
    ),
    User(
        id=uuid4(),
        name="Marie Curie",
        age=66,
    ),
    User(
        id=uuid4(),
        name="Stephen Hawking",
        age=76,
    ),
    User(
        id=uuid4(),
        name="Katherine Johnson",
        age=101,
    ),
]


# Start app:
@app.get("/")
async def root():
    return {"greeting": "Hello world, welcome to my FastAPI :)"}


# Get all users:
@app.get("/api/v1/users")
async def get_all_users():
    return db


# Get a user by id:
@app.get("/api/v1/users/{id}")
async def get_user_by_id(id: UUID):
    for user in db:
        if user.id == id:
            return {"name": user.name, "age": user.age}
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")


# Create new user:
@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


# Update a user:
@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.name is not None:
                user.name = user_update.name
            if user_update.age is not None:
                user.age = user_update.age
        return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")


# Deleted a user:
@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
    return
    raise HTTPException(
        status_code=404,
        detail=f"Delete user failed, id {id} not found."
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
