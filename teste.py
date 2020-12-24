import requests

url = 'https://webhookifestalk.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
    "message": "Oi",
    "sender": 1,
    }

x = requests.post(url, json = myobj)
print(x.text)