import gspread
import json

# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# 認証情報設定
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'D:\Python\gspread-sample-274519-4a41cd7b3ded.json', scope)

# OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

# 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '1bEwiWs_kH8IvlFlwU9n8wPAjwwI6uEfzc6mVAvYzWqs'

# 共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

# A1セルの値を受け取る
import_value = int(worksheet.acell('A1').value)

# A1セルの値に100加算した値をB1セルに表示させる
export_value = import_value+100
worksheet.update_cell(1, 2, export_value)

# B1セルの値に100掛けた値をC1セルに表示させる
export_value = int(worksheet.acell('B1').value)*100
worksheet.update_cell(1, 3, export_value)
