import numpy as np

class Target:
    def __init__(self, distance, velocity, rcs0, angle_deg=0.0):
        self.distance = distance
        self.velocity = velocity
        self.rcs0 = rcs0
        self.angle_deg = angle_deg

    def effective_rcs(self):
        theta = np.deg2rad(self.angle_deg)
        return self.rcs0 * (np.cos(theta) ** 2 + 0.1)


class MultiTargetScenario:
    def __init__(self, targets):
        self.targets = targets

    def simulate(self, radar, num_chirps):
        t, tx = radar.generate_chirp_burst(num_chirps)
        num_chirps_, N = tx.shape
        rx = np.zeros_like(tx, dtype=complex)

        for target in self.targets:
            sigma = target.effective_rcs()

            for m in range(num_chirps_):
                dist = target.distance + target.velocity * (m * radar.sweep_time)
                delay = 2 * dist / radar.c
                shift = int(delay * radar.fs)

                if shift >= N:
                    continue

                rx[m, shift:] += tx[m, :N - shift] * sigma

        return t, tx, rx
