import os
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# .env ファイルを読み込む
load_dotenv()

# 環境変数から設定を取得
FOLDER_ID = os.environ.get('GOOGLE_DRIVE_FOLDER_ID')

# 権限設定
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    # 実行ファイルからの相対パスで各ファイルの場所を設定
    base_dir = os.path.dirname(os.path.abspath(__file__))
    creds_path = os.path.join(base_dir, 'credentials.json')
    token_path = os.path.join(base_dir, 'token.json')

    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # 1. あなたが用意したファイル名を指定
    target_filename = 'test_data.txt' 
    test_file_path = os.path.join(base_dir, target_filename)

    # (ファイル作成の with open... ブロックは削除)

    # 2. アップロード時の名前も元のファイル名にする
    file_metadata = {'name': target_filename}
    # --- ここまで修正 ---

    if FOLDER_ID:
        file_metadata['parents'] = [FOLDER_ID]

    media = MediaFileUpload(test_file_path, mimetype='text/plain')
    
    print("Googleドライブへアップロード中...")
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"完了しました！ ファイルID: {file.get('id')}")

if __name__ == '__main__':
    main()