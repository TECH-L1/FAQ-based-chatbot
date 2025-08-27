#!/usr/bin/env python3
"""
HCP Technical Support FAQ Chatbot Runner
This script provides a simple way to run the chatbot with various options.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from src.utils.config import Config
from src.utils.logger import setup_logger

def check_requirements():
    """Check if all required dependencies are installed."""
    try:
        import streamlit
        import langchain
        import ollama
        print("All required dependencies are installed")
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_environment():
    """Check if environment is properly configured."""
    config = Config()
    
    try:
        config.validate()
        print("Configuration is valid")
        return True
    except ValueError as e:
        print(f"Configuration error: {e}")
        return False

def run_streamlit_app(port=8501, debug=False):
    """Run the Streamlit application."""
    cmd = ["streamlit", "run", "app.py", "--server.port", str(port)]
    
    if debug:
        cmd.extend(["--logger.level", "debug"])
    
    print(f"Starting HCP FAQ Chatbot on port {port}")
    print(f"Open your browser and go to: http://localhost:{port}")
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start application: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nApplication stopped by user")

def setup_project():
    """Set up the project for first-time use."""
    print("Setting up HCP FAQ Chatbot project...")
    
    # Create .env file if it doesn't exist
    if not Path(".env").exists():
        if Path(".env.example").exists():
            print("Creating .env file from template...")
            with open(".env.example", "r") as src, open(".env", "w") as dst:
                dst.write(src.read())
            print("Please edit .env file and configure your LLM provider")
        else:
            print(".env.example not found")
    
    # Check directories
    config = Config()
    print(f"FAQ data directory: {config.faq_data_path}")
    print(f"Embeddings directory: {config.embeddings_path}")
    print(f"Logs directory: {config.logs_path}")
    
    print("Project setup complete!")
    print("\nNext steps:")
    print("1. Edit .env file and add your OpenAI API key")
    print("2. Add FAQ documents to data/faqs/ directory")
    print("3. Run: python run.py --start")

def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description="HCP Technical Support FAQ Chatbot Runner")
    
    parser.add_argument("--start", action="store_true", help="Start the Streamlit application")
    parser.add_argument("--setup", action="store_true", help="Set up the project for first-time use")
    parser.add_argument("--check", action="store_true", help="Check dependencies and configuration")
    parser.add_argument("--port", type=int, default=8501, help="Port to run the application on")
    parser.add_argument("--debug", action="store_true", help="Run in debug mode")
    
    args = parser.parse_args()
    
    if args.setup:
        setup_project()
    elif args.check:
        print("Checking system requirements...")
        deps_ok = check_requirements()
        config_ok = check_environment()
        
        if deps_ok and config_ok:
            print("System is ready!")
        else:
            print("System check failed")
            sys.exit(1)
    elif args.start:
        # Check requirements before starting
        if not check_requirements() or not check_environment():
            print("❌ Please fix the issues above before starting the application")
            sys.exit(1)
        
        run_streamlit_app(port=args.port, debug=args.debug)
    else:
        # Default behavior - show help and basic info
        print("HCP Technical Support FAQ Chatbot")
        print("=====================================")
        print()
        parser.print_help()
        print("\nQuick start:")
        print("1. python run.py --setup    # First-time setup")
        print("2. python run.py --check    # Verify configuration")
        print("3. python run.py --start    # Start the application")

if __name__ == "__main__":
    main()