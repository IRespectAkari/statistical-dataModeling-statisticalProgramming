from matplotlib import pyplot as plt


def t1():
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    data = {
        "math": [100, 85, 90, 95, 80, 80, 75, 65, 65, 60, 55, 45, 45],
        "science": [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48],
        "society": [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60],
    }
    df = pd.DataFrame(data)
    print(df.head())

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.scatter(df["math"], df["science"])
    ax1.set_title("Math and Science")
    ax1.set_xlabel("Math")
    ax1.set_ylabel("Science")
    ax1.set_xlim([40, 100])
    ax1.set_ylim([45, 100])

    ax2.scatter(df["science"], df["society"])
    ax2.set_title("Math and Society")
    ax2.set_xlabel("Math")
    ax2.set_ylabel("Society")
    ax2.set_xlim([40, 100])
    ax2.set_ylim([45, 100])

    fig.tight_layout()
    plt.savefig("8th_test.png", dpi=350)
    plt.show()


# t1()
# グラフから読み取れること
# 数学も理科も計算問題が多い
# 数学は計算問題が多く、社会は知識を問う問題が多い
# 両方できる人はなに？ --> 頭が良い人は両方できるから

def t2():
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    data = {
        "math": [100, 85, 90, 95, 80, 80, 75, 65, 65, 60, 55, 45, 45],
        "science": [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48],
        "society": [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60],
    }
    df = pd.DataFrame(data)
    print("Math and Science ->", df.corr()["math"]["science"])
    print("Math and Society ->", df.corr()["math"]["society"])
    # 相関のことを英語でCorrelation


# t2()


def t3():
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    data = {
        "math": [100, 85, 90, 95, 80, 80, 75, 65, 65, 60, 55, 45, 45],
        "science": [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48],
        "society": [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60],
    }

    df = pd.DataFrame(data)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    sns.regplot(data=df, x="math", y="science", line_kws={"color": "red"}, ax=ax1)
    ax1.set_title("Math and Science")
    ax1.set_xlabel("Math")
    ax1.set_ylabel("Science")
    ax1.set_xlim([40, 100])
    ax1.set_ylim([45, 100])

    sns.regplot(data=df, x="math", y="society", line_kws={"color": "red"}, ax=ax2)
    ax2.set_title("Math and Society")
    ax2.set_xlabel("Math")
    ax2.set_ylabel("Society")
    ax2.set_xlim([40, 100])
    ax2.set_ylim([45, 100])

    fig.tight_layout()
    plt.savefig("8th_test2.png", dpi=350)
    plt.show()


# t3()


# 今回の新関数 sns.regplot(data=データの配列, x=データの変数名, y=データの変数名, line_kws={"color": "色"})
# 今回の使用例 sns.regplot(data=df, x="math", y="science", line_kws={"color": "red"}, ax=ax1)
# 赤い直線  線形回帰
# 薄く赤い範囲　信頼区間（95％の確率でこの範囲内に入る）
# 何故赤く塗るのか  散布図を作るときはregplotを使うように
# 線形かどうかを判断するために直線を引くと、それがどのくらい相関係数があるのかを見た目で判断しにくい
# regplotを使うと（信頼区間を表示すると）大体の相関係数が伝わるから


def t4():
    import pandas as pd
    import seaborn as sns

    data = {
        "x": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        "y": [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
    }

    # データフレームを作成
    df = pd.DataFrame(data)

    # ピアソンの相関係数を計算
    print("x and y ->", df.corr().loc["x"]["y"])

    # 散布図を作成
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df["x"], df["y"], s=60)
    ax.set_title("x and y")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    plt.savefig("8th_test4.png", dpi=350)
    plt.show()


# t4()


# t4()では相関係数が無いと判断された！相関を評価できる関数を調べて書き換えよう
def t5():
    import pandas as pd
    import seaborn as sns
    # import minepy as mine
    # import dcor

    def distance_correlation(x, y):
        import numpy as np

        x = np.asarray(x, dtype=float).ravel()
        y = np.asarray(y, dtype=float).ravel()

        # データ間の距離を計算
        a = np.abs(x[:, None] - x[None, :])
        b = np.abs(y[:, None] - y[None, :])

        # 距離行列の中心化
        A = a - a.mean(axis=0) - a.mean(axis=1)[:, None] + a.mean()
        B = b - b.mean(axis=0) - b.mean(axis=1)[:, None] + b.mean()

        # 距離共分散・距離分散
        dcov = np.mean(A * B)
        dvar_x = np.mean(A ** 2)
        dvar_y = np.mean(B ** 2)

        if dvar_x == 0 or dvar_y == 0:
            return np.nan

        return np.sqrt(max(dcov, 0) / np.sqrt(dvar_x * dvar_y))

    data = {
        "x": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        "y": [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
    }

    # データフレームを作成
    df = pd.DataFrame(data)

    # ピアソンの相関係数を計算
    fig, ax = plt.subplots(figsize=(6, 4))

    # ピアソンの相関係数
    pearson = df["x"].corr(df["y"])
    # 距離相関係数
    dcor = distance_correlation(df["x"], df["y"])


    print(f"ピアソンの相関係数: {pearson:.4f}")
    print(f"距離相関係数: {dcor:.4f}")

    sns.regplot(data=df, x="x", y="y", order=2, line_kws={"color": "red"}, ax=ax)
    ax.set_title("x and y")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    fig.tight_layout()
    plt.savefig("8th_test5.png", dpi=350)
    plt.show()


t5()


# 説明用
def distance_correlation2(x, y):
    import numpy as np

    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()

    # データ間の距離を計算
    a = np.abs(x[:, None] - x[None, :])
    b = np.abs(y[:, None] - y[None, :])

    # 距離行列の中心化
    A = a - a.mean(axis=0) - a.mean(axis=1)[:, None] + a.mean()
    B = b - b.mean(axis=0) - b.mean(axis=1)[:, None] + b.mean()

    # 距離共分散・距離分散
    dcov = np.mean(A * B)
    dvar_x = np.mean(A ** 2)
    dvar_y = np.mean(B ** 2)

    if dvar_x == 0 or dvar_y == 0:
        return np.nan

    return np.sqrt(max(dcov, 0) / np.sqrt(dvar_x * dvar_y))

# 空行削除版
def distance_correlation3(x, y):
    import numpy as np;
    x = np.asarray(x, dtype=float).ravel();
    y = np.asarray(y, dtype=float).ravel();
    a = np.abs(x[:, None] - x[None, :]);
    b = np.abs(y[:, None] - y[None, :]);
    A = a - a.mean(axis=0) - a.mean(axis=1)[:, None] + a.mean();
    B = b - b.mean(axis=0) - b.mean(axis=1)[:, None] + b.mean();
    dcov = np.mean(A * B);
    dvar_x = np.mean(A ** 2);
    dvar_y = np.mean(B ** 2);
    if dvar_x == 0 or dvar_y == 0:
        return np.nan;
    return np.sqrt(max(dcov, 0) / np.sqrt(dvar_x * dvar_y));