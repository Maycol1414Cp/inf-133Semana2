from zeep import Client
client=Client("http://localhost:8008")
result=client.service.saludar("Michael")
print(result)