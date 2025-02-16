import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



API_KEY = "AIzaSyD9tBP0NaJ6s-vA_qEOwbBtAMu34g1tw9c"
genai.configure(api_key=API_KEY)


genai_model = genai.GenerativeModel('models/gemini-1.5-flash')

chroma_client = chromadb.PersistentClient(path='vector_db')

gemini_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=API_KEY)

chroma_collection = chroma_client.get_or_create_collection(name='finance_gpt' , embedding_function=gemini_ef)




loader = PyPDFLoader('ldf2025.pdf')
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000)
docs = text_splitter.split_documents(data) 
document = []
ids = []
i = 1
for doc in docs : 
    ids.append(str(i))
    i+=1
    document.append(doc.page_content)


chroma_collection.upsert(
    documents=document,
    ids=ids
)