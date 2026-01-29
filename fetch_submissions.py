import requests
import json
import os
import time
from bs4 import BeautifulSoup

USER_ID = "zaki_8"
SUBMISSIONS_DIR = "submissions"

# 言語名に含まれる文字列から拡張子を判定する辞書
EXTENSION_MAP = {
    "C++": "cpp",
    "Python": "py",
    "PyPy": "py",
    "Java": "java",
    "C#": "cs",
    "Ruby": "rb",
    "Rust": "rs",
    "Go": "go",
    "JavaScript": "js",
    "TypeScript": "ts",
    "PHP": "php",
    "Haskell": "hs",
    "Fortran": "f90"
}

def get_extension(language_name):
    """言語名から拡張子を返す。見つからない場合は txt"""
    for key, ext in EXTENSION_MAP.items():
        if key in language_name:
            return ext
    return "txt"

def get_code(contest_id, sub_id):
    url = f"https://atcoder.jp/contests/{contest_id}/submissions/{sub_id}"
    headers = {"User-Agent": "Mozilla/5.0 (GitHub Actions)"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200: return None
        soup = BeautifulSoup(response.text, 'html.parser')
        code_block = soup.find(id="submission-code")
        return code_block.text if code_block else None
    except:
        return None

def main():
    if not os.path.exists(SUBMISSIONS_DIR):
        os.makedirs(SUBMISSIONS_DIR)

    url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={USER_ID}&from_second=0"
    headers = {"User-Agent": "Mozilla/5.0 (GitHub Actions)"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200: return

    submissions = response.json()

    for sub in submissions:
        if sub["result"] != "AC":
            continue

        contest_id = sub["contest_id"]
        problem_id = sub["problem_id"]
        sub_id = sub["id"]
        
        # 拡張子を決定
        ext = get_extension(sub["language"])
        
        path = os.path.join(SUBMISSIONS_DIR, contest_id, problem_id)
        if not os.path.exists(path):
            os.makedirs(path)

        # ファイル名を ID + 拡張子 に変更
        file_path = os.path.join(path, f"{sub_id}.{ext}")

        if os.path.exists(file_path):
            continue

        print(f"Fetching {sub_id} ({ext})...")
        code = get_code(contest_id, sub_id)
        
        if code:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
            time.sleep(3)

if __name__ == "__main__":
    main()
