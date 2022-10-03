import random
import matplotlib.pyplot as plt
import math
import numpy as np
import sys
import time


class FrequencySimulation:
    """This is the frequency simulator"""
    """"""
    def __init__(self, l):
        self.l = l

    @property
    def frequency_data(self):
        qt = time.perf_counter()
        print(qt - st)
        return {j: len([i for i in self.l if i == j])/len(self.l) for j in set(self.l)}


class DiceSimulation(FrequencySimulation):
    def __init__(self, faces, roll_amt, sum_amt):
        super().__init__([sum([random.choice(faces) for q in range(0, sum_amt)]) for i in range(0, roll_amt)])


r = FrequencySimulation([random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2 < 1 for i in range(0, 10000)])
