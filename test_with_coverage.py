#!/usr/bin/env python3
"""
Wrapper script to run pytest with coverage and generate badges.
This provides a single command that does both testing and badge generation.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and print its status."""
    print(f"🚀 {description}...")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ {description} failed with exit code {result.returncode}")
        return False
    print(f"✅ {description} completed successfully")
    return True

def main():
    """Main function to run tests and generate coverage badge."""
    
    # Run pytest with coverage
    if not run_command("pytest", "Running tests with coverage"):
        sys.exit(1)
    
    # Generate coverage badge
    if not run_command("python generate_coverage_badge.py", "Generating coverage badge"):
        sys.exit(1)
    
    print("\n🎉 All tasks completed successfully!")
    print("📊 Coverage badge generated: coverage_badge.svg")
    
    # Show the current coverage
    if os.path.exists("COVERAGE.txt"):
        with open("COVERAGE.txt", "r") as f:
            print(f"📈 {f.read().strip()}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())