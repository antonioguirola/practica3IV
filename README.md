Práctica 3 de IV
==================

Práctica 3 de la asignatura IV: creación de máquinas virtuales.

## Introducción

El objetivo de esta práctica es crear máquinas virtuales con un propósito específico, en mi caso correr una aplicación web, de forma que se asignen los recursos a las mismas de la forma más eficiente posible. Para ello crearé varias máquinas virtuales (de aquí en adelante MV) en Windows Azure con diferentes configuraciones y ejecutaré sobre las mismas una batería de peticiones usando el software [Apache Benchmark](http://httpd.apache.org/docs/2.2/programs/ab.html).

## La aplicación

La aplicación que voy a ejecutar sobre las máquinas virtuales es la creada para la asignatura DAI, la cual se puede descargar desde [éste repositorio](https://github.com/antonioguirola/appdai-public), sólo es necesario establecer los parámetros de conexión a la base de datos.

Como nos encontramos en un entorno de pruebas voy a usar el servidor web integrado en el propio framework.

### Base de datos

Voy a utilizar una base de datos común para todas las instacias de la aplicación, para ello, como la aplicación está preparada para usar MongoDB, he creado una base de datos en la nube usando [MongoLab](www.mongolab.com) a la cual se conectarán las instancias:

![captura](capturas/db-1.png)

Los parámetros para la conexión que tendremos que introducir en el código los podemos consultar haciendo click sobre la base de datos:

![captura](capturas/db-2.png)

### Despliegue de la aplicación en las MV

Para agilizar el despliegue de la aplicación en las distintas MV realizaré la instalación desde un repositorio privado en [bitbucket](www.bitbucket.org) en el cual se encuentra la aplicación con todas las opciones de configuración ya establecidas.

Para solventar las dependencias de Python voy a usar un [script](generateEnvironment.sh) que genere un entorno virtual en el cual se instalen las dependencias necesarias:

```sh
#!/bin/bash

# Instalación de los paquetes necesarios
sudo apt-get install -y python-virtualenv
sudo apt-get install -y git
sudo apt-get install -y python-dev
sudo apt-get install -y libxml2-dev libxslt-dev

# Creación del entorno virtual Python
cd ~
mkdir env
cd env
virtualenv --distribute env1
cd env1/
source bin/activate

# Instalación de los paquetes Python necesarios
# dentro del entorno virtual
pip install web.py
pip install mako
pip install pymongo
pip install lxml
pip install tweepy

# Recuperamos la aplicación del repositorio privado
git clone https://antonioguirola@bitbucket.org/antonioguirola/appdai.git
cd appdai

# Ejecutamos el servidor web de web.py en el puerto 80
python code.py 80
```

### Creación de las máquinas virtuales

#### Máquina 1: Ubuntu Server 12.04 LTS extra pequeño

![captura](capturas/inst-1.png)
![captura](capturas/inst-2.png)
![captura](capturas/inst-3.png)
![captura](capturas/inst-4.png)

##### Conexión a la MV

Una vez arrancada la MV podemos acceder por SSH:

![captura](capturas/ssh-conn.png)

