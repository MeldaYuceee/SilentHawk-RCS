import matplotlib.pyplot as plt

def draw_table(title, data, filename=None):
    fig, ax = plt.subplots(figsize=(10, 2 + len(data) * 0.4))
    ax.axis("off")

    plt.title(title, fontsize=16, fontweight="bold", pad=20)

    table = plt.table(
        cellText=data,
        colLabels=["Feature", "Description", "Module"],
        cellLoc="center",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.8)

    if filename:
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.show()


range_fft_table = [
    ["FMCW Chirp Generation", "Single sweep signal", "radar_model.py"],
    ["Beat Signal Mixing", "Tx × conj(Rx)", "rcs_engine.py"],
    ["Range FFT", "Distance spectrum", "visualizer.py"],
    ["SNR Effect", "Stealth target may disappear", "rcs_engine.py"],
]

range_doppler_table = [
    ["Chirp Burst", "Multiple chirps", "radar_model.py"],
    ["2D FFT", "Range and velocity map", "visualizer.py"],
    ["Velocity Estimation", "Doppler to speed", "visualizer.py"],
    ["Heatmap", "2D color display", "visualizer.py"],
]

multi_target_table = [
    ["Multiple Targets", "Simulate more than one target", "multi_target.py"],
    ["Range Update", "Distance changes per chirp", "multi_target.py"],
    ["Velocity Model", "Approaching or receding", "multi_target.py"],
    ["Echo Summation", "All target echoes combined", "multi_target.py"],
]

rcs_table = [
    ["Base RCS", "Initial target visibility", "multi_target.py"],
    ["Angle RCS", "cos²(theta) model", "multi_target.py"],
    ["Stealth Effect", "Target fades at some angles", "multi_target.py"],
    ["Attenuation", "Reduces echo strength", "multi_target.py"],
]

jammer_table = [
    ["Jammer Noise", "Noise added to selected chirps", "rcs_engine.py"],
    ["Jammer SNR", "10–30 dB suppression", "rcs_engine.py"],
    ["ECCM Threshold", "Detectable or not", "detect_stealth_threshold"],
    ["Robustness Test", "Radar performance check", "examples/"],
]


if __name__ == "__main__":
    draw_table("1) RANGE FFT", range_fft_table)
    draw_table("2) RANGE–DOPPLER", range_doppler_table)
    draw_table("3) MULTI-TARGET", multi_target_table)
    draw_table("4) RCS / STEALTH", rcs_table)
    draw_table("5) JAMMER & ECCM", jammer_table)

