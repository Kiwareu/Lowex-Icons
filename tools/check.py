#!/usr/bin/env python3
"""检查 icons/ 里的 PNG 是否符合规格（正方形、256 或 512 像素、文件名是已知组 id）。用法：python3 tools/check.py"""
import json, os, struct, sys
ids = {g["id"] for g in json.load(open("mapping.json"))["groups"]}
bad = 0
for f in sorted(os.listdir("icons")):
    if not f.endswith(".png") or f.startswith("_"):
        continue
    with open(os.path.join("icons", f), "rb") as fh:
        h = fh.read(24)
    if h[:8] != b"\x89PNG\r\n\x1a\n":
        print("不是 PNG:", f); bad += 1; continue
    w, hh = struct.unpack(">II", h[16:24])
    if w != hh or w not in (256, 512):
        print(f"尺寸不合规 {w}x{hh}:", f); bad += 1
    if f[:-4] not in ids:
        print("未知组 id:", f); bad += 1
print("OK" if not bad else f"{bad} 个问题")
sys.exit(1 if bad else 0)
