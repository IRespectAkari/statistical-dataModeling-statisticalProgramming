# 複数データを同時に比較する方法

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

    sns.heatmap(df.corr(), annot=True, vmax=1, vmin=-1, center=0, cmap="blue")
    # heatmap(データ, annot=True, vmax=最大値, vmin=最小値, center=0)
    # cmap="bwr"やcmap="blue"
    plt.savefig("9th_test.png", dpi=350)
    plt.show()


# t1()
# kaizenplatform.com/content/heat-map

# 複数データを同時に比較する方法

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

    sns.pairplot(data=df)
    # mathとmathなど、同じ項目が交差する所がヒストグラムになっている
    # 同じ縦列の横軸のスケールは統一されていて、同じ横列の縦軸のスケールも統一されている
    plt.savefig("9th_test_2.png", dpi=350)
    plt.show()


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

    sns.pairplot(data=df)
    # mathとmathなど、同じ項目が交差する所がヒストグラムになっている
    # 同じ縦列の横軸のスケールは統一されていて、同じ横列の縦軸のスケールも統一されている
    # 分かりにくいからオススメしない
    plt.savefig("9th_test_3.png", dpi=350)
    plt.show()


# t3()


def t4():
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    data = {
        "math": [100, 85, 90, 95, 80, 80, 75, 65, 65, 60, 55, 45, 45],
        "science": [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48],
        "society": [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60],
    }

    df = pd.DataFrame(data)

    # sns.pairplot(df, kind="kde")
    sns.pairplot(df, kind="reg")
    # mathとmathなど、同じ項目が交差する所がヒストグラムになっている
    # 同じ縦列の横軸のスケールは統一されていて、同じ横列の縦軸のスケールも統一されている
    # 分かりにくいからオススメしない
    plt.savefig("9th_test_4.png", dpi=350)
    plt.show()


t4()
