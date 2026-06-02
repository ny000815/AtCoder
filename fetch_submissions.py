import os
import sys
import time

import cloudscraper
from bs4 import BeautifulSoup

USER_ID = "zaki_8"
SUBMISSIONS_DIR = "submissions"

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
    "Fortran": "f90",
}

scraper = cloudscraper.create_scraper(
    browser={"browser": "chrome", "platform": "darwin", "mobile": False}
)


def get_extension(language_name):
    for key, ext in EXTENSION_MAP.items():
        if key in language_name:
            return ext
    return "txt"


def get_code(contest_id, sub_id):
    url = f"https://atcoder.jp/contests/{contest_id}/submissions/{sub_id}"
    try:
        response = scraper.get(url, timeout=30)
        if response.status_code != 200:
            print(f"  WARN: code page {sub_id} returned {response.status_code}")
            return None
        soup = BeautifulSoup(response.text, "html.parser")
        code_block = soup.find(id="submission-code")
        return code_block.text if code_block else None
    except Exception as e:
        print(f"  WARN: failed to fetch code for {sub_id}: {e}")
        return None


def main():
    os.makedirs(SUBMISSIONS_DIR, exist_ok=True)

    url = (
        "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions"
        f"?user={USER_ID}&from_second=0"
    )

    response = scraper.get(url, timeout=60)
    response.raise_for_status()

    submissions = response.json()
    if not submissions:
        print("ERROR: API returned 0 submissions. Aborting (likely blocked).")
        sys.exit(1)

    print(f"Fetched {len(submissions)} submissions from API.")

    latest_ac = {}
    for sub in submissions:
        if sub["result"] != "AC":
            continue
        pid = sub["problem_id"]
        if pid not in latest_ac or sub["epoch_second"] > latest_ac[pid]["epoch_second"]:
            latest_ac[pid] = sub

    print(f"{len(latest_ac)} problems have at least one AC.")

    new_count = 0
    for pid, sub in latest_ac.items():
        contest_id = sub["contest_id"]
        sub_id = sub["id"]
        ext = get_extension(sub["language"])

        path = os.path.join(SUBMISSIONS_DIR, contest_id)
        os.makedirs(path, exist_ok=True)

        for old in EXTENSION_MAP.values():
            old_path = os.path.join(path, f"{pid}.{old}")
            if old != ext and os.path.exists(old_path):
                os.remove(old_path)

        file_path = os.path.join(path, f"{pid}.{ext}")

        marker = file_path + ".id"
        if os.path.exists(marker):
            with open(marker, "r", encoding="utf-8") as f:
                if f.read().strip() == str(sub_id):
                    continue

        print(f"Fetching {pid} (sub {sub_id}, {ext})...")
        code = get_code(contest_id, sub_id)
        if code:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
            with open(marker, "w", encoding="utf-8") as f:
                f.write(str(sub_id))
            new_count += 1
        time.sleep(3)

    print(f"Done. {new_count} files written/updated.")


if __name__ == "__main__":
    main()
