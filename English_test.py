import mojimoji
import random
import pprint
import pandas as pd
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
SPREADSHEET_KEY = '18F-BuJnErlMz4AG8EaGNyaP82yHU_6ajX28Qb0PeVR8'

# 共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

# シートの一覧を二次元配列に格納する
cell_list = worksheet.get_all_values()
df = pd.DataFrame(cell_list, columns=['単語', '日本語訳'])

# 全角文字幅を考慮
pd.set_option('display.unicode.east_asian_width', True)


# 判定
def Judge(word, ans):
    cell = worksheet.find(word)
    if df.at[int(cell.row)-1, '日本語訳'] == ans:
        print('★  正解')
    else:
        print('★  不正解')
        print('正解 => ' + df.at[int(cell.row)-1, '日本語訳'])
    print('---------------------------------------')


# テスト
def test():
    # 何回やるか
    play = int(mojimoji.zen_to_han(input('何回やりますか => ')))
    print('---------------------------------------')

    # プレイ
    count = 0
    while play > count:
        # 問題
        word = df.at[random.randint(0, len(df)-1), '単語']
        # 回答
        ans = input(word + ' => ')
        # 判定
        Judge(word, ans)

        count += 1


# 問題を追加
def add():
    row_count = 1
    end = ['end', 'End', 'END']
    while True:
        colValues_list = worksheet.col_values(1)
        word = input('『end, End, END』と入力すると終わります > ')
        if word in end:
            break

        check = False
        for i in colValues_list:
            if i == word:
                check = True
                break
        if not check:
            worksheet.update_cell(len(df) + row_count, 1, word)
            word = input('日本語訳を入力してください > ')
            worksheet.update_cell(len(df) + row_count, 2, word)
            row_count += 1
        else:
            print('既に入力されています')


# プレイ
def play():
    print('★  テストをするなら『t』\n★  問題を追加するなら『a』')
    hoge = input('> ')
    if hoge == 't':
        test()
    elif hoge == 'a':
        add()
    else:
        play()


if __name__ == "__main__":
    play()
