import numpy as np

class RCSEngine:
    def __init__(self, noise_power=0.01):
        self.noise_power = noise_power

    def add_noise(self, signal):
        if signal.ndim == 1:
            N = signal.shape[0]
            noise = np.sqrt(self.noise_power / 2) * (
                np.random.randn(N) + 1j * np.random.randn(N)
            )
            return signal + noise

        if signal.ndim == 2:
            M, N = signal.shape
            noise = np.sqrt(self.noise_power / 2) * (
                np.random.randn(M, N) + 1j * np.random.randn(M, N)
            )
            return signal + noise

        raise ValueError("Signal must be 1D or 2D")

    def mix(self, tx, rx):
        return tx * np.conjugate(rx)


class Jammer:
    def __init__(self, start_chirp=0, end_chirp=None, jam_snr_db=20.0):
        self.start_chirp = start_chirp
        self.end_chirp = end_chirp
        self.jam_snr_db = jam_snr_db

    def apply(self, rx, base_noise_power):
        num_chirps, N = rx.shape
        start = self.start_chirp
        end = self.end_chirp if self.end_chirp is not None else num_chirps

        jam_power = base_noise_power * 10 ** (self.jam_snr_db / 10)

        for m in range(start, min(end, num_chirps)):
            noise = np.sqrt(jam_power / 2) * (
                np.random.randn(N) + 1j * np.random.randn(N)
            )
            rx[m] += noise

        return rx


def detect_stealth_threshold(beat, noise_power, snr_min_db=8.0):
    power = np.abs(beat) ** 2
    avg_power = np.mean(power)

    snr_linear = max(avg_power - noise_power, 0) / (noise_power + 1e-12)
    snr_db = 10 * np.log10(snr_linear + 1e-12)

    return snr_db >= snr_min_db, snr_db
