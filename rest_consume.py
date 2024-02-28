import requests
card_number = "BT1-010"
url=f"https://digimoncard.io/apip-public/search.php?card={card_number}"
respose = requests.request(
    method="GET",
    url=url,
    headers={"Content-Type":"application/json"},
    data={}
    )
print(respose.text)
