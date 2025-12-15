import numpy as np

class Target:
    def __init__(self, distance, velocity, rcs0, angle_deg=0.0):
        """
        distance: başlangıç mesafesi (m)
        velocity: hız (m/s) (+ uzaklaşıyor, - yaklaşıyor)
        rcs0: temel RCS (m^2)
        angle_deg: radar ile hedef arasındaki açı (derece)
        """
        self.distance = distance
        self.velocity = velocity
        self.rcs0 = rcs0
        self.angle_deg = angle_deg

    def effective_rcs(self):
        """
        Çok basit bir pattern:
        sigma(θ) = rcs0 * (cos^2(θ) + 0.1)
        Yani bazı açılarda hedef daha görünmez.
        """
        theta = np.deg2rad(self.angle_deg)
        pattern = np.cos(theta) ** 2 + 0.1
        return self.rcs0 * pattern


class MultiTargetScenario:
    def __init__(self, targets):
        self.targets = targets

    def simulate(self, radar, num_chirps: int):
        """
        Birden fazla hedef için tx/rx matrisleri üretir.
        """
        t, tx = radar.generate_chirp_burst(num_chirps)
        num_chirps_, N = tx.shape
        rx = np.zeros_like(tx, dtype=complex)

        for target in self.targets:
            sigma = target.effective_rcs()

            for m in range(num_chirps_):
                # Hedefin bu chirpteki mesafesi
                dist_m = target.distance + target.velocity * (m * radar.sweep_time)
                delay = 2 * dist_m / radar.c
                shift = int(delay * radar.fs)
                if shift >= N:
                    continue

                echo = np.zeros(N, dtype=complex)
                echo[shift:] = tx[m, :N-shift] * sigma
                rx[m] += echo

        return t, tx, rx
