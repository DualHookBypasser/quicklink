from flask import Flask
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app from the main app.py file
from app import app

# Vercel expects the WSGI application to be named 'app'
# This is the entry point for Vercel serverless functions
if __name__ == "__main__":
    app.run()