# CI/CD Pipeline Flow

## 1. Overview

The Cloud DevOps CI/CD Platform uses GitHub Actions to automate the
software delivery lifecycle.

The pipeline is designed to provide:

- Automated testing
- Security validation
- Container image creation
- Container image publishing
- Deployment readiness
- Traceability between source code and artifacts

---

## 2. Pipeline Architecture

```text
Developer
    │
    ▼
Git Push / Pull Request
    │
    ▼
GitHub Repository
    │
    ├─────────────────────────────┐
    │                             │
    ▼                             ▼
CI Workflow                 Security Workflow
    │                             │
    ├── Checkout                  ├── Checkout
    ├── Python Setup              ├── Trivy Scan
    ├── Install Dependencies      └── Dockerfile Scan
    ├── Unit Tests
    └── Docker Build
    │
    └──────────────┬──────────────┘
                   │
                   ▼
             Docker Image
                   │
                   ▼
           GitHub Container Registry
                   │
                   ▼
              Deployment
                   │
                   ▼
              Kubernetes
