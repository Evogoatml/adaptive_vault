from flask import Flask
import subprocess
import threading

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "Adaptive Vault running", "ok": True}

def run_vault():
    subprocess.run(["python", "adaptive_vault.py", "--demo"])

if __name__ == "__main__":
    threading.Thread(target=run_vault, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
