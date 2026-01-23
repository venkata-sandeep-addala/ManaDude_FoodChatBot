from fastapi import FastAPI
from fastapi import Request
import db_helper
import generic_helper
    
app = FastAPI()

inprogress_orders = {}

@app.post("/")
async def dialogflow_webhook(request: Request):
    payload = await request.json()

    intent = payload["queryResult"]["intent"]["displayName"]
    parameters = payload["queryResult"]["parameters"]
    session = payload["session"]
    
    session_id = session.split("/")[-1]
    
    intent_handlers = {
        "new.order - context: ongoing-order": new_order,
        "order.add - context: ongoing-order": add_to_order,
        "order.remove - context: ongoing-order": remove_from_order,
        "order.complete - context: ongoing-order": complete_order,
        "track.order - context: ongoing-tracking": track_order
    }

    return intent_handlers[intent](parameters, session_id)


def new_order(parameters: dict, session_id: str):
    inprogress_orders[session_id] = {}
    return {"fulfillmentText": "Sure! You can start adding items to your order."}

def save_to_db(order: dict):
    next_order_id = db_helper.get_next_order_id()

    for food_item, quantity in order.items():
        rcode = db_helper.insert_order_item(
            food_item,
            quantity,
            next_order_id
        )

        if rcode == -1:
            return -1

    db_helper.insert_order_tracking(next_order_id, "in progress")

    return next_order_id


def complete_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text = "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
    else:
        order = inprogress_orders[session_id]
        order_id = save_to_db(order)
        if order_id == -1:
            fulfillment_text = "Sorry, I couldn't process your order due to a backend error. Please place a new order again"
        else:
            
            order_total = db_helper.get_total_order_price(order_id)
            
            fulfillment_text = f"Awesome. We have placed your order. " \
                           f"Here is your order id # {order_id}. " \
                           f"Your order total is {order_total} which you can pay at the time of delivery!"\
                           f"Thank you for ordering with us!"
            
        del inprogress_orders[session_id]
    return {"fulfillmentText": fulfillment_text}


def remove_from_order(parameters: dict, session_id: str):
    food_items = parameters['food-item']
    items_not_in_order = []
    if session_id in inprogress_orders:
        current_order = inprogress_orders[session_id]
        for item in food_items:
            if item in current_order:
                del current_order[item]
            else:
                items_not_in_order.append(item)
        inprogress_orders[session_id] = current_order
    else:
        return {"fulfillmentText": "You don't have any ongoing order to remove items from.Please add items first."}
    
    if session_id in inprogress_orders and inprogress_orders[session_id]:
        order_str = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
        items_not_in_order = ", ".join(items_not_in_order)
        if items_not_in_order:
            return {"fulfillmentText": f"{items_not_in_order} item(s) are not in your order \n You have following items in your order {order_str}. You can add more items or complete the order."}
        else:
            return {"fulfillmentText": f"Updated order: {order_str}. You can add more items or complete the order."}
    else:
        return {"fulfillmentText": "Your order is now empty. You can add new items to your order."}

def add_to_order(parameters: dict, session_id: str):
    
    food_items = parameters['food-item']
    quantities = parameters['number']
    
    if len(food_items) != len(quantities):
        return {"fulfillmentText": "The number of food items and quantities do not match."}
    
    else:
        
        new_items = dict(zip(food_items, quantities))
        
        if session_id in inprogress_orders:
            current_order = inprogress_orders[session_id]
            for key, value in new_items.items():
                if key in current_order:
                    current_order[key] += value
                else:
                    current_order[key] = value
            inprogress_orders[session_id] = current_order
        else:
            inprogress_orders[session_id] = new_items
    order_str = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
    
    return {"fulfillmentText": f"So far your order contains: {order_str}. You can add more items or complete the order."}
    
    
    

def track_order(parameters: dict, session_id: str):
    
    order_id = int(parameters['orderid'])
    status = db_helper.get_order_status(order_id)
    
    if status is None:
        return {"fulfillmentText": f"Sorry, I couldn't find any order with ID {order_id}."}
    
    return {"fulfillmentText": f"The status of your order {order_id} is: {status}"}