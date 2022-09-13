def run_simu(poids, longi, lat):
    return f"cd .\Documents\simu; python bridge_ui.py --long={longi} --lat={lat} --weight={poids}"
    
def run_attack(attack, options):
    if attack == 'dos':
        return f"cd .\Documents\\attaques; python dos.py"
    elif attack == 'deviation':
        return f"cd .\Documents\\attaques; python dos.py"