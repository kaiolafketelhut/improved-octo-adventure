import java.io.*;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class ERPTime {
    static double NORMAL = 8.0;
    static double BREAK_H = 0.5;

    static void calc(String emp, String date, String cin, String cout) {
        DateTimeFormatter f = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime in = LocalDateTime.parse(date + " " + cin, f);
        LocalDateTime out = LocalDateTime.parse(date + " " + cout, f);
        if (out.isBefore(in)) out = out.plusDays(1);
        double hours = Duration.between(in, out).toMinutes() / 60.0;
        if (hours > 6) hours -= BREAK_H;
        double ot = Math.max(0, hours - NORMAL);
        String status = ot > 0 ? "OVERTIME" : (hours >= 8 ? "OK" : "UNDER-TIME");
        System.out.printf("%-12s %-12s %-6s %-6s %-6.2f %-8.2f %s%n", emp, date, cin, cout, hours, ot, status);
    }

    public static void main(String[] args) throws Exception {
        String path = args[0];
        System.out.println("--- ERP Report Java: " + path + " ---");
        BufferedReader br = new BufferedReader(new FileReader(path));
        String line = br.readLine(); // header
        double total = 0;
        while ((line = br.readLine()) != null) {
            String[] p = line.split(",");
            // We need to re-calc to get total - quick calc here
            calc(p[0], p[1], p[2], p[3]);
        }
        br.close();
        System.out.println("Done - Rules: 8h normal, 0.5h break, OT after 8h");
    }
}
