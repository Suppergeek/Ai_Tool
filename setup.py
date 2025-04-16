import os
import subprocess
import sys
import shutil

def install_media_tool():
    repo_url = "https://github.com/Suppergeek/Ai_Tool.git"
    clone_path = "/content/Ai_Tool/program"

    print("📁 Cloning MEDIA TOOL repo...")

    # Remove existing directory if it exists
    if os.path.exists(clone_path):
        print("⚠️ Removing existing directory...")
        shutil.rmtree(clone_path)

    try:
        subprocess.run(["git", "clone", repo_url, clone_path], check=True)
        print("✅ Repo cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git clone failed: {e}")
        sys.exit(1)

    os.chdir(clone_path)

    venv_path = os.path.join(clone_path, "venv")
    print("🐍 Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Virtual environment creation failed: {e}")
        sys.exit(1)

    pip_path = os.path.join(venv_path, "bin", "pip")
    print("⬆️ Upgrading pip...")
    subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)

    print("📦 Installing requirements.txt...")
    try:
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✅ Installation complete! Run `launcher.py` to start MEDIA TOOL.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Dependency installation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_media_tool()
