import requests
import json
import os
import time
import re
from bs4 import BeautifulSoup

USER_ID = "zaki_8"
SUBMISSIONS_DIR = "submissions"

def get_code(contest_id, sub_id):
    """AtCoderの提出ページからソースコードを抽出する"""
    url = f"https://atcoder.jp/contests/{contest_id}/submissions/{sub_id}"
    headers = {"User-Agent": "Mozilla/5.0 (GitHub Actions)"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # id="submission-code" の中にある pre タグを探す
        code_block = soup.find(id="submission-code")
        if code_block:
            return code_block.text
    except Exception as e:
        print(f"Error fetching code for {sub_id}: {e}")
    return None

def main():
    if not os.path.exists(SUBMISSIONS_DIR):
        os.makedirs(SUBMISSIONS_DIR)

    # 1. 提出一覧を取得
    url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={USER_ID}&from_second=0"
    headers = {"User-Agent": "Mozilla/5.0 (GitHub Actions)"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    submissions = response.json()

    # 取得数が多い場合の負荷軽減のため、新しい順に一定数のみ処理するか、
    # 既存ファイルがある場合は飛ばす運用にする
    for sub in submissions:
        if sub["result"] != "AC":
            continue

        contest_id = sub["contest_id"]
        problem_id = sub["problem_id"]
        sub_id = sub["id"]
        
        # フォルダ構造作成
        path = os.path.join(SUBMISSIONS_DIR, contest_id, problem_id)
        if not os.path.exists(path):
            os.makedirs(path)

        # ファイル名は SubmissionID.py (仮)
        # 本来は sub["language"] から拡張子を判別すべきですが、まずは .txt や .py で保存
        file_path = os.path.join(path, f"{sub_id}.txt")

        # すでにファイルがあればスキップ
        if os.path.exists(file_path):
            continue

        print(f"Fetching source code for {sub_id}...")
        code = get_code(contest_id, sub_id)
        
        if code:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
            # 公式サーバーへの負荷軽減のため 3秒待機
            time.sleep(3)
        else:
            print(f"Failed to get code for {sub_id}")
            time.sleep(1)

if __name__ == "__main__":
    main()
