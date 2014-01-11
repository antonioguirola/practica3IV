#!/bin/bash

# Instalación de los paquetes necesarios
sudo apt-get install -y python-virtualenv
sudo apt-get install -y git
sudo apt-get install -y python-dev
sudo apt-get install -y libxml2-dev libxslt-dev

# Variable de entorno necesaria para twitter
export LC_ALL=C

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

# Ejecutamos el servidor web de web.py
python code.py