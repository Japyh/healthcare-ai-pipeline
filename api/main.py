from fastapi import FastAPI

from api.routers import monitoring, risk, claim

print("main.py loaded")
print("Risk module:", risk)
print("Claim module:", claim)

app = FastAPI(title="Healthcare ML API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Healthcare ML API"}

@app.get("/health")
def read_health():
    return {"status": "OK"}

# Register routers
app.include_router(risk.router, prefix="/predict", tags=["Risk Score Prediction"])
app.include_router(claim.router, prefix="/predict", tags=["Claim Status Prediction"])
app.include_router(monitoring.router, prefix="/monitor", tags=["Monitoring"])