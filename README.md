# Actividad 1 y 2
Concentracion Analisis de Datos 

## Comparación con activity2_solution

**Diferencia 1: carpeta .streamlit/.**
La solución incluye el archivo .streamlit/config.toml con un tema de colores y una plantilla de secrets.toml. Decidi no agregarla ya que me quise centrar en aprender las funciones básicas. Batalle un poco para subir todos los archivos correctamente y que se pudiera actualizar mi app, por lo que decidi centrarme en eso.

**Diferencia 2: limpieza de datos en clean_sales.**
La solución elimina duplicados y unidades negativas y calcula revenue. Yo elimino duplicados y filas sin date, units o sku. No calcule revenue porque el CSV ya la trae y no filtre unidades negativas porque revise los datos y no hay ninguna.
