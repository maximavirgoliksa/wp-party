from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
import json

app = Flask(_name_)

Configuración Twilio
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_WHATSAPP_NUMBER']
client = Client(account_sid, auth_token)

Cargar ofertas
with open("templates.json") as f:
offers = json.load(f)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hola" in incoming_msg:
        msg.body("Hola! ¿Qué tipo de ofertas te interesan? Comida, Tecnología, Moda?")
    elif "comida" in incoming_msg:
        msg.body(f"Estas son las ofertas de comida:offers['comida']")
    elif "tecnologia" in incoming_msg:
        msg.body(f"Estas son las ofertas de tecnología:offers['tecnologia']")
    elif "moda" in incoming_msg:
        msg.body(f"Estas son las ofertas de moda:offers['moda']")
    else:
        msg.body("No entendí. Por favor responde con Comida, Tecnología o Moda.")

    return str(resp)

if _name_ == "_main_":
    app.run(debug=True)
