# REA First Analysis - Bluh Edition
Date: 2026-11-15 | Method: file + strings + sha256sum

## File 1: test-main-fnt.js
- Type: ASCII text, 185 bytes
- SHA256: cc2bc8d0bd64fcdbca7a9527e1149aa2f03e10499e871b45f58053764dfea8c8
- Functions: calcReNo(hours, rate), checkFAT(path)
- Finding: ReNo calc + FAT check in 3 lines. DIY as Promotion in miniature.

## File 2: website/public/showcase/ctf/solve.py
- Type: Python script, ASCII, executable, 3559 bytes
- SHA256: 9f691d1ea7470195c4ce0fb630c7a10155c3f75c3b0f066e02b22314ce542fe9
- Finding: REA showcase CTF solver. Evidence without execution.

## REA Principle Proven
1. file = What is it?
2. strings = What is inside without running it?
3. sha256sum = Proof / Audit Trail / FAT Obligation
