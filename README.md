## PRAKTIKUM 8
### OOP
## Diagram Class

| Daftar Nilai Mahasiswa   |
| ------------------------ |
| - daftar_nilai: list     |
| ------------------------ |
| + **init**()             |
| + tambah(nama, nilai)    |
| + tampilkan()            |
| + hapus(nama)            |
| + ubah(nama, nilai)      |

# Code program
``` py
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_nilai = []

    def tambah(self, mahasiswa):
        self.daftar_nilai.append(mahasiswa)
        print(f"Data {mahasiswa.nama} berhasil ditambahkan.")

    def tampilkan(self):
        print("Daftar Nilai Mahasiswa:")
        for mahasiswa in self.daftar_nilai:
            print(f"Nama: {mahasiswa.nama}, Nilai: {mahasiswa.nilai}")

    def hapus(self, nama):
        for mahasiswa in self.daftar_nilai:
            if mahasiswa.nama == nama:
                self.daftar_nilai.remove(mahasiswa)
                print(f"Data {nama} berhasil dihapus.")
                return
        print(f"Data {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for mahasiswa in self.daftar_nilai:
            if mahasiswa.nama == nama:
                mahasiswa.nilai = nilai_baru
                print(f"Data {nama} berhasil diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Data {nama} tidak ditemukan.")

def main():
    # Contoh penggunaan
    daftar_nilai_mahasiswa = DaftarNilaiMahasiswa()

    # Menambahkan data
    mahasiswa1 = Mahasiswa("Dhiya", 85)
    mahasiswa2 = Mahasiswa("Ulhaq", 92)
    print("======================================")

    daftar_nilai_mahasiswa.tambah(mahasiswa1)
    daftar_nilai_mahasiswa.tambah(mahasiswa2)
    print("======================================")

    # Menampilkan data
    daftar_nilai_mahasiswa.tampilkan()
    print("======================================")

    # Menghapus data
    daftar_nilai_mahasiswa.hapus("Dhiya")
    print("======================================")

    # Menampilkan data setelah penghapusan
    daftar_nilai_mahasiswa.tampilkan()
    print("======================================")

    # Mengubah data
    daftar_nilai_mahasiswa.ubah("Ulhaq", 95)
    print("======================================")

    # Menampilkan data setelah perubahan
    daftar_nilai_mahasiswa.tampilkan()
    print("======================================")

if __name__ == "__main__":
    main()
```
**Penjelasan:**
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

   ## Output
   ![Screenshot 2023-12-12 145552](https://github.com/Pynixz/praktikum8/assets/147568964/3d9459a3-82ae-46b2-b64e-cd6819694f07)

   ## Flowchart
   ![Flowchart praktikum8](https://github.com/Pynixz/praktikum8/assets/147568964/d909514c-101d-412d-8948-a11fe26388bc)
