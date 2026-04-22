package dosen;

import src.Mahasiswa;

public class MainDosen {
    public static void main(String[] args) {
        Mahasiswa mhs = new Mahasiswa(
            "Fauzan",
            "25051204003",
            "TI A 2025",
            2025,
            "Teknik Informatika"
        );

        System.out.println(mhs.nama);
        System.out.println(mhs.nim);
        System.out.println(mhs.kelas);
        System.out.println(mhs.jurusan);
    }
}
