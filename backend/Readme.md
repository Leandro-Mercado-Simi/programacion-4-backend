## Generar la carpeta venv:

```
python -m venv .venv
```

## Activar entorno:

En directorio:

```
source .venv/bin/activate
```

## Instalar dependencias:

```
pip install -r requirements.txt

# para corroborar la instalación de las dependencias:

pip list
```

## Para poner a correr el servidor

```
python -m fastapi dev app/main.py
```
