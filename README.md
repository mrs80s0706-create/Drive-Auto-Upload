# Drive-Auto-Upload

![Google Drive API連携 ファイル自動アップロードシステム](banner.png)

Google Driveへのファイル自動アップロードツールです。OAuth2認証を使用し、指定ファイルをGoogle Driveの特定フォルダへ自動でアップロードします。

## 概要 / Overview

**日本語:**
このツールは、Pythonスクリプトを使ってローカルファイルをGoogle Driveへ自動的にアップロードします。Google OAuth2による安全な認証フローに対応しており、一度認証するとトークンが保存されて次回から自動ログインが可能です。

**English:**
This tool automatically uploads local files to Google Drive using Python scripts. It supports secure authentication via Google OAuth2, and once authenticated, the token is saved for automatic login on subsequent runs.

---

## インストール方法 / Installation

```bash
pip install -r requirements.txt
```

### 必要ライブラリ / Dependencies

| ライブラリ | バージョン |
|---|---|
| google-api-python-client | 2.115.0 |
| google-auth-httplib2 | 0.2.0 |
| google-auth-oauthlib | 1.2.0 |
| python-dotenv | 1.0.1 |

---

## Google Cloud Consoleでの認証設定手順 / Google Cloud Setup

### 1. プロジェクトを作成する
1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. 右上の「プロジェクトを選択」→「新しいプロジェクト」をクリック
3. プロジェクト名を入力して「作成」

### 2. Google Drive APIを有効化する
1. 左メニュー「APIとサービス」→「ライブラリ」
2. 検索欄に「Google Drive API」と入力
3. 「Google Drive API」を選択して「有効にする」

### 3. OAuth 2.0 認証情報を作成する
1. 「APIとサービス」→「認証情報」→「認証情報を作成」→「OAuthクライアントID」
2. アプリケーションの種類：「デスクトップアプリ」を選択
3. 名前を入力して「作成」
4. ダウンロードボタンからJSONファイルをダウンロード
5. ダウンロードしたファイルを **** にリネームして、このスクリプトと同じディレクトリに配置

### 4. OAuth同意画面を設定する（初回のみ）
1. 「OAuth同意画面」→ユーザーの種類「外部」→「作成」
2. アプリ名・メールアドレスを入力して保存
3. 「テストユーザー」に自分のGoogleアカウントのメールアドレスを追加

---

## 設定項目 / Configuration

プロジェクトルートに  ファイルを作成して以下を設定してください。

```env
GOOGLE_DRIVE_FOLDER_ID=your_folder_id_here
```

| 設定キー | 説明 | 取得方法 |
|---|---|---|
|  | アップロード先フォルダのID | Google DriveでフォルダURLの末尾の文字列 |

**フォルダIDの確認方法:**
Google Driveでフォルダをブラウザで開いた際のURL例：

この場合、 がフォルダIDです。

---

## 実行方法 / Usage

### 1. アップロードするファイルを準備する
スクリプトと同じディレクトリに  を配置します（ファイル名はスクリプト内で変更可能）。

### 2. スクリプトを実行する
```bash
python upload_test.py
```

### 3. 初回認証
初回実行時はブラウザが自動で開き、Googleアカウントでのログインを求められます。
ログイン・許可後、 が自動生成され、次回からは認証不要になります。

---

## ディレクトリ構成 / Project Structure

```
Drive-Auto-Upload/
├── upload_test.py      # メイン実行ファイル
├── credentials.json    # Google Cloud認証情報（要作成・Gitignore推奨）
├── token.json          # 認証トークン（初回認証後に自動生成）
├── test_data.txt       # アップロード対象ファイル（要準備）
├── requirements.txt    # 依存ライブラリ一覧
├── .env                # 環境変数設定ファイル
└── README.md           # 本説明書
```

> **セキュリティ注意:**  と  は個人の認証情報です。 に追加してGitHubにpushしないように注意してください。

---

## ライセンス / License

MIT License
