# Order Service

This service uses the Python Flask web framework to expose a POST method that receives JSON orders (see `order_example.json`). The service is secured using HTTPBasicAuth.

## Features

- **Order Handling**: Receives orders in JSON format.
- **Database Integration**: Saves the orders to an SQLite database with two tables: `orders` and `candleItems`.
- **Messaging**: Sends the order formatted as a WhatsApp message using GreenAPI.
- **Containerization**: Includes a `Dockerfile` to dockerize the service, accessible via exposed port `8765`.
- **Testing**: Sample tests included using `pytest`.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite
- GreenAPI
- Docker
- pytest

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JonathanYK/order-service.git
    cd order-service
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**:
    ```bash
    python setup_db.py
    ```

4. **Run the Flask app**:
    ```bash
    python app.py
    ```

5. **Run the tests**:
    ```bash
    pytest
    ```

### Docker

To build and run the Docker container:

1. **Build the Docker image**:
    ```bash
    docker build -t order-service .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 8765:8765 order-service
    ```

### Usage

Send a POST request with the order JSON to the service:
  ```bash
  curl -X POST http://localhost:8765/order -u username:password -H "Content-Type: application/json" -d @order_example.json
  ```

### Important Notice
**Before executing the project, please make sure to update the `.env` file with the necessary configurations.**
