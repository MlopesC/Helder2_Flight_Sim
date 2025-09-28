# config/rocket_parameters.py
"""
Parâmetros do foguete Helder 2 baseados no PDF
"""

# =============================================================================
# DIMENSÕES GERAIS
# =============================================================================
ROCKET_PARAMS = {
    'name': 'Helder 2',
    'mass': 5.220,  # kg (com motor)
    'radius': 0.055,  # m (11cm diâmetro / 2)
    'length': 2.30,  # m (estimado baseado nos componentes)
}

# =============================================================================
# COMPONENTES E MASSA
# =============================================================================
COMPONENTS = {
    'nose_cone': {
        'mass': 0.124,  # kg
        'length': 0.15,  # m
        'material': 'PLA',
        'type': 'haack'
    },
    'body_tube': {
        'mass': 1.400,  # kg
        'length': 2.10,  # m
        'material': 'fiberglass'
    },
    'fins': {
        'mass': 0.260,  # kg
        'count': 4,
        'material': 'PLA',
        'type': 'trapezoidal'
    },
    'motor': {
        'mass': 1.990,  # kg (J681) - usando J669 com massa similar
        'length': 0.58,  # m
        'diameter': 0.0508  # m
    },
    'recovery': {
        'parachute_mass': 0.256,  # kg
        'diameter': 0.916,  # m
        'cd': 1.475
    }
}

# =============================================================================
# CENTRO DE MASSA E ESTABILIDADE
# =============================================================================
STABILITY_PARAMS = {
    'cg_position': 1.66,  # m da base
    'cp_position': 2.00,  # m da base  
    'static_margin': 0.15,  # 15%
    'caliber_stability': 3.13  # cal
}

# =============================================================================
# PARÂMETROS AERODINÂMICOS
# =============================================================================
AERO_PARAMS = {
    'fin_root_chord': 0.18,  # m (estimado)
    'fin_tip_chord': 0.10,   # m (estimado) 
    'fin_span': 0.176,        # m (estimado)
    'fin_sweep_length': 0.03, # m (estimado)
}

# =============================================================================
# PARÂMETROS DE LANÇAMENTO
# =============================================================================
LAUNCH_PARAMS = {
    'rail_length': 4.0,     # m
    'inclination': 85,      # graus
    'heading': 0,           # graus
    'latitude': -21.916667,      # LASC - Tatuí
    'longitude': -48.968000
}