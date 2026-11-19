import numpy as np
import math
import matplotlib.pyplot as plt


# マルサスモデル
# 単位時間当たりの人口の増加量 = 人口の増加率 x 人口
# dy/dt = ky (y: 人口, t: 時間, k: 人口の増加量)
def malthus() -> None:
    t = np.arange(0, 1000, 0.1)

    y_0: int = 100
    k: float = 0.01

    y = y_0 * math.e ** (k * t)

    plt.plot(t, y)
    plt.title("Malthus model")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.show()


# malthus()

# ロジスティック方程式
# 環境による人口上限などを反映した方程式
# C: 環境収容力
def logistic() -> None:
    t = np.arange(0, 1000, 0.1)

    y_0: int = 100
    k: float = 0.01
    C: int = 10000

    ekt = math.e ** (k * t)

    y = (y_0 * C * ekt) / (C - y_0 + y_0 * ekt)

    plt.plot(t, y)
    plt.title("Logistic model")
    plt.xlabel("Time")
    plt.ylabel("Population")

    plt.savefig('logistic.png', dpi=350)  # レポート等の為にdpi=350を推奨

    plt.show()


logistic()
