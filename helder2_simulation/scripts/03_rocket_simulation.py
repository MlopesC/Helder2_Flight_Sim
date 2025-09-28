# scripts/rocket_simulation.py
"""
Simulacao principal do foguete Helder 2
"""

import sys
import os

# Adicionar o diretorio pai ao path para importar config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rocketpy import Rocket, SolidMotor, Flight, Environment
import matplotlib.pyplot as plt

# Importar configuracoes
try:
    from config.rocket_parameters import *
except ImportError:
    # Configuracoes padrao caso o arquivo nao exista
    ROCKET_PARAMS = {'mass': 5.220, 'radius': 0.055}
    COMPONENTS = {'motor': {'mass': 0.990}, 'recovery': {'diameter': 0.916, 'cd': 2.2}}
    STABILITY_PARAMS = {'cg_position': 1.66}
    AERO_PARAMS = {'fin_root_chord': 0.18, 'fin_tip_chord': 0.10, 'fin_span': 0.12}
    LAUNCH_PARAMS = {'rail_length': 3.0, 'inclination': 85, 'latitude': -28.6, 'longitude': -48.0}

def run_helder2_simulation():
    """Executa simulacao completa do Helder 2"""
    
    print("🚀 SIMULACAO HELDER 2")
    print("=" * 50)
    
    # 1. CONFIGURAR AMBIENTE
    print("1. Configurando ambiente...")
    env = Environment(
        latitude=LAUNCH_PARAMS['latitude'],
        longitude=LAUNCH_PARAMS['longitude']
    )
    env.set_date((2024, 1, 1, 9, 0, 0))  # Data exemplo
    env.set_atmospheric_model(type='standard_atmosphere')
    
    # 2. CONFIGURAR MOTOR J669
    print("2. Configurando motor J669...")
    motor = SolidMotor(
        thrust_source="data/motors/J669.eng",
        dry_mass=COMPONENTS['motor']['mass'],
        dry_inertia=(0.150, 0.150, 0.003),
        nozzle_radius=0.0254,  # 50.8mm / 2000
        grain_number=1,
        grain_density=1700,
        grain_outer_radius=0.024,
        grain_initial_inner_radius=0.008,
        grain_initial_height=0.35,
        center_of_dry_mass_position=0.2,
        nozzle_position=0,
        burn_time=1.47
    )
    
    # 3. CONFIGURAR FOGUETE
    print("3. Configurando foguete...")
    rocket = Rocket(
        radius=ROCKET_PARAMS['radius'],
        mass=ROCKET_PARAMS['mass'],
        inertia=(8.0, 8.0, 0.05),
        center_of_mass_without_motor=STABILITY_PARAMS['cg_position'],
        power_off_drag=None  # Usaremos dados padrao do RocketPy
    )
    
    # Adicionar motor
    rocket.add_motor(motor, position=-0.2)
    
    # 4. CONFIGURAR AERODINAMICA
    print("4. Configurando aerodinamica...")
    
    # Nariz Haack
    rocket.add_nose(
        length=0.15,  # 15cm do PDF
        kind="von karman",
        position=2.15  # Posicao estimada
    )
    
    # Aletas trapezoidais
    rocket.add_trapezoidal_fins(
        n=4,
        root_chord=AERO_PARAMS['fin_root_chord'],
        tip_chord=AERO_PARAMS['fin_tip_chord'],
        span=AERO_PARAMS['fin_span'],
        position=0,
        airfoil=("linear", 0.001)
    )
    
    # 5. CONFIGURAR RECUPERACAO
    print("5. Configurando sistema de recuperacao...")
    main_chute = rocket.add_parachute(
        name="Main Parachute",
        cd_s=COMPONENTS['recovery']['cd'] * (3.1416 * (COMPONENTS['recovery']['diameter']/2)**2),
        trigger=800,  # Acionamento a 800m
        sampling_rate=105,
        lag=1.5
    )
    
    # 6. EXECUTAR SIMULACAO
    print("6. Executando simulacao...")
    flight = Flight(
        rocket=rocket,
        environment=env,
        rail_length=LAUNCH_PARAMS['rail_length'],
        inclination=LAUNCH_PARAMS['inclination'],
        heading=0,
        terminate_on_apogee=True,
        verbose=True
    )
    
    return flight

def save_simulation_results(flight):
    """Salva resultados da simulacao"""
    
    print("\n💾 SALVANDO RESULTADOS...")
    
    results = {
        'apogee': flight.apogee,
        'max_velocity': flight.max_speed,
        'max_mach': flight.max_mach_number,
        'max_acceleration': flight.max_acceleration,
        'apogee_time': flight.apogee_time,
        'flight_time': flight.t_final
    }
    
    # Salvar resultados em arquivo
    with open('simulation_results.txt', 'w') as f:
        f.write("RESULTADOS DA SIMULACAO HELDER 2\n")
        f.write("=" * 40 + "\n")
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
    
    print("✅ Resultados salvos em simulation_results.txt")
    return results

if __name__ == "__main__":
    flight = run_helder2_simulation()
    results = save_simulation_results(flight)
    
    print("\n📊 RESULTADOS:")
    for key, value in results.items():
        print(f"{key}: {value}")