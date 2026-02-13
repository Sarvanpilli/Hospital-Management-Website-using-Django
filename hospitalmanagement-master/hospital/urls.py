from hospital.views_chatbot import chatbot_response

urlpatterns = [
    # ... existing urls ...
    path('chatbot/', chatbot_response, name='chatbot_response'),
] 