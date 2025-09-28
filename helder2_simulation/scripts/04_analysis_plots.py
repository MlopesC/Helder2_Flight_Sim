# scripts/analysis_plots.py
"""
Gera graficos de analise da simulacao
"""

import sys
import os
import matplotlib.pyplot as plt

# Adicionar o diretorio pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_analysis_plots(flight):
    """Gera todos os graficos de analise"""
    
    print("\n📈 GERANDO GRAFICOS DE ANALISE...")
    
    try:
        # 1. Trajetoria
        print("• Trajetoria do voo")
        fig1 = flight.plot_trajectory()
        plt.title('Helder 2 - Trajetoria de Voo')
        plt.savefig('trajectory_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 2. Velocidade
        print("• Perfil de velocidade")
        fig2 = flight.plot_velocity()
        plt.title('Helder 2 - Velocidade vs Tempo')
        plt.savefig('velocity_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 3. Aceleracao
        print("• Perfil de aceleracao")
        fig3 = flight.plot_acceleration()
        plt.title('Helder 2 - Aceleracao vs Tempo')
        plt.savefig('acceleration_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 4. Estabilidade
        print("• Analise de estabilidade")
        fig4 = flight.plot_stability()
        plt.title('Helder 2 - Margem de Estabilidade')
        plt.savefig('stability_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 5. Forcas aerodinamicas
        print("• Forcas aerodinamicas")
        fig5 = flight.plot_forces()
        plt.title('Helder 2 - Forcas Aerodinamicas')
        plt.savefig('forces_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 6. Desempenho do motor
        print("• Curva de empuxo do motor")
        fig6 = flight.plot_thrust()
        plt.title('Helder 2 - Curva de Empuxo do Motor J669')
        plt.savefig('thrust_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # 7. Trajetoria 3D
        print("• Trajetoria 3D")
        fig7 = flight.plot_3d_trajectory()
        plt.title('Helder 2 - Trajetoria 3D')
        plt.savefig('3d_trajectory.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Todos os graficos gerados e salvos!")
        
    except Exception as e:
        print(f"⚠️ Erro ao gerar graficos: {e}")

if __name__ == "__main__":
    # Este script deve ser executado apos a simulacao principal
    print("Execute primeiro: python scripts/rocket_simulation.py")