package src;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in); 

        System.out.print("Nama: ");
        String nama = input.nextLine();

        System.out.print("NIM: ");
        String nim = input.nextLine();

        System.out.print("Kelas: ");
        String kelas = input.nextLine();

        System.out.print("Angkatan: ");
        int angkatan = input.nextInt();
        input.nextLine();

        System.out.print("Bahasa: ");
        String bahasa = input.nextLine();

        System.out.print("Negara: ");
        String negara = input.nextLine();

        System.out.print("Nilai: ");
        int nilai = input.nextInt();

        System.out.print("Visa aktif? (true/false): ");
        boolean visa = input.nextBoolean();

        MahasiswaInternasional mhs = new MahasiswaInternasional(
                nama,
                nim,
                kelas,
                angkatan,
                bahasa,
                negara,
                nilai,
                visa);

        mhs.tampilkanInformasi();

        input.close();
    }
}
