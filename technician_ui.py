import requests
def display(technician):
    req=requests.technician_get(technician)
    if req==[]:
        print("no requests")
    else:
        print(req)