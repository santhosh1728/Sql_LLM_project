import streamlit as st
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os
import google.generativeai as genai
# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
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
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name {uploaded_file.name.split('.')[0].upper()} and contains the following columns - {', '.join(df.columns)}.
    This database is then stored in
    For example:
    Example 1 - How many entries of records are present?
    The SQL command will be something like this: SELECT COUNT(*) FROM {uploaded_file.name.split('.')[0].upper()};

    Example 2 - Retrieve records based on specific criteria?
    The SQL command structure would be: SELECT * FROM {uploaded_file.name.split('.')[0].upper()} WHERE <criteria>;

    In Example 2, '<criteria>' should be replaced with your specific condition to filter the records. This could include any column in the dataset.

    Example 3, SELECT DISTINCT "<Coulumn_Name>" FROM MDI_IOT, if coulmn name has a space in its words then enclose the column name in " " or ' '
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
        question=st.text_input("Enter Your Operation: ",key="input")
        submit=st.button("Submit")
        if submit:
            response=get_gemini_response(question,prompt)
            print(response)
            response=read_sql_query(response,f"{file}.db")
            st.subheader("The Response is")
            for row in response:
                print(row)
                st.header(row)

        # Here you can add code to perform operations based on user input and API key

        # Close the connection
        connection.close()