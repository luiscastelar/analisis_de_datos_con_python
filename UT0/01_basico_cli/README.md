# Ejemplo sencillo

1. Integración del script `hola_mundo.py` **dentro** de la imágen
    - Ventajas:
	    - distribución simplificada de la aplicación.
	- Inconvenientes:
        - modificaciones del mismo requieren reconstruir la imagen.
	    - aumento de tamaño.
2. Ejecución del shell por defecto `/bin/sh` en el _entrypoint_ implícito.
3. Lanzamiento del comando `python hola_mundo.py` con el _CMD_ en formato array de argumentos.
4. Ejecución sencilla del contenedor.
