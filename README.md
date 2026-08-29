# Loan Prediction (ApplAi)

![Docker CI/CD](https://github.com/aliabdallah7/loan_prediction_ApplAi/actions/workflows/docker-ci.yml/badge.svg)
[![Docker Hub](https://img.shields.io/docker/pulls/aliabdallah7/loan-prediction)](https://hub.docker.com/r/aliabdallah7/loan-prediction)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Predicts whether a loan application will be accepted or rejected, based on historical labeled applicant data (income, credit history, loan amount, etc.), using several classical machine learning classifiers.

Originally built during a 2-week machine learning workshop run by [ApplAi](https://github.com/ApplAi2023), a student activity at Ain Shams University.

**Live demo:** https://loanprediction.streamlit.app/

## Models evaluated
- Logistic Regression (final model used in production)
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- ID3 Decision Tree
- Random Forest

## Tech stack
- **ML:** scikit-learn
- **App:** Streamlit
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Infrastructure:** Terraform, Azure Container Instances

## Running locally (without Docker)
```bash
pip install -r requirements.txt
streamlit run loan-prediction.py
```

## Running with Docker
Pull the pre-built image directly from Docker Hub:
```bash
docker pull aliabdallah7/loan-prediction:latest
docker run -p 8501:8501 aliabdallah7/loan-prediction:latest
```
Then open http://localhost:8501 in your browser.

Or build it yourself from source:
```bash
docker build -t loan-prediction .
docker run -p 8501:8501 loan-prediction
```

## CI/CD pipeline
Every push to `main` triggers a GitHub Actions workflow (`.github/workflows/docker-ci.yml`) that:
1. Builds the Docker image
2. Runs a smoke test against the Streamlit health-check endpoint to confirm the container actually starts and serves traffic
3. Logs in to Docker Hub using repository secrets (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`) — no credentials are ever stored in the repo
4. Pushes the image to [Docker Hub](https://hub.docker.com/r/aliabdallah7/loan-prediction) tagged both `latest` and with the commit SHA

## Infrastructure as Code (Terraform + Azure)
The `terraform/` folder provisions an Azure Container Instance and deploys this image, exposing the app on a public URL — no manual clicks in the Azure Portal.

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Terraform prints an `app_url` output once complete. Tear the environment down with:
```bash
terraform destroy
```

See [`terraform/README.md`](terraform/README.md) for full details and prerequisites.

## Project structure
```
├── loan-prediction.py              # Streamlit app entry point
├── loan_predition_model_LR.pkl     # Trained Logistic Regression model
├── loan_predition_model_RF         # Trained Random Forest model
├── loan_data.csv                   # Training dataset
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .github/workflows/docker-ci.yml
└── terraform/                      # Azure infrastructure as code
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── README.md
```

## License
MIT — see [LICENSE](LICENSE).
