import numpy as np
import matplotlib.pyplot as plt

class Visualizer:
    def plot_range(self, beat, fs):
        N = len(beat)
        spectrum = np.abs(np.fft.fft(beat, N))
        freqs = np.fft.fftfreq(N, 1/fs)

        plt.figure(figsize=(10, 4))
        plt.plot(freqs[:N//2], spectrum[:N//2])
        plt.title("Range Spectrum")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid()
        plt.show()

    def plot_range_doppler(self, beat, radar):
        """
        beat: (num_chirps x N)
        """
        num_chirps, N = beat.shape

        RD = np.fft.fftshift(np.fft.fft2(beat), axes=0)
        RD_mag = 20 * np.log10(np.abs(RD) + 1e-6)

        # Range ekseni
        freqs_r = np.fft.fftfreq(N, 1 / radar.fs)
        slope = radar.f_sweep / radar.sweep_time
        ranges = radar.c * freqs_r / (2 * slope)

        # Doppler ekseni (yaklaşma/uzaklaşma hızı)
        freqs_d = np.fft.fftfreq(num_chirps, radar.sweep_time)
        velocities = freqs_d * radar.c / (2 * radar.f_start)

        plt.figure(figsize=(8, 6))
        plt.imshow(
            RD_mag[:, :N//2],
            aspect="auto",
            origin="lower",
            extent=[ranges[0], ranges[N//2], velocities[0], velocities[-1]],
        )
        plt.colorbar(label="Magnitude (dB)")
        plt.xlabel("Range (m)")
        plt.ylabel("Velocity (m/s)")
        plt.title("Range-Doppler Map")
        plt.show()
