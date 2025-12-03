# WithSecure Healthcheck Deployment 🚀

Repository established by TerrenceDevOps


<p align="center"> <img src="https://img.shields.io/badge/Kubernetes-Minikube-blue?logo=kubernetes&logoColor=white" /> <img src="https://img.shields.io/badge/Container-Docker-blue?logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Tools-kubectl-brightgreen" /> <img src="https://img.shields.io/badge/Infrastructure-No%20Terraform-lightgrey" /> <img src="https://img.shields.io/badge/Status-Running%20%26%20Tested-success" /> </p>
Kubernetes Deployment Using Minikube

# Prerequisites & Environment Setup 🛠️
## Required Installations

Make sure the following tools are installed:

#### Docker – to build and run container images

#### kubectl – Kubernetes CLI tool

#### Minikube – local Kubernetes cluster

Helm (optional) – not used in this project, but can be added for advanced templating in the future

Kubernetes Solution Used:

#### Minikube (single-node Kubernetes cluster running locally)

Why Minikube

Fast and reliable local Kubernetes environment

Perfect for development and testing

No cloud infrastructure required

# Deployment Instructions ⚡
Step 1 — Start Minikube
```
minikube start
```
Step 2 — Deploy Kubernetes Resources

Deploy everything at once:
```
kubectl apply -f k8s/
```

Or deploy components individually:
```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/configmap.yaml
```

Step 3 — Access the Application

Option 1 — Minikube Service URL
```
minikube service list
```

Option 2 — Port Forwarding
```
kubectl port-forward svc/<service-name> 8080:80
```
3. Testing Commands ✅
Check Cluster & Deployment Status
```
kubectl get pods
kubectl get services
kubectl get deployments
kubectl logs <pod-name>
```
# Test Application Endpoints

On PowerShell (example NodePort URL):
```
curl.exe http://127.0.0.1:61340/health
curl.exe http://127.0.0.1:61340/info
```

If using port-forwarding (access in browser or curl):
```
curl http://localhost:8080/health
curl http://localhost:8080/info
```

## Expected Results

/health → returns service health status ✅

/info → returns application metadata ℹ️

Both endpoints have been successfully validated, confirming full deployment.

# Explanation of the Approach 🧩

This project uses pure Kubernetes YAML manifests, without Terraform or Helm, for full transparency and direct control.

Minikube provides a lightweight local environment, enabling fast iteration and testing.

Endpoints /health and /info are implemented for simple monitoring.


# Trade-offs / Notes:

Manual port-forwarding is used for local access instead of automated CI/CD deployment; future iterations could integrate full automation.

Minikube was chosen for cost-free local development; it is not designed for production-scale workloads.

YAML manifests prioritize simplicity and clarity; Helm could be introduced later for templating and more advanced deployment management.


Minikube was chosen for cost-free local development; it is not designed for production-scale workloads.

YAML manifests prioritize simplicity and clarity; Helm could be introduced later for templating and more advanced deployment management.
