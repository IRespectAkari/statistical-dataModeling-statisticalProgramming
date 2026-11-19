# 待ち行列理論

# 1909年 アグナー・アーラン 数学者・統計課・技術者
# 電話会社に勤務していたとき、「電話サービスを提供するために必要な回線数」という問題に、ポアソン分布が適用できることを証明した
# ポアソン分布    離散確率分布の一種　0以上　平均発生数が大きくなるにつれ、分布形状がなだらか、かつ右に移行する

# ポアソン到着
# t時間以内にk人の客が到着する確率
# P(k) = e^{-\lambda k} \frac{(\lambda t)^k}{k!}
# 1時間当たり6人の時に8人来る確率 -> P(8) = e^{-6 x 1} \frac{(6 x 1)^8}{8!} ≒ 0.103

# 逆に、その時間に客が来るかどうかを求める
# T = -\frac{1}{\lambda} \log_e{(1 - P_{arr}(T))}
# 時間間隔Tの間に客が到着するかしないか
# T = [01]（来ない|来る）
# 1時間(t)辺り6人のATMに30人来る確率


def t1():
    import numpy as np
    from scipy.stats import poisson
    from scipy.stats import uniform
    import matplotlib.pyplot as plt

    np.random.seed(123)

    Num = 30
    t_arrive = np.zeros(Num)
    lamb = 6

    sum = 0.0
    for i in range(Num):
        sum = sum - (1 / lamb) * np.log(1 - uniform.rvs(size=1))
        t_arrive[i] = sum[0]

    plt.subplots(figsize=(6, 3))
    plt.vlines(t_arrive, ymin=0, ymax=1)
    plt.xlabel("time[k]")
    plt.tight_layout()

    plt.savefig("7th_Poisson_Arrival.png", dpi=350)
    plt.show()


# t1()

def t2():
    """
    このシミュレーションの設定
    ATM 1時間平均 6人
        操作時間 5分
    ==> 理論上の1時間当たり並ばずに使用できる人数は12人 のはず

    t1は到着した時間、t2は実際に仕えた時間を表している
    ATMに10分おきに客が来れば、誰も待たずに使えるはず
    ==> 理論上では待ち時間はないが、シミュレーションにより待ち時間が発生することが判明
    """
    import numpy as np
    from scipy.stats import poisson
    from scipy.stats import uniform
    import matplotlib.pyplot as plt

    np.random.seed(123)

    Num = 30
    t_arrive = np.zeros(Num)
    lamb = 6

    operation_time = 5

    sum = 0.0
    count = 0
    w_t = 0.0
    for i in range(Num):
        sum = sum - (1 / lamb) * np.log(1 - uniform.rvs(size=1))
        t_arrive[i] = sum[0]
        if i > 0:
            if t_arrive[i] < t_arrive[i - 1] + (operation_time / 60):
                t_arrive[i] = t_arrive[i - 1] + (operation_time / 60)
                count += 1
                w_t = w_t + (t_arrive[i] - sum[0])

    print("The number of people ->"+str(count))
    print("Average waiting time ->"+str((w_t/count)*60)+"min")
    plt.subplots(figsize=(6, 3))
    plt.vlines(t_arrive, ymin=0, ymax=1)
    plt.xlabel("time[k]")
    plt.tight_layout()

    plt.savefig("7th_Poisson_Arrival_2.png", dpi=350)
    plt.show()


# t2()

# 行列があった方が良いものもある
# ex.ラーメン屋  行列のある飲食店の方がおいしそうに見える
# しかし、待たせすぎると印象が悪くなる -> 丁度良い待ち時間が必要になる
# 1時間に10人の行列を作りたい場合、提供時間を何分にすればよいのか…これもマーケティング

def t3(num):
    """
    このシミュレーションの設定
    ATM 1時間平均 6人
        操作時間 5分
    ==> 理論上の1時間当たり並ばずに使用できる人数は12人 のはず

    t1は到着した時間、t2は実際に仕えた時間を表している
    ATMに10分おきに客が来れば、誰も待たずに使えるはず
    ==> 理論上では待ち時間はないが、シミュレーションにより待ち時間が発生することが判明
    """
    import numpy as np
    from scipy.stats import poisson
    from scipy.stats import uniform
    import matplotlib.pyplot as plt

    np.random.seed(123)

    Num = 30
    t_arrive = np.zeros(Num)
    lamb = num

    operation_time = 5

    sum = 0.0
    count = 0
    w_t = 0.0
    for i in range(Num):
        sum = sum - (1 / lamb) * np.log(1 - uniform.rvs(size=1))
        # sum = sum - (1 / lamb) * np.log(1 - uniform.rvs())
        t_arrive[i] = sum[0]
        # t_arrive[i] = sum
        if i > 0:
            if t_arrive[i] < t_arrive[i - 1] + (operation_time / 60):
                t_arrive[i] = t_arrive[i - 1] + (operation_time / 60)
                count += 1
                w_t = w_t + (t_arrive[i] - sum[0])
                # w_t = w_t + (t_arrive[i] - sum)

    print("The number of people ->"+str(count))
    print("Average waiting time ->"+str((w_t/count)*60)+"min")
    plt.subplots(figsize=(6, 3))
    plt.vlines(t_arrive, ymin=0, ymax=1)
    plt.xlabel("time[k]")
    plt.tight_layout()

    plt.savefig(f"7th_Poisson_Arrival_2_num={num}.png", dpi=350)
    plt.show()


t3(10)























