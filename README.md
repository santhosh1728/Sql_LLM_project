# SQL_LLM_Project

This repository contains a project that integrates a Local Language Model (LLM) application with a SQL database, enabling users to query and interact with the database using natural language. The project utilizes **Streamlit** for the web interface and **Gemini Pro** for LLM capabilities, providing a user-friendly environment for seamless database interaction.

In addition to standard SQL queries, this project also includes an advanced feature: **interactive plots** based on SQL query outputs, implemented in `app2.py`.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Local Server](#local-server)
- [Key Components](#key-components)
- [Interactive Plots (app2.py)](#interactive-plots-app2.py)
- [Try it Yourself](#try-it-yourself)
- [Google API Key](#google-api-key)

## Installation

To set up the project locally, follow these steps:

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

For interactive plots, you can run:
```sh
streamlit run app2.py
```

## Usage

After setting up the project, you can interact with the application through a local server. The main functionalities include querying the SQL database using natural language and interacting with the generated results through a streamlined interface.

### Local Server

Once running, you can access the application locally at: [http://localhost:8501](http://localhost:8501).

## Project Structure

```
SQL_LLM_project/
├── app.py
├── app2.py               # For interactive plots
├── requirements.txt
├── venv/
├── README.md
└── ...
```

## Key Components

- **SQL Database (SQLite):** The project provides functionality for inserting and managing records in an SQLite database using Python.
- **LLM Application (Gemini Pro):** The Local Language Model processes natural language queries and converts them into SQL queries, executed on the SQLite database.
- **Streamlit Interface:** A web-based interface that enables users to input queries and view results, as well as interactive visualizations.
- **Interactive Plots (app2.py):** Attempts to create visual plots like bar charts and line graphs from the SQL query results, allowing users to explore data visually.

## Prompts and Workflow

The application follows this workflow:

1. **User Prompt -> LLM (Gemini Pro):** The user inputs a natural language query.
2. **LLM -> SQL Query:** The query is converted into an SQL query.
3. **SQL Query -> Database:** The SQL query is executed, fetching the relevant data from the database.
4. **Response -> User Interface:** The results are displayed, either as text or visualized through plots (if using `app2.py`).

## Interactive Plots (app2.py)

The file `app2.py` includes functionality to generate interactive plots based on the SQL query output. It offers a dynamic experience where users can visualize data in different formats, making the query results more intuitive and insightful. If use wish to contribute do contribute on this file.

## Try it Yourself

A live version of the project can be found at: [https://dbmscapstone.streamlit.app/](https://dbmscapstone.streamlit.app/)

## Google API Key

Some advanced features might require a Google API key. You can obtain it by visiting the [Google API Key page](https://aistudio.google.com/app/apikey).

---

By following these steps, you should be able to set up and run the SQL_LLM_Project with ease. The README outlines the project components and provides guidance to ensure a smooth experience with both basic queries and advanced interactive visualizations.
