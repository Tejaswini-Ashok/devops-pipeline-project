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
```
