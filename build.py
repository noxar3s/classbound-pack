# -*- coding: utf-8 -*-
"""Pakuje resource pack do ZIP-a (sciezki z "/", stale daty -> stale sha1) i wypisuje sha1.

Uzycie:  python build.py
"""
import hashlib
import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'ClassBound-ResourcePack.zip')
FIXED_DATE = (2026, 1, 1, 0, 0, 0)

files = ['pack.mcmeta']
for base, _, names in os.walk(os.path.join(ROOT, 'assets')):
    for n in names:
        files.append(os.path.relpath(os.path.join(base, n), ROOT).replace(os.sep, '/'))
files.sort()
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in files:
        info = zipfile.ZipInfo(f, FIXED_DATE)
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, open(os.path.join(ROOT, f), 'rb').read())
print('plikow:', len(files))
print('sha1:', hashlib.sha1(open(OUT, 'rb').read()).hexdigest())
