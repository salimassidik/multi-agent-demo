#!/usr/bin/env python3
"""
virtual_ram.py — Multi-Agent dengan Virtual RAM sederhana.

Alur:
  1. Buat folder virtual-ram/ + file per agent
  2. Setiap agent (thread paralel) menulis hasil ke file-nya
  3. VALIDASI: cek folder + file ada & terisi
  4. SELESAI: hapus semua file di dalam folder (RAM dibersihkan)

Cara pakai:
  python3 virtual_ram.py                # jalankan semua agent
  python3 virtual_ram.py --agents 5     # jumlah agent kustom
"""
import argparse, os, threading, time, json

RAM_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "virtual-ram")

# Data tugas per agent (simulasi agent mengerjakan bagiannya)
TASKS = {
    "agent-a": {"tugas": "riset topik", "hasil": "menemukan 3 sumber: A, B, C"},
    "agent-b": {"tugas": "analisis data", "hasil": "rata-rata = 42.5, trend naik"},
    "agent-c": {"tugas": "tulis laporan", "hasil": "draft 2 halaman selesai"},
    "agent-d": {"tugas": "review kode", "hasil": "0 bug, 1 peringatan"},
}

def agent_kerja(nama, info):
    """Simulasi agent: tulis info ke file virtual RAM-nya."""
    waktu = time.strftime("%H:%M:%S")
    isi = json.dumps({
        "agent": nama,
        "tugas": info["tugas"],
        "hasil": info["hasil"],
        "waktu": waktu,
    }, indent=2)
    fp = os.path.join(RAM_DIR, f"{nama}.txt")
    with open(fp, "w") as f:
        f.write(isi)
    time.sleep(0.3)  # simulasi kerja
    print(f"  ✅ {nama} selesai: {info['hasil']}")

def main():
    ap = argparse.ArgumentParser(description="Multi-Agent Virtual RAM")
    ap.add_argument("--agents", type=int, default=None, help="jumlah agent (default: semua)")
    args = ap.parse_args()

    # 1. Buat folder RAM
    os.makedirs(RAM_DIR, exist_ok=True)
    print(f"[1] Folder RAM: {RAM_DIR}")

    # pilih agent
    items = list(TASKS.items())
    if args.agents:
        items = items[:args.agents]

    # 2. Jalankan agent paralel (thread)
    print(f"[2] Jalankan {len(items)} agent paralel...")
    threads = []
    for nama, info in items:
        t = threading.Thread(target=agent_kerja, args=(nama, info))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("    semua agent selesai")

    # 3. VALIDASI folder + file
    print("[3] Validasi...")
    files = sorted(os.listdir(RAM_DIR))
    ok = True
    for nama, _ in items:
        fp = os.path.join(RAM_DIR, f"{nama}.txt")
        if os.path.exists(fp) and os.path.getsize(fp) > 0:
            print(f"  ✅ {nama}.txt ada & terisi ({os.path.getsize(fp)} B)")
        else:
            print(f"  ❌ {nama}.txt MISSING/KOSONG")
            ok = False
    if not ok:
        print("VALIDASI GAGAL"); return
    print(f"  ✅ {len(files)} file tervalidasi")

    # 4. SELESAI: hapus semua file di dalam folder
    print("[4] Bersihkan RAM (hapus file)...")
    for fn in files:
        os.remove(os.path.join(RAM_DIR, fn))
        print(f"  🗑  hapus {fn}")
    sisa = os.listdir(RAM_DIR)
    print(f"    sisa file di folder: {len(sisa)}")
    if not sisa:
        print("✅ RAM bersih — semua file tugas terhapus")
    else:
        print(f"⚠️  masih ada {sisa}")

if __name__ == "__main__":
    main()
