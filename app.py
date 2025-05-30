from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from google.oauth2 import service_account
import google.auth.transport.requests
import os
from typing import Optional
from pydantic import BaseModel

app = FastAPI(
    title="Google Token API",
    description="API to get Google access tokens using service account credentials",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variables
API_KEY = os.getenv('API_KEY')
PORT = int(os.getenv('PORT', 5001))

# Response model
class TokenResponse(BaseModel):
    access_token: str

# API key dependency
async def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
    return x_api_key

@app.get("/google-token", 
         response_model=TokenResponse,
         summary="Get Google Access Token",
         description="Retrieves a Google access token using service account credentials")
async def get_token(api_key: str = Depends(verify_api_key)):
    try:
        SERVICE_ACCOUNT_FILE = '/etc/secrets/account_service_credentials.json'
        SCOPES = [
            'https://www.googleapis.com/auth/drive',
            "https://spreadsheets.google.com/feeds"
        ]

        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        auth_req = google.auth.transport.requests.Request()
        creds.refresh(auth_req)
        
        return TokenResponse(access_token=creds.token)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error getting token: {str(e)}"
        )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
