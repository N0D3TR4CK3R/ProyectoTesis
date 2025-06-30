# ProyectoTesis

Este proyecto es una plataforma para la gestión de activos, desarrollada con Django para el backend y una estructura de frontend basada en templates HTML. Incluye manejo de datos y una arquitectura modular.

## Estructura del Proyecto

```
ProyectoTesis/
│
├── backend/         # Proyecto Django
│   ├── manage.py
│   ├── activos/     # App principal para gestión de activos
│   └── config/      # Configuración del proyecto Django
│
├── frontend/        # Archivos estáticos y templates
│   ├── templates/   # HTML para la interfaz de usuario
│
├── data/            # Archivos de datos (CSV, Excel)
│   ├── data.csv
│   └── data.xlsx
│
├── requirements.txt # Dependencias del proyecto
└── README.md        # Este archivo
```

## Descripción

La aplicación permite gestionar activos, almacenando información relevante como tipo, nombre, ubicación, cantidad y código. Utiliza Django como framework principal y organiza la lógica en una app llamada `activos`.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/N0D3TR4CK3R/ProyectoTesis.git
   cd ProyectoTesis
   ```
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Aplica migraciones y ejecuta el servidor:
   ```bash
   cd backend
   python manage.py migrate
   python manage.py runserver
   ```

## Uso

- Accede a la interfaz web en `http://127.0.0.1:8000/`.
- Gestiona activos desde la app principal.
- Los datos pueden ser exportados/importados desde la carpeta `data/`.

## Arquitectura

El proyecto sigue una arquitectura modular:
- **Backend:** Django, app `activos`, base de datos SQLite.
- **Frontend:** Templates HTML.
- **Datos:** Archivos CSV y Excel.

## Diagrama de Arquitectura

El diagrama de arquitectura se encuentra a continuación en formato PlantUML:

```plantuml
@startuml
!includeurl https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(user, "Usuario", "Interactúa con la plataforma de gestión de activos")
System_Boundary(s1, "ProyectoTesis") {
  Container(web, "Frontend (HTML)", "HTML", "Interfaz de usuario basada en templates")
  Container(api, "Backend (Django)", "Python/Django", "Lógica de negocio y API")
  ContainerDb(db, "Base de Datos", "SQLite", "Almacena información de activos")
  Container(data, "Archivos de Datos", "CSV/Excel", "Importación y exportación de datos")
}
Rel(user, web, "Usa")
Rel(web, api, "Solicita datos y operaciones")
Rel(api, db, "Lee/Escribe")
Rel(api, data, "Importa/Exporta")
@enduml
```

Puedes visualizar este diagrama en [PlantUML Online Server](https://www.plantuml.com/plantuml/).

---

Si tienes dudas o sugerencias, contacta al autor del repositorio. 