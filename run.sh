#!/bin/bash
echo "Starting Emotional Support App..."
cd backend && uvicorn main:app --reload &   # Start FastAPI in the background
cd ../frontend && streamlit run app.py      # Start Streamlit UI
