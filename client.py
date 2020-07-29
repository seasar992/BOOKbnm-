import requests

files={'file':open(r'C:\Users\Zhao Fulong\Desktop\000.jpg','rb')}
r=requests.post('http://127.0.0.1:8080/test',files=files)

print(r.text)