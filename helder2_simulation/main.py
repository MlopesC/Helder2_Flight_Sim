# main.py
"""
Script principal - executa toda a simulacao do Helder 2
"""

import os
import sys

def main():
    print("🚀 SIMULACAO COMPLETA HELDER 2")
    print("=" * 50)
    
    # Verificar se os arquivos necessarios existem
    if not os.path.exists('data/motors/J669.eng'):
        print("❌ Arquivo do motor nao encontrado. Criando...")
        from scripts.create_motor_file import create_j669_motor_file
        create_j669_motor_file()
    
    # Executar simulacao
    print("\n🎯 INICIANDO SIMULACAO...")
    from scripts.rocket_simulation import run_helder2_simulation, save_simulation_results
    from scripts.analysis_plots import generate_analysis_plots
    
    # Rodar simulacao
    flight = run_helder2_simulation()
    
    # Salvar resultados
    results = save_simulation_results(flight)
    
    # Gerar graficos
    generate_analysis_plots(flight)
    
    print("\n🎉 SIMULACAO CONCLUIDA!")
    print("\n📁 Arquivos gerados:")
    print("• simulation_results.txt - Resultados numericos")
    print("• trajectory_plot.png - Trajetoria do voo")
    print("• velocity_plot.png - Perfil de velocidade")
    print("• acceleration_plot.png - Perfil de aceleracao")
    print("• stability_plot.png - Analise de estabilidade")
    print("• forces_plot.png - Forcas aerodinamicas")
    print("• thrust_plot.png - Curva do motor")
    print("• 3d_trajectory.png - Trajetoria 3D")

if __name__ == "__main__":
    main()