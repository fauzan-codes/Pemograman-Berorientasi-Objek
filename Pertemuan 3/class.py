class mahasiswa:
    def __init__ ( self, nama, nim, jurusan, umur):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.umur = umur   

    def introduction (self):
        print(f"my name is {self.nama}, and i am from {self.jurusan}")

    