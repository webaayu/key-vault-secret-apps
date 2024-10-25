from flask import Flask, render_template
import os
import time
import threading

app = Flask(__name__)

# Initial default values for environment variables
secrets = {
    "link": os.getenv("LINK", "http://www.cloudyuga.guru/"),
    "text1": os.getenv("TEXT1", "CloudYuga"),
    "text2": os.getenv("TEXT2", "Secret Rotation Example!"),
    "logo": os.getenv("LOGO", "https://raw.githubusercontent.com/cloudyuga/rsvpapp/master/static/cloudyuga.png"),
    "company": os.getenv("COMPANY", "CloudYuga Technology Pvt. Ltd.")
}

# Function to load secrets from files (if updated by Kubernetes secret rotation)
def load_secrets():
    secrets["link"] = read_secret("/mnt/secrets-store/LINK") or secrets["link"]
    secrets["text1"] = read_secret("/mnt/secrets-store/TEXT1") or secrets["text1"]
    secrets["text2"] = read_secret("/mnt/secrets-store/TEXT2") or secrets["text2"]
    secrets["logo"] = read_secret("/mnt/secrets-store/LOGO") or secrets["logo"]
    secrets["company"] = read_secret("/mnt/secrets-store/COMPANY") or secrets["company"]

# Helper function to read secret file content
def read_secret(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None  # Return None if file is not yet available

# Background thread to periodically refresh secrets every 5 seconds
def watch_secrets():
    while True:
        load_secrets()
        time.sleep(5)

# Start the background thread
thread = threading.Thread(target=watch_secrets, daemon=True)
thread.start()

@app.route('/')
def index():
    return render_template('index.html', link=secrets["link"], text1=secrets["text1"], 
                           text2=secrets["text2"], logo=secrets["logo"], 
                           company=secrets["company"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
