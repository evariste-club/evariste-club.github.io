#!/usr/bin/env python3
"""
ProSort Launcher Script
Simple script to launch the ProSort system
"""

import subprocess
import sys
import os

def main():
    """Launch the ProSort system"""
    print("🧮 Launching ProSort Mathematical Competition System...")
    print("📚 Loading problem bank and initializing system...")
    
    try:
        # Check if required packages are installed
        import streamlit
        import pandas
        import plotly
        print("✅ All required packages are installed")
        
        # Launch the Streamlit app
        print("🚀 Starting Streamlit application...")
        print("🌐 The app will open in your browser at: http://localhost:8501")
        print("⏹️  Press Ctrl+C to stop the application")
        print("-" * 50)
        
        # Run the Streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "false"
        ])
        
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("💡 Please install required packages using:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 ProSort system stopped by user")
    except Exception as e:
        print(f"❌ Error launching ProSort: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
