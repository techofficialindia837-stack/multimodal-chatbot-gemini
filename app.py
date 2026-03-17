import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyClLleub1jtMqCPPv0yf5FbZ3AGeX_wX3U")

model = genai.GenerativeModel("gemini-2.5-flash")

def chatbot(prompt, image_path=None):

    if image_path:
        img = Image.open(image_path)
        response = model.generate_content([prompt, img])
    else:
        response = model.generate_content(prompt)

    return response.text


while True:

    user_input = input("Ask: ")

    if user_input == "exit":
        break

    img_path = input("Image path (optional): ")

    if img_path == "":
        print(chatbot(user_input))
    else:
        print(chatbot(user_input, img_path))