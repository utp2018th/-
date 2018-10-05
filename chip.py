import numpy as np
import matplotlib.pyplot as plt

class Model:
    def __init__(self,coin,time,group):
        self.coin = coin
        self.time = time
        self.group = group
        self.array = [0]*6

    def destribution(self):
        for i in range(self.coin):
            n = np.random.randint(6)
            self.array[n] += 1
        return self.array

    def exchange(self):
        for i in range(self.time):
            give = np.random.randint(6)
            get = np.random.randint(6)
            if self.array[give] > 0:
                self.array[give] -= 1
                self.array[get] += 1
        return self.array

    def reset(self):
        self.array = [0]*6

    def repeat(self):
        result = [0]*self.coin
        for i in range(self.group):
            p = self.destribution()
            q = self.exchange()
            for i in q:
                result[i] += 1
            self.reset()
        return result

    def plot(self,height):
        left = range(self.coin)
        # height = self.repeat()
        plt.bar(left,height)
        plt.title("MaxCoin = {}, Exchange Time = {}, People = {}".format(self.coin,self.time,self.group*6))
        plt.xlabel("number of coins")
        plt.ylabel("number of persons")
        plt.show()

def check_decimal(str):
    while 1:
        print(str)
        n = input()
        if n.isdecimal():
            n = int(n)
            break
        else: print("エラー : １以上の整数を入力してください")
    return n

if __name__ == "__main__" :
    str_array = [
    "１グループに分配するコインの枚数を決めてください",
    "１グループがコインを交換する回数を決めてください",
    "試行するグループの数を決めてください"
    ]
    input_array = [0,0,0]
    for i in range(3):
        input_array[i] = check_decimal(str_array[i])
    model = Model(input_array[0],input_array[1],input_array[2])
    result = model.repeat()
    model.plot(result)
