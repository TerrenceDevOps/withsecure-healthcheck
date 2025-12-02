from fastapi import FastAPI
import os

app = FastAPI()

ENV_VALUE = os.getenv("APP_ENV", "development")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/info")
async def get_info():
    return {
        "service": "hello-service",
        "environment": ENV_VALUE
    }

# For debugging - can remove later
print("✓ FastAPI app created successfully!")
print(f"✓ App object ID: {id(app)}")
