# T1. Captura, limpieza y normalización de datos

## 0. Requisitos
Trabajaremos con cuadernos Jupyter y necesitamos importar:
- `numpy` para el trabajo con arrays
- `pandas` para las `Series` y `DataFrames`
- `json` para la manipulación de archivos Json
- `pyarrow` para la manipulación de archivos Parquet 
- `openpyxl` para Excel

## 1. El Flujo de Trabajo en el Análisis de Datos (Data Analysis Workflow)

[Desarrollo](1_flujo_de_trabajo.md)

## 2. Introducción al ecosistema de datos en Python

[Desarrollo](2_intro_ecosistema_python.ipynb)

## 3. NumPy

[Desarrollo](3_NumPy.ipynb)

## 4. Captura de datos desde CSV

[Desarrollo](4_Captura_desde_csv.ipynb)

## 5. Pandas

[Desarrollo](5_Pandas.ipynb)

## 6. Captura de datos desde JSON, Parquet y Excel

[Desarrollo](6_Captura_desde_json_y_parquet.ipynb)

## 7. Limpieza de datos

[Desarrollo](7_Limpieza_de_datos.ipynb)

## 8. Tabla Resumen de Cobertura (RA1)

| Criterio de Evaluación (C.E.) | Descripción del Criterio | Actividades / Ejercicios del Cuaderno |
| :--- | :--- | :--- |
| **CE1.a** | Se conocen y se importan las librerías usadas en ciencia de datos (NumPy, Pandas, PyArrow). | Teoría UT1.2, UT1.3, UT1.5, UT1.6 + Todos los ejercicios (importación explícita). |
| **CE1.b** | Se ha escrito código que permite leer datos de distintos orígenes (CSV, JSON, Parquet). | Ejemplo Guiado (UT1.4), Ejercicio 1.2 (UT1.4), Ejercicios 1.1, 1.2 y 1.4 (UT1.6), Ejercicio 1.3 (UT1.7). |
| **CE1.c** | Se ha escrito código que permite exportar datos procesados (CSV, JSON, Parquet). | Ejemplo Guiado (UT1.4), Ejercicio 1.2 (UT1.4), Ejercicios 1.2 y 1.3 (UT1.6). |
| **CE1.d** | Se han analizado los datos leídos (inspección, agregaciones, estadísticas). | Ejercicio 3.3.6 (UT1.3), Ejercicios 1.1–1.3 (UT1.5). |
| **CE1.e** | Se han aplicado operaciones de normalización y estandarización. | Ejercicios 3.3.3 y 3.3.4 (UT1.3), Ejercicio 1.3 (UT1.7). |
| **CE1.f** | Se ha escrito código para limpiar datos (nulos, outliers, tipos, cadenas, fechas). | Ejercicio 3.3.5 (UT1.3), Ejercicios 1.1, 1.2 y 1.3 (UT1.7). |



## Fuentes:
- De consulta:
    - "Libro" [Elements of Data Science](https://allendowney.github.io/ElementsOfDataScience/index.html)
        - [`NumPy` Arrays](https://allendowney.github.io/ElementsOfDataScience/03_arrays.html#numpy-arrays)
        - [`Pandas` DataFrames](https://allendowney.github.io/ElementsOfDataScience/07_dataframes.html)
    - Guía de [`NumPy`](https://universopython.com/es/blog/numpy-python-guia-completo)
    - Guía de [`Pandas`](https://universopython.com/es/blog/python-pandas-guia-definitiva-analisis-datos)
    - [Extraer datos de PDF](https://github.com/traversaal-ai/pdf-parser-table-extraction-fast-api)

- De datos:
    - [INE](https://www.ine.es/)
    - [NSFG (INE de EEUU)](https://www.cdc.gov/nchs/nsfg/)


