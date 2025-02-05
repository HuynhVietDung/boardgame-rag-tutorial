# Board Game Assistant using RAG

This repository is for learning how to use Retrieval-Augmented Generation (RAG) with Ollama to answer questions about 6 boardgames: Uno, Exploading Kittens, Bang!, Werewolves, Monopoly and Ticket to Ride. Follow the steps below to set up and run the project.

## Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd boardgame-rag-tutorial
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Setting Up the Database

1. Place your PDF documents in the data directory. You should name the files to the name of boardgames.
 
2. Populate the database with the documents:
    ```sh
    cd src
    python populate_database.py --reset
    ```

## Querying the Database

To query the database, run the query.py script with your query text:
```sh
python query.py "Your query text here"
```
## Project Structure
