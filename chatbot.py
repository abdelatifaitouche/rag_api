import google.generativeai as genai



import chromadb
import google.generativeai as genai
from chromadb.utils import embedding_functions




def chatbot(query_text):

    API_KEY = "AIzaSyD9tBP0NaJ6s-vA_qEOwbBtAMu34g1tw9c"
    genai.configure(api_key=API_KEY)


    genai_model = genai.GenerativeModel('models/gemini-1.5-pro')

    chroma_client = chromadb.PersistentClient('vector_db')

    gemini_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=API_KEY)


    collection = chroma_client.get_collection(name='finance_gpt' , embedding_function=gemini_ef)

    n_result = 5


    results = collection.query(
        query_texts=[query_text],
        n_results=n_result,
        include=['documents' , 'distances']
    )

    prompt = "en tant que consultant en finance, Repond a cette question en utilisant le Document comme context"
    prompt += f'question : {query_text}'
    prompt += f"Document : {results['documents']}"



    response = genai_model.generate_content(prompt, stream=False)

    return response.text


