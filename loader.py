import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from os import listdir
from os.path import isfile, join
from tqdm import tqdm


from langchain_community.document_loaders import UnstructuredURLLoader


urls = [
    "https://aapi.dz/systeme-fiscal/#:~:text=Un%20taux%20normal%20de%2019,23%20du%20code%20des%20TCA."
]


API_KEY = "AIzaSyD9tBP0NaJ6s-vA_qEOwbBtAMu34g1tw9c"
genai.configure(api_key=API_KEY)


genai_model = genai.GenerativeModel('models/gemini-1.5-flash')

chroma_client = chromadb.PersistentClient(path='vector_db')


gemini_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=API_KEY)

chroma_collection = chroma_client.get_or_create_collection(name='finance_gpt' , embedding_function=gemini_ef)


onlyfiles = [f for f in listdir("docs") if isfile(join("docs", f))]


loader = UnstructuredURLLoader(urls=urls)

data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000)

docs  = text_splitter.split_documents(data)

document = []
ids = []
i = 1

for doc in docs : 
    ids.append(str(i))
    i+=1
    document.append(doc.page_content)

    chroma_collection.upsert(
        documents=document,
        ids = ids
    )


"""

for file in tqdm(onlyfiles) : 
    loader = PyPDFLoader("docs/" + file)
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
"""