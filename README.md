# Juegos Divertidos — Python (Tkinter)

Aplicación de escritorio con dos juegos clásicos desarrollada en Python
como proyecto académico de **Algoritmos y Estructuras de Datos II** en la
Facultad Politécnica — Universidad Nacional de Asunción (FPUNA).

## Juegos incluidos

### Sopa de Letras
- Tablero generado aleatoriamente con palabras ocultas
- Temporizador configurable por el usuario (formato mm:ss)
- Selección de palabras con el mouse
- Pantalla de instrucciones integrada

### Batalla Naval
- Tablero 10×10 con posicionamiento aleatorio de barcos
- Modo jugador vs. máquina con IA aleatoria
- Turnos alternados: el jugador ataca, luego responde la máquina
- Sistema de puntuación (28 impactos para ganar)
- Pantallas de resultado (ganaste / perdiste) con imágenes

## Tecnologías
- Python 3.x
- Tkinter (interfaz gráfica)
- Pillow / PIL (imágenes de fondo y assets visuales)
- Módulo `random` (generación de tableros e IA)

## Requisitos

```bash
pip install pillow
```

Python 3.8 o superior con Tkinter incluido (viene por defecto en la mayoría de instalaciones).

## Cómo ejecutar

```bash
python Hi_5_.py
```

>  El proyecto requiere las imágenes de fondo en la misma carpeta:
> `pantalla_principal.png`, `intruccion_Sopa.png`,
> `reusltado_1_batalla_naval.png`, `ganaste_batalla_naval.png`,
> `perdiste_batalla_naval.png`

## Estructura del proyecto
Hi_5_.py # Código fuente completo (~1160 líneas)
pantalla_principal.png
intruccion_Sopa.png
*.png # Assets visuales


## Contexto académico
Proyecto grupal — Algoritmos y Estructuras de Datos II, FPUNA (2023)  
Arquitectura monolítica con navegación entre pantallas via Canvas de Tkinter.

## Autor
**Marcos González Lovera** — [@megl-fp](https://github.com/megl-fp)  
Ingeniería Informática — FPUNA
