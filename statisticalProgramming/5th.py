import pandas as pd
import matplotlib.pyplot as plt


def t1():
    df1 = pd.read_csv('titanic.csv', index_col=0)

    df_male = len(df1[df1['Sex'] == 'male'])
    df_female = len(df1[df1['Sex'] == 'female'])

    x = [df_male, df_female]
    labels = ['male', 'female']
    colors = ['blue', 'red']

    plt.pie(x, labels=labels, colors=colors, autopct='%.1f%%')
    # pie -> 円グラフ
    # autopct='%.1f%%' -> 勝手に比率を計算して表示してくれる
    # %.1f%で計算し、最後に%を表示用に追加している
    plt.show()


# t1()


def t2():
    df1 = pd.read_csv('titanic.csv', index_col=0)

    df_male = df1[df1["Sex"] == "male"]
    df_female = df1[df1["Sex"] == "female"]

    left = [1, 2]
    x = [df_male["Age"].mean(), df_female["Age"].mean()]
    err = [df_male["Age"].sem(), df_female["Age"].sem()]
    err2 = [df_male["Age"].std(), df_female["Age"].std()]
    # sem: 標準誤差, sd: 標準偏差, sd = sqrt(分散)
    # sem: sd / sqrt(n), sd = sqrt(sigma(i=1, n, x_i - Ave) / n)
    # semよりstdの方が誤差が大きく出る。だからちょっとでも誤魔化したいときはsem, データがきれいだと主張したいときはstd
    labels = ['male', 'female']
    colors = ['blue', 'red']

    plt.bar(left, x, yerr=err, capsize=10, color=colors, align='center')
    # plt.bar(left, x, yerr=err2, capsize=10, color=colors, align='center')
    plt.xticks(left, labels)
    plt.ylabel('The number of people')
    plt.xlabel('The number of people')
    plt.show()


# t2()

def t3():
    import seaborn as sns

    df1 = pd.read_csv('titanic.csv', index_col=0)

    df_male = df1[df1["Sex"] == "male"]
    df_female = df1[df1["Sex"] == "female"]

    left = [0, 1]
    x = [df_male["Age"], df_female["Age"]]
    labels = ['male', 'female']

    sns.boxplot(x, width=0.2)
    plt.xticks(left, labels)
    plt.xlabel('Sex')
    plt.ylabel('The number of people')
    plt.show()
    # 汚いデータも含まれるのが平均値、汚いデータは汚いデータとしてプロットされるのが箱ひげ図


# t3()


def t4():
    import seaborn as sns

    df1 = pd.read_csv('titanic.csv', index_col=0)

    sns.set_theme(style='whitegrid', context='talk')

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=df1,
        x="Sex",
        y="Age",
        hue="Sex",
        width=0.2,
        flierprops={
            "marker": "d",
            "markerfacecolor": "black",
        }
    )

    plt.xlabel("Sex")
    plt.ylabel("The number of people")

    plt.savefig('5th_titanic_boxplot.png', dpi=350)
    plt.show()


t4()
