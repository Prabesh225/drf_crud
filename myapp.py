import requests
import json

URl='http://127.0.0.1:8000/studnet/'

# def get_data(id=None):
#     data={}
#     if id is not None:
#         data={'id':id}
#         json_data=json.dumps(data)
#         r=requests.get(url=URl, data=json_data)
#         data=r.json()
#         print(data)

# get_data()

def Post_data():
    data={
        'name':'John Doe',
        'roll':123,
        'address':'123 Main St'
    }
    headers={'Content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URl, data=json_data)
    data=r.json()
    print(data)

Post_data()