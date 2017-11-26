import pandas as pd
import numpy as np


class Predictor:
    def __init__(self, dataset):

        self.datasets = []
        self.probabilities = [0] * 15
        self.last_cluster = 0

        tmp = pd.read_csv(dataset, delimiter='~')
        tmp.sort_values(' rating', ascending=[False])
        for i in range(15):
            self.probabilities[i] = 1.0 / 15
        for i in range(15):
            self.datasets.append(tmp.loc[tmp[' cluster'] == i])

    @staticmethod
    def get_random_cluster():
        return np.random.choice(range(15))

    def get_film(self, size=20):
        self.last_cluster = self.get_random_cluster()
        film = np.random.choice(range(len(self.datasets[self.last_cluster][:size])))
        print(film)

        return np.array(self.datasets[self.last_cluster][:size].iloc[film:film + 1])

    def update(self, answer):
        # if you passed probably as an anwser you should increase size in getFilm next time!
        if answer == 'yes':
            pass
        if answer == 'no':
            temp_p = self.probabilities[self.last_cluster] / 2
            self.probabilities[self.last_cluster] -= temp_p
            for i in range(15):
                if i != self.last_cluster:
                    self.probabilities[i] += temp_p / 14
        if answer == 'probably':
            pass
