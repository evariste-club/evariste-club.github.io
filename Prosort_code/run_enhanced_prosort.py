#!/usr/bin/env python3
"""
Enhanced ProSort Launcher
Launches the ProSort system with authentication and participation tracking
"""

import subprocess
import sys
import os

def main():
    """Launch the enhanced ProSort system"""
    print("🧮 Launching Enhanced ProSort Mathematical Competition System...")
    print("🔐 Authentication system enabled")
    print("📊 Participation tracking enabled")
    print("📚 Loading problem bank and initializing system...")
    
    try:
        # Check if required packages are installed
        import streamlit
        import pandas
        import plotly
        print("✅ All required packages are installed")
        
        # Launch the enhanced Streamlit app
        print("🚀 Starting Enhanced Streamlit application...")
        print("🌐 The app will open in your browser at: http://localhost:8501")
        print("🔐 Login with sample accounts:")
        print("   - Username: math_wizard, Password: password123")
        print("   - Username: problem_solver, Password: password123")
        print("   - Username: calculus_master, Password: password123")
        print("⏹️  Press Ctrl+C to stop the application")
        print("-" * 50)
        
        # Run the enhanced Streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "enhanced_streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "false"
        ])
        
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("💡 Please install required packages using:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Enhanced ProSort system stopped by user")
    except Exception as e:
        print(f"❌ Error launching Enhanced ProSort: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
