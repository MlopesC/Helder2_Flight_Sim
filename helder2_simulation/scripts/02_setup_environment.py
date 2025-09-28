# scripts/setup_environment.py
"""
Configura ambiente e instala dependencias
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala pacotes necessarios"""
    
    requirements = [
        "rocketpy",
        "matplotlib", 
        "numpy",
        "scipy"
    ]
    
    print("📦 Instalando dependencias...")
    
    for package in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} instalado")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Erro com {package}: {e}")

def verify_environment():
    """Verifica se o ambiente esta pronto"""
    
    print("\n🔍 Verificando ambiente...")
    
    try:
        # Testar imports
        import rocketpy
        import matplotlib.pyplot as plt
        import numpy as np
        
        print("✅ Todas as dependencias importadas com sucesso")
        
        # Verificar arquivos
        required_files = [
            'data/motors/J669.eng',
            'config/rocket_parameters.py'
        ]
        
        for file in required_files:
            if os.path.exists(file):
                print(f"✅ {file} encontrado")
            else:
                print(f"❌ {file} nao encontrado")
                
        return True
        
    except ImportError as e:
        print(f"❌ Erro de importacao: {e}")
        return False

if __name__ == "__main__":
    print("🚀 CONFIGURANDO AMBIENTE HELDER 2")
    print("=" * 50)
    
    install_requirements()
    
    if verify_environment():
        print("\n🎉 Ambiente configurado com sucesso!")
        print("\nProximos passos:")
        print("1. python scripts/create_motor_file.py")
        print("2. python scripts/rocket_simulation.py")
    else:
        print("\n❌ Problemas na configuracao do ambiente")