import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # load Google API key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # Load Model

st.title("Query-Builder-Chatbot")
st.subheader("Your Query-Builder Buddy")
query = st.text_input("write to generate the query")
submit = st.button('Subject')
examples = [
    {
        "input": "Show me all employees whose salary is more than 50000.",
        "output": "SELECT * FROM employees WHERE salary > 50000;"
    },
    {
        "input": "Find all customers from New York who made a purchase last month.",
        "output": "SELECT * FROM customers WHERE city = 'New York' AND last_purchase_date >= '2024-10-01';"
    },
    {
        "input": "Get the names of all products in the 'Electronics' category.",
        "output": "SELECT product_name FROM products WHERE category = 'Electronics';"
    },
    {
        "input": "List all orders placed by customers who are from California.",
        "output": "SELECT * FROM orders WHERE customer_id IN (SELECT customer_id FROM customers WHERE state = 'California');"
    },
    {
        "input": "who is the pm of pakistan?",
        "output": "sorry i just only have Query related knowledge."
    },
    {
        "input": "2+2 is =",
        "output": "sorry i just only have Query related knowledge."
    }
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}")
])

fewshot = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a help assistant for creating queries based on the user's input."),
    fewshot,
    ("human", "{query}")
])
if submit:
    if query:
        formatted = final_prompt.format_messages(query=query)
        result = llm.invoke(formatted)
        res = result.content
        st.write(res)
