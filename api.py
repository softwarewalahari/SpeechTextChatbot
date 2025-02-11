import google.generativeai as genai

# 🔹 Replace 'YOUR_API_KEY_HERE' with your actual API key
API_KEY = "AIzaSyCgsuE2irqE8Bsupq2_bh3Icp4fGQU5CSY"

# 🔹 Configure the API
genai.configure(api_key=API_KEY)

# 🔹 Create a model instance (Gemini-Pro)
model = genai.GenerativeModel("gemini-pro")

# 🔹 Start a chat session
chat = model.start_chat()

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

# 🔹 Chat loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("🤖 Chatbot: Goodbye!")
        break

    response = chat.send_message(user_input)
    print("🤖 Chatbot:", response.text)
