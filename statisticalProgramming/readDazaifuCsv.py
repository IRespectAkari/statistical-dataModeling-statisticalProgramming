import pandas as pd


def readCsv(path):
    try:
        df = pd.read_csv(path, index_col=0)
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding='Shift_JIS', index_col=0)
    return df


# df = pd.read_csv("dazaifu.csv") # UTF-8として読込
# df = pd.read_csv("dazaifu.csv", encoding='Shift_JIS') # エンコードをShift_JISに指定
# df = pd.read_csv("dazaifu.csv", encoding='Shift_JIS', index_col=0) # 左に連番を振らない
# df = pd.read_csv("dazaifu.csv", encoding='Shift_JIS', index_col=0, header=None) # headerが無いデータとして読込、自動的に0始まり連番が振られる
df = readCsv("dazaifu.csv")
print(df)
print(df.columns)
print(df.index)
print(len(df))
print(df["平均気温(℃)"])  # SELECT 平均気温(℃) FROM df;
print(df[["平均気温(℃)", "降水量の合計(mm)"]])  # SELECT 平均気温(℃), 降水量の合計(mm) FROM df;　headerを2つ選ぶときは、[]を2重にする！
print(df.iloc[0])  # SELECT * FROM df WHERE id = 0;
print(df.iloc[0]["平均気温(℃)"])  # SELECT 平均気温(℃) FROM df WHERE id = 0;
print(df.iloc[0, 0])  # 上`print(df.iloc[0]["平均気温(℃)"])`と等しい
# 何故なら、index_col=0でインデックスを非表示にしたことで年月日がインデックスとして扱われ、平均気温(℃)がヘッダーの0番目になっているから


# ###### 授業メモ ######
# headerを指定したいプログラムを書きたいときは、目で見て入力するのではなく、df.columnsで表示させたheaderをコピペすること！！
