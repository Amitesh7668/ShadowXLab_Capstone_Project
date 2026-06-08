# ShadowXLab Docker & Kubernetes Capstone Project

## Project Overview
ShadowXLab Cyber Learning Portal is a cloud-native web application containerized using Docker and deployed on Kubernetes.

## Application Features
- Displays application name
- Displays version
- Displays hostname
- Displays current date/time
- Displays environment information
- Provides health endpoint at /health

## Technologies Used
- Python Flask
- Docker
- Docker Hub
- Kubernetes
- kubectl

## Folder Structure
```text
shadowxlab-capstone/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    └── service.yaml
```

## Commands
Replace `Amitesh7668` with your Docker Hub username before running push/deploy commands.

```bash
docker build -t shadowxlab-portal:v1 .
docker run -d -p 5000:5000 --name shadowxlab shadowxlab-portal:v1
docker tag shadowxlab-portal:v1 <dockerhub-username>/shadowxlab-portal:v1
docker push <dockerhub-username>/shadowxlab-portal:v1
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get all -n shadowxlab
kubectl scale deployment shadowxlab-deployment --replicas=4 -n shadowxlab
kubectl set image deployment/shadowxlab-deployment shadowxlab-container=<dockerhub-username>/shadowxlab-portal:v2 -n shadowxlab
kubectl rollout status deployment/shadowxlab-deployment -n shadowxlab
kubectl rollout undo deployment/shadowxlab-deployment -n shadowxlab
```

