---

<a> Demostracion del Face Mesh.<a>

<p align="center">
  <img src="Screenshot 2025-03-11 at 19-01-44 Calculadora.png" alt="Captura de pantalla" width="120">
</p>

---

# Python Face Mesh

Proyecto sencillo en Python que utiliza MediaPipe y OpenCV para detectar la malla facial (face mesh) en tiempo real desde la cámara. El repositorio contiene un ejemplo mínimo que captura video, procesa los frames con MediaPipe Face Mesh y dibuja la red de puntos sobre el rostro.

## Captura de pantalla / demostración

La siguiente imagen muestra el resultado del programa: la malla facial (landmarks) dibujada sobre la cara de la persona en tiempo real.

## Requisitos

- Python 3.10+ (el entorno de trabajo usado es un virtualenv llamado `venv_mediapipe`)
- OpenCV
- mediapipe

El archivo `requirements.txt` en `src/` lista las dependencias utilizadas en el proyecto.

Ejemplo de instalación (Windows PowerShell):

```powershell
# activar el entorno virtual si existe
.\venv_mediapipe\Scripts\Activate.ps1; 
# o crear uno y activarlo
python -m venv venv_mediapipe; .\venv_mediapipe\Scripts\Activate.ps1; 
# instalar dependencias
pip install -r src\requirements.txt
```

## Estructura del repositorio

- `src/`
	- `main.py`         -> Script principal que abre la cámara y dibuja la malla facial.
	- `utils.py`        -> Funciones auxiliares (por ejemplo, inicializar la cámara, dibujado, etc.).
	- `requirements.txt`-> Dependencias del proyecto.
- `db/`               -> Código relacionado con persistencia (ej. `database.py`).
- `venv_mediapipe/`   -> Virtualenv (no versionar normalmente).
- `assets/`           -> Carpeta sugerida para imágenes, capturas y demos (crear manualmente).

## Cómo ejecutar

1. Activar el entorno virtual (si ya lo tienes) o crear uno como se muestra arriba.
2. Instalar dependencias: `pip install -r src\requirements.txt`.
3. Ejecutar el script principal:

```powershell
cd src; python main.py
```

El script abrirá una ventana mostrando el video de la webcam con la malla facial dibujada. Presiona `q` en la ventana de OpenCV para salir.

## Detalles técnicos

- El proyecto usa MediaPipe Face Mesh para detectar hasta varios cientos de puntos faciales por rostro.
- OpenCV se usa para captura y visualización (BGR <-> RGB conversiones gestionadas antes de procesar con MediaPipe).
- Se sugiere usar una GPU o aceleración nativa si tu instalación de mediapipe lo soporta para mejor rendimiento.

