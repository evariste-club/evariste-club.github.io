#!/usr/bin/env python3
"""
Launcher script for the Évariste Math Club Streamlit application.
Run this script to start the app.
"""

import subprocess
import sys
import os

def main():
    """Launch the Streamlit application."""
    print("🚀 Starting Évariste Math Club Application...")
    print("📚 Loading mathematical tools and resources...")
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Launch the app
    print("🌐 Launching web application...")
    print("📱 The app will open in your default browser")
    print("🔗 If it doesn't open automatically, go to: http://localhost:8501")
    print("\n" + "="*50)
    
    # Run the enhanced app
    subprocess.run(["streamlit", "run", "app_enhanced.py", "--server.port", "8501"])

if __name__ == "__main__":
    main()
