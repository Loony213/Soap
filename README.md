# Hello World in Python SOAP - Docker Image

This Docker image contains a simple Python Flask SOAP service that prints a "Hello, World!" message via a SOAP endpoint.

## Contents of the Image

The image contains the following files and configurations:

- **app.py:**:  The main Python script that defines a simple Flask SOAP service using the spyne library
- **Dockerfile**: Configuration file that defines the Docker image, the Python environment, and the steps needed to run the application when the container starts.
- **requirements.txt:**: List of Python dependencies, including Flask and Spyne
- **Flask:**:  Uses the base Python image and installs the necessary libraries to run the SOAP service.

## How to Use This Image

To run the program on your machine, make sure Docker is installed. Then, follow these steps:

- **Run the Docker Container:**:  Once the image is built, you can run the container with the following command:

```bash
docker run -p 5000:5000 kamartinez/pysoap:v4

**Access the API**:  After the container is running, you can access the API endpoint by opening your browser or using curl:

```bash
curl http://localhost:5000/soap
