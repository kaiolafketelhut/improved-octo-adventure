// oneyepdf.c - One Eye PDF - Minimal PDF writer in pure C, no libs
// Usage: gcc oneyepdf.c -o oneyepdf && ./oneyepdf
// Output: summary.pdf
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE *f;
long offsets[10];

void write_line(const char *text, int x, int y, int size, int bold) {
    // Escape ( ) \ in PDF text
    char esc[512];
    int j = 0;
    for (int i = 0; text[i] && j < 500; i++) {
        if (text[i] == '(' || text[i] == ')' || text[i] == '\\') esc[j++] = '\\';
        esc[j++] = text[i];
    }
    esc[j] = 0;
    fprintf(f, "BT /F%d %d Tf %d %d Td (%s) Tj ET\n", bold ? 2 : 1, size, x, y, esc);
}

int main() {
    f = fopen("summary.pdf", "wb");
    if (!f) { printf("Cannot create summary.pdf\n"); return 1; }

    // PDF Header
    fprintf(f, "%%PDF-1.4\n");

    // We build content stream first in memory via temp file
    FILE *tmp = fopen("content.tmp", "wb");
    FILE *old = f;
    f = tmp;

    int y = 800;
    write_line("TIER Software Integration Project", 50, y, 18, 1); y -= 28;
    write_line("ERP Suite - Employee Work Time Calculation", 50, y, 13, 1); y -= 22;
    write_line("Summary.md | BOM - Bill of Materials | PDF Version", 50, y, 10, 0); y -= 18;
    write_line("--------------------------------------------------", 50, y, 10, 0); y -= 30;

    write_line("1. Project Overview", 50, y, 12, 1); y -= 22;
    write_line("Repo: kaiolafketelhut/improved-octo-adventure - Branch: main", 50, y, 11, 0); y -= 18;
    write_line("Commit: 6dc1f9f - Fix summary.md formatting", 50, y, 11, 0); y -= 18;
    write_line("Rules: 8.0h normal, 0.5h break if >6h, Overtime after 8h", 50, y, 11, 0); y -= 28;

    write_line("2. BOM - Bill of Materials", 50, y, 12, 1); y -= 22;
    write_line("Main.java - MAIN.JAR hash checker", 50, y, 11, 0); y -= 18;
    write_line("hexdiff.py - Hexdiff + signature checks", 50, y, 11, 0); y -= 18;
    write_line("erp_time.py / ERPTime.java - ERP calc CSV + BIN", 50, y, 11, 0); y -= 18;
    write_line("timesheet.csv / timesheet.bin - Test timesheets", 50, y, 11, 0); y -= 18;
    write_line("kdp.ximg - Macintosh MIDI substitute, 161 bytes", 50, y, 11, 0); y -= 18;
    write_line("summary.md / BOM.csv - This documentation", 50, y, 11, 0); y -= 28;

    write_line("3. Reference Checks - a.bin / b.bin", 50, y, 12, 1); y -= 22;
    write_line("Boot Sig [510-511]: 55AA -> OK 0x55AA", 50, y, 11, 0); y -= 18;
    write_line("Mac Type [0-3]: 4D696469 = 'Midi'", 50, y, 11, 0); y -= 18;
    write_line("TIER ID 0x5254 ('RT'): FOUND at offset 512", 50, y, 11, 0); y -= 18;
    write_line("0x0200   52             58             <-- DIFF", 50, y, 11, 0); y -= 28;

    write_line("4. Actual Check - kdp.ximg", 50, y, 12, 1); y -= 22;
    write_line("Size: 161 bytes", 50, y, 11, 0); y -= 18;
    write_line("SHA256: 09aad2cfd9d2e80881bbed17a93c418ee8d99b8756374d4959f8147914214f33", 50, y, 9, 0); y -= 18;
    write_line("Header [0-3]: 58 49 4D 47 = 'XIMG'", 50, y, 11, 0); y -= 18;
    write_line("Header [4-5]: 01 01 = Version 1.1", 50, y, 11, 0); y -= 18;
    write_line("Header [14-15]: 78 9C = zlib header", 50, y, 11, 0); y -= 18;
    write_line("Boot Sig [510-511]: file too short -> NOT APPLICABLE", 50, y, 11, 0); y -= 18;
    write_line("Mac Type: XIMG (not Midi) | TIER RT: NOT FOUND", 50, y, 11, 0); y -= 18;
    write_line("Conclusion: Valid XIMG container, not boot sector, not raw MIDI.", 50, y, 11, 0); y -= 28;

    write_line("5. ERP Results - Verified", 50, y, 12, 1); y -= 22;
    write_line("Kai   2026-11-17  08:00  17:30  9.00h  1.00h OT  OVERTIME", 50, y, 11, 0); y -= 18;
    write_line("Anna  2026-11-17  09:00  18:00  8.50h  0.50h OT  OVERTIME", 50, y, 11, 0); y -= 18;
    write_line("Total: 17.50h", 50, y, 11, 0); y -= 28;

    write_line("6. How To Use", 50, y, 12, 1); y -= 22;
    write_line("sha256sum -c timesheet.sha256", 50, y, 11, 0); y -= 18;
    write_line("python3 hexdiff.py a.bin b.bin", 50, y, 11, 0); y -= 18;
    write_line("python3 erp_time.py timesheet.csv / timesheet.bin", 50, y, 11, 0); y -= 18;
    write_line("java ERPTime timesheet.csv", 50, y, 11, 0); y -= 18;
    write_line("gcc oneyepdf.c -o oneyepdf && ./oneyepdf", 50, y, 11, 0); y -= 18;

    fclose(tmp);
    f = old;

    // Read content.tmp size
    tmp = fopen("content.tmp", "rb");
    fseek(tmp, 0, SEEK_END);
    long clen = ftell(tmp);
    fseek(tmp, 0, SEEK_SET);
    char *content = malloc(clen + 1);
    fread(content, 1, clen, tmp);
    fclose(tmp);

    // Object 1: Catalog
    offsets[1] = ftell(f);
    fprintf(f, "1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n");
    // Object 2: Pages
    offsets[2] = ftell(f);
    fprintf(f, "2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n");
    // Object 3: Page
    offsets[3] = ftell(f);
    fprintf(f, "3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>\nendobj\n");
    // Object 4: Font Regular
    offsets[4] = ftell(f);
    fprintf(f, "4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n");
    // Object 5: Font Bold
    offsets[5] = ftell(f);
    fprintf(f, "5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n");
    // Object 6: Content
    offsets[6] = ftell(f);
    fprintf(f, "6 0 obj\n<< /Length %ld >>\nstream\n", clen);
    fwrite(content, 1, clen, f);
    fprintf(f, "\nendstream\nendobj\n");

    long xref_pos = ftell(f);
    fprintf(f, "xref\n0 7\n");
    fprintf(f, "0000000000 65535 f \n");
    for (int i = 1; i <= 6; i++) {
        fprintf(f, "%010ld 00000 n \n", offsets[i]);
    }
    fprintf(f, "trailer\n<< /Size 7 /Root 1 0 R >>\nstartxref\n%ld\n%%%%EOF\n", xref_pos);

    fclose(f);
    free(content);
    remove("content.tmp");
    printf("Saved summary.pdf with oneyepdf.c - OK\n");
    return 0;
}

