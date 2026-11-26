# 2次システム
# 2次遅れ系
# 適切な温度に設定したいとき、
#   早く温めようとすると、適切な温度を超えてしまう
#   ゆっくり温めようとすると、適切な温度になかなかならない
# このシミュレーション
# G(s) = \frac{\omega^2_n}{s^2 + 2\zeta\omega_{n}s + \omega^2_n}
# G: 出力
# s: ステップ
# K: ゲイン。目標値を決めるパラメータ
# \omega: 固有各振動数。即応性を決めるパラメータ
# \zeta: 減衰係数。減衰性（安定度）を決めるパラメータ
#   \zeta < 0 -> 発散
#   \zeta = 0 -> 振動
#   0 < \zeta < 1 -> 振動しながら収束
#   \zeta >= 1 -> 振動せず収束
#
# 逆ラプラス変換したものが以下
# y(t) = K\{ 1 - \frac{1}{\sqrt{1 - \zeta^2}} \\
#   e^{\zeta\omega_{n}^t} \\
#   \sin{\left( \omega_n\sqrt{1 - \zeta^2} * \tan^{-1}\left( \frac{\sqrt{1 - \zeta^2}}{\zeta} \right) \right)} \\
# \}



def t1():
    import numpy as np
    import matplotlib.pyplot as plt

    t = np.linspace(0, 10, 1000)

    K = 1
    zeta = 0.5
    omega = 1
    root = np.sqrt(1 - zeta ** 2)

    y = K * (
            1 - (1 / np.sqrt(1 - zeta ** 2))
            * np.exp(-1 * zeta * omega * t)
            * np.sin(
        omega * np.sqrt(1 - zeta ** 2) * t + np.arctan(np.sqrt(1 - zeta ** 2) / zeta)
    )
    )

    y = K * (
            1 - (1 / root)
            * np.exp(-1 * zeta * omega * t)
            * np.sin(
        omega * root * t + np.arctan(root / zeta)
    )
    )

    plt.plot(t, y, "k-")
    plt.grid(color="k", linestyle="dotted", linewidth=1)
    plt.show()


# t1()


def t2():
    import numpy as np
    import matplotlib.pyplot as plt

    def SODS(K, zeta, omega, t):
        root = np.sqrt(1 - zeta ** 2)
        y = K * (
            1 - (1 / root)
            * np.exp(-1 * zeta * omega * t)
            * np.sin(
                omega * root * t + np.arctan(root / zeta)
            )
        )
        return y

    t = np.linspace(0, 10, 1000)

    K_1 = 1
    zeta_1 = 0.5
    omega_1 = 1

    K_2 = 0.5
    zeta_2 = 0.5
    omega_2 = 1

    K_3 = 2
    zeta_3 = 0.5
    omega_3 = 1

    y_1 = SODS(K_1, zeta_1, omega_1, t)
    y_2 = SODS(K_2, zeta_2, omega_2, t)
    y_3 = SODS(K_3, zeta_3, omega_3, t)

    plt.plot(t, y_1, "r-", label="K=" + str(K_1) + ",zeta=" + str(zeta_1) + ",omega=" + str(omega_1))
    plt.plot(t, y_2, "g-", label="K=" + str(K_2) + ",zeta=" + str(zeta_2) + ",omega=" + str(omega_2))
    plt.plot(t, y_3, "m-", label="K=" + str(K_3) + ",zeta=" + str(zeta_3) + ",omega=" + str(omega_3))
    plt.grid(color="k", linestyle="dotted", linewidth=1)
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()


# t2()


def t3():
    import numpy as np
    import matplotlib.pyplot as plt

    def SODS(K, zeta, omega, t):
        root = np.sqrt(1 - zeta ** 2)
        y = K * (
            1 - (1 / root)
            * np.exp(-1 * zeta * omega * t)
            * np.sin(
                omega * root * t + np.arctan(root / zeta)
            )
        )
        return y

    t = np.linspace(0, 10, 1000)

    K_1 = 1
    zeta_1 = 0.5
    omega_1 = 0.5

    K_2 = 1
    zeta_2 = 0.5
    omega_2 = 1

    K_3 = 1
    zeta_3 = 0.5
    omega_3 = 2

    y_1 = SODS(K_1, zeta_1, omega_1, t)
    y_2 = SODS(K_2, zeta_2, omega_2, t)
    y_3 = SODS(K_3, zeta_3, omega_3, t)

    plt.plot(t, y_1, "r-", label="K=" + str(K_1) + ",zeta=" + str(zeta_1) + ",omega=" + str(omega_1))
    plt.plot(t, y_2, "g-", label="K=" + str(K_2) + ",zeta=" + str(zeta_2) + ",omega=" + str(omega_2))
    plt.plot(t, y_3, "m-", label="K=" + str(K_3) + ",zeta=" + str(zeta_3) + ",omega=" + str(omega_3))
    plt.grid(color="k", linestyle="dotted", linewidth=1)
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()


# t3()


def t4():
    import numpy as np
    import matplotlib.pyplot as plt

    def SODS(K, zeta, omega, t):
        root = np.sqrt(1 - zeta ** 2)
        y = K * (
            1 - (1 / root)
            * np.exp(-1 * zeta * omega * t)
            * np.sin(
                omega * root * t + np.arctan(root / zeta)
            )
        )
        return y

    t = np.linspace(0, 10, 1000)

    K_1 = 1
    zeta_1 = -0.1
    omega_1 = 1

    K_2 = 1
    zeta_2 = 0
    omega_2 = 1

    K_3 = 1
    zeta_3 = 0.5
    omega_3 = 1

    K_4 = 1
    zeta_4 = 1
    omega_4 = 1

    y_1 = SODS(K_1, zeta_1, omega_1, t)
    y_2 = SODS(K_2, zeta_2, omega_2, t)
    y_3 = SODS(K_3, zeta_3, omega_3, t)
    y_4 = SODS(K_4, zeta_4, omega_4, t)

    plt.plot(t, y_1, "r-", label="K=" + str(K_1) + ",zeta=" + str(zeta_1) + ",omega=" + str(omega_1))
    plt.plot(t, y_2, "g-", label="K=" + str(K_2) + ",zeta=" + str(zeta_2) + ",omega=" + str(omega_2))
    plt.plot(t, y_3, "m-", label="K=" + str(K_3) + ",zeta=" + str(zeta_3) + ",omega=" + str(omega_3))
    plt.plot(t, y_4, "b-", label="K=" + str(K_4) + ",zeta=" + str(zeta_4) + ",omega=" + str(omega_4))
    plt.grid(color="k", linestyle="dotted", linewidth=1)
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.savefig("9th_Step Response of First-Order System", dpi=350)
    plt.show()


t4()

# 時定数で評価することが多い？が、時定数以外にも評価項目がある
# 振動しながら近づく時は時定数だけでは判断できない
# 何故なら、時定数が小さい＝傾きが急≒求めている値を大幅に超えやすい＝ロスが出る（浪費する）
# 例えば、アクセルべた踏みすれば60km/hに到達するのは早いが、60km/hを大幅に超過する可能性も出てくる
# この時にべた踏みする人と、もう少し踏む力を抑える人、どちらが運転が上手いと言えるのか？
# これは時定数だけでは判断できない
#
# 比較方法は、目標値から外れた領域の面積を比較すればよい（積分）
# 面積が少ないほどロスが少ない
#
# 2次システムを使ったケトルや保温機能は、1990年代まで？らしい
# 今はフィードバックシステム
# 過去と今の情報から未来の情報（温度など）を予測し、変化量（加熱するかしないか、加速するかしないか）を調整する


