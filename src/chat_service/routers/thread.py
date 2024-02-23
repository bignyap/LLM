''' thread endpoints '''

import uuid

from fastapi import APIRouter, HTTPException, Depends

import database.database as dbd
import database.thread as dbt

import dependencies.dependencies as dp

router = APIRouter(
    prefix="/thread",
    tags=["thread"],
    dependencies=[Depends(dp.validate_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/create_chat_thread")
async def create_chat_thread(
    name: str = uuid.uuid4(),
    user_details: dict = Depends(dp.validate_token_header),
    cursor =  Depends(dbd.get_db_cursor)
):
    """
    Create a message thread
    
    """
    try:
        res = dbt.create_thread(cursor, name, user_details['azp'])
        return res
    except KeyError as e:
        raise HTTPException(status_code=400, detail="Invalid token") from e
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error while creating the thread") from e
    

@router.get("/list_chat_thread")
async def list_chat_thread(
    user_details: dict = Depends(dp.validate_token_header),
    cursor =  Depends(dbd.get_db_cursor)
):
    """
    Create a message thread
    
    """
    try:
        res = dbt.list_thread(cursor, user_details['azp'])
        return res
    except KeyError as e:
        raise HTTPException(status_code=400, detail="Invalid token") from e
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error while fetching the threads") from e
    

@router.delete("/delete_chat_thread")
async def delete_chat_thread(
    thread_id: int,
    user_details: dict = Depends(dp.validate_token_header),
    cursor =  Depends(dbd.get_db_cursor)
):
    """
    Create a message thread
    
    """
    try:
        res = dbt.delete_thread(cursor, thread_id, user_details['azp'])
        return res
    except KeyError as e:
        raise HTTPException(status_code=400, detail="Invalid token") from e
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error while deleting the threads") from e