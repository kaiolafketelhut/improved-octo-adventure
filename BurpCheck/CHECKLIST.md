# TIER Project - CHECKLIST.md
## Use this for every new project - same style as BurpCheck / ERP Suite

### 1. Project Setup

- [x] Create repo: `kaiolafketelhut/improved-octo-adventure`
- [x] Branch: `main`
- [x] Folder: `BurpCheck/`
- [x] Create `.gitignore` - ignore `*.jar`, `*.class`, `bin/`, `obj/`
- [ ] Clone on new device: `git clone https://github.com/kaiolafketelhut/improved-octo-adventure.git`

### 2. Code Files

- [x] `Main.java` - MAIN.JAR hash checker
- [x] `hexdiff.py` - Hexdiff + signature checks
- [x] `erp_time.py` - ERP calc Python
- [x] `ERPTime.java` - ERP calc Java
- [x] `oneyepdf.c` - PDF maker in pure C
- [ ] Test each file: `python3 <file>.py` / `java <file>` / `gcc <file>.c -o <file>`

### 3. Binary Checks - hexdiff

- [x] Boot Sig [510-511]: `55AA` -> OK `0x55AA`
- [x] Mac Type [0-3]: `4D696469` = `'Midi'`
- [x] TIER ID `0x5254` ('RT'): FOUND at offset 512
- [x] Diff at `0x0200`: `52` vs `58` <-- DIFF
- [ ] Run: `python3 hexdiff.py a.bin b.bin`
- [ ] Check size: `ls -lh <file>` / `wc -c <file>`
- [ ] Check hash: `sha256sum <file>`
- [ ] Check header: `xxd <file> | head -n 10`

### 4. kdp.ximg Check - Mac MIDI Substitute

- [x] Size: 161 bytes
- [x] SHA256: `09aad2cfd9d2e80881bbed17a93c418ee8d99b8756374d4959f8147914214f33`
- [x] Header [0-3]: `58 49 4D 47` = `'XIMG'`
- [x] Header [4-5]: `01 01` = Version 1.1
- [x] Header [14-15]: `78 9C` = zlib header
- [x] Boot Sig: file too short -> NOT APPLICABLE
- [x] Mac Type: XIMG (not Midi) | TIER RT: NOT FOUND
- [ ] Conclusion: Valid XIMG container, not boot sector, not raw MIDI

### 5. ERP - Work Time Calculation

- [x] Rules: 8.0h normal, 0.5h break if >6h, Overtime after 8h
- [x] Test CSV: `python3 erp_time.py timesheet.csv`
- [x] Test BIN: `python3 erp_time.py timesheet.bin`
- [x] Test Java: `java ERPTime timesheet.csv`
- [x] Result: Kai 9.00h / 1.00h OT, Anna 8.50h / 0.50h OT, Total 17.50h
- [ ] Check new timesheet with same commands

### 6. Documentation - BOM

- [x] `summary.md` - Full summary + BOM table
- [x] `BOM.csv` - Bill of Materials for Excel / ERP import
- [x] `summary.pdf` - PDF version, made by C
- [x] `README.md` - Links all files, shows on GitHub top
- [x] `CHECKLIST.md` - This file
- [ ] Check formatting: no nested ``` inside ```, tables have `| --- |`
- [ ] Check SHA256 has no space in middle

### 7. PDF with oneyepdf.c - Pure C, No Python Lib

- [x] Create `oneyepdf.c`
- [x] Compile: `gcc oneyepdf.c -o oneyepdf`
- [x] Run: `./oneyepdf`
- [x] Check: `Saved summary.pdf with oneyepdf.c - OK`
- [x] Check size: `ls -lh summary.pdf` - must be ~3.4K
- [x] Check header: `head -c 20 summary.pdf` - must show `%PDF-1.4`
- [x] Check text: `strings summary.pdf | head` - must show TIER, Kai, Anna

### 8. Git Push

- [x] `git add <files>`
- [x] `git commit -m "Clear message"`
- [x] `git push origin main`
- [x] Check output: `main -> main`
- [ ] Check on GitHub: `https://github.com/kaiolafketelhut/improved-octo-adventure/tree/main/BurpCheck`

### 9. Final Verification - Before You Say Done

- [x] README shows on GitHub?
- [x] summary.md table renders?
- [x] BOM.csv opens in Excel?
- [x] summary.pdf opens and shows TIER text?
- [x] All commits pushed? Latest: `14a8110`
- [ ] New commit for CHECKLIST.md pushed?

### Commits - This Project

- `ab19ed3` - ERP Suite
- `6dc1f9f` - Fix summary.md formatting
- `ab31799` - Add oneyepdf.c + summary.pdf
- `14a8110` - Add README.md
- Next: `CHECKLIST.md` - Add checklist

### Quick Commands - Copy For Next Project

    cd ~/improved-octo-adventure/BurpCheck
    gcc oneyepdf.c -o oneyepdf && ./oneyepdf
    python3 hexdiff.py a.bin b.bin
    python3 erp_time.py timesheet.csv
    sha256sum kdp.ximg
    git add . && git commit -m "Update" && git push origin main

