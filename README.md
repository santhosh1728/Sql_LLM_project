# SQL_LLM_Project

This repository contains a project that integrates a Local Language Model (LLM) application with a SQL database, allowing users to query and interact with the database using natural language. The project uses Streamlit for the web interface and Gemini Pro for LLM capabilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Local Server](#local-server)
- [Key Components](#key-components)
- [Try it Yourself](#try-it-yourself)
- [Google API Key](#google-api-key)

## Installation

Follow these steps to set up the project locally:

1. **Create a virtual environment:**
   ```sh
   conda create -p venv python==3.10 -y
   ```

2. **Activate the virtual environment:**
   ```sh
   conda activate venv/
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```sh
   streamlit run app.py
   ```

## Usage

After setting up the project, you can interact with the application via a local server. The main functionalities include inserting records into an SQLite database and querying the database using the LLM application.

### Local Server

You can browse the application locally at: [http://localhost:8501](http://localhost:8501)

## Project Structure

```
SQL_LLM_project/
├── app.py
├── requirements.txt
├── venv/
├── README.md
└── ...
```

## Key Components

- **SQL Database (SQLite):** The project includes functionality to insert and manage records in an SQLite database using Python.
- **LLM Application:** Integrates Gemini Pro for querying the SQL database and providing responses based on the queries.
- **Streamlit:** Provides the web interface for users to interact with the LLM and the database.

## Prompts and Workflow

The general workflow of the application is as follows:

1. **User Prompt -> LLM (Gemini Pro):** The user inputs a query.
2. **LLM -> SQL Database:** The query is processed and converted into an SQL query.
3. **SQL Database -> Response:** The SQL query is executed, and the response is sent back to the user.

## Try it Yourself

You can try the live version of the application at: [https://dbmscapstone.streamlit.app/](https://dbmscapstone.streamlit.app/)

## Google API Key

For additional functionalities, you may need a Google API key. You can obtain it from [Google API Key](https://aistudio.google.com/app/apikey).

---

By following the above steps, you should be able to set up and run the SQL_LLM_Project seamlessly. This README provides a structured overview and setup instructions to ensure a smooth experience.
