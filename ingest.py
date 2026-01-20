from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load TXT runbook
loader = TextLoader("runbooks/prod_runbook.txt")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100
)
chunks = splitter.split_documents(documents)

# Create embeddings (uses OPENAI_API_KEY)
embeddings = OpenAIEmbeddings()

# Store in FAISS
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save index
vectorstore.save_local("runbook_index")

print("✅ Runbook indexed successfully")
