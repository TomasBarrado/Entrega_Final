# Veterinaria Coder - Proyecto Final del Curso de Python (CoderHouse) Barrado Tomas

## Descripción del Proyecto
Este proyecto consiste en una aplicación web desarrollada con Django para la gestión integral de una veterinaria. Ofrece funcionalidades como registro e inicio de sesión de usuarios, visualización y administración de mascotas, veterinarios y servicios ofrecidos por la clínica. Además, los clientes registrados pueden gestionar la información de sus mascotas.

### Funcionalidades Principales:
1. **Gestión de Mascotas:**
   - Los usuarios autenticados pueden registrar, editar y visualizar sus mascotas.
   - Los administradores tienen permisos adicionales para visualizar todas las mascotas registradas.

2. **Gestión de Veterinarios (admin o usuarios con permisos):**
   - Lista de veterinarios con detalles básicos, editable por el administrador.

3. **Gestión de Servicios:**
   - Visualización de servicios ofrecidos (atención veterinaria, peluquería, etc.).

4. **Perfil de Usuario:**
   - Usuarios autenticados pueden editar su perfil (nombre, correo, avatar) o cambiar su imagen de perfil.
  
5. **Autenticación:**
   - Registro de nuevos usuarios.
   - Inicio de sesión.
   - Cierre de sesión.
   - Opciones para editar el perfil y cambiar la contraseña.

6. **Página "Acerca de mí":**
   - Información sobre el desarrollador del proyecto o el propósito de la aplicación.

---

## Usuarios de Prueba

Para probar la aplicación, puedes usar los siguientes usuarios con permisos preconfigurados:

**Usuario Administrador**  
- **Usuario:** tomasbarrado
- **Contraseña:** tomas123

**Usuarios Comunes**  
- **Usuario:** consuelo  
- **Contraseña:** carmela123 
---

Al levantar la página web desde la terminal: python manage.py runserver (Asegurarse de estar en la ruta correcta) Directamente nos dirige al inicio de la pagina, sin la necesidad de ingresar manualmente con /inicio por ejemplo. Link principal: http://127.0.0.1:8000/

La pagina principal contiene dintintos botones en la barra de navegación que te permiten realizar todas las funcionalidades de la misma, sin la necesidad de ingresar a rutas que no esten a simple vista o con el alcance de un botón. Los botones de la barra de navegación son los siguientes:

Navegación en la Aplicación
La barra de navegación incluye los siguientes botones:

Inicio: Página principal.
Servicios: Visualiza los servicios ofrecidos por la veterinaria.
Veterinarios: Muestra una lista de veterinarios disponibles.
Mis Mascotas: Disponible solo para usuarios autenticados. Permite gestionar información de las mascotas.
Perfil: Opciones para editar el perfil, cambiar la imagen de perfil o cerrar sesión (visible tras autenticarse).
Registrarse / Iniciar Sesión: Permite a los usuarios registrarse o autenticarse.


Espero que la pagina sea de su agrado. Saludos!
