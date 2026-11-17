#!/usr/bin/env python3
import csv, sys, hashlib
from datetime import datetime, timedelta

NORMAL = 8.0
BREAK = 0.5

def calc_one(emp, date, clock_in, clock_out):
    t_in = datetime.strptime(f"{date} {clock_in}", "%Y-%m-%d %H:%M")
    t_out = datetime.strptime(f"{date} {clock_out}", "%Y-%m-%d %H:%M")
    if t_out < t_in:
        t_out += timedelta(days=1)
    hours = (t_out - t_in).total_seconds() / 3600
    if hours > 6:
        hours -= BREAK
    overtime = max(0, hours - NORMAL)
    status = "OVERTIME" if overtime > 0 else ("OK" if hours >= 8 else "UNDER-TIME")
    print(f"{emp:<12} {date:<12} {clock_in:<6} {clock_out:<6} {hours:<6.2f} {overtime:<8.2f} {status}")
    return hours

def from_csv(path):
    print(f"--- ERP Report CSV: {path} ---")
    print(f"{'Employee':<12} {'Date':<12} {'In':<6} {'Out':<6} {'Total':<6} {'Overtime':<8} {'Status'}")
    total = 0
    with open(path) as f:
        for row in csv.DictReader(f):
            total += calc_one(row['employee'], row['date'], row['clock_in'], row['clock_out'])
    print(f"\nTotal: {total:.2f}h")

def from_bin(path):
    # Fingerprint machine format for your TIER project:
    # Each record = 32 bytes: [EmpID 10 bytes][Date 10 bytes YYYY-MM-DD][In 5 bytes HH:MM][Out 5 bytes HH:MM][2 bytes 55 AA]
    print(f"--- ERP Report BIN: {path} ---")
    print(f"{'Employee':<12} {'Date':<12} {'In':<6} {'Out':<6} {'Total':<6} {'Overtime':<8} {'Status'}")
    total = 0
    data = open(path,'rb').read()
    for i in range(0, len(data), 32):
        chunk = data[i:i+32]
        if len(chunk) < 32: break
        # Check boot signature style 55 AA at end of record
        if chunk[30:32] != b'\x55\xaa':
            print(f"Record {i//32} CORRUPT - no 55AA")
            continue
        emp = chunk[0:10].decode().strip('\x00 ')
        date = chunk[10:20].decode().strip('\x00 ')
        cin = chunk[20:25].decode().strip('\x00 ')
        cout = chunk[25:30].decode().strip('\x00 ')
        total += calc_one(emp, date, cin, cout)
    print(f"\nTotal: {total:.2f}h")

def check_hash(path):
    h = hashlib.sha256(open(path,'rb').read()).hexdigest()
    print(f"SHA256 {path}: {h}")

if __name__ == "__main__":
    p = sys.argv[1]
    check_hash(p)
    if p.endswith('.csv'):
        from_csv(p)
    else:
        from_bin(p)
