import os
import platform
import subprocess

def linux_installation(project_name):
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")
    os.system("sudo apt install -y python3.12-venv")
    os.system(f"python3 -m venv {project_name}")
    os.system(f"source /base-project/{project_name}/bin/activate")

def windows_installation(project_name):
    subprocess.run(["pip", "install", "virtualenv"], check=True)
    subprocess.run(["python", "-m", "venv", project_name], check=True)
    
    # List items in the current directory on Windows
    result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
    print(result.stdout)
    
    # Activate the virtual environment
    activate_script = os.path.join(project_name, "Scripts", "Activate.ps1")
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", activate_script], check=True)

def macos_installation(project_name):
    print(f"Coming soon!!")

def main(project_name):
    directory = 'django-base'
    if not os.path.exists(directory):
        subprocess.run(["git", "clone", "https://github.com/sigmaenigma/django-base.git"], check=True)
    print(f'Changing Directory...')
    os.chdir("django-base")
    
    if platform.system() == "Linux":
        linux_installation(project_name)
    elif platform.system() == "Windows":
        windows_installation(project_name)
    elif platform.system() == "Darwin":
        macos_installation(project_name)

if __name__ == '__main__':
    main(project_name='main-project')
