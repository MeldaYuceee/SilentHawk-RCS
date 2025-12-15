from src.radar_model import RadarModel
from src.target_signature import TargetSignature
from src.rcs_engine import RCSEngine
from src.visualizer import Visualizer

radar = RadarModel()
t, tx = radar.generate_chirp()

target = TargetSignature(distance=150, velocity=0, rcs=0.008)
rx = target.apply(tx, radar.fs)

rcs_engine = RCSEngine(noise_power=0.01)
rx_noisy = rcs_engine.add_noise(rx)
beat = rcs_engine.mix(tx, rx_noisy)

vis = Visualizer()
vis.plot_range(beat, radar.fs)

