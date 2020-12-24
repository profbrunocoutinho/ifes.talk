import requests

url = 'https://webhookifestalk.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
    "message": "Oi",
    "sender": "Bruno",
    }

x = requests.post(url, json = myobj)
print(x.text)