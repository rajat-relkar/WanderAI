
# WanderAI – AI Travel Itinerary Planner

WanderAI is an **AI-powered travel itinerary planning application** that generates personalized travel plans using Large Language Models (LLMs).
The application is built using **LangChain + Groq LLM**, deployed via **Docker & Kubernetes (Minikube on GCP VM)**, and monitored using a complete **ELK Stack (Filebeat, Logstash, Elasticsearch, Kibana)**.

---

## Key Features

- AI-generated personalized travel itineraries
- Powered by **Groq LLM** via **LangChain**
- Interactive UI built with **Streamlit**
- Containerized using **Docker**
- Deployed on **Kubernetes (Minikube inside GCP VM)**
- Centralized logging and monitoring using **ELK Stack**
- Real-time log visualization in **Kibana Dashboards**
- Version-controlled using **GitHub**

---

## High-Level Architecture

 <img width="1350" height="811" alt="AI+travel+planner+Workflow" src="https://github.com/user-attachments/assets/17d8c285-6c5b-440f-accf-5776811eaea2" />

---

## Architecture and Project Workflow

### 1. Development Phase
This phase focuses on building the core application logic.

- Project and API Setup: Initializing the project structure and configuring necessary API keys (Groq).

- Configuration Code: Setting up environmental variables and application settings.

- Itinerary Chain Code: Developing the LangChain code responsible for prompting the LLM and structuring the output.

- Travel Planner Code: Implementing the logic that orchestrates the data flow.

- Application Code using Streamlit: Building the interactive frontend application.

### 2. Containerization & Deployment
The application is prepared for a containerized deployment on Kubernetes.

- Dockerfile: Creating a file to define the Docker image for the Streamlit application.

- Kubernetes Deployment File: Defining the Kubernetes resources (Deployment, Service) for the application.

- Filebeat Deployment File: Defining the Kubernetes configuration for deploying Filebeat as a DaemonSet to collect logs.

- Logstash Deployment File: Defining the Kubernetes configuration for the Logstash service.

- Elasticsearch Deployment File: Defining the Kubernetes configuration for the Elasticsearch service.

- Kibana Deployment File: Defining the Kubernetes configuration for the Kibana service.

### 3. Version Control & Cloud Setup
Setting up the cloud environment and integrating version control.

- Code Versioning using GitHub: Committing all application and configuration files to a GitHub repository.

- GCP VM Instance Setup: Provisioning a Virtual Machine on Google Cloud Platform.

- Setup with Docker Engine, Minikube, and Kubectl: Installing all necessary tools on the VM to run the Kubernetes cluster and manage containers.

- Integrate GitHub to VM: Cloning the repository onto the GCP VM.

### 4. Build, Deploy & Monitor
The final phase involves deploying the application and setting up the monitoring system.

- Build and Deploy app on Minikube Kubernetes Cluster in VM: Using Docker to build the image and Kubectl to deploy the application and the entire ELK Stack onto the Minikube cluster.

- ELK Stack Setup with Filebeat: Configuring Filebeat to scrape logs from the application pods and forward them to Logstash, which then sends them to Elasticsearch.

- Monitoring of Logs in Kibana Dashboards: Accessing the Kibana UI to visualize and analyze the application and system logs, ensuring observability.

---

## Tech Stack

| Category | Technology |
|--------|------------|
| LLM | Groq Model(llama-3.3-70b-versatile) |
| AI Framework | LangChain |
| Frontend | Streamlit |
| Containerization | Docker |
| Orchestration | Kubernetes (Minikube) |
| Cloud | Google Cloud Platform (VM) |
| SCM | GitHub |
| CLI | kubectl |
| Logging | Filebeat, Logstash |
| Storage | Elasticsearch |
| Monitoring | Kibana |

---

## Project Structure

```
WanderAI/
├── src/
│   ├── chains/
│   │   ├── itinerary_chain.py
│   │   └── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── core/
│   │   ├── planner.py
│   │   └── __init__.py
│   └── utils/
│       ├── logger.py
│       ├── custom_exceptions.py
│       └── __init__.py
│
├── app.py
├── Dockerfile
├── k8s-deployment.yaml
├── filebeat.yaml
├── logstash.yaml
├── elasticsearch.yaml
├── kibana.yaml
├── requirements.txt
├── README.md
├── setup.py
└── .gitignore
```

---

## Monitoring & Observability

All application and Kubernetes logs are collected using **Filebeat**, processed by **Logstash**, stored in **Elasticsearch**, and visualized in **Kibana**.

---

## Use Cases

- AI-based travel planning
- LLM-powered recommendation systems
- Kubernetes + ELK stack learning project
- End-to-end AI + DevOps showcase

---

 
