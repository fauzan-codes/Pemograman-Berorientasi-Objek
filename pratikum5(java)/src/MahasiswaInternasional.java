package src;

public class MahasiswaInternasional extends Mahasiswa {

    public String bahasa;
    public String negaraAsal;
    public int nilai;
    public boolean visaAktif;

    public MahasiswaInternasional(
            String nama,
            String nim,
            String kelas,
            int angkatan,
            String jurusan,

            String bahasa,
            String negaraAsal,
            int nilai,
            boolean visaAktif
        ) {

        super(nama, nim, kelas, angkatan, jurusan);

        this.nama = nama;
        this.nim = nim;
        this.kelas = kelas;
        this.angkatan = angkatan;
        this.jurusan = jurusan;
        this.bahasa = bahasa;
        this.negaraAsal = negaraAsal;
        this.nilai = nilai;
        this.visaAktif = visaAktif;
        

        System.out.println("Data sudah disimpan\n");
    }

    public void perkenalan() {
        System.out.println("Nama: " + nama);
        System.out.println("NIM: " + nim);
        System.out.println("Kelas: " + kelas);
        System.out.println("Jurusan: " + jurusan);
    }
}
