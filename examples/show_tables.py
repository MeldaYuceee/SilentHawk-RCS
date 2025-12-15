import matplotlib.pyplot as plt

def draw_table(title, data, filename=None):
    fig, ax = plt.subplots(figsize=(10, 2 + len(data)*0.4))
    ax.axis('off')

    # Başlık
    plt.title(title, fontsize=16, fontweight="bold", pad=20)

    # Tablo
    table = plt.table(cellText=data,
                      colLabels=["Özellik", "Açıklama", "Modül"],
                      cellLoc='center',
                      loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.8)

    # Kaydetme isteğe bağlı
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.show()


# ---- TABLOLAR ---- #

range_fft_table = [
    ["FMCW Chirp Üretimi", "Tek sweep üretir", "radar_model.py"],
    ["Beat Sinyal Hesabı", "Tx × conj(Rx)", "rcs_engine.py"],
    ["Range FFT", "Mesafe spektrumu çıkarır", "visualizer.py"],
    ["SNR Etkisi", "Stealth hedef kaybolabilir", "rcs_engine.py"],
]

range_doppler_table = [
    ["Chirp Burst", "N chirp üretir", "radar_model.py"],
    ["2D FFT", "Mesafe + hız haritası", "visualizer.py"],
    ["Velocity Estimation", "Doppler → hız", "visualizer.py"],
    ["Heatmap", "2D renkli görüntü", "visualizer.py"],
]

multi_target_table = [
    ["Çoklu Hedef", "Birden fazla hedef simülasyonu", "multi_target.py"],
    ["Mesafe Güncelleme", "Her chirpte değişir", "multi_target.py"],
    ["Hız Modeli", "Yaklaşma/uzaklaşma", "multi_target.py"],
    ["Echo Toplama", "Tüm hedeflerin ekosu birleşir", "multi_target.py"],
]

rcs_table = [
    ["Base RCS", "Hedefin temel görünürlüğü", "multi_target.py"],
    ["Angle RCS", "cos²(θ) modeli", "multi_target.py"],
    ["Stealth Davranışı", "Bazı açılarda kaybolma", "multi_target.py"],
    ["Attenuation", "Echo şiddetini azaltır", "multi_target.py"],
]

jammer_table = [
    ["Jammer Noise", "Belirli chirplerde gürültü ekler", "rcs_engine.py"],
    ["Jammer SNR", "10–30 dB bastırma", "rcs_engine.py"],
    ["ECCM Threshold", "Hedef görünür/görünmez", "detect_stealth_threshold"],
    ["Dayanıklılık Testi", "Radar performans analizi", "examples/"],
]


if __name__ == "__main__":
    draw_table("1) RANGE FFT", range_fft_table)
    draw_table("2) RANGE–DOPPLER", range_doppler_table)
    draw_table("3) MULTI-TARGET", multi_target_table)
    draw_table("4) RCS / STEALTH", rcs_table)
    draw_table("5) JAMMER & ECCM", jammer_table)
