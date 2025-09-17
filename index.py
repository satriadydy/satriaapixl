# File: api/index.py

from flask import Flask, jsonify
import sys
import os

# --- LANGKAH PENTING! ---
# Anda harus meletakkan semua file Python dari proyek me-cli Anda di sini
# di folder 'api' ini. Atau, atur path agar Python bisa menemukannya.
# Contoh:
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from me_cli_main_file import me_cli_function_to_run_command # Ganti nama ini
# --- END LANGKAH PENTING ---

app = Flask(__name__)

# Ini adalah alamat khusus yang akan dipanggil dari website (frontend)
@app.route('/api/cek_saldo', methods=['GET'])
def cek_saldo():
    try:
        # --- LANGKAH 1: Panggil fungsi dari kode me-cli Anda di sini ---
        # Contoh: Jika Anda punya fungsi yang mengecek saldo, panggil di sini
        # hasil = me_cli_function_to_run_command('cek_saldo')
        
        # Contoh sementara: data saldo yang Anda dapatkan dari kode Anda
        # data_saldo_dari_me_cli = hasil.get('saldo') # Ganti sesuai output kode Anda

        # --- LANGKAH 2: Ganti kode di bawah ini dengan kode Anda ---
        # Karena ini contoh, kita pakai data palsu
        data_saldo_dari_me_cli = "Rp 125.000"
        
        # Kembalikan data dalam format JSON
        return jsonify({
            "status": "success",
            "message": "Berhasil mendapatkan saldo.",
            "saldo": data_saldo_dari_me_cli
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Terjadi kesalahan: {str(e)}"
        }), 500
