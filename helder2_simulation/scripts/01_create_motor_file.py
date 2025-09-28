# scripts/create_motor_file.py
"""
Cria arquivo de motor J669 baseado nos dados fornecidos
"""

import os

def create_j669_motor_file():
    """Cria arquivo .eng do motor J669"""
    
    motor_data = """J669 50.58 629.0 P 0.918073 1.956073 marcosbraz
0 0.01
0.03 545.8374
0.06 553.5249
0.09 561.0699
0.12 568.4724
0.15 575.7326
0.18 582.8507
0.21 589.8268
0.24 596.6611
0.27 603.3538
0.3 609.905
0.33 616.3148
0.36 622.5834
0.39 628.7109
0.42 634.6974
0.45 640.543
0.48 646.2479
0.51 651.8122
0.54 657.236
0.57 662.5193
0.6 667.6624
0.63 672.6652
0.66 677.5279
0.69 682.2506
0.72 686.8333
0.75 691.2761
0.78 697.3093
0.81 706.2531
0.84 714.9918
0.87 723.5151
0.9 731.8127
0.93 739.8744
0.96 747.6903
0.99 755.2506
1.02 762.5458
1.05 769.5666
1.08 776.3038
1.11 782.7486
1.14 788.8926
1.17 794.7276
1.2 800.2457
1.23 805.4394
1.26 810.3017
1.29 814.8259
1.32 819.0056
1.35 822.8351
1.38 826.309
1.41 829.4222
1.44 832.1705
1.47 0.0
"""
    
    # Criar diretorio se nao existir
    os.makedirs('data/motors', exist_ok=True)
    
    # Escrever arquivo
    with open('data/motors/J669.eng', 'w') as f:
        f.write(motor_data)
    
    print("✅ Arquivo J669.eng criado em data/motors/")
    print("📊 Dados do motor: 629.0 Ns total impulse, 1.47s burn time")

if __name__ == "__main__":
    create_j669_motor_file()