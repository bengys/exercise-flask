# app.py
from flask import Flask
import docker

app = Flask(__name__)

@app.route('/')
def list_containers():

    client = docker.from_env()
    
    containers = client.containers.list()
    
    container_info = []
    for container in containers:
        container_info.append(f"ID: {container.short_id}, Name: {container.name}, Status: {container.status}")

    return '<br>'.join(container_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
