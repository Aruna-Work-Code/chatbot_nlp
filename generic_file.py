import re  


def extract_session_id(session_str: str):

    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    
    return "" 

def get_str_from_dress_dict(dress_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in dress_dict.items()])
    




# To know whether the session is fetching or not
if __name__=="__main__":
    print(get_str_from_dress_dict({"kurta set": 2, "plazza": 3}))
    
    # print(extract_session_id("projects/hopper-chatbot-for-vivavi-sqmw/agent/sessions/96815ab9-ce35-1178-4359-ea7e9a954197/contexts/ongoing-order"))
    
