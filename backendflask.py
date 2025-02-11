from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# 🔹 Replace with your actual API key
API_KEY = "AIzaSyCgsuE2irqE8Bsupq2_bh3Icp4fGQU5CSY"

# 🔹 Configure Google Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# 🔹 Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"response": "Please enter a message!"})

    # 🔹 Get AI response
    response = model.generate_content(user_message)
    bot_reply = response.text if response else "I'm sorry, I couldn't generate a response."

    # 🔹 Add Custom Bot Name ("HarithaBot")
    return jsonify({"response": f"🤖 Harithafriend: {bot_reply}"})

if __name__ == "__main__":
    app.run(debug=True)
