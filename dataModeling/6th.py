# マルコフ過程
# 条件付き確率
# 今日と明日の天気の対応関係をカウントして確率にするだけでできるのが、マルコフ過程
# 今年の10月のデータに来年の10月データを追加するときも、AIのような学習ではなく数え上げるだけで確率が上がっていく

def t1():
    import numpy as np
    import random as rm

    states = ["sunny", "cloudy", "rainy"]
    transitions = [["SS", "SC", "SR"], ["CS", "CC", "CR"], ["RS", "RC", "RR"]]
    T = [[0.611, 0.278, 0.111], [0.556, 0.333, 0.111], [0.5, 0.5, 0.0]]

    def weather_forecast(n_days, weather_today="sunny"):
        weather_list = [weather_today]
        n = 0
        while n != n_days:
            if weather_list[n] == "sunny":
                change = np.random.choice(transitions[0], p=T[0])
                if change == "SS":
                    weather_list.append(states[0])
                elif change == "SC":
                    weather_list.append(states[1])
                else:
                    weather_list.append(states[2])
            elif weather_list[n] == "cloudy":
                change = np.random.choice(transitions[1], p=T[1])
                if change == "CS":
                    weather_list.append(states[0])
                elif change == "CC":
                    weather_list.append(states[1])
                else:
                    weather_list.append(states[2])
            else:
                change = np.random.choice(transitions[2], p=T[2])
                if change == "RS":
                    weather_list.append(states[0])
                elif change == "RC":
                    weather_list.append(states[0])
                else:
                    weather_list.append(states[1])
            n = n + 1

        return weather_list

    future_weathers = weather_forecast(n_days=5)
    print(future_weathers)


# t1()


def t2():
    import numpy as np
    import random as rm

    # シカ色デイズに存在する言葉のパターン
    states = ["しか", "のこ", "こし", "たん", "<eos>"]

    # 状態遷移
    transitions = [["しかしか", "しかのこ", "しかこし", "しかたん", "しか<eos>"],
                   ["のこしか", "のこのこ", "のここし", "のこたん", "のこ<eos>"],
                   ["こししか", "こしのこ", "こしこし", "こしたん", "こし<eos>"],
                   ["たんしか", "たんのこ", "たんこし", "たんたん", "たん<eos>"]]

    # 状態遷移行列
    T = [[0.0, 1.0, 0.0, 0.0, 0.0],
         [0.0, 0.67, 0.33, 0.0, 0.0],
         [0.0, 0.0, 0.0, 1.0, 0.0],
         [0.0, 0.0, 0.0, 0.5, 0.5]]

    def shikairodays(shikanoko="しか"):
        shikairodays_song = [shikanoko]
        n = 0

        # while文を使った無限ループ
        while True:
            # 「しか」の後に来る言葉の予測
            if shikairodays_song[n] == "しか":
                change = np.random.choice(transitions[0], p=T[0])
                if change == "しかしか":
                    shikairodays_song.append(states[0])
                elif change == "しかのこ":
                    shikairodays_song.append(states[1])
                elif change == "しかこし":
                    shikairodays_song.append(states[2])
                elif change == "しかたん":
                    shikairodays_song.append(states[3])
                else:
                    shikairodays_song.append(states[4])

            # 「のこ」の後に来る言葉の予測
            elif shikairodays_song[n] == "のこ":
                change = np.random.choice(transitions[1], p=T[1])
                if change == "のこしか":
                    shikairodays_song.append(states[0])
                elif change == "のこのこ":
                    shikairodays_song.append(states[1])
                elif change == "のここし":
                    shikairodays_song.append(states[2])
                elif change == "のこたん":
                    shikairodays_song.append(states[3])
                else:
                    shikairodays_song.append(states[4])

            # 「こし」の後に来る言葉の予測
            elif shikairodays_song[n] == "こし":
                change = np.random.choice(transitions[2], p=T[2])
                if change == "こししか":
                    shikairodays_song.append(states[0])
                elif change == "こしのこ":
                    shikairodays_song.append(states[1])
                elif change == "こしこし":
                    shikairodays_song.append(states[2])
                elif change == "こしたん":
                    shikairodays_song.append(states[3])
                else:
                    shikairodays_song.append(states[4])

            # 「たん」の後に来る言葉の予測
            elif shikairodays_song[n] == "たん":
                change = np.random.choice(transitions[3], p=T[3])
                if change == "たんしか":
                    shikairodays_song.append(states[0])
                elif change == "たんのこ":
                    shikairodays_song.append(states[1])
                elif change == "たんこし":
                    shikairodays_song.append(states[2])
                elif change == "たんたん":
                    shikairodays_song.append(states[3])
                else:
                    shikairodays_song.append(states[4])

            # 「<eos>」の場合は無限ループを抜け出す
            else:
                break

            n = n + 1

        # 戻り値としてshikairodays_songを返す
        return shikairodays_song

    # print(shikairodays())
    s = shikairodays()
    while len(s) < 30:
        s = shikairodays()
    print(s)


t2()
