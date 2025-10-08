===========================================
 Proyecto: MiViñeta_PaulaAzqueta / permupack
===========================================

Descripción
-----------
Este proyecto contiene tanto un cuaderno Jupyter (exportado también a HTML) 
como un paquete Python (`permupack`) en el que se desarrollan ejemplos de estadística, 
discretización, permutaciones y visualización de datos. 

El enfoque es didáctico: mostrar de forma clara cómo funcionan 
estas técnicas mediante mini-ejemplos inspirados en un "mini-festival".

Contenido
---------
Estructura principal del repositorio:

- **notebooks/**
  - `MiViñeta_PaulaAzqueta.ipynb` → Notebook principal (código y explicaciones).
  - `MiViñeta_PaulaAzqueta.html` → Versión exportada en HTML.

- **permupack/** (paquete Python)
  - `perm_utils.py` → Funciones auxiliares (normalización, estandarización, 
    permutaciones, discretización, entropía, utilidades varias).
  - `Permutation.py` → Clase `Permutation` para gestionar y operar con permutaciones.
  - `perm_plotting.py` → Funciones de visualización (curva ROC, correlaciones, etc.).
  - `__init__.py` → Inicialización del paquete.

- **test/** → Pruebas unitarias.  
- **build/**, **dist/**, **permupack.egg-info/** → Carpetas generadas automáticamente al instalar.  
- **setup.py** → Script de instalación del paquete.  
- **LICENSE**, **README.md**, **CHANGES**, **MANIFEST.in** → Archivos de metadatos del proyecto.

Dependencias
------------
El código requiere Python 3.x y las siguientes librerías:
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

Instalación
-----------
Para instalar el paquete en modo editable:

```bash
git clone https://github.com/TU_USUARIO/permupack.git
cd permupack
pip install -e .

