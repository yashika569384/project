from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] ="your-groq-api-key"


llm = ChatGroq(
    model="llama-3.3-70b-versatile",  
    temperature=0.7
)


template = """You are a helpful assistant.
Topic: {topic}

Give a clear explanation with:
1. Introduction
2. Key concepts
3. Conclusion

Response:"""

prompt = PromptTemplate(input_variables=["topic"], template=template)


chain = prompt | llm


topic = input("Enter a topic: ")
response = chain.invoke({"topic": topic})

print("\n--- Generated Response ---")
print(response.content)