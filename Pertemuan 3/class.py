class mahasiswa:
    def __init__ ( self, nama, nim, jurusan, umur):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.umur = umur   

    def introduction (self):
        print(f"my name is {self.nama}, and i am from {self.jurusan}, and i am {self.umur} years old")

    def umur_2031(self):
        print(f"Umur {self.nama} pada tahun 2031 adalah {self.umur + 5}")

student1 = mahasiswa("deva", 1234, "mechanical laba laba sunda", 20)
student2 = mahasiswa("ujang", 3872, "mechanical", 19)


student1.introduction()
student1.umur_2031()

student2.introduction()
student2.umur_2031()