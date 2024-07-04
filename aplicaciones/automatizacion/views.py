from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.http import HttpResponse
from datetime import datetime
import json 


import google.generativeai as genai
 
# Create your views here.
# add here to your generated API key
genai.configure(api_key="AIzaSyDDURhIdmkTmkxvPKTnya0kg63hGStcSkk")
from django.views.decorators.csrf import csrf_exempt

data_example = {
  "trabajos": [
    {
      "nombre": "Modista",
      "telefono" : "000000"
    },
    {
      "nombre": "Plomero",
      "telefono" : "000000"
    },
    {
      "nombre": "Pintor",
      "telefono" : "000000"
    },
    {
      "nombre": "Cortador de césped",
      "telefono" : "000000"
    }
  ]
}
data_example = json.dumps(data_example)
print("tipo data example", type(data_example))

def chat(request):

    if request.method == 'GET':
        print("GET METODO")
        model =genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        user_text = f"Hola, te vas a comportar como un asistente que me ayuda a elegir cual es la mejor persona para ayudarme, te voy a compartir una tabla con las personas encargadas de cada area y sus cualidades, vas a estar hablando con una persona entonces necesito que actues de la forma mas cordial posible, la tabla de gente es la siguiente {data_example}"
        response = chat.send_message(user_text)
        response_data = {
            "text": response.text,
        }
        return render(request, 'chat.html', response_data)

    if request.method == 'POST':
        user_text = request.POST.get('user_text')
        model =genai.GenerativeModel("gemini-pro")
        user_text =  f"de acuerdo a la conversacion este el mensaje de mi cliente, responde como si fueras un chatbot:, responde basado en la base de datos: {data_example} {user_text}"
        chat = model.start_chat()
        response = chat.send_message(user_text)
        response_data = {
            "text": response.text,
        }
        return render(request, 'chat.html', response_data)
    
    else:
        return render(request, 'chat.html')
