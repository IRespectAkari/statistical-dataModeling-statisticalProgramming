import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('titanic.csv', index_col=0)

# 1回目
def t1():
    plt.hist(df1['Age'], bins=20)
    plt.title('Histogram')
    plt.xlabel('Age')
    plt.ylabel('The number of people')
    plt.show()


# t1()

# 2回目
def t2():
    ave = df1["Age"].mean()  # <-- 欠損値は存在しないものとして計算される

    y_min = 0
    y_max = 110

    plt.hist(df1['Age'], bins=20)
    plt.title('Histogram')
    plt.xlabel('Age')
    plt.ylabel('The number of people')
    plt.vlines([ave], y_min, y_max, "red", label='Mean=' + str(ave))  #  ,linestyle='dashed'
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
    plt.show()


# t2()

# 3回目
def t3():
    ave = df1["Age"].mean()  # <-- 欠損値は存在しないものとして計算される
    med = df1["Age"].median()  # <-- 欠損値は存在しないものとして計算される

    y_min = 0
    y_max = 110

    plt.hist(df1['Age'], bins=20)
    plt.title('Histogram')
    plt.xlabel('Age')
    plt.ylabel('The number of people')
    plt.vlines([ave], y_min, y_max, "red", label='Mean=' + str(ave))  #  ,linestyle='dashed'
    plt.vlines([med], y_min, y_max, "yellow", label='Median=' + str(med))  #  ,linestyle='dashed'
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
    plt.show()


# t3()

# 4回目
def t4():
    ave = df1["Age"].mean()  # <-- 欠損値は存在しないものとして計算される
    med = df1["Age"].median()  # <-- 欠損値は存在しないものとして計算される
    mo = df1["Age"].mode()[0]  # <-- 欠損値は存在しないものとして計算される
    # modeは文字列でも出来るから、df1["Sex"]とするとmaleとfemaleのどちらが多く出てるかを出せる

    y_min = 0
    y_max = 110

    plt.hist(df1['Age'], bins=20)
    plt.title('Histogram')
    plt.xlabel('Age')
    plt.ylabel('The number of people')
    plt.vlines([ave], y_min, y_max, "red", label='Mean=' + str(ave))  #  ,linestyle='dashed'
    plt.vlines([med], y_min, y_max, "yellow", label='Median=' + str(med))  #  ,linestyle='dashed'
    plt.vlines([mo], y_min, y_max, "pink", label='Mode=' + str(mo))  #  ,linestyle='dashed'
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right')

    plt.savefig('titanic_histgram.png', dpi=350)  # レポート等の為にdpi=350を推奨

    plt.show()


t4()
