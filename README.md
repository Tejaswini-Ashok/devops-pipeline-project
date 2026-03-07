# devops-pipeline-project
# Cloud Native DevOps Pipeline

## Architecture
```
Developer pushes code
        ↓
GitHub Actions (CI) — Build & Push Docker image to ECR
        ↓
ArgoCD (CD) — Detects change, syncs Helm chart to EKS
        ↓
EKS Cluster — Runs Flask app with HPA autoscaling
        ↓
AWS Secrets Manager — Injects secrets into pods
        ↓
CloudWatch Container Insights — Monitors cluster metrics
```

## Tech Stack
- **App**: Python Flask
- **Containerization**: Docker
- **Registry**: AWS ECR
- **CI/CD**: GitHub Actions
- **GitOps**: ArgoCD
- **Orchestration**: Kubernetes (AWS EKS)
- **Package Manager**: Helm
- **Infrastructure**: Terraform
- **Autoscaling**: HPA (Horizontal Pod Autoscaler)
- **Secrets**: AWS Secrets Manager
- **Monitoring**: AWS CloudWatch Container Insights
- **Cloud**: AWS (eu-north-1)

## Project Structure
```
devops-pipeline-project/
├── app/                    # Flask application
├── kubernetes/             # Raw Kubernetes manifests
├── helm/flask-app/         # Helm charts
├── terraform/              # EKS infrastructure
└── .github/workflows/      # CI/CD pipeline
```

## Features
- Automated CI/CD pipeline triggered on every GitHub push
- GitOps deployment using ArgoCD
- Auto scaling based on CPU utilization (2-5 replicas)
- Secrets management via AWS Secrets Manager
- Infrastructure as Code using Terraform
- Container monitoring with CloudWatch

## Setup Instructions

### Prerequisites
- AWS Account
- GitHub Account
- kubectl, helm, terraform installed

### Deploy Infrastructure
```bash
cd terraform
terraform init
terraform apply
```

### Deploy Application
```bash
helm install flask-app helm/flask-app
```

### Access Application
```
http://<LoadBalancer-URL>
```<img width="1366" height="768" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/02dd32a7-8e72-4449-b952-c4c93911dffc" />

<img width="1366" height="768" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/bbc074dd-d277-4195-bb1e-7afaa3145df0" />
<img width="1366" height="768" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/dd48c03d-0473-4fe3-aefa-d456195abac4" />
<img width="1366" height="768" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/723ab78a-ea6e-4eb0-bb53-4384848d38e5" />
