# Integrantes:

- Edison Harvey Cubillos Casallas (ID BANNER: 100160562)

# Historias de usuario:

- **Como** usuario, **quiero** buscar información del clima de una ciudad específica, **para** estar informado sobre las condiciones climáticas actuales.

- **Como** usuario, **quiero** ver un desglose detallado del clima de la ciudad buscada, **para** conocer la temperatura, sensación térmica, humedad y velocidad del viento.

- **Como** usuario, **quiero** que la aplicación guarde las consultas recientes, **para** poder revisar las búsquedas previas sin tener que ingresarlas nuevamente.

- **Como** usuario, **quiero** tener la opción de volver del historial de consultas al buscador principal, **para** buscar nuevas ciudades fácilmente.

- **Como** usuario, **quiero** que la interfaz tenga un icono dinámico según el clima de la ciudad, **para** poder entender si está nublado, lluvioso y demás de manera sencilla.

# Comandos Git:

- Una vez creado el repositorio en GitHub y haber instalado Git, ejecutamos el siguiente comando para inicializar un repositorio local donde en el directorio de nuestro proyecto.

```bash
git init
```
![](https://i.imgur.com/oNoS4x0.png)

- Vemos el estado de los archivos que están en el repositorio local con el siguiente comando:

```bash
git status -s
```
![](https://i.imgur.com/RlP6AAr.png)

- Agregamos los archivos que queramos a nuestra área de trabajo o staging area con el siguiente comando y vemos el estado nuevamente:

```bash
git add .
```
![](https://i.imgur.com/yBngaqs.png)

- Pasamos los archivos que están en nuestra área de trabajo o staging area al repositorio local con el siguiente comando:

```bash
git commit -m "Comentario commit"
```
![](https://i.imgur.com/3vUn4o2.png)

- Vemos el log de los commits hechos en el repositorio con el siguiente comando:

```bash
git log --oneline
```
![](https://i.imgur.com/aKYRQHC.png)

- Enlazamos el repositorio local a uno en la nube de GitHub con el siguiente comando:

```bash
git remote add origin https://github.com/bluefishh/app-consulta-clima.git
```
![](https://i.imgur.com/SEyE8dL.png)

- Vemos con qué repositorio quedamos enlazados en la nube de GitHub con el siguiente comando:

```bash
git remote -v
```
![](https://i.imgur.com/wFRrHCW.png)

- Establecemos el brazo o rama sobre el que queremos subir contenido al repositorio en GitHub con el siguiente comando:

```bash
git branch -M main
```
![](https://i.imgur.com/h64KDpM.png)

- Subimos los cambios del repositorio local al repositorio de la nube de GitHub con el siguiente comando:

```bash
git push -u origin main
```
![](https://i.imgur.com/QhtJQtN.png)

- Podemos actualizar el repositorio local con los cambios que se hagan en el repositorio de la nube de GitHub con el siguiente comando:

```bash
git pull
```
![https://i.imgur.com/1cXqiSN.png]()