# Import library tkinter untuk GUI
import tkinter as tk
# Import library sqlite3 untuk interaksi dengan database SQLite
import sqlite3

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai tertinggi
def prediksi_fakultas(biologi, fisika, inggris): 
    # Jika nilai biologi lebih besar dari fisika dan biologi lebih besar dari inggris
    if biologi > fisika and biologi > inggris:
        # Maka fakultas yang diprediksi adalah "Kedokteran"
        return "Kedokteran"
    # Jika nilai fisika lebih besar dari biologi dan fisika lebih besar dari inggris
    elif fisika > biologi and fisika > inggris:
         # Maka fakultas yang diprediksi adalah "Teknik"
        return "Teknik"
    # Jika nilai inggris lebih besar dari biologi dan inggris lebih besar dari fisika
    elif inggris > biologi and inggris > fisika:
         # Maka fakultas yang diprediksi adalah "Bahasa"
        return "Bahasa"
    # Jika tidak memenuhi kondisi di atas
    else:
        # Maka menampilkan "Tidak dapat memprediksi fakultas"
        return "Tidak dapat memprediksi fakultas"

# Fungsi untuk menyimpan data ke dalam database SQLite
def simpan_data(nama_siswa, biologi, fisika, inggris):
    prediksi = prediksi_fakultas(biologi, fisika, inggris)

    try:
        # Membuat koneksi ke database SQLite
        conn = sqlite3.connect("LiteSQL.db")
        cursor = conn.cursor()

        # Mengecek dan membuat tabel jika belum ada
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nilai_siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_siswa TEXT NOT NULL,
                biologi INTEGER NOT NULL,
                fisika INTEGER NOT NULL,
                inggris INTEGER NOT NULL,
                prediksi_fakultas TEXT NOT NULL
            )
        ''')

        # Menyimpan data ke dalam tabel
        cursor.execute('''
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        ''', (nama_siswa, biologi, fisika, inggris, prediksi))

        # Commit dan menutup koneksi database
        conn.commit()
        conn.close()

        # Mengupdate label prediksi dengan pesan sukses dan prediksi fakultas
        label_prediksi.config(text=f"Data berhasil disimpan. Prediksi Fakultas: {prediksi}", fg="green")
    except Exception as e:
        # Mengupdate label prediksi dengan pesan kesalahan
        label_prediksi.config(text=f"Terjadi kesalahan: {str(e)}", fg="red")

# Fungsi untuk menangani klik tombol submit
def submit_nilai():
    # Mengambil nilai dari input entry untuk nama, biologi, fisika, dan inggris
    nama_siswa = entry_nama.get()
    biologi = entry_biologi.get()
    fisika = entry_fisika.get()
    inggris = entry_inggris.get()

    try:
        # Validasi input  # Mengkonversi nilai biologi, fisika, dan inggris menjadi integer
        biologi = int(biologi)
        fisika = int(fisika)
        inggris = int(inggris)

        # Memeriksa apakah nilai berada dalam rentang 0-100
        if 0 <= biologi <= 100 and 0 <= fisika <= 100 and 0 <= inggris <= 100:
            # Mendapatkan prediksi fakultas
            prediksi = prediksi_fakultas(biologi, fisika, inggris)
            
            # Menyimpan data dan menampilkan pesan sukses dengan prediksi fakultas
            simpan_data(nama_siswa, biologi, fisika, inggris)
        else:
            # Menampilkan pesan kesalahan jika nilai tidak valid
            label_prediksi.config(text="Masukkan nilai antara 0 dan 100.", fg="red")
    except ValueError:
        # Menampilkan pesan kesalahan jika terjadi kesalahan konversi ke integer
        label_prediksi.config(text="Masukkan nilai numerik.", fg="red")

# Membuat objek utama Tkinter
root = tk.Tk()
root.title("Form Nilai Siswa")

# Mendapatkan lebar dan tinggi layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Mendapatkan lebar dan tinggi jendela
window_width = 400  # Sesuaikan dengan kebutuhan
window_height = 300  # Sesuaikan dengan kebutuhan

# Menghitung posisi tengah jendela
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Menentukan ukuran dan posisi jendela
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Label dan Entry untuk Nama Siswa
label_nama = tk.Label(root, text="Nama Siswa:")
# Menempatkan label di grid pada baris 0 dan kolom 0, dengan padding dan melekat di sebelah barat (kiri)
label_nama.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
# Membuat objek Entry sebagai kotak input untuk memasukkan nama siswa
entry_nama = tk.Entry(root)
# Menempatkan kotak input di grid pada baris 0 dan kolom 1, dengan padding
entry_nama.grid(row=0, column=1, padx=10, pady=5)

# Label dan Entry untuk Nilai Biologi
label_biologi = tk.Label(root, text="Nilai Biologi:")
# Menempatkan label di grid pada baris 1 dan kolom 0, dengan padding dan melekat di sebelah barat (kiri)
label_biologi.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
# Membuat objek Entry sebagai kotak input untuk memasukkan nilai biologi
entry_biologi = tk.Entry(root)
# Menempatkan kotak input di grid pada baris 1 dan kolom 1, dengan padding
entry_biologi.grid(row=1, column=1, padx=10, pady=5)

# Label dan Entry untuk Nilai Fisika
label_fisika = tk.Label(root, text="Nilai Fisika:")
# Menempatkan label di grid pada baris 2 dan kolom 0, dengan padding dan melekat di sebelah barat (kiri)
label_fisika.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
# Membuat objek Entry sebagai kotak input untuk memasukkan nilai fisika
entry_fisika = tk.Entry(root)
# Menempatkan kotak input di grid pada baris 2 dan kolom 1, dengan padding
entry_fisika.grid(row=2, column=1, padx=10, pady=5)

# Label dan Entry untuk Nilai Inggris
label_inggris = tk.Label(root, text="Nilai Inggris:")
# Menempatkan label di grid pada baris 3 dan kolom 0, dengan padding dan melekat di sebelah barat (kiri)
label_inggris.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
# Membuat objek Entry sebagai kotak input untuk memasukkan nilai Inggris
entry_inggris = tk.Entry(root)
# Menempatkan kotak input di grid pada baris 3 dan kolom 1, dengan padding
entry_inggris.grid(row=3, column=1, padx=10, pady=5)

# Tombol Submit
button_submit = tk.Button(root, text="Submit", command=submit_nilai)
# Menempatkan tombol di grid pada baris 4 dan kolom 0, menempati dua kolom, dengan padding di bagian bawah
button_submit.grid(row=4, column=0, columnspan=2, pady=10)

# Label untuk Prediksi Fakultas
label_prediksi = tk.Label(root, text="", fg="black")
# Menempatkan label di grid pada baris 5 dan kolom 0, menempati dua kolom, dengan padding di bagian bawah
label_prediksi.grid(row=5, column=0, columnspan=2, pady=5)

# Menjalankan loop utama Tkinter
root.mainloop()

