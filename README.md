# AtCoder Submission Backup 

*([日本語版](#日本語版) / Japanese version below)*

A GitHub Actions workflow that automatically backs up your **accepted (AC)** AtCoder submissions to a Git repository on a daily schedule.

For each problem you have solved, it keeps the source code of your latest AC submission, organized by contest:

```
submissions/
├── abc459/
│   ├── abc459_a.py
│   ├── abc459_b.py
│   └── abc459_c.py
├── abc460/
│   └── abc460_a.py
└── ...
```

The backup runs entirely on GitHub Actions, so once it is set up you do not need to run anything manually. As a nice side effect, the daily auto-commits show up on your GitHub contribution graph — see [Commit identity & contribution graph](#commit-identity--contribution-graph) for how to set this up correctly.

---

## How it works

1. It calls the [AtCoder Problems API](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md) (by kenkoooo) to get the list of your submissions.
2. The API returns up to 500 submissions per request, so the script **paginates** through all of them using the `from_second` parameter until everything has been fetched.
3. It keeps only the latest AC submission per problem.
4. For each of those, it fetches the source code from the AtCoder submission page and writes it to `submissions/<contest_id>/<problem_id>.<ext>`.
5. The workflow commits and pushes any new or changed files.

If a file for a problem already exists, it is skipped — so the daily run only fetches code for newly solved problems.

---

## Setup

1. **Fork or copy** this repository into your own GitHub account.

2. **Set your AtCoder user ID.** Open `fetch_submissions.py` and change:

   ```python
   USER_ID = "your_atcoder_id"
   ```

3. **Enable GitHub Actions.** Go to the **Actions** tab of your repository and enable workflows if prompted.

4. **Check the workflow permissions.** The workflow needs write access to push commits. The included workflow already requests this:

   ```yaml
   permissions:
     contents: write
   ```

5. **Set the commit identity.** See the next section — this controls whether the auto-commits appear on your contribution graph, and how to avoid exposing your email.

6. **Run it.** You can trigger it manually from the Actions tab (**Run workflow**), or wait for the daily scheduled run.

The first run will back up your entire AC history, so it may take a while. Subsequent runs only fetch newly solved problems and finish quickly.

---

## Commit identity & contribution graph

The workflow makes the actual commits, so **who the commit is attributed to** depends on the `git config` lines in `.github/workflows/atcoder-backup.yml`:

```yaml
- name: Commit and Push
  run: |
    git config user.name  "your_github_username"
    git config user.email "your_github_username@users.noreply.github.com"
    git add -A
    if ! git diff --staged --quiet; then
      git commit -m "Auto backup: $(date -u)"
      git push
    fi
```

### Do you want the commits to count toward your contribution graph?

GitHub only adds a commit to your contribution graph when the commit's **author email matches a verified email on your GitHub account**. So your choice of email matters:

| Email you set | Email exposed publicly? | Counts as contribution? |
| --- | --- | --- |
| `your_github_username@users.noreply.github.com` | No | **Yes** |
| `12345678+your_github_username@users.noreply.github.com` | No | **Yes** |
| Your real email (e.g. a personal/work address) | **Yes — gets scraped for spam** | Yes |
| `github-actions[bot]@users.noreply.github.com` | No | No (shows as a bot) |

**Recommended:** use your personal GitHub no-reply address. It keeps your real email private **and** still grows your grass.

### How to find your no-reply address

1. Go to **GitHub → Settings → Emails**.
2. Enable **Keep my email addresses private** if it is not already on.
3. Your no-reply address is shown there, in one of these forms:
   - `username@users.noreply.github.com`, or
   - `ID+username@users.noreply.github.com` (newer accounts include a numeric ID).
4. Put that exact address in the `git config user.email` line above, and set `user.name` to your GitHub username.

> **Never put a real email address in the workflow.** A plain-text email in a public repo gets harvested by spam bots. The no-reply address avoids this completely.

> Note: this only affects **future** commits. Email addresses already written into past commit history are not changed by editing the workflow.

---

## Scheduling and time zones

The daily run is controlled by the `cron` line in `.github/workflows/atcoder-backup.yml`:

```yaml
schedule:
  - cron: '0 5 * * *'   # 05:00 UTC every day
```

A few things to know:

- **GitHub Actions cron is always in UTC.** It does **not** use your local time zone. To run at a specific local time, convert that time to UTC yourself. For example, `0 5 * * *` is 05:00 UTC, which is midnight in US Eastern Standard Time (UTC−5).
- **Daylight Saving Time is not handled automatically.** Since the schedule is fixed in UTC, a time that is midnight during standard time becomes 1:00 AM during daylight time (e.g. EDT, UTC−4). If you need an exact local time year-round, adjust the cron value when the clocks change, or just pick a time where a one-hour shift does not matter.
- Scheduled runs can be delayed by a few minutes (sometimes more) when GitHub's runners are busy, so do not rely on the job firing at the exact minute.

To change the time, edit the cron value. For example, `0 15 * * *` runs at 15:00 UTC daily.

---

## Supported languages

The file extension is chosen from the submission language. Currently mapped:

`C++` `Python` `PyPy` `Java` `C#` `Ruby` `Rust` `Go` `JavaScript` `TypeScript` `PHP` `Haskell` `Fortran`

Anything not in the list is saved with a `.txt` extension. To add a language, edit the `EXTENSION_MAP` dictionary in `fetch_submissions.py`.

---

## Please use this responsibly

This tool relies on two external services. Please keep it well-behaved so that everyone can keep using these resources.

- **AtCoder Problems API (kenkoooo):** Per the [API documentation](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md), do not call the API too frequently and leave **at least one second** between requests. This tool is designed to run **at most once a day** and only fetches **your own** submissions, which keeps it far below any level that would cause load. Do not modify it into something that crawls many users or runs at high frequency.
- **AtCoder:** Source code is fetched directly from the AtCoder submission pages. The script sleeps a few seconds between requests for the same reason. Again, please only back up your own submissions.

If you ever need to make a large number of requests, read the API documentation first and contact the maintainers as it suggests.

---

## Notes & limitations

- Submissions take time to appear in the AtCoder Problems database after a contest (sometimes hours, occasionally longer), so a problem you just solved may not be backed up until the next day's run.
- The AtCoder Problems API is provided **unofficially**. The maintainers may change or deprecate endpoints, so if the backup stops working, check the [API documentation](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md) for changes.
- The code page is fetched with [`cloudscraper`](https://pypi.org/project/cloudscraper/) because the API sits behind Cloudflare.

---

## Credits

- Submission data is provided by [AtCoder Problems](https://kenkoooo.com/atcoder/) by [@kenkoooo](https://github.com/kenkoooo). Thank you for the great service.

---
---

# 日本語版 

# AtCoder 提出コードバックアップ

自分の **AC（正解）した** AtCoder の提出コードを、毎日定期的に Git リポジトリへ自動バックアップする GitHub Actions ワークフローです。

解いた各問題について、最新の AC 提出のソースコードをコンテストごとに整理して保存します。

```
submissions/
├── abc459/
│   ├── abc459_a.py
│   ├── abc459_b.py
│   └── abc459_c.py
├── abc460/
│   └── abc460_a.py
└── ...
```

バックアップは GitHub Actions 上で完結するため、一度セットアップすれば手動で何かを実行する必要はありません。毎日の自動コミットは GitHub のコントリビューショングラフ（いわゆる「草」）にも反映されます。正しく設定する方法は [コミットの author 設定とコントリビューショングラフ](#コミットの-author-設定とコントリビューショングラフ) を参照してください。

---

## 仕組み

1. [AtCoder Problems API](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md)（kenkoooo 氏作）を呼び出し、自分の提出一覧を取得します。
2. この API は 1 リクエストにつき最大 500 件しか返さないため、スクリプトは `from_second` パラメータを使って全件取得できるまでページングします。
3. 各問題について、最新の AC 提出だけを残します。
4. それぞれの提出について、AtCoder の提出ページからソースコードを取得し、`submissions/<contest_id>/<problem_id>.<ext>` に書き出します。
5. ワークフローが、新規・変更されたファイルをコミットしてプッシュします。

ある問題のファイルが既に存在する場合はスキップされます。そのため、毎日の実行では新しく解いた問題のコードだけを取得します。

---

## セットアップ

1. このリポジトリを自分の GitHub アカウントに **フォーク（または複製）** します。

2. **自分の AtCoder ユーザー ID を設定** します。`fetch_submissions.py` を開いて次を変更します。

   ```python
   USER_ID = "your_atcoder_id"
   ```

3. **GitHub Actions を有効化** します。リポジトリの **Actions** タブを開き、プロンプトが出たらワークフローを有効化してください。

4. **ワークフローの権限を確認** します。コミットをプッシュするには書き込み権限が必要です。同梱のワークフローはすでにこれを要求しています。

   ```yaml
   permissions:
     contents: write
   ```

5. **コミットの author を設定** します。次のセクションを参照してください。これによって、自動コミットがコントリビューショングラフに反映されるか、そしてメールアドレスを公開せずに済むかが決まります。

6. **実行** します。Actions タブから手動で実行（**Run workflow**）するか、毎日の定期実行を待ちます。

初回実行では AC 履歴の全件をバックアップするため、時間がかかることがあります。2 回目以降は新しく解いた問題だけを取得するので、すぐに終わります。

---

## コミットの author 設定とコントリビューショングラフ

実際のコミットはワークフローが行うため、**そのコミットが誰の貢献として記録されるか**は `.github/workflows/atcoder-backup.yml` 内の `git config` の行で決まります。

```yaml
- name: Commit and Push
  run: |
    git config user.name  "your_github_username"
    git config user.email "your_github_username@users.noreply.github.com"
    git add -A
    if ! git diff --staged --quiet; then
      git commit -m "Auto backup: $(date -u)"
      git push
    fi
```

### コミットをコントリビューショングラフ（草）に反映させたいか？

GitHub は、コミットの **author メールが自分の GitHub アカウントに登録済み（verified）のメールと一致する場合にのみ**、そのコミットをコントリビューショングラフ（草）に加えます。したがって、どのメールを設定するかが重要です。

| 設定するメール | メールが公開される？ | 草が生える？ |
| --- | --- | --- |
| `your_github_username@users.noreply.github.com` | されない | **生える** |
| `12345678+your_github_username@users.noreply.github.com` | されない | **生える** |
| 実際のメール（個人用・職場用など） | **される — スパムに収集される** | 生える |
| `github-actions[bot]@users.noreply.github.com` | されない | 生えない（bot 扱い） |

**推奨：** 自分の GitHub no-reply アドレスを使ってください。実際のメールを非公開に保ったまま、草も生やせます。

### no-reply アドレスの確認方法

1. **GitHub → Settings → Emails** を開きます。
2. **Keep my email addresses private** がオフなら、オンにします。
3. no-reply アドレスがそこに表示されます。次のいずれかの形式です。
   - `username@users.noreply.github.com`、または
   - `ID+username@users.noreply.github.com`（新しめのアカウントは数字 ID 付き）
4. その正確なアドレスを上の `git config user.email` に設定し、`user.name` には自分の GitHub ユーザー名を設定します。

> **実際のメールアドレスをワークフローに書かないでください。** 公開リポジトリ内の平文メールはスパムボットに収集されます。no-reply アドレスを使えばこれを完全に回避できます。

---

## スケジュールとタイムゾーン

毎日の実行は `.github/workflows/atcoder-backup.yml` 内の `cron` 行で制御されます。

```yaml
schedule:
  - cron: '0 5 * * *'   # 毎日 05:00 UTC
```

- **GitHub Actions の cron は常に UTC です。** ローカルのタイムゾーンは使われません。特定の現地時刻に実行したい場合は、自分でその時刻を UTC に変換してください。例えば `0 5 * * *` は 05:00 UTC で、これはアメリカ東部標準時（EST, UTC−5）の深夜 0 時にあたります。
- **夏時間（サマータイム）は自動調整されません。** スケジュールは UTC 固定なので、標準時で深夜 0 時だった時刻は、夏時間（例：EDT, UTC−4）になると現地の 1:00 AM にずれます。一年を通して正確な現地時刻が必要なら、時計が切り替わるタイミングで cron の値を調整するか、1 時間ずれても問題ない時間帯を選んでください。
- 定期実行は、GitHub のランナーが混雑しているときに数分（場合によってはそれ以上）遅延することがあります。指定した分ちょうどに実行されることを当てにしないでください。

時刻を変更するには cron の値を編集します。例えば `0 15 * * *` は 15:00 UTC、日本時間（JST, UTC+9）の翌日 0:00（深夜）に実行されます。

---

## 対応言語

ファイルの拡張子は提出言語から選ばれます。現在マッピングされているもの：

`C++` `Python` `PyPy` `Java` `C#` `Ruby` `Rust` `Go` `JavaScript` `TypeScript` `PHP` `Haskell` `Fortran`

リストにないものは `.txt` 拡張子で保存されます。言語を追加するには、`fetch_submissions.py` 内の `EXTENSION_MAP` 辞書を編集してください。

---

## 節度を持って利用してください

このツールは 2 つの外部サービスに依存しています。今後もこれらのリソースを使い続けられるよう、行儀よく利用しましょう。

- **AtCoder Problems API（kenkoooo 氏）：** [API ドキュメント](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md)に従い、API を頻繁に叩かず、リクエスト間に**最低 1 秒**の間隔を空けてください。このツールは**1 日 1 回まで**の実行を想定しており、**自分自身の**提出のみを取得するため、負荷をかけるレベルにはるかに及びません。多数のユーザーをクロールしたり高頻度で実行したりするように改造しないでください。
- **AtCoder：** ソースコードは AtCoder の提出ページから直接取得しています。同じ理由で、スクリプトはリクエスト間に数秒スリープします。こちらも、自分自身の提出のみをバックアップしてください。

---

## 注意点・制約

- 提出はコンテスト後、AtCoder Problems のデータベースに反映されるまで時間がかかります（数時間、場合によってはそれ以上）。そのため、解いたばかりの問題は翌日の実行までバックアップされないことがあります。
- AtCoder Problems API は**非公式に**提供されています。メンテナがエンドポイントを変更・廃止することがあるため、バックアップが動かなくなった場合は [API ドキュメント](https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md)で変更を確認してください。
- API が Cloudflare の背後にあるため、コードページの取得には [`cloudscraper`](https://pypi.org/project/cloudscraper/) を使用しています。

---

## クレジット

- 提出データは [@kenkoooo](https://github.com/kenkoooo) 氏による [AtCoder Problems](https://kenkoooo.com/atcoder/) から提供されています。素晴らしいサービスをありがとうございます。
