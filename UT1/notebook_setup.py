# Configuración inicial del cuaderno
# ----------------------------------
# TDD
import ipytest, pytest
ipytest.autoconfig()
#ipytest.autoconfig(addopts=('-rA', '--tb=short'))
# Limpieza de namespace: Jupyter conserva variables globales en memoria. Si notas que tests viejos se están reejecutando inesperadamente ejecuta 
ipytest.clean()
