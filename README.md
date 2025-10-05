# API dockenizada

**Objetivo**.- Crear una api sencilla junto con docker para poder montarla en la plataforma Render

**Requisitos**
1. tener instalado python
2. tener instalada la libreria virtualenv puedes checar tus librerias instaladas con pip list 

**Paso 1**Desde la terminal de Visual Studio Code crear una carpeta llamada retoApi con el comando virtualenv y el nombre de tu entorno virtual , entra a la carpeta que se crea con el comando cd más el nombre de la carpeta, una vez que estes dentro teclea: .\<Nombre del entorno>\scripts\activate para activar el entorno virtual y poder probar la api
 
y dentro de esta crear un entorno virtual de python 
para que solamente se instalen las librerias a usar y no llevarnos más al hacer el archivo requirements.txt
Crea una carpeta 
```
C:tuCarpeta\virtualenv <Nombre del entorno>
C:tuCarpeta\cd <Nombre del entorno>
C:tuCarpeta\<Nombre del entorno>\.\<Nombre del entorno>\Scripts\activate
```
**Paso 2** Desarrollar los metodos de la api y probarla, con el siguiente comando se levanta el servicio web de la api, para esto tienes que estar al nivel del archivo main.py si es que lo generas dentro de alguna otra carpeta, sino te marcara error
```
uvicorn main:app --reload
```
