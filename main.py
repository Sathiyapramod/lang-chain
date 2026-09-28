from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant specialized in {topic}."),
    ("human", "{question}"),
])

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

chain = prompt | model | StrOutputParser()


def main():
    response = chain.invoke({
        "topic": "Python programming",
        "question": "What is the difference between a list and a tuple?",
    })
    print(response)


if __name__ == "__main__":
    main()
