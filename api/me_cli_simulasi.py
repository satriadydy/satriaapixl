# File: proyek-website-me/api/me_cli_simulasi.py
import time
import random

# --- TEMPAT ANDA MELETAKKAN KODE ASLI me-cli ---
# Ganti fungsi di bawah ini dengan fungsi yang ada di proyek me-cli Anda
# Fungsi ini harus bisa menerima perintah dan mengembalikan hasilnya

def jalankan_perintah_me_cli(perintah):
    """
    Fungsi ini mensimulasikan logika dari kode me-cli.
    """
    print(f"Menerima perintah: {perintah}")
    
    # Simulasikan waktu pemrosesan
    time.sleep(1) 
    
    # Logika sederhana berdasarkan perintah
    if perintah == 'cek_saldo':
        saldo_acak = random.randint(10000, 100000)
        return {
            "status": "success",
            "pesan": "Berhasil mendapatkan saldo.",
            "saldo": f"Rp {saldo_acak:,}".replace(",", ".")
        }
    else:
        return {
            "status": "error",
            "pesan": f"Perintah '{perintah}' tidak dikenal."
        }
