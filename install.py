import subprocess
import sys
import os

def main():
    print("--- 🎨 AI Image Generator: Automated Setup ---")
    
    # Step 1: Create virtual environment
    venv_dir = ".venv"
    if not os.path.exists(venv_dir):
        print(f"Creating virtual environment in '{venv_dir}'...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    else:
        print("Virtual environment already exists. Skipping creation.")

    # Determine pip and python paths based on the operating system
    if os.name == "nt":  # Windows
        pip_path = os.path.join(venv_dir, "Scripts", "pip")
        python_path = os.path.join(venv_dir, "Scripts", "python")
    else:  # Mac/Linux
        pip_path = os.path.join(venv_dir, "bin", "pip")
        python_path = os.path.join(venv_dir, "bin", "python")

    # Step 2: Upgrade pip
    print("\nUpgrading pip...")
    subprocess.check_call([python_path, "-m", "pip", "install", "--upgrade", "pip"])

    # Step 3: Install dependencies
    print("\nInstalling required packages (this might take a few minutes)...")
    packages = [
        "torch",
        "torchvision",
        "diffusers",
        "transformers",
        "accelerate",
        "pillow",
        "pyinstaller"
    ]
    subprocess.check_call([pip_path, "install"] + packages)

    print("\n✨ Setup completed successfully!")
    print(f"To run your app, use: {python_path} main.py")

if __name__ == "__main__":
    main()
