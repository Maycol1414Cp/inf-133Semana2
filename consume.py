from zeep import Client
client = Client(
    "https://dataaccess.com/webservicesserver/numberconversion.wso?WSDL"
)
result = client.service.NumberToWords(124)
print(result)