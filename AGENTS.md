# Multi-Agent Virtual RAM — Aturan Proyek

## Tujuan
Demo multi-agent dengan **virtual RAM** (folder + file) sebagai shared memory antar agent.

## Struktur
```
multi-agent-demo/
├── virtual_ram.py      ← orchestrator + virtual RAM (satu file)
├── AGENTS.md
└── virtual-ram/        ← folder RAM (dibuat runtime, dihapus isinya saat selesai)
    ├── agent-a.txt
    ├── agent-b.txt
    └── ...
```

## Alur
1. Orchestrator buat folder `virtual-ram/` + file per agent
2. Setiap agent tulis hasil/tugas ke file-nya (via thread paralel)
3. **Validasi**: cek folder + file ada & terisi
4. **Selesai**: hapus semua file di dalam folder (RAM dibersihkan)

## Aturan
- Kode eksperimen → `experiment/` (AGENTS.md global), proyek ini = demo terstruktur
- Hemat token: satu-file Python, output ringkas
