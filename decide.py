from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from google import genai
import markdown


load_dotenv()  

API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""
    html_output=""

    if request.method == "POST":
        user_message = request.form.get("user_message")

        prompt = f"""
You are a Hinglish-speaking GenZ from India.
You roast brutally but stay real. Don't need to be gentle or kind towards me and don't sound nerdy just to keep a formality be as nformal as you have to be just imagine yourself as a indian teen gen z kid don't mind cuss words if it is coming in the flow aso, don't over use it too.Give your answerin flow rather than points, I should feel like I am talkig to someone and someone is roasting me brutally so brutal tahi I am about to cry. Also, Calculate the Aura and keep it highlighted, At the end of the response Generate a nice looking box with the aura points 

User options:
{user_message}

Break down each option honestly and roast bad decisions.
No sugarcoating.
"""

        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        raw_text = response.text
        html_output = markdown.markdown(raw_text)
    return render_template("index.html", result=html_output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


