import requests

WEBHOOK_URL = "https://test.up.railway.app/trigger"
data = {
    "secret": "yoursecret",   # must match server
    "event": "light",
    "args": {"Mode": "active"}
}

r = requests.post(WEBHOOK_URL, json=data)
print(r.status_code, r.json())
