''' 
routes for users

//routes
//@router.get('/')               -- to get all users details
//@router.get("/{user_id}")      -- to get a single user details
//@router.post("/")              -- to create a new user 
//@router.put("/{user_id}")      -- to update a user
//@router.delete('/{user_id}')   -- to delete a user
'''

from fastapi import APIRouter



router = APIRouter(
    prefix="/api/v1/users"
)

@router.get('/')
async def get_all_users():
    return ("all users")

@router.get("/{user_id}")
async def get_user(user_id: str):
    return {f"got user with id {user_id}"}

@router.post("/")
async def create_user():
    return {"created a new user"}

@router.put("/{user_id}")
async def update_user(user_id: str):
    return { f"udated user with id {user_id}"}

@router.delete('/{user_id}')
async def delete_user(user_id: str):
    return { f"deleted user with id {user_id}"}


