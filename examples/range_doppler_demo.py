from src.radar_model import RadarModel
from src.multi_target import Target, MultiTargetScenario
from src.rcs_engine import RCSEngine, Jammer, detect_stealth_threshold
from src.visualizer import Visualizer

def main():
    radar = RadarModel()
    num_chirps = 64

    # 2 hedef: biri normal, biri stealth
    scenario = MultiTargetScenario([
        Target(distance=120, velocity=10,  rcs0=0.1,  angle_deg=5),   # daha görünür
        Target(distance=200, velocity=-15, rcs0=0.01, angle_deg=40),  # stealth hedef
    ])

    t, tx, rx = scenario.simulate(radar, num_chirps)

    rcs_engine = RCSEngine(noise_power=0.001)
    rx_noisy = rcs_engine.add_noise(rx)

    # Jammer: ortadaki chirplerde sinyali bastırıyor
    jammer = Jammer(start_chirp=20, end_chirp=40, jam_snr_db=15)
    rx_jammed = jammer.apply(rx_noisy, rcs_engine.noise_power)

    beat = rcs_engine.mix(tx, rx_jammed)

    vis = Visualizer()
    vis.plot_range_doppler(beat, radar)

    detectable, snr_db = detect_stealth_threshold(beat, rcs_engine.noise_power)
    print(f"SNR ≈ {snr_db:.1f} dB | Detectable? {detectable}")

if __name__ == "__main__":
    main()
