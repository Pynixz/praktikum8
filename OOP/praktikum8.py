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