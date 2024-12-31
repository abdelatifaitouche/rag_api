import google.generativeai as genai





def chatbot(prompt:str):

    API_KEY = "AIzaSyD9tBP0NaJ6s-vA_qEOwbBtAMu34g1tw9c"


    genai.configure(api_key=API_KEY)

    genai_model = genai.GenerativeModel('models/gemini-1.5-flash')


    response = genai_model.generate_content(prompt)

    return response.text