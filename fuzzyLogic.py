# sistem_fuzzy/fuzzy_logic.py
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def build_fis():
    hb = ctrl.Antecedent(np.arange(10, 20.1, 0.1), 'hb')
    sistolik = ctrl.Antecedent(np.arange(70, 201, 1), 'sistolik')
    tidur = ctrl.Antecedent(np.arange(0, 13, 1), 'tidur')
    kelayakan = ctrl.Consequent(np.arange(0, 101, 1), 'kelayakan')

    # rendah: 10 - 12.0 (turun habis di 12.5)
    hb['rendah'] = fuzz.trapmf(hb.universe, [10.0, 10.0, 11.0, 12.5])
    # normal: naik mulai 12.0, puncak 13-16, turun habis di 17.5
    hb['normal'] = fuzz.trapmf(hb.universe, [12.0, 13.0, 16.0, 17.5])
    # tinggi: naik mulai 17.0, penuh di 18+
    hb['tinggi'] = fuzz.trapmf(hb.universe, [17.0, 18.0, 20.0, 20.0])

    # rendah: < 90 (turun habis di 95)
    sistolik['rendah'] = fuzz.trapmf(sistolik.universe, [70, 70, 85, 95])
    # normal: 95 - 140 (naik mulai 90, turun habis di 145)
    sistolik['normal'] = fuzz.trapmf(sistolik.universe, [90, 100, 130, 145])
    # tinggi: naik mulai 140 (penuh di 160+)
    sistolik['tinggi'] = fuzz.trapmf(sistolik.universe, [140, 160, 200, 200])

    tidur['kurang'] = fuzz.trapmf(tidur.universe, [0, 0, 3, 5])
    tidur['cukup'] = fuzz.trapmf(tidur.universe, [4, 6, 12, 12])

    kelayakan['rendah'] = fuzz.trimf(kelayakan.universe, [0, 0, 40])
    kelayakan['sedang'] = fuzz.trimf(kelayakan.universe, [30, 50, 70])
    kelayakan['tinggi'] = fuzz.trimf(kelayakan.universe, [60, 85, 100])

    rules = [
        ctrl.Rule(hb['normal'] & sistolik['normal'] & tidur['cukup'],  kelayakan['tinggi']),

        # Kondisi sedang — satu parameter kurang optimal
        ctrl.Rule(hb['normal'] & sistolik['normal'] & tidur['kurang'], kelayakan['sedang']),
        ctrl.Rule(hb['normal'] & sistolik['tinggi'] & tidur['cukup'],  kelayakan['sedang']),
        ctrl.Rule(hb['normal'] & sistolik['rendah'] & tidur['cukup'],  kelayakan['sedang']),
        ctrl.Rule(hb['tinggi'] & sistolik['normal'] & tidur['cukup'],  kelayakan['sedang']),

        # Kondisi tidak layak — parameter kritis bermasalah
        ctrl.Rule(hb['rendah'],     kelayakan['rendah']),
        ctrl.Rule(sistolik['rendah'] & tidur['kurang'], kelayakan['rendah']),
        ctrl.Rule(sistolik['tinggi'] & hb['rendah'],   kelayakan['rendah']),
        ctrl.Rule(hb['tinggi'] & sistolik['tinggi'],   kelayakan['rendah']),
        ctrl.Rule(hb['tinggi'] & tidur['kurang'],      kelayakan['rendah']),

        ctrl.Rule(hb['normal'] & sistolik['tinggi'] & tidur['kurang'], kelayakan['rendah']),   
        ctrl.Rule(hb['normal'] & sistolik['rendah'] & tidur['kurang'], kelayakan['sedang']),
        ctrl.Rule(hb['tinggi'] & sistolik['rendah'] & tidur['cukup'],  kelayakan['sedang']),
    ]

    control_system = ctrl.ControlSystem(rules)
    simulation = ctrl.ControlSystemSimulation(control_system)
    return simulation

def evaluasi_fuzzy(input_hb, input_sistolik, input_tidur):
    if not (10 <= input_hb <= 20) or not (70 <= input_sistolik <= 200) or not (0 <= input_tidur <= 12):
        return 0, "Input tidak valid", "text-slate-400"

    sim = build_fis()
    sim.input['hb'] = input_hb
    sim.input['sistolik'] = input_sistolik
    sim.input['tidur'] = input_tidur
    sim.compute()

    score = float(sim.output['kelayakan'])

    if score < 40:
        status = "Tidak Layak"
        warna = "text-red-500"
    elif score < 60:
        status = "Tunda / Periksa Lanjutan"
        warna = "text-yellow-500"
    else:
        status = "Sangat Layak"
        warna = "text-emerald-500"

    return round(score, 1), status, warna