import json
# import pickle
import requests 

with open("response1.json","r")as f:
    data = json.load(f)

print (data['receipts'][0].keys())

items = data['receipts'][0]['items']
print(items)

for item in items:
    print(f"{item['description']} - ${item['amount']}")

print(f"Subtotal:{data['receipts'][0]['currency']} {data['receipts'][0]['subtotal']}")
print(f"Total:{data['receipts'][0]['total']}")
# url = "https://ocr.asprise.com/api/v1/receipt"
# image = "r.jpg"


# res = requests.post(url,data={
#     'api_key': 'TEST',
#     'recognizer': 'auto',
#     'ref_no': 'oct_python_123'
#     },
#     files = {
#     'file': open(image,'rb')
#     })
# with open("response1.json","w")as f :json.dump(json.loads(res.text),f)