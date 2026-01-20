from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

# Load embeddings
embeddings = OpenAIEmbeddings()

# Load FAISS index
vectorstore = FAISS.load_local(
    "runbook_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are a senior Production Support Engineer.

Answer ONLY using the runbook content below.
If the issue is not mentioned, say:
"Not found in runbook. Escalate to L3 support."

Runbook Content:
{context}

User Issue:
{question}

Provide:
1. Root cause
2. Step-by-step resolution
3. Validation steps
""")

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# -------- CLI LOOP --------
while True:
    query = input("\n🛠️ Enter production issue (or 'exit'): ")
    if query.lower() == "exit":
        break

    # 1. Retrieve relevant docs
    docs = retriever.invoke(query)

    # 2. Combine docs into context
    context = "\n\n".join(doc.page_content for doc in docs)

    # 3. Build prompt
    messages = prompt.invoke({
        "context": context,
        "question": query
    })

    # 4. Call LLM
    response = llm.invoke(messages)

    print("\n📘 Runbook Response:\n", response.content)
