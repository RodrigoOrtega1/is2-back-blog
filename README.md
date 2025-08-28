# is2-back-blog
Backend para aplicación de Blog de Reseñas creado para la materia Ingeniería de Software 2

## Bibliotecas requeridas
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Alembic

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

### Ejecutar pruebas unitarias


```sh
python -m unittest tests/test.py
```
