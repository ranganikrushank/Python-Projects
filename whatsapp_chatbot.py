from flask import Flask, request
from flask_socketio import SocketIO
import requests

app = Flask(__name__)
socketio = SocketIO(app)

def send_whatsapp_message(phone_number, message):
    url = "https://api.twilio.com/2010-04-01/Accounts/YOUR_TWILIO_ACCOUNT_SID/Messages.json"
    auth = ("YOUR_TWILIO_ACCOUNT_SID", "YOUR_TWILIO_AUTH_TOKEN")
    data = {
        "To": f"whatsapp:{phone_number}",
        "From": "whatsapp:+917778888578",
        "Body": message,
    }
    requests.post(url, data=data, auth=auth)

@app.route('/send_message', methods=['POST'])
def send_message():
    phone_number = request.form['phone_number']
    message = request.form['message']
    send_whatsapp_message(phone_number, message)
    return 'Message sent'

if __name__ == '__main__':
    socketio.run(app)
