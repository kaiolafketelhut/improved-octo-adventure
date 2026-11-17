# TIER Software Integration Project - Summary.md
## ERP Suite - Employee Work Time Calculation
## BOM - Bill of Materials

### 1. Project Overview

- Project: BurpCheck / ERP Suite
- Repo: kaiolafketelhut/improved-octo-adventure
- Branch: main
- Purpose: Verify binary files with hexdiff + calculate employee work time
- Rules: 8.0h normal, 0.5h break if >6h, Overtime after 8h

### 2. BOM - Bill of Materials (Files)

| File | Type | Purpose |
| --- | --- | --- |
| Main.java | Java | MAIN.JAR hash checker |
| hexdiff.py | Python | Hexdiff + signature checks |
| erp_time.py | Python | ERP calc CSV + BIN |
| ERPTime.java | Java | ERP calc CSV |
| timesheet.csv | CSV | Test timesheet |
| timesheet.bin | BIN | Fingerprint machine test, 32-byte records |
| kdp.ximg | XIMG | Macintosh MIDI substitute, custom container |
| summary.md | Markdown | This file |
| BOM.csv | CSV | Bill of Materials for ERP import |
| .gitignore | Config | Ignore *.jar, *.class, bin/, obj/ |

### 3. Reference Checks - Test Files a.bin / b.bin

    Boot Sig [510-511]: 55AA -> OK 0x55AA
    Mac Type [0-3]: 4D696469 = 'Midi'
    TIER ID 0x5254 ('RT'): FOUND at offset 512
    0x0200   52             58             <-- DIFF

- Boot Sig 510-511 = 55 AA = Bootable sector signature. OK.
- Mac Type 0-3 = 4D 69 64 69 = ASCII 'Midi' = Macintosh File Type Code for MIDI.
- TIER ID 0x5254 = 'RT' = Custom TIER identification word at DS:DX via INT 48h.
- Diff at 0x0200 = File A has 0x52 ('R'), File B has 0x58 ('X').

### 4. Actual Check - kdp.ximg (Macintosh MIDI Substitute)

File: https://github.com/kaiolafketelhut/index.html/blob/main/kdp.ximg

    Size: 161 bytes
    SHA256: 09aad2cfd9d2e80881bbed17a93c418ee8d99b8756374d4959f8147914214f33
    Header [0-3]: 58 49 4D 47 = 'XIMG'
    Header [4-5]: 01 01 = Version 1.1
    Header [14-15]: 78 9C = zlib header (compressed data)
    Boot Sig [510-511]: file too short -> NOT APPLICABLE
    Mac Type [0-3]: 58494D47 = 'XIMG' (not 'Midi')
    TIER ID 0x5254 ('RT'): NOT FOUND
    Has Midi? NO
    Has MIDI? NO

Conclusion:

- kdp.ximg is a valid XIMG container, not a boot sector, not a raw MIDI file.
- It uses zlib compression (78 9C), so it must be decompressed before hexdiff.
- It is used as Macintosh MIDI substitute: we treat XIMG as the container.

### 5. ERP Results - Verified

    SHA256 timesheet.bin: 245c2a7d8f9403396affbb10c4575be5c1fc74a6ae843fc97da5be04fb
    Employee   Date         In     Out    Total  Overtime Status
    Kai        2026-11-17   08:00  17:30  9.00   1.00     OVERTIME
    Anna       2026-11-17   09:00  18:00  8.50   0.50     OVERTIME
    Total: 17.50h

Commit: ab19ed3 - ERP Suite: Employee work time calc CSV+BIN, 8h/0.5 break/OT, Java+Python

### 6. How To Use

    sha256sum -c timesheet.sha256
    python3 hexdiff.py a.bin b.bin
    python3 erp_time.py timesheet.csv
    python3 erp_time.py timesheet.bin
    java ERPTime timesheet.csv
    xxd kdp.ximg | head -n 10

### 7. Notes / Limitations

- INT 48h + 0x5254 is a custom TIER check, not a standard DOS interrupt.
- 0x55AA only applies to 512-byte boot sectors, not to 161-byte XIMG files.
- kdp.ximg last bytes check with xxd -s -2 fails on Termux (lseek error) - use tail -c 2 | xxd instead.
