from fuzzyLogic import evaluasi_fuzzy

test_cases = [
    # (hb, sistolik, tidur, label_ekspektasi)
    (14.0, 115, 8,   "Sangat Layak"),
    (14.0, 115, 3,   "Dipertimbangkan"),
    (11.0, 115, 8,   "Tidak Layak"),
    (17.2, 115, 8,   "?? overlap Hb"),
    (14.0, 143, 8,   "?? overlap sistolik"),
    (14.0, 115, 4.5, "?? overlap tidur"),
    (18.0, 170, 8,   "Tidak Layak"),
    (10.0, 70,  0,   "Tidak Layak"),
    (20.0, 200, 12,  "Tidak Layak"),
]

print("=" * 65)
print(f"{'Hb':>5} | {'Sis':>5} | {'Tidur':>5} | {'Score':>6} | {'Status':<25} | Ekspektasi")
print("=" * 65)

for hb, sis, tidur, label in test_cases:
    score, status, _ = evaluasi_fuzzy(hb, sis, tidur)
    print(f"{hb:>5} | {sis:>5} | {tidur:>5} | {score:>6} | {status:<25} | [{label}]")

print("=" * 65)