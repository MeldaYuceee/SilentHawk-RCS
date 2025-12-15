import numpy as np

class RadarModel:
    def __init__(self, fs=2e6, sweep_time=1e-3, f_start=24e9, f_sweep=200e6, c=3e8):
        self.fs = fs
        self.sweep_time = sweep_time
        self.f_start = f_start
        self.f_sweep = f_sweep
        self.c = c

    def generate_chirp(self):
        # Tek chirp (eski kodun için, main.py bunu kullanıyor)
        t = np.linspace(0, self.sweep_time, int(self.fs * self.sweep_time), endpoint=False)
        k = self.f_sweep / self.sweep_time
        phase = 2 * np.pi * (self.f_start * t + 0.5 * k * t**2)
        chirp = np.exp(1j * phase)
        return t, chirp

    def generate_chirp_burst(self, num_chirps: int):
        """
        Range-Doppler için N chirp üretir.
        :return: t (N örnek), tx (num_chirps x N kompleks matris)
        """
        t = np.linspace(0, self.sweep_time, int(self.fs * self.sweep_time), endpoint=False)
        k = self.f_sweep / self.sweep_time
        phase = 2 * np.pi * (self.f_start * t + 0.5 * k * t**2)
        chirp = np.exp(1j * phase)
        tx = np.tile(chirp, (num_chirps, 1))
        return t, tx
