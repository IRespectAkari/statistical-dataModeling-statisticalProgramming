import numpy as np
import matplotlib.pyplot as plt
from superqt import switch


def lotkaVolterra():
    t_star = 0  # 開始年数
    t_stop = 20  # 経過年数
    dt = 0.001  # シミュレーション間隔: 小さいほど詳細、0.001で十分な精度

    p = 1.1
    q = 0.6
    r = 1.3
    s = 0.6

    start_predator = 1.0
    start_prey = 2.0

    t = np.arange(t_star, t_stop, dt)
    prey = np.zeros(t.size)
    predator = np.zeros(t.size)
    prey[0] = start_prey
    predator[0] = start_predator

    for i in range(t.size - 1):
        prey[i + 1] = prey[i] + (p * prey[i] - q * prey[i] * predator[i]) * dt
        predator[i + 1] = predator[i] + (-r * predator[i] + s * prey[i] * predator[i]) * dt

    plt.plot(t, prey, label="prey")
    plt.plot(t, predator, label="predator")
    plt.legend(loc='upper right')
    plt.title("Lotka-Volterra equations")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.show()


# lotkaVolterra()

def lotkaVolterra2():
    t_star = 0  # 開始年数
    t_stop = 20  # 経過年数
    dt = 0.001  # シミュレーション間隔: 小さいほど詳細、0.001で十分な精度

    p = 1.1
    q = 0.6
    r = 1.3
    s = 0.6

    start_predator = 1.0
    start_prey = 2.0

    t = np.arange(t_star, t_stop, dt)
    prey = np.zeros(t.size)
    predator = np.zeros(t.size)
    prey[0] = start_prey
    predator[0] = start_predator

    for i in range(t.size - 1):
        prey[i + 1] = prey[i] + (p * prey[i] - q * prey[i] * predator[i]) * dt
        predator[i + 1] = predator[i] + (-r * predator[i] + s * prey[i] * predator[i]) * dt

    plt.plot(prey, predator)
    # plt.legend(loc='upper right')
    plt.title("Lotka-Volterra equations")
    plt.xlabel("Prey")
    plt.ylabel("Predator")
    plt.show()


# lotkaVolterra2()


def lotkaVolterra0(mode="解曲線"):
    t_star = 0  # 開始年数
    t_stop = 20  # 経過年数
    dt = 0.001  # シミュレーション間隔: 小さいほど詳細、0.001で十分な精度

    p = 1.1
    q = 0.6
    r = 1.3
    s = 0.6

    start_predator = 1.0
    start_prey = 2.0

    t = np.arange(t_star, t_stop, dt)
    prey = np.zeros(t.size)
    predator = np.zeros(t.size)
    prey[0] = start_prey
    predator[0] = start_predator

    for i in range(t.size - 1):
        prey[i + 1] = prey[i] + (p * prey[i] - q * prey[i] * predator[i]) * dt
        predator[i + 1] = predator[i] + (-r * predator[i] + s * prey[i] * predator[i]) * dt

    match mode:
        case "解曲線":
            plt.plot(prey, predator)
            # plt.legend(loc='upper right')
            plt.title("Lotka-Volterra equations")
            plt.xlabel("Prey")
            plt.ylabel("Predator")
            plt.savefig('5th_lotkaVolterra_kaikyokusexn.png', dpi=350)
        case "曲線":
            plt.plot(t, prey, label="prey")
            plt.plot(t, predator, label="predator")
            plt.legend(loc='upper right')
            plt.title("Lotka-Volterra equations")
            plt.xlabel("Time")
            plt.ylabel("Population")
            plt.savefig('5th_lotkaVolterra_kyokusexn.png', dpi=350)

    plt.show()


lotkaVolterra0("曲線")
