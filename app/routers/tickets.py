from fastapi import APIRouter

router =  APIRouter()

@router.get("/tickets")
def get_tickets():

    return {
        "tickets":[
            {
            "id":1,
            "title":"Laptop Wi-Fi not working",
            "status":"open"
            },
            {
            "id": 2,
            "title": "Unable to access email",
            "status": "in_progress"
            } 
        ] 
    }