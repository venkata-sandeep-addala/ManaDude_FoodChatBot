from fastapi import FastAPI
from fastapi import Request
import db_helper

    
app = FastAPI()

@app.post("/")
async def dialogflow_webhook(request: Request):
    payload = await request.json()

    intent = payload["queryResult"]["intent"]["displayName"]
    parameters = payload["queryResult"]["parameters"]
    session = payload["session"]
    
    session_id = session.split("/")[-1]
    
    intent_handlers = {
        "order.add - context: ongoing-order": add_to_order,
        # "order.remove - context: ongoing-order": remove_from_order,
        # "order.complete - context: ongoing-order": complete_order,
        "track.order - context: ongoing-tracking": track_order
    }

    return intent_handlers[intent](parameters, session_id)

def add_to_order(parameters: dict, session_id: str):
    
    food_item = parameters['food-item']
    quantity = int(parameters['number'])
    
    return {"fulfillmentText": f"Added {quantity} of {food_item} to your order."}
    
def track_order(parameters: dict, session_id: str):
    
    order_id = int(parameters['orderid'])
    status = db_helper.get_order_status(order_id)
    
    if status is None:
        return {"fulfillmentText": f"Sorry, I couldn't find any order with ID {order_id}."}
    
    return {"fulfillmentText": f"The status of your order {order_id} is: {status}"}