# Technical Interview For Sr Python Developer

---

## Levantar Ambiente

### Requisitos

* Java version > 17
* Python 3.9


### Instalación 

1. Clonar el repositorio y en la ruta clonada acceder a la carpeta <code>assets/data/parquets</code> y colocar los .parquet adjuntos en el instructivo de esta prueba.

![parquets](docs/images/parquets.png)

2. Ingresar al directorio <code>api</code> y crear un ambiente virtual para los paquetes en python y activarlo

```bash 
$python3 -m virtualenv env

$source env/bin/activate
```

3. Instalar los requerimientos

```bash
$(env) pip3 install -r requirements.txt
```

4. Run Microservicio (2 formas)

<code>productivo</code>
```bash
$(env) python main.py
```

<code>Desarrollo</code>
```bash
$(env) fastapi dev main.py
```

5. (Opcional) Run UnitTesting

```bash
$(env) pytest
```

### Next Steps

* [Arquitectura](docs/architecture.md)
* [Servicios/Api](docs/api.md)
