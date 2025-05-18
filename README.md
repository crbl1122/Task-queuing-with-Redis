Implementing Redis Task Queues with Flask and Docker Compose

This project demonstrates how to implement Redis-based task queues in a Flask application and deploy the setup using Docker Compose.
🧰 Features

    Asynchronous task processing using Redis queues

    Flask web application for task submission

    Background worker to process queued tasks

    Containerized deployment with Docker Compose
    TestDriven.io

📦 Prerequisites

    Docker

    Docker Compose
    Anto Subash

🚀 Getting Started

    Clone the repository:

    git clone https://github.com/yourusername/redis-task-queue.git
    cd redis-task-queue

    Build and start the services:

    docker-compose up --build

    Access the Flask application:

    Navigate to http://localhost:5000 in your web browser.

🛠️ Project Structure

├── app/
│   ├── app.py           # Flask application
│   ├── worker.py        # Background worker script
│   └── tasks.py         # Task definitions
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image for Flask app and worker
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # Project documentation

⚙️ Docker Compose Services

    web: Runs the Flask application.

    worker: Processes tasks from the Redis queue.

    redis: In-memory data store used as a message broker.
    Medium+4TestDriven.io+4blog.abbasmj.com+4
    Amazon Web Services, Inc.+1Stack Overflow+1
    Squash+3Anto Subash+3Medium+3

📖 Acknowledgments

This implementation is based on the tutorial by Abbas Mohammed: Implementing Redis Task Queues and Deploying on Docker Compose
