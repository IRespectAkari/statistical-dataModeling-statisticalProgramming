# ばらつきの珍しさ

def t1():
    # 平均値0のものを標準ガウスなんちゃらと言う
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats import norm

    mean = 0
    std = 1
    value = 3

    cdf = norm.cdf(x=value, loc=mean, scale=std)

    print(value, "は、上から", (1 - cdf) * 100, "%")
    # 上から何％かを知りたいときは(1 - cdf)

    x = np.linspace(-4, 4, 100)
    y_pdf = norm.pdf(x)

    plt.plot(x, y_pdf)
    plt.xlabel("x")
    plt.ylabel("p")
    plt.title("Standard normal distribution")
    plt.ylim([0, 0.44])
    plt.vlines(3, 0, norm.pdf(3), color="r")
    plt.savefig("7th_test.png", dpi=350)
    plt.show()
    # 競技人口10万人の平均スコア0、標準偏差1、スコア3の人の数は10万×0.13=130人程
    # だと言うことになる


# t1()


def t2():
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats import norm

    mean = 0
    std = 1

    ppf = norm.ppf(q=(1 - 0.00001), loc=mean, scale=std)
    # scipy.stats.norm.ppf(q, loc=0, scale=1)
    # 〇%を取るためには何を取る必要があるのかを教えてくれる
    # （競技人口10万人のゲームにおいてスコア約3.09以上とれば、1位になれることが予想できる）
    # また、スコア3.00～約3.09の間で130人が競っていることも予想できる
    # 知りたい確率、平均値（初期値0）、標準偏差（初期値1）
    # 知りたい確率が正規分布において、下からどの位置かを算出
    # 上からの位置を知りたいときは(1 - 確率)とする

    print("Score ->", ppf)
    # Score -> 4.264890793923841


# t2()

def t3():
    # 数学試験の平均は50、標準偏差5
    # 英語試験の平均は70、標準偏差8
    # Aくんは数学60、英語80、数学と英語どちらを褒める？
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats import norm

    scoreM = 60
    meanM = 50
    stdM = 5

    scoreE = 80
    meanE = 70
    stdE = 8

    cdf_M = norm.cdf(x=scoreM, loc=meanM, scale=stdM)
    cdf_E = norm.cdf(x=scoreE, loc=meanE, scale=stdE)

    print("cdf_M ->", (1 - cdf_M) * 100, "%")
    print("cdf_E ->", (1 - cdf_E) * 100, "%")
    # 上位何%かを表示している
    # それは赤い線から右端までの面積と等しい
    # ヒストグラムだから面積

    x = np.linspace(0, 100, 1000)
    y_M = norm.pdf(x=x, loc=meanM, scale=stdM)
    y_E = norm.pdf(x=x, loc=meanE, scale=stdE)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y_M)
    ax1.set_title("Math")
    ax1.set_xlabel("x")
    ax1.set_ylabel("p")
    ax1.set_ylim([0, 0.09])
    ax1.vlines(scoreM, 0, norm.pdf(scoreM, meanM, stdM), color="r")

    ax2.plot(x, y_E)
    ax2.set_title("English")
    ax2.set_xlabel("x")
    ax2.set_ylabel("p")
    ax2.set_ylim([0, 0.09])
    ax2.vlines(scoreE, 0, norm.pdf(scoreE, meanE, stdE), color="r")

    fig.tight_layout()
    plt.savefig("7th_test.png", dpi=350)
    plt.show()


t3()
