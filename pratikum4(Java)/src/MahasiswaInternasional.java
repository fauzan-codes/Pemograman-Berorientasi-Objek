
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
            String bahasa,
            String negaraAsal,
            int nilai,
            boolean visaAktif) {

        super(nama, nim, kelas, angkatan);

        this.bahasa = bahasa;
        this.negaraAsal = negaraAsal;
        this.nilai = nilai;
        this.visaAktif = visaAktif;
    }

    public void tampilkanInformasi() {

        super.tampilkanInformasi();

        System.out.println("INFORMASI TAMBAHAN");
        System.out.println("Bahasa : " + bahasa);
        System.out.println("Negara : " + negaraAsal);
        System.out.println("Nilai : " + nilai);

        if (nilai >= 75) {
            System.out.println("Mahasiswa LULUS");
        } else if (nilai >= 60) {
            System.out.println("Remedial diperbolehkan");
        } else {
            System.out.println("Harus mengulang");
        }

        if (visaAktif) {
            System.out.println("Visa aktif, mahasiswa diizinkan tinggal");
        } else {
            System.out.println("Visa tidak aktif, segera perpanjang");
        }

        if (nilai < 60 && !visaAktif) {
            System.out.println("PERINGATAN: Mahasiswa harus mengulang dan perpanjang visa!");
        }
    }
}
