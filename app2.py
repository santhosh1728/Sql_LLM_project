import streamlit as st
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os
import google.generativeai as genai
import matplotlib.pyplot as plt

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

## Function To retrieve query from the database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Function to create SQLite database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        st.error(e)
    return conn

# Title of the application
st.title('Interactive Data Analysis App')

# File upload component
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file is not None:
    # Read data from uploaded file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file, engine='openpyxl')
    file = uploaded_file.name.split('.')[0].upper()

    ## Define Your Prompt
    prompt = [f"""
    You are an expert in converting English questions to SQL queries and creating data visualizations with Matplotlib!
    The SQL database has the name {uploaded_file.name.split('.')[0].upper()} and contains the following columns - {', '.join(df.columns)}.
    This database is then stored in a SQLite database.

    For example, to display a histogram of a specific column:

    **Prompt:** How can I visualize the distribution of values in the "{column_name}" column using a histogram?

    **SQL Query (example):**
    ```sql
    SELECT "{column_name}" FROM {uploaded_file.name.split('.')[0].upper()};
    ```

    **Python Command (example):**
    ```python
    import matplotlib.pyplot as plt

    # Assuming the retrieved data is stored in 'data'

    plt.hist(data["{column_name}"])
    plt.xlabel("{column_name}")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of values in {column_name}")
    plt.show()
    ```

    **Visualization (example):**
    [Image of a histogram]

    Remember, the SQL code should not have 'sql' in the output and should not be enclosed in ``` at the beginning or end.
    """]

    # Display uploaded data
    st.write("Uploaded Data:")
    st.write(df)

    # SQLite database operations
    connection = create_connection(f"{file}.db")
    if connection is not None:
        # Insert data into SQLite table
        try:
            df.to_sql(f'{file}', connection, if_exists='replace', index=False)
            st.success("Data inserted into SQLite database successfully!")
        except sqlite3.Error as e:
            st.error(f"Error inserting data into SQLite database: {e}")

        # User interface for making operations with prompts and Gemini API key
        st.subheader("Perform Operations with Prompts and Gemini API Key")
        question = st.text_input("Enter Your Operation: ", key="input")
        submit = st.button("Submit")
        if submit:
            response = get_gemini_response(question, prompt)
            print(response)

            # Extract SQL query and Python code from Gemini response
            sql_query, python_code = response.split("```", 2)[1:-1]

            # Execute SQL query and retrieve data
            data = read_sql_query(sql_query, f"{file}.db")

            # Execute Python code
            # Execute Python code for visualization (if applicable)
            if "```python" in response:
                try:
                    # Replace column names with actual data column names
                    python_code = python_code.replace("{column_name}", data.columns[0])  # Assuming data has one column

                    # Execute the Python code using eval (carefully!)
                    eval(python_code)

                    # Optional: Clear existing plot before rendering a new one
                    # plt.clf()

                    # Call st.pyplot within rendering context
                    st.pyplot()
                except Exception as e:
                    st.error(f"Error executing Python code for visualization: {e}")

            # Display the response (SQL query and Python code, if applicable)
            st.subheader("The Response is:")
            st.write("**SQL Query:**")
            st.code(sql_query)
            if "```python" in response:
                st.write("**Python Code (for Visualization):**")
                st.code(python_code)

        # Close the connection
        connection.close()
