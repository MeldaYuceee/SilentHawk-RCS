import numpy as np

class TargetSignature:
    def __init__(self, distance=150, velocity=20, rcs=0.01):
        self.distance = distance
        self.velocity = velocity
        self.rcs = rcs

    def apply(self, chirp, fs, c=3e8):
        delay = 2 * self.distance / c
        shift = int(delay * fs)

        atten = self.rcs  
        echo = np.zeros_like(chirp)
        echo[shift:] = chirp[:-shift] * atten

        return echo

