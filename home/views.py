from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "you not getting my API key bro"


# Create your views here.
def home(request):
    return render(request, "index.html")

def chatAPI(request):
    if request.method == "POST":
        user_message = request.POST["prompt"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return JsonResponse(response)
    
    return HttpResponse("Bad request")
