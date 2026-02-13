import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # Gemini Generative AI API endpoint
        url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=" + settings.GEMINI_API_KEY
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {"parts": [{"text": user_message}]}
            ]
        }
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            print("Gemini API status code:", response.status_code)
            print("Gemini API response:", response.text)
            response.raise_for_status()
            result = response.json()
            # Extract the generated text
            bot_reply = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sorry, I could not understand that.")
        except Exception as e:
            print("Gemini API error:", e)
            bot_reply = "Sorry, there was an error connecting to the AI service."
        return JsonResponse({"reply": bot_reply})
    return JsonResponse({"error": "POST request required"}, status=400) 