import os

def open_app(app_name):
    """
    Open specified applications in Windows based on the voice command.

    Parameters:
    app_name (str): The name of the application to open.
    """
    app_paths = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
        "notepad": "notepad.exe",
        "vscode": r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "file explorer": "explorer.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "command prompt": "cmd.exe",
        "task manager": "taskmgr.exe",
        "capcut": r"C:\Program Files\CapCut\CapCut.exe"  # Update path as necessary
    }

    path = app_paths.get(app_name)
    if path:
        os.startfile(path)
        print(f"{app_name.capitalize()} has been opened.")
    else:
        print(f"Error: No application found for '{app_name}'.")


def execute_command(command):
    """Execute the command based on the recognized voice input."""
    if "open" in command:
        app_name = command.replace("open ", "").strip()
        open_app(app_name)
    else:
        print("Error: Command not recognized.")


