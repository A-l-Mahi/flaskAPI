from flask import Flask, request, jsonify
import json
import requests

app  = Flask(__name__)


@app.route('/admin', methods = ['POST'])
def create_admin():
    
    req_Json = request.json

    url =  "https://p1haj6tplc.execute-api.us-east-2.amazonaws.com/test/umg"

    payload = {
        "method":"POST",
        "type":"user",
        "body": {
            "accountId": req_Json['id'],
            "email": "value2@ssaas.com",
            "password": "BUNSHino1818",
            "fullname": "dadasd",
            "zoneId":"Kankia",
            "role" : "admin",
            "phone": "0802322334"
        }
    }

    response = requests.post(url, data = json.dumps(payload))

    print(response)
    bo = json.dumps(response.text)  
   
    return {'status': bo} 


if __name__ == '__main__':
    app.run()
