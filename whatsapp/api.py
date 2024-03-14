import requests

url = "https://graph.facebook.com/v18.0/246226881906387/messages"

headers = {
    "Authorization": "Bearer EAAFQ4eZAYAY8BO9z1Df36co46bqAKsvS97riOn8gagwOMGOcsz6ZCdHbXaZBlWJgg2pUy04VgU5dlaTF1YH7ZBeZCQLzD26sG4jcBOPvywFawkwxPeB66pYLVeWmHU59x99ULukcfbvEkoFh5gAgZCd1LdifVZBpwtVMhlgI2WJF0laqo4uOX9ZATt7gnKzTcSTvxQYOZBDP6s07e1w2AF3VM",
    "Content-Type": "application/json",
}

data = {
    "messaging_product": "whatsapp",
    "to": "919321878531",
    "type": "template",
    "template": {"name": "snehil", "language": {"code": "en_US"}},
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
