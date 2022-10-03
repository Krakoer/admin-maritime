def run_simu(poids, longi, lat):
    #return f"cd .\Documents\simu; python bridge_ui.py" # --long={longi} --lat={lat} --weight={poids}"
    return f"cd C:\\Users\\Jean\\Documents\\simu; python.exe bridge_ui.py"

def run_attack(attack, options):
    if attack == 'dos':
        return f""
        #return f"cd .\Documents\\attaques; python dos.py"
    elif attack == 'deviation':
        return f"cd C:\\Users\\Jean\\Documents; python.exe sniffer.py"

def run_others(cmd, options):
    if cmd == "reset_TZ":
        return f"cd C:\\Users\\Jean\\Documents; ./reset"
    elif cmd == "start_TZ":
        return f"cd \"C:\\Program Files (x86)\\TimeZero\\Recreational\"; ./TimeZeroService.exe"
