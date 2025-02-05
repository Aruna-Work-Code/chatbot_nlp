from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper
import generic_file


app = FastAPI()

inprogress_orders = {}

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()
    
    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from DialogFlow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    
    session_id = generic_file.extract_session_id(output_contexts[0]['name'])
    
    
    intent_handler_dict = {
        'order.add - context: ongoing-order': add_to_order,
        'order.complete - context: ongoing-order': complete_order,
        #'order.remove - context: ongoing-order': remove_from_order,
        'track.order - context: ongoing-tracking': track_order
    }
    
    return intent_handler_dict[intent](parameters, session_id)

def add_to_order(parameters: dict, session_id: str):
    dress_items = parameters["dress-item"]
    quantities = parameters["number"]

    if len(dress_items) != len(quantities):
        fulfillment_text = "Sorry I didn't understand. Can you please specify dress items and quantities clearly"
    else:
        new_dress_dict = dict(zip(dress_items, quantities))
        
        if session_id in inprogress_orders:
            current_dress_dict = inprogress_orders[session_id]
            current_dress_dict.update(new_dress_dict)
            inprogress_orders[session_id] = current_dress_dict     
        else:
            inprogress_orders[session_id] = new_dress_dict
            
        order_str = generic_file.get_str_from_dress_dict(inprogress_orders[session_id])
        
        fulfillment_text = f"So far you have: {order_str}. Do you need anything else?"    

    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
    })


def complete_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text = "I'm having a trouble finding your order. Sorry! Can you place a new order"
    else:
        order = inprogress_orders[session_id]
        order_id = save_to_db(order)
        
        if order_id == -1:
            fulfillment_text = "Sorry, I couldn't process your order due to backend error. " \
                "Please place a new order again"
                
        else:
            order_total = db.helper.get_total_order_price(order_id)
            fulfillment_text = f"Awesome. We have placed your order. " \
                f"Here is your order id # {order_id}, " \
                f"Your order total is {order_total} which you can pay at the time of delivery!"
                    
                    
        del inprogress_orders[session_id]
                    
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
    })
    
    
    
def save_to_db(order: dict):
    next_order_id = db_helper.get_next_order_id()
    
    
    for dress_item, quantity in order.items():
        rcode = db_helper.insert_order_item(
            dress_item,
            quantity,
            next_order_id
        )
        
        if rcode == -1:
            return -1
        
    rcode = db.helper.insert_order_tracking(next_order_id, "in progress")
    
    return next_order_id
        
        
def track_order(parameters: dict, session_id: str):
    order_id = int(parameters['order_id'])
    order_status = db_helper.get_order_status(order_id)
      
    if order_status:
        fulfillment_text = f"The order status for order id: {order_id} is {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"
        
        
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
    })

