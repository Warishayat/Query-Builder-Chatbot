# Query-Builder-Chatbot

Query-Builder-Chatbot is a Streamlit application that assists users in generating SQL queries based on natural language input. It uses LangChain and Google's Generative AI model for language understanding and query generation.

## Features

- Interactive user interface with Streamlit
- Natural language input for generating SQL queries
- Pre-defined examples for common queries
- Real-time query generation using Google Generative AI model

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Warishayat/Query-Builder-Chatbot
   cd Query-Builder-Chatbot
   ```

2. **Create a virtual environment**

   Create a virtual environment named `chatbot`:

   ```bash
   python3 -m venv chatbot
   ```

3. **Activate the virtual environment**

   - For Windows:
     ```bash
     chatbot\Scripts\activate
     ```
   - For macOS and Linux:
     ```bash
     source chatbot/bin/activate
     ```

4. **Install dependencies**

   Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**

   Create a `.env` file in the project root directory and add your Google API key:

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

1. **Run the application**

   Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the chatbot**

   - Enter your natural language query in the text input box.
   - Click the 'Submit' button to generate the SQL query.
   - View the generated SQL query displayed on the screen.

## Docker Setup

1. **Build the Docker image**

   ```bash
   docker build -t query-builder .
   ```

2. **Run the Docker container**

   ```bash
   docker run -p 8501:8501 query-builder
   ```

3. **Access the application**

   - On your local machine: `http://localhost:8501`
   - On your local network: `http://192.168.18.149:8501`

## Examples

Here are some example inputs and their corresponding SQL queries:

- **Input:** Show me all employees whose salary is more than 50000.
  **Output:** `SELECT * FROM employees WHERE salary > 50000;`

- **Input:** Find all customers from New York who made a purchase last month.
  **Output:** `SELECT * FROM customers WHERE city = 'New York' AND last_purchase_date >= '2024-10-01';`

- **Input:** Get the names of all products in the 'Electronics' category.
  **Output:** `SELECT product_name FROM products WHERE category = 'Electronics';`

- **Input:** List all orders placed by customers who are from California.
  **Output:** `SELECT * FROM orders WHERE customer_id IN (SELECT customer_id FROM customers WHERE state = 'California');`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
```
