## 1. El Flujo de Trabajo en el Análisis de Datos (Data Analysis Workflow)

### 1.1. Por qué necesitamos un flujo estructurado

El análisis de datos en la industria actual va mucho más allá de ejecutar consultas esporádicas o aplicar scripts aislados. Al abordar un problema real, nos enfrentamos a volúmenes masivos de información heterogénea y frecuentemente incompleta o errónea. Adoptar un **flujo de trabajo estructurado (*Data Analysis Workflow*)** aporta tres beneficios clave:

1. **Sistemática y Reducción de Errores:** Define una secuencia clara de pasos que minimiza la omisión de validaciones críticas (como la detección de nulos o el filtrado de valores atípicos).
2. **Repetibilidad (*Reproducibility*):** Permite que cualquier miembro del equipo (o un pipeline automatizado) ejecute las mismas transformaciones sobre datos futuros y obtenga resultados consistentes.
3. **Escalabilidad:** Facilita la transición desde prototipos analíticos locales hacia entornos de producción en la nube o arquitecturas *Big Data*.


### 1.2. Etapas del ciclo de vida del dato

Aunque existen metodologías estándar como [CRISP-DM](https://www.ibm.com/docs/es/spss-modeler/saas?topic=dm-crisp-help-overview), en el contexto del desarrollo de software con Python se adopta una aproximación iterativa e interactiva basada en 5 fases principales:

![diagrama](https://files.realpython.com/media/ie-data-analysis-workflowv3.bfb835b95c5e.png)

| Fase | Descripción | Salida/Entregable |
| --- | --- | --- |
| **1. Objetivos** | Definición de las preguntas clave y métricas de éxito. | Documento de requisitos / KIPs |
| **2. Adquisición** | Lectura e ingesta de datos (*CSV, JSON, SQL, APIs*). | Raw Dataset (inmutable) |
| **3. Limpieza** | Corrección de tipos, imprecisos, atípicos y nulos. | Cleaned Dataset / Data Lake |
| **4. Análisis** | Exploración de patrones, agrupaciones y correlaciones. | Gráficos, métricas y modelos |
| **5. Comunicación** | Informes visuales o despliegue de dashboards/APIs. | Reporte final / API REST |

!!!NOTE
    La naturaleza del proceso es **iterativa** (líneas discontinuas del diagrama). Durante la fase de análisis es habitual descubrir anomalías que obligan a regresar a la fase de limpieza o a reformular preguntas en la fase de objetivos.

### 1.3. Definición de Objetivos: Preguntas de negocio vs. Exploración abierta

Antes de escribir una sola línea de código en Python, es imprescindible definir el alcance. La falta de objetivos claros conduce a análisis dispersos (*parálisis por análisis*).

* **Exploración Abierta:** "Vamos a ver qué datos hay en el archivo `james_bond_data.csv`." (Útil para un primer contacto, pero ineficiente para tomar decisiones).
* **Preguntas de Negocio Concretas:**
1. ¿Existe correlación directa entre el presupuesto (*Budget*) y la recaudación global (*World Gross*)?
2. ¿El cambio de actor protagonista influye en las puntuaciones medias de la audiencia (*IMDb* vs *Rotten Tomatoes*)?
3. ¿Se pueden corregir los incoherencias tipográficas en las fechas de estreno antes de procesar la rentabilidad histórica?



### 1.4. Entorno de trabajo práctico: Jupyter Notebooks `.ipynb` vs Scripts `.py`

Para el análisis exploratorio de datos, el estándar industrial es el entorno de cuadernos interactivos (**Jupyter Notebooks / JupyterLab**).

#### ¿Por qué Jupyter para el análisis de datos?

* **REPL extendido:** Permite ejecutar celdas de código de manera independiente sin recargar todo el dataset en memoria.
* **Prototipado rápido:** Inspección inmediata del estado de los `DataFrames` de pandas mediante tablas formateadas en HTML.
* **Integración narrativa:** Combina explicaciones en Markdown, ecuaciones LaTeX, código ejecutable y gráficos intercalados en un solo documento (`.ipynb`).

[Continuar](2_intro_ecosistema_python.ipynb)