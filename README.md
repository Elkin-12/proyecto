Este repositorio contiene el diseño de la base de datos relacional y la API de persistencia implementada en **Python** utilizando el framework **Django**. El proyecto está estructurado para optimizar la asignación de citas, la gestión de historias clínicas mediante notas y una relación flexible (Muchos a Muchos) entre el personal médico y sus especialidades.

---

## 👥 Integrantes del Proyecto
* **Anyelo Rodriguez Sandoval**
* **Elkin Medina**
* **Maria Camila Hernandez**
* **Omar Medina**

# 🏥 Sistema de Gestión Hospitalaria

Este es un sistema de gestión hospitalaria robusto y moderno desarrollado en **Python** utilizando el framework web **Django**. Permite administrar la información de pacientes (clientes), especialidades médicas, servicios médicos, médicos y la programación de citas de forma rápida y sencilla.

---

## 📋 Tabla de Contenidos
1. [Requisitos del Sistema](#-requisitos-del-sistema)
2. [Instalación y Configuración](#%EF%B8%8F-instalación-y-configuración)
3. [Migraciones de Base de Datos](#-migraciones-de-base-de-datos)
4. [Ejecución del Servidor](#-ejecución-del-servidor)
5. [Acceso al Panel de Administración](#-acceso-al-panel-de-administración)
6. [Estructura del Proyecto y Modelos](#-estructura-del-proyecto-y-modelos)

---

## 🔍 Requisitos del Sistema

Para ejecutar este proyecto de manera óptima, necesitarás tener instalado lo siguiente en tu equipo:

*   **Python:** Versión `3.10` o superior (Recomendado `3.12+`).
*   **SQLite:** Gestor de base de datos relacional (incluido por defecto con Python).
*   **Django:** Versión `5.2` o superior (especificado en `requirements.txt`).
*   **Pip:** Administrador de paquetes de Python (generalmente viene incluido al instalar Python).
*   **Entorno Virtual (Opcional pero recomendado):** `venv` para aislar las dependencias del proyecto.

---

## 🛠️ Instalación y Configuración

Sigue estos sencillos pasos para clonar, configurar y preparar tu entorno de desarrollo local:

### 1. Acceder al repositorio
Abre tu terminal (PowerShell, CMD, Bash) en la carpeta raíz de este proyecto:
```bash
cd "/ruta/al/proyecto/hospital - copia"
```

### 2. Crear un Entorno Virtual (Recomendado)
Para mantener las dependencias aisladas y evitar conflictos globales:
*   **En Windows (PowerShell/CMD):**
    ```bash
    python -m venv venv
    ```
*   **En macOS/Linux:**
    ```bash
    python3 -m venv venv
    ```

### 3. Activar el Entorno Virtual
*   **En Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
*   **En Windows (CMD):**
    ```cmd
    .\venv\Scripts\activate.bat
    ```
*   **En macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Instalar Dependencias
Instala Django y las dependencias requeridas mediante el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🗄️ Migraciones de Base de Datos

Las migraciones permiten preparar y estructurar la base de datos (creación de tablas, relaciones y restricciones) basándose en los modelos definidos en el sistema.

Para aplicar las migraciones existentes y configurar la base de datos SQLite por primera vez, ejecuta los siguientes comandos en tu terminal con el entorno virtual activo:

```bash
# 1. Detectar cambios en los modelos y preparar las migraciones (opcional si no hay cambios nuevos)
python manage.py makemigrations

# 2. Aplicar las migraciones en la base de datos
python manage.py migrate
```

Al ejecutar `python manage.py migrate`, Django creará automáticamente un archivo llamado `db.sqlite3` en la raíz del proyecto para almacenar toda la información del sistema.

---

## 🚀 Ejecución del Servidor

Una vez que las migraciones se hayan completado correctamente, puedes iniciar el servidor de desarrollo local integrado de Django ejecutando:

```bash
python manage.py runserver
```

Por defecto, el servidor se iniciará localmente en el puerto `8000`. Puedes acceder a él abriendo tu navegador e ingresando a la siguiente dirección:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

*(Para detener la ejecución del servidor en cualquier momento, presiona `Ctrl + C` en tu terminal).*

---

## 🔐 Acceso al Panel de Administración

El proyecto cuenta con la interfaz de administración nativa de Django completamente configurada y adaptada para gestionar de manera visual e interactiva todas las entidades del hospital.

### 1. Crear una Cuenta de Administrador (Superusuario)
Para poder ingresar, primero debes crear un superusuario administrador ejecutando la siguiente instrucción en tu consola:

```bash
python manage.py createsuperuser
```

La consola te solicitará ingresar de forma interactiva la siguiente información:
*   **Username (Usuario):** Define tu nombre de usuario (ej. `admin`).
*   **Email address (Correo electrónico):** Ingresa un correo electrónico de tu elección.
*   **Password (Contraseña):** Escribe una contraseña segura (los caracteres no se mostrarán en la pantalla al escribir por razones de seguridad).
*   **Password (again):** Vuelve a escribir la contraseña para confirmar.

### 2. Iniciar sesión en el Administrador
1. Asegúrate de tener el servidor en ejecución (`python manage.py runserver`).
2. Abre tu navegador y dirígete a: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**
3. Introduce el **Usuario** y **Contraseña** que acabas de configurar.
4. ¡Listo! Tendrás acceso completo al panel de control para registrar pacientes, médicos, especialidades, servicios y programar citas.

---

## 📂 Estructura del Proyecto y Modelos

El módulo central de la lógica hospitalaria está ubicado en la aplicación `sistema/`, la cual cuenta con las siguientes entidades registradas en el panel administrativo:

1.  **`Cliente` (Pacientes):** Almacena el perfil personal de los pacientes (Nombre, Apellido, Email único, Teléfono, Dirección, Tipo de Documento y Número de Documento único).
2.  **`Especialidades`:** Nombre de las áreas de especialización médica disponibles (ej: Cardiología, Pediatría, Medicina General).
3.  **`Servicio`:** Listado de consultas, procedimientos o chequeos que se ofrecen en la institución.
4.  **`Medico`:** Registro de doctores con una relación de muchos a muchos (`ManyToManyField`) con sus respectivas especialidades.
5.  **`Cita`:** Programación y control de citas. Vincula a un `Cliente`, un `Medico`, un `Servicio` específico, fecha y hora de la cita, y un estado que puede ser *Pendiente*, *Confirmada* o *Cancelada*.
