import subprocess

def clean_remotes():
    try:
        # Run git remote -v
        output = subprocess.check_output(["git", "remote", "-v"], text=True)
    except subprocess.CalledProcessError:
        print("❌ Not a git repository or git command failed.")
        return

    remotes = set()
    for line in output.splitlines():
        if line.strip():
            name = line.split()[0]
            remotes.add(name)

    count = 0 
    for remote in remotes:
        if remote not in ("origin", "upstream"):
            print(f"🗑 Removing remote: {remote}")
            subprocess.run(["git", "remote", "rm", remote])
            count += 1

    if count == 0:
        print("🧹 Repo tidy! No extra git remotes detected.")

