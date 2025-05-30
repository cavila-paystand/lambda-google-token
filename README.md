# Google Token API

A FastAPI service that provides Google access tokens using service account credentials. This service can be deployed as an AWS Lambda function or run locally using Docker.

## Features

- FastAPI-based REST API
- Google service account token generation
- API key authentication
- Docker support for local development
- AWS Lambda deployment ready
- Automatic API documentation

## Prerequisites

- Python 3.9+
- Docker and Docker Compose (for local development)
- Google Cloud service account credentials
- AWS account (for Lambda deployment)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd lambda-google-token
```

2. Create a secrets directory and add your Google service account credentials:
```bash
mkdir -p secrets
# Copy your service account credentials to secrets/account_service_credentials.json
```

3. Create a `.env` file (use `.env-copy` as a template):
```bash
cp .env-copy .env
# Edit .env with your actual values
```

## Local Development

1. Start the service using Docker Compose:
```bash
docker-compose up --build
```

The service will be available at `http://localhost:5001`

## API Documentation

Once the service is running, you can access:
- Swagger UI documentation: `http://localhost:5001/docs`
- ReDoc documentation: `http://localhost:5001/redoc`

## API Usage

### Get Google Access Token

```bash
curl -X GET "http://localhost:5001/google-token" \
     -H "X-API-Key: your-api-key"
```

Response:
```json
{
    "access_token": "ya29.abc123..."
}
```

## Environment Variables

- `API_KEY`: Your API key for authentication
- `PORT`: Port number (default: 5001)

## AWS Lambda Deployment

1. Install the Serverless Framework:
```bash
npm install -g serverless
```

2. Deploy to AWS:
```bash
serverless deploy
```

## Security Notes

- Never commit your `.env` file or service account credentials
- Keep your API key secure
- In production, consider using AWS Secrets Manager for credentials
- Update CORS settings in production to restrict origins

## License

[Your License Here]

