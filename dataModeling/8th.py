# 1次システム（1次遅れ系ステップ応答）
# P(s) = K/(1 + Ts)
# P　出力、s　ステップ、K　ゲイン、T　時定数

# 逆ラプラス変換（入力であるステップ関数は離散的な関数であるため）
# P(s) = K/(1 - exp(-t/T))  (t：時間、exp(-t/T) = e^(-t/T))

def t1():
    import numpy as np
    import matplotlib.pyplot as plt

    K = 1.0
    T = 2.0

    t = np.linspace(0, 10, 1000)
    u = np.ones_like(t)
    y = K * (1 - np.exp(-t / T))

    plt.plot(t, u, "b-", label="Step Input")
    plt.plot(t, y, "r-", label="Step Response")
    plt.xlabel("Time(sec)")
    plt.ylabel("Amplitude")
    plt.title("Step Response of First-Order System")
    plt.legend()
    plt.grid()
    plt.show()


# K（ゲイン）は最大値となる値
# 時定数は最大値（目標値）の約63.2%に到達する時間を表す
# e≒2.7, 1/e≒3.7, 1-1/e≒0.63

# t1()


def t2():
    import numpy as np
    import matplotlib.pyplot as plt

    K_1 = 1.0
    T_1 = 2.0

    K_2 = 2.0
    T_2 = 2.0

    K_3 = 3.0
    T_3 = 2.0

    t = np.linspace(0, 10, 1000)
    u = np.ones_like(t)

    y_1 = K_1 * (1 - np.exp(-t / T_1))
    y_2 = K_2 * (1 - np.exp(-t / T_2))
    y_3 = K_3 * (1 - np.exp(-t / T_3))

    plt.plot(t, y_1, "r-", label="K=1, tau=2.0", color="orange")
    plt.plot(t, y_2, "r-", label="K=2, tau=2.0", color="g")
    plt.plot(t, y_3, "r-", label="K=3, tau=2.0", color="purple")
    plt.xlabel("Time(sec)")
    plt.ylabel("Amplitude")
    plt.title("Step Response of First-Order System")
    plt.legend()
    plt.grid()
    plt.show()


# t2()


def t3():
    import numpy as np
    import matplotlib.pyplot as plt

    K_1 = 1.0
    T_1 = 1.0

    K_2 = 1.0
    T_2 = 2.0

    K_3 = 1.0
    T_3 = 3.0

    t = np.linspace(0, 10, 1000)
    u = np.ones_like(t)

    y_1 = K_1 * (1 - np.exp(-t / T_1))
    y_2 = K_2 * (1 - np.exp(-t / T_2))
    y_3 = K_3 * (1 - np.exp(-t / T_3))

    plt.plot(t, y_1, "-", label="K=1, tau=2.0", color="orange")
    plt.plot(t, y_2, "-", label="K=2, tau=2.0", color="g")
    plt.plot(t, y_3, "-", label="K=3, tau=2.0", color="purple")
    plt.xlabel("Time(sec)")
    plt.ylabel("Amplitude")
    plt.title("Step Response of First-Order System")
    plt.legend()
    plt.grid()
    plt.savefig("8th_Step Response of First-Order System", dpi=350)
    plt.show()


# 時定数とは、最大値（目標値）の約63.2%に到達する時間
# 時定数が小さい方が最大値（目標値）に早く到達する
# 時定数がシステムや製品を評価するときに使われることがある
# 例えば、電気ケトル（目標温度に到達するのにかかる時間だったり）
# 例えば、最高速度などが違う車たちを比較検証する手段

# t3()


def t4():
    import numpy as np
    import matplotlib.pyplot as plt

    K = 1.0
    T = 0.0

    t = np.linspace(0, 10, 1000)
    u = np.ones_like(t)
    y = K * (1 - np.exp(-t / T))

    plt.plot(t, u, "b-", label="Step Input")
    plt.plot(t, y, "r-", label="Step Response")
    plt.xlabel("Time(sec)")
    plt.ylabel("Amplitude")
    plt.title("Step Response of First-Order System")
    plt.legend()
    plt.grid()
    plt.show()


t4()
