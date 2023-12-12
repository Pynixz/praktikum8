### OOP

**Penjelasan Kode:**

1. **Kelas Mahasiswa:**
   - `__init__(self, nama, nilai)`: Konstruktor inisialisasi objek mahasiswa dengan atribut `nama` dan `nilai`.

2. **Kelas DaftarNilaiMahasiswa:**
   - `__init__(self)`: Konstruktor inisialisasi objek daftar nilai mahasiswa dengan atribut `daftar_nilai` yang merupakan list untuk menyimpan objek mahasiswa.
   - `tambah(self, mahasiswa)`: Menambahkan objek mahasiswa ke dalam list `daftar_nilai`.
   - `tampilkan(self)`: Menampilkan daftar nilai mahasiswa dengan iterasi melalui list `daftar_nilai`.
   - `hapus(self, nama)`: Menghapus objek mahasiswa dari list `daftar_nilai` berdasarkan nama.
   - `ubah(self, nama, nilai_baru)`: Mengubah nilai objek mahasiswa dalam list `daftar_nilai` berdasarkan nama.

3. **Fungsi Utama (`main()`):**
   - Membuat objek `daftar_nilai_mahasiswa` dari kelas `DaftarNilaiMahasiswa`.
   - Membuat dua objek mahasiswa (`mahasiswa1` dan `mahasiswa2`) dari kelas `Mahasiswa`.
   - Menambahkan dua objek mahasiswa ke dalam daftar nilai dan menampilkan pesan.
   - Menampilkan daftar nilai.
   - Menghapus data mahasiswa dengan nama "Dhiya".
   - Menampilkan daftar nilai setelah penghapusan.
   - Mengubah nilai mahasiswa dengan nama "Ulhaq" menjadi 95.
   - Menampilkan daftar nilai setelah perubahan.
