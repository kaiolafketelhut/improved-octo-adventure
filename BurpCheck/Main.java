import java.io.*;
import java.security.MessageDigest;
import java.nio.file.*;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.print("Path to file to check: ");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String path = br.readLine().trim().replace("\"", "");

        byte[] data = Files.readAllBytes(Paths.get(path));
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hash = md.digest(data);

        StringBuilder sb = new StringBuilder();
        for (byte b : hash) sb.append(String.format("%02X", b));

        System.out.println("\n--- SHA256 HASH ---");
        System.out.println(sb.toString());
        System.out.println("Compare with official hash on portswigger.net");
        System.out.println("Same = Clean, Different = Tampered");
    }
}
