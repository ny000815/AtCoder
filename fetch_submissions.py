import os
import sys
import time
import cloudscraper
from bs4 import BeautifulSoup

USER_ID = "zaki_8"
SUBMISSIONS_DIR = "submissions"

EXTENSION_MAP = {
    "C++": "cpp", "Python": "py", "PyPy": "py", "Java": "java",
    "C#": "cs", "Ruby": "rb", "Rust": "rs", "Go": "go",
    "JavaScript": "js", "TypeScript": "ts", "PHP": "php",
    "Haskell": "hs", "Fortran": "f90",
}

scraper = cloudscraper.create_scraper(
    browser={"browser": "chrome", "platform": "darwin", "mobile": False}
)


def get_extension(language_name):
    for key, ext in EXTENSION_MAP.items():
        if key in language_name:
            return ext
    return "txt"


def fetch_all_submissions(user_id):
    all_subs = []
    seen_ids = set()
    from_second = 0
    while True:
        url = (
            "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions"
            f"?user={user_id}&from_second={from_second}"
        )
        response = scraper.get(url, timeout=60)
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break

        new_in_batch = 0
        for s in batch:
            if s["id"] not in seen_ids:
                seen_ids.add(s["id"])
                all_subs.append(s)
                new_in_batch += 1

        max_second = max(s["epoch_second"] for s in batch)
        print(f"  from_second={from_second}: {len(batch)} rows, "
              f"{new_in_batch} new (total {len(all_subs)}), max_epoch={max_second}")

        if len(batch) < 500:
            break
        if new_in_batch == 0 and max_second <= from_second:
            break

        from_second = max_second
        time.sleep(1)

    return all_subs


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

    submissions = fetch_all_submissions(USER_ID)
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
        file_path = os.path.join(path, f"{pid}.{ext}")

        if os.path.exists(file_path):
            continue

        code = get_code(contest_id, sub_id)
        if code is None:
            time.sleep(3)
            continue

        for old in EXTENSION_MAP.values():
            old_path = os.path.join(path, f"{pid}.{old}")
            if old != ext and os.path.exists(old_path):
                os.remove(old_path)

        print(f"Writing {pid} (sub {sub_id}, {ext})...")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        new_count += 1
        time.sleep(3)

    print(f"Done. {new_count} files written/updated.")


if __name__ == "__main__":
    main()
