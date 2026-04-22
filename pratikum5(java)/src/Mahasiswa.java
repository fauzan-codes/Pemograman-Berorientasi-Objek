package src;

public class Mahasiswa {

    public String nama;
    public String kelas;
    public int angkatan;
    String jurusan;
    
    // constructor
    public Mahasiswa(String nama, String nim, String kelas, int angkatan) {
        this.nama = nama;
        this.nim = nim;
        this.kelas = kelas;
        this.angkatan = angkatan;
        this.angkatan = angkatan;

        System.out.println("Data sudah disimpan\n");
    }

    public void tampilkanInformasi() {

        System.out.println("INFORMASI MAHASISWA");
        System.out.println("Nama : " + nama);
        System.out.println("NIM : " + nim);
        System.out.println("Kelas : " + kelas);
        System.out.println("Angkatan : " + angkatan);
        System.out.println("Jurusan: ");
        System.out.println();
    }
}
