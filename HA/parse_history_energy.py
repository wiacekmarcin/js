import os

fhistory = "/home/marcin/Pobrane/history.csv"
fname = ".wszystko"





prev = None
sum_taryf1 = 0
sum_taryf2 = 0
with open(fhistory, 'r') as f:
    for l in f.readlines()[1:]:
        chunks = l.split(",")
        if len(chunks) != 3:
            continue
        _, e, d = chunks
        
        if e == 'unavailable' or e == 'unknown' or len(e) == 0:
            continue
        
        ef = float(e)
        if prev is None or prev != ef:
            if prev is None:
                diff = 0.01
            else:
                diff = ef - prev
            
            if diff <= 0:
                continue

            prev = ef
            _, tts = d.split('T')
            h, _, _ = tts.split(':')
            h = int(h)
            if h < 6:
                taryfa2 = True
            elif h < 13:
                taryfa2 = False
            elif h < 15:
                taryfa2 = True
            elif h < 22:
                taryfa2 = False
            else:
                taryfa2 = True
            
            if taryfa2:
                sum_taryf2 += diff
            else:
                sum_taryf1 += diff
print(fname)
print(f"Taryfa 1: {sum_taryf1}")
print(f"Taryfa 2: {sum_taryf2}")

with open(os.path.join('history', fname + '_all_energy.txt'), 'w+') as f:
    f.write("%0.2f\n" % (sum_taryf1 + sum_taryf2))

with open(os.path.join('history', fname + '_all_cost.txt'), 'w+') as f:
    f.write("%f\n" % (1.21*sum_taryf1 + 0.75*sum_taryf2))

with open(os.path.join('history', fname + '_all_cost_g11.txt'), 'w+') as f:
    f.write("%f\n" % (1.15*sum_taryf1 + 1.15*sum_taryf2))

with open(os.path.join('history', fname + '_prev_energy.txt'), 'w+') as f:
    f.write("%0.2f\n" % (prev))

with open(os.path.join('history', fname + '_day_energy.txt'), 'w+') as f:
    f.write("%0.2f\n" % (sum_taryf1))

with open(os.path.join('history', fname + '_day_cost.txt'), 'w+') as f:
    f.write("%f\n" % (1.21* sum_taryf1))    

with open(os.path.join('history', fname + '_night_energy.txt'), 'w+') as f:
    f.write("%0.2f\n" % (sum_taryf2))

with open(os.path.join('history', fname + '_night_cost.txt'), 'w+') as f:
    f.write("%f\n" % (0.75* sum_taryf2))    


