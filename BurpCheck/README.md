# TIER Software Integration Project
## ERP Suite - Employee Work Time Calculation

Repo: `kaiolafketelhut/improved-octo-adventure` - Branch: `main`

### What is this?

1. **Verify binary files** with hexdiff - Boot Sig, Mac Type, TIER RT
2. **Calculate employee work time** - 8.0h normal, 0.5h break if >6h, Overtime after 8h
3. **Macintosh MIDI substitute** - `kdp.ximg` as XIMG container

### Files - Start Here

| File | What is it? | How to use? |
| --- | --- | --- |
| `README.md` | This file | Read first |
| `summary.md` | Full summary + BOM | Read for details |
| `BOM.csv` | Bill of Materials | Open in Excel / ERP import |
| `summary.pdf` | PDF version of summary | Send / print / archive |
| `oneyepdf.c` | Makes the PDF in pure C | `gcc oneyepdf.c -o oneyepdf && ./oneyepdf` |
| `hexdiff.py` | Hexdiff + signature checks | `python3 hexdiff.py a.bin b.bin` |
| `erp_time.py` | ERP calc Python | `python3 erp_time.py timesheet.csv` |
| `ERPTime.java` | ERP calc Java | `java ERPTime timesheet.csv` |
| `Main.java` | MAIN.JAR hash checker | Original BurpCheck |
| `kdp.ximg` | Mac MIDI substitute | 161 bytes, XIMG + zlib |
| `timesheet.csv` / `timesheet.bin` | Test timesheets | Test data for ERP |

### Reference Checks - Test Files a.bin / b.bin

    Boot Sig [510-511]: 55AA -> OK 0x55AA
    Mac Type [0-3]: 4D696469 = 'Midi'
    TIER ID 0x5254 ('RT'): FOUND at offset 512
    0x0200   52             58             <-- DIFF

- Boot Sig `55 AA` = Bootable sector signature
- Mac Type `4D 69 64 69` = 'Midi' = Macintosh File Type Code
- TIER ID `0x5254` = 'RT' = Custom TIER word via INT 48h
- Diff at `0x0200` = File A `0x52` ('R') vs File B `0x58` ('X')

### Actual Check - kdp.ximg

    Size: 161 bytes
    SHA256: 09aad2cfd9d2e80881bbed17a93c418ee8d99b8756374d4959f8147914214f33
    Header [0-3]: 58 49 4D 47 = 'XIMG'
    Header [4-5]: 01 01 = Version 1.1
    Header [14-15]: 78 9C = zlib header
    Boot Sig [510-511]: file too short -> NOT APPLICABLE
    Mac Type: XIMG (not Midi) | TIER RT: NOT FOUND

Conclusion: Valid XIMG container, not a boot sector, not a raw MIDI file.

### ERP Results - Verified

    Kai   2026-11-17  08:00  17:30  9.00h  1.00h OT  OVERTIME
    Anna  2026-11-17  09:00  18:00  8.50h  0.50h OT  OVERTIME
    Total: 17.50h

### How To Use

    # 1. Build PDF from C (no Python lib needed)
    gcc oneyepdf.c -o oneyepdf
    ./oneyepdf
    ls -lh summary.pdf

