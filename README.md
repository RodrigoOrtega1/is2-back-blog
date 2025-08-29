# is2-back-blog
Backend para aplicación de Blog de Reseñas creado para la materia Ingeniería de Software 2

## Bibliotecas requeridas
- SQLAlchemy
- Flask
- Flask-Migrate
- Flask-SQLAlchemy
- flask-cors
- python-dotenv

### Creación y activación de entorno virtual
```sh
python -m venv .venv
source .venv/bin/activate
```

### Instalación de bibliotecas
```sh
pip install -r requirements.txt
```

## Funcionamiento

### Inicializar migraciones

```sh
flask db init
```

### Crear nueva migración
```sh
flask db migrate -m "mensaje"
```

### Aplicar migración a la base de datos

```sh
flask db upgrade
```

### Poblar la base de datos con datos dummy (opcional)

```sh
python app/seed.py
```

### Ejecutar el servidor

```sh
python run.py
```

El backend estará disponible en `http://localhost:5000`.

Opcionalmente, se puede ejecutar en otro puerto, creando un archivo .env en el directorio raíz del proyecto, con la variable de entorno: `PORT=5001` con el valor del puerto a utilizar.

### Ejecutar pruebas unitarias


```sh
python -m unittest tests/test.py
```
