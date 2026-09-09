"""
Run this on YOUR computer (not on Hugging Face's website).

What it does:
1. Logs you into Hugging Face with a token.
2. Uploads this ENTIRE folder to your Space in one single atomic commit
   (app.py, model.py, requirements.txt, class_names.txt, examples/, and
   the .pth weights file that you must copy into this same folder first).

This avoids the browser drag-and-drop uploader, which is what silently
corrupted the big .pth file before.

STEPS TO USE:
1. pip install huggingface_hub --break-system-packages
2. Copy your file "09_pretrained_effnetb2_feature_extractor_food101_20_percent.pth"
   into this same folder (next to this deploy.py file).
3. Copy your "class_names.txt" and "examples/" folder into this same folder too
   (if you don't have them handy, tell Claude and it will regenerate them).
4. Get a WRITE token from https://huggingface.co/settings/tokens
5. Run:  python deploy.py
6. Paste your token when it asks (or set env var HF_TOKEN beforehand).
"""

from huggingface_hub import HfApi, login
import os

REPO_ID = "Sakshamks/Food-Vision"  # <-- change this if your Space has a different name
LOCAL_FOLDER = os.path.dirname(os.path.abspath(__file__))

def main():
    login()  # will prompt for your token if HF_TOKEN env var isn't set

    api = HfApi()

    required_files = [
        "app.py",
        "model.py",
        "requirements.txt",
        "class_names.txt",
        "09_pretrained_effnetb2_feature_extractor_food101_20_percent.pth",
    ]
    missing = [f for f in required_files if not os.path.exists(os.path.join(LOCAL_FOLDER, f))]
    if missing:
        print("STOP: these required files are missing from this folder before you deploy:")
        for f in missing:
            print(f"  - {f}")
        print("\nAdd them to this folder, then re-run this script.")
        return

    print(f"Uploading {LOCAL_FOLDER} -> {REPO_ID} ...")
    api.upload_folder(
        folder_path=LOCAL_FOLDER,
        repo_id=REPO_ID,
        repo_type="space",
        ignore_patterns=["deploy.py", "*.pyc", "__pycache__", ".ipynb_checkpoints"],
    )
    print("Done! Now go to your Space settings and click 'Factory reboot'.")

if __name__ == "__main__":
    main()
