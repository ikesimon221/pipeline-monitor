from fastapi import FastAPI
from app.database import Base, engine
from app.models import segment, reading  # importing them registers the tables with Base

app = FastAPI(title="Pipeline Monitor API")

# Create any tables that don't exist yet in Supabase
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Pipeline Monitor API is running"}