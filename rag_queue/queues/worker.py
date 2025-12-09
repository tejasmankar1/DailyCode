from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

###vector Embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

###vector db

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding = embedding_model
)

async def process_query(query:str):
    print("Searching Chunks: ",query)
    search_results = vector_db.similarity_search(query=query)

    context = "\n\n\n".join([f"Page_content: {result.page_content}\nPage_number: {result.metadata['page_label']}\nFile_location: {result.metadata['source']}"for result in search_results])

    SYSTEM_PROMPT = """
    You are a helpfull AI Assistant who answeres user query based on the available context retrieved from a PDF file along with page_contents and page number.

    You should only ans the user based on the following context and navigate the user to open the right page number to know more.

    Context : {context}
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role" : "system", "content" : SYSTEM_PROMPT},
            {"role" : "user", "content" : query}
        ]
    )
    print(f"🤖: {response.choices[0].message.content}")
    return response.choices[0].message.content