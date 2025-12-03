# withsecure-healthcheck

README.md
<p align="center"> <img src="https://img.shields.io/badge/Kubernetes-Minikube-blue?logo=kubernetes&logoColor=white" /> <img src="https://img.shields.io/badge/Container-Docker-blue?logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Tools-kubectl-brightgreen" /> <img src="https://img.shields.io/badge/Infrastructure-No%20Terraform-lightgrey" /> <img src="https://img.shields.io/badge/Status-Running%20%26%20Tested-success" /> </p>
Kubernetes Deployment Using Minikube

This repository contains a complete Kubernetes deployment using Minikube and standard YAML manifests.
It includes Deployment, Service, ConfigMap, and Secret resources — no Terraform, no Ingress, and everything runs locally via Minikube.

1. Prerequisites & Environment Setup
Required Installations

Make sure the following tools are installed:

Docker – to build and run container images

kubectl – Kubernetes CLI

Minikube – local Kubernetes cluster

Helm (optional) – not used but helpful for future improvements

Kubernetes Solution Used

Minikube (single-node Kubernetes cluster running locally)

Why Minikube

Minikube is fast to set up, reliable for local development, and provides a realistic Kubernetes environment without requiring a cloud provider.

2. Deployment Instructions
Start Minikube
minikube start

Deploy All Kubernetes Resources
kubectl apply -f k8s/

Or Deploy Components Individually
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml

3. Accessing the Application
Option 1 — Minikube Service URL
minikube service list

Option 2 — Port Forwarding
kubectl port-forward svc/<service-name> 8080:80

4. Testing Commands
Check Kubernetes Resources
kubectl get pods
kubectl get services
kubectl get deployments
kubectl logs <pod-name>

Test Application Endpoints

Your confirmed working tests:

curl.exe http://127.0.0.1:61340/health
curl.exe http://127.0.0.1:61340/info


If using port-forwarding:

curl http://localhost:8080/health
curl http://localhost:8080/info


Expected results:

/health → service health status

/info → application metadata

Both endpoints returned correct responses, confirming full deployment success.

5. Explanation of the Approach

This deployment uses pure Kubernetes YAML manifests for maximum clarity and direct resource control.
Minikube acts as the local Kubernetes cluster, providing a simple and accurate environment for development.
Since Terraform and Ingress were unnecessary for this project, the focus stayed on minimal, functional components: Deployment, Service, ConfigMap, and Secret.
Testing was performed using Minikube’s NodePort (e.g., 127.0.0.1:61340) and curl, ensuring that both /health and /info endpoints responded correctly.