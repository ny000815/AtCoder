import requests
import json
import os
import time

USER_ID = "zaki_8"
SUBMISSIONS_DIR = "submissions"

def main():
    # フォルダがなければ作成
    if not os.path.exists(SUBMISSIONS_DIR):
        os.makedirs(SUBMISSIONS_DIR)

    # Kenkoooo APIから提出一覧を取得 (User-Agentを付与)
    url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={USER_ID}&from_second=0"
    headers = {"User-Agent": "Mozilla/5.0 (GitHub Actions)"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    submissions = response.json()

    for sub in submissions:
        # AC (正解) 以外はスキップする場合はこの条件を有効にする
        if sub["result"] != "AC":
            continue

        contest_id = sub["contest_id"]
        problem_id = sub["problem_id"]
        sub_id = sub["id"]
        ext = "txt" # 拡張子の判定は簡易的に txt
        
        # フォルダ構造作成 (例: submissions/abc300/abc300_a/12345.txt)
        path = os.path.join(SUBMISSIONS_DIR, contest_id, problem_id)
        if not os.path.exists(path):
            os.makedirs(path)

        # ファイルが既に存在すればスキップ
        file_name = f"{sub_id}.txt"
        file_path = os.path.join(path, file_name)
        if os.path.exists(file_path):
            continue

        # 個別の提出コードを取得（API負荷軽減のため1秒待機）
        print(f"Fetching {sub_id}...")
        # 注: 提出コード詳細APIは公式ではないため、ここではメタデータ保存に留めるか、
        # 必要に応じて追加の取得ロジックを書きます。
        with open(file_path, "w") as f:
            f.write(f"Submission ID: {sub_id}\nContest: {contest_id}\nProblem: {problem_id}\nPoint: {sub['point']}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
