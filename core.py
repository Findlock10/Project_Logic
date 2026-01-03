import subprocess, sys, os, shutil
from datetime import datetime

def github_guard():
    try:
        status = subprocess.check_output(["git", "status", "--porcelain"]).decode("utf-8")
        if status:
            subprocess.run(["git", "add", "."])
            ts = datetime.now().strftime("%Y-%m-%d %H:%M")
            subprocess.run(["git", "commit", "-m", f"Logic Sync @ {ts}"])
            subprocess.run(["git", "push"])
            print("[✓] SUCCESS: GitHub Updated.")
    except Exception as e: print(f"[X] ERROR: {e}")

def spawn_project():
    base_path = "C:\\Scripts"
    projects = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    print("\n--- AI PORTFOLIO ---")
    for i, p in enumerate(projects, 1): print(f" [{i}] {p}")
    print("\n [N] Spawn New Project")
    choice = input("\n >> SELECT MODE: ").strip().lower()
    if choice == "n":
        new_name = input("\n Enter Project Name: ").strip()
        if new_name:
            new_path = os.path.join(base_path, new_name)
            os.makedirs(new_path, exist_ok=True)
            os.makedirs(os.path.join(new_path, "Assets"), exist_ok=True)
            os.makedirs(os.path.join(new_path, "Logs"), exist_ok=True)
            for f in ["core.py", "AI_Interface.ps1", "AI_Workforce_Start.bat"]:
                src = os.path.join("C:\\Scripts\\AiWorkforce", f)
                if os.path.exists(src): shutil.copy(src, os.path.join(new_path, f))
            print(f"[✓] SUCCESS: {new_name} spawned at {new_path}")
    elif choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(projects): os.startfile(os.path.join(base_path, projects[idx]))

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "dev"
    if arg == "dev": github_guard()
    elif arg == "spawn": spawn_project()