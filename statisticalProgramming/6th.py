import pandas as pd
import matplotlib.pyplot as plt


def t1():
    data = {
        "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "A": [59, 24, 62, 48, 58, 19, 32, 88, 47, 63],
    }

    df = pd.DataFrame(data)

    a_ave = df["A"].mean()

    v = sum((df["A"] - a_ave) ** 2) / len(df["A"])
    # pyではdf["A"] - 5という方法でスカラー倍などの行列計算が行える

    # ddof
    #   1: (既定)一部のデータから全体のデータを推測して計算
    #   0: 与えられたデータが集合全体である、として計算
    # 既定では v = sum((df["A"] - a_ave) ** 2) / (len(df["A"]) - 1) と等しい
    print("Arithmetic variance ->", v)
    print("Variance function ->", df["A"].var(ddof=0))
    print("")

    SD = v ** 0.5
    print("Arithmetic standard deviation ->", SD)
    print("SD function ->", df["A"].std(ddof=0))
    print("")

    SE = SD / len(df["A"]) ** 0.5
    print("Arithmetic standard error ->", SE)
    print("SE function ->", df["A"].sem(ddof=0))
    print("")


# t1()

def t2():
    data = {
        "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "A": [59, 24, 62, 48, 58, 19, 32, 88, 47, 63],
        "B": [49, 50, 49, 54, 45, 52, 56, 48, 45, 52],
    }

    df = pd.DataFrame(data)

    a_ave = df["A"].mean()
    b_ave = df["B"].mean()

    print("A average -> ", a_ave)
    print("B average -> ", b_ave)

    fig = plt.figure(tight_layout=True)

    x_min = 0
    x_max = 11

    ax1 = fig.add_subplot(1, 2, 1)
    ax1 = plt.scatter(df["ID"], df["A"], c="b")
    plt.hlines(a_ave, x_min, x_max, "black")
    plt.xlabel("ID")
    plt.ylabel("A")
    plt.xlim(x_min, x_max)
    plt.ylim(0, 100)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2 = plt.scatter(df["ID"], df["B"], c="r")
    plt.hlines(b_ave, x_min, x_max, "black")
    plt.xlabel("ID")
    plt.ylabel("B")
    plt.xlim(x_min, x_max)
    plt.ylim(0, 100)

    plt.show()


# t2()


def t3():
    data = {
        "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "A": [59, 24, 62, 48, 58, 19, 32, 88, 47, 63],
        "B": [49, 50, 49, 54, 45, 52, 56, 48, 45, 52],
    }

    df = pd.DataFrame(data)

    a_ave = df["A"].mean()
    b_ave = df["B"].mean()

    print("A average -> ", a_ave)
    print("B average -> ", b_ave)
    print()

    a_std = df["A"].std(ddof=0)
    b_std = df["B"].std(ddof=0)
    print("A STD -> ", a_std)
    print("B STD -> ", b_std)
    print()

    print("A range ->", a_ave - a_std, "to", a_ave + a_std)
    print("B range ->", b_ave - b_std, "to", b_ave + b_std)

    fig = plt.figure(tight_layout=True)

    x_min = 0
    x_max = 11

    ax1 = fig.add_subplot(1, 2, 1)
    ax1 = plt.scatter(df["ID"], df["A"], c="b")
    plt.hlines(a_ave, x_min, x_max, "black")
    plt.hlines(a_ave + a_std, x_min, x_max, color="red", linestyle="dashed")
    plt.hlines(a_ave - a_std, x_min, x_max, color="red", linestyle="dashed")
    plt.xlabel("ID")
    plt.ylabel("A")
    plt.xlabel("ID")
    plt.ylabel("A")
    plt.xlim(x_min, x_max)
    plt.ylim(0, 100)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2 = plt.scatter(df["ID"], df["B"], c="r")
    plt.hlines(b_ave, x_min, x_max, "black")
    plt.hlines(b_ave + b_std, x_min, x_max, color="red", linestyle="dashed")
    plt.hlines(b_ave - b_std, x_min, x_max, color="red", linestyle="dashed")
    plt.xlabel("ID")
    plt.ylabel("B")
    plt.xlim(x_min, x_max)
    plt.ylim(0, 100)

    plt.savefig("6th_t3.png", dpi=350)
    plt.show()


t3()


def t4():
    import random
    import pandas as pd
    import matplotlib.pyplot as plt

    # step数は釘の数みたいなもの
    # count個の鉄球を落とした時にどんな風に積みあがるかを表す
    def galton(steps, count):
        ans = []
        for i in range(count):
            val = 50
            for j in range(steps):
                if random.randint(0, 1) == 0:
                    val -= 1
                else:
                    val += 1

            ans.append(val)
        df = pd.DataFrame(ans)
        df[0].plot.hist()
        plt.title(str(steps) + " steps (" + str(count) + ")")
        plt.ylabel("")
        plt.savefig(str(steps) + "_steps_(" + str(count) + ").png", dpi=350)
        plt.show()

    # 試行回数を増やしていくと、中心部分に寄っていく
    # これを「中心極限定理」と言う
    galton(10, 10000)


t4()
