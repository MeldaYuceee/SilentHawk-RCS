import numpy as np

class RCSEngine:
    def __init__(self, noise_power=0.01):
        self.noise_power = noise_power

    def add_noise(self, signal):
        # Hem 1D hem 2D sinyali desteklesin
        if signal.ndim == 1:
            N = len(signal)
            noise = np.sqrt(self.noise_power / 2) * (
                np.random.randn(N) + 1j * np.random.randn(N)
            )
            return signal + noise
        elif signal.ndim == 2:
            num_chirps, N = signal.shape
            noise = np.sqrt(self.noise_power / 2) * (
                np.random.randn(num_chirps, N) + 1j * np.random.randn(num_chirps, N)
            )
            return signal + noise
        else:
            raise ValueError("Signal must be 1D or 2D")

    def mix(self, tx, rx):
        return tx * np.conjugate(rx)


class Jammer:
    def __init__(self, start_chirp=0, end_chirp=None, jam_snr_db=20.0):
        self.start_chirp = start_chirp
        self.end_chirp = end_chirp
        self.jam_snr_db = jam_snr_db

    def apply(self, rx, base_noise_power):
        """
        rx: (num_chirps x N)
        base_noise_power: RCSEngine.noise_power
        """
        num_chirps, N = rx.shape
        start = self.start_chirp
        end = self.end_chirp if self.end_chirp is not None else num_chirps

        jam_var = base_noise_power * 10 ** (self.jam_snr_db / 10)

        for m in range(start, min(end, num_chirps)):
            noise = np.sqrt(jam_var / 2) * (
                np.random.randn(N) + 1j * np.random.randn(N)
            )
            rx[m] += noise

        return rx


def detect_stealth_threshold(beat, noise_power, snr_min_db=8.0):
    """
    Çok basit bir stealth tespit metriği:
    Ortalama SNR gürültü eşiğinin üstünde mi?
    """
    power = np.abs(beat) ** 2
    signal_power = np.mean(power)
    snr_linear = max(signal_power - noise_power, 0) / (noise_power + 1e-12)
    snr_db = 10 * np.log10(snr_linear + 1e-12)

    detectable = snr_db >= snr_min_db
    return detectable, snr_db
