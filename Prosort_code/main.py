#!/usr/bin/env python3
"""
ProSort Main Entry Point
Run this file to start the ProSort mathematical competition system
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from streamlit_app import ProSortStreamlitApp


def main():
    """Main function to run the ProSort system"""
    print("🧮 Starting ProSort Mathematical Competition System...")
    
    try:
        # Initialize and run the ProSort Streamlit app
        app = ProSortStreamlitApp()
        app.run()
        
    except KeyboardInterrupt:
        print("\n👋 ProSort system stopped by user")
    except Exception as e:
        print(f"❌ Error running ProSort system: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
