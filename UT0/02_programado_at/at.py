#!/usr/bin/env python3
import os
import sched
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo  # Módulo nativo en Python 3.9+


def ejecutar_cadena_scripts(scripts):
    """Ejecuta los scripts secuencialmente. Se detiene si alguno falla (exit status != 0)."""
    # Obtenemos la hora actual respetando Europe/Madrid
    zona_madrid = ZoneInfo("Europe/Madrid")
    ahora_str = datetime.now(zona_madrid).strftime("%H:%M:%S")
    print(f"\n[{ahora_str}] Iniciando secuencia de scripts...")
    
    for script in scripts:
        print(f"\n---> Ejecutando: {script}")
        
        if not os.path.exists(script):
            print(f"Error: El archivo '{script}' no existe. Abortando secuencia.")
            sys.exit(1)
            
        resultado = subprocess.run([sys.executable, script])
        
        if resultado.returncode != 0:
            print(
                f"\n[ERROR] '{script}' terminó con código {resultado.returncode}. "
                "Cancelando la ejecución de los scripts restantes."
            )
            sys.exit(resultado.returncode)
            
        print(f"[ÉXITO] '{script}' finalizó correctamente (exit 0).")

    print(f"\n[{datetime.now(zona_madrid).strftime('%H:%M:%S')}] Todos los scripts se ejecutaron con éxito.")


def main():
    if len(sys.argv) < 3:
        print("Uso: python at.py HHMM script1.py [script2.py script3.py ...]")
        print("Ejemplo: python at.py 0726 paso1.py paso2.py paso3.py")
        sys.exit(1)

    hora_raw = sys.argv[1]
    scripts = sys.argv[2:]

    # 1. Validar formato HHMM
    if len(hora_raw) != 4 or not hora_raw.isdigit():
        print("Error: El formato de hora debe ser de 4 dígitos HHMM (ejemplo: '0726').")
        sys.exit(1)

    # 2. Validar que los archivos existan
    for script in scripts:
        if not os.path.exists(script):
            print(f"Error: El archivo '{script}' no existe.")
            sys.exit(1)

    # 3. Parsear hora objetivo
    horas = int(hora_raw[:2])
    minutos = int(hora_raw[2:])

    if horas > 23 or minutos > 59:
        print("Error: Hora inválida. Las horas van de 00-23 y minutos de 00-59.")
        sys.exit(1)

    # Define explícitamente la zona horaria Madrid (CET/CEST)
    zona_madrid = ZoneInfo("Europe/Madrid")
    
    # Obtenemos la hora actual EN MADRID
    ahora_madrid = datetime.now(zona_madrid)

    # Creamos la hora objetivo fijándola en Madrid
    hora_objetivo = ahora_madrid.replace(
        hour=horas,
        minute=minutos,
        second=0,
        microsecond=0
    )

    # Calcular delay (la diferencia entre dos datetimes con la misma timezone es exacta)
    delay = (hora_objetivo - ahora_madrid).total_seconds()

    if delay < 0:
        print(f"Error: La hora {hora_raw[:2]}:{hora_raw[2:]} ya ha pasado hoy en hora local (Europe/Madrid).")
        sys.exit(1)

    # 4. Mostrar información de depuración
    print(f"Hora actual (Madrid)   : {ahora_madrid.strftime('%H:%M:%S %Z')}")
    print(f"Hora de ejecución      : {hora_objetivo.strftime('%H:%M:%S %Z')}")
    print(f"Scripts en cola ({len(scripts)}): {', '.join(scripts)}")
    print(f"Esperando {int(delay)} segundos ({int(delay // 60)} min)...")

    # Usamos time.monotonic para evitar que el scheduler sufra descompensaciones por NTP
    scheduler = sched.scheduler(time.monotonic, time.sleep)
    scheduler.enter(delay, 1, ejecutar_cadena_scripts, argument=(scripts,))

    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("\nEjecución cancelada por el usuario.")


if __name__ == "__main__":
    main()
