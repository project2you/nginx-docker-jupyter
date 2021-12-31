# nginx-docker-jupyter
Jupyter Lab behind a NGINX reverse proxy- the Docker way

# 1.ติดตั้ง Docker
sudo apt update && sudo apt -y upgrade

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
docker --version

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

#2.  ติดตั้ง Docker Compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version


#Option manual
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh
source ~/.bashrc
conda info
conda update conda
conda update anaconda
conda create --name myenv python=3.8
conda activate myenv
#conda install -c conda-forge jupyterlab
conda install -c anaconda jupyter 

jupyter notebook --generate-config

nano  /home/ubuntu/.jupyter/jupyter_notebook_config.py

allow_remote_access='True'
App.allow_origin='*'
c.NotebookApp.ip = '0.0.0.0' # listen on all IPs 

#3 Edit nginx.config
#file nginx.conf 

    upstream jupyter {
        server <hostname/ip>:8888;
    }

    proxy_pass http://<hostname/ip>;
 
#Don't Delete 
rm /etc/nginx/sites-enabled/default

#4 Install OpenSSL
sudo apt-get install -y openssl

# 2.Docker Compose
docker compose up -d
docker exec -it jupyterhub /bin/bash


