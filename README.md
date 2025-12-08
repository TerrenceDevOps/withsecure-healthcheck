# WithSecure Healthcheck Deployment 🚀

Repository established by **TerrenceDevOps**

<p align="center">
 <img src="https://img.shields.io/badge/Kubernetes-Minikube-blue?logo=kubernetes&logoColor=white" />
 <img src="https://img.shields.io/badge/Container-Docker-blue?logo=docker&logoColor=white" />
 <img src="https://img.shields.io/badge/Tools-kubectl-brightgreen" />
 <img src="https://img.shields.io/badge/Infrastructure-No%20Terraform-lightgrey" />
 <img src="https://img.shields.io/badge/Status-Running%20%26%20Tested-success" />
</p>

---

# 📁 Project Structure

* **Source code:** Located in `app.py`
* **Dependencies:** Found in `requirements.txt`
* **Kubernetes Manifests:** Inside the `k8s/` directory

---

# 🛠️ Prerequisites & Environment Setup

Ensure the following tools are installed:

* Docker
* kubectl
* Minikube
* Helm (optional — not used but can be introduced later)

### Kubernetes Solution Used: **Minikube**

**Why Minikube?**

* Fast and reliable local Kubernetes cluster
* Ideal for development/testing
* No cloud costs

---

# 🐳 Docker Build & Run Instructions

### Build Docker Image

```bash
docker build -t health-check-service:latest .
```

Tag for Docker Hub (optional):

```bash
docker tag health-check-service:latest terrence045/withsecure-healthcheck:latest
```

### Run Docker Container

```bash
docker run -p 8080:8080 -e APP_ENV=local health-check-service:latest
```

Run in background:

```bash
docker run -d -p 8080:8080 --name health-check terrence045/withsecure-healthcheck:latest
```

### Test Local Endpoints

```bash
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/info
```

Expected:

```json
{"status":"healthy"}
{"service":"hello-service","environment":"local"}
```

---

# 🚀 Deploying to Kubernetes (Minikube)

### Step 1 — Start Minikube

```bash
minikube start
```

### Step 2 — Deploy K8s Resources

Apply all manifests at once:

```bash
kubectl apply -f k8s/
```

Or apply individually:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/configmap.yaml
```

### Step 3 — Access the Application

#### Option 1 — Minikube Service URL

```bash
minikube service list
```

Get service URL:

```bash
minikube service health-check-service -n health-check-namespace --url
```

#### Option 2 — Port Forward (quick test)

```bash
kubectl port-forward svc/health-check-service 8080:80 -n health-check-namespace
```

Now test:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/info
```

---

# 🧪 Testing Commands

Check cluster resources:

```bash
kubectl get pods
kubectl get services
kubectl get deployments
kubectl logs <pod-name>
```

Test NodePort or Minikube-assigned URL:

```bash
curl http://127.0.0.1:<nodeport>/health
curl http://127.0.0.1:<nodeport>/info
```

Example:

```bash
curl http://127.0.0.1:61340/health
curl http://127.0.0.1:61340/info
```

If using a URL returned by Minikube:

```bash
curl http://192.168.49.2:<port>/health
```

---

# 🧩 Explanation of the Approach

* Uses pure Kubernetes YAML manifests for clarity and transparency
* Minikube chosen for cost-free, fast local development
* `/health` and `/info` endpoints validate application health and metadata

---

# ⚖️ Trade-offs / Notes

* Manual port-forwarding used instead of automated CI/CD
* Minikube is not intended for production-scale workloads
* YAML kept simple; **Helm may be added later** for templating and improved management

---

✔️ All invalid/duplicated/incorrect instructions have been removed.
✔️ Clean structure and correct endpoint usage included.
✔️ Commands properly formatted using code blocks.

