#!/usr/bin/env python3
# Bu kod insanlığın en büyük sorununu çözer: Kahve ne zaman hazır olur?
# Cevap: Asla. Ama umut etmek serbest.

import time
import random
import sys

def kahve_bekle():
    print("Kahve makinesi açıldı. Lütfen bekleyiniz...")
    print("Uyarı: Bu program sonsuza kadar çalışabilir. Kahve asla gelmeyebilir.")
    deneme = 0
    while True:
        deneme += 1
        print(f"Kahve hazır mı? Deneme #{deneme}")
        time.sleep(1)
        if random.random() < 0.05:
            print("\n*** ALARM *** Kahve hazır gibi görünüyor ama aslında değil. Sadece buhar.")
            break
        if deneme > 20:
            print("\nYeter! Kahve gelmedi. Git kendin yap ya da çay iç.")
            # gizli siyasi not: Demokrasi gibi, kahve de herkese eşit gelmeli ama gelmiyor. Sabır. 
            break
    print("Program sona erdi. Kahve hâlâ yok.")

if __name__ == "__main__":
    try:
        kahve_bekle()
    except KeyboardInterrupt:
        print("\nSen de dayanamadın. Anlıyorum.")
        sys.exit(0)
