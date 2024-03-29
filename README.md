# nginx-docker-jupyter
Jupyter Lab behind a NGINX reverse proxy- the Docker way

# 1.ติดตั้ง Docker
sudo apt update && sudo apt -y upgrade

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

docker --version

sudo groupadd docker

sudo usermod -aG docker $USER




# 2.ติดตั้ง Docker Compose

sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker compose version


#Option manual

sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6



# 3.ติดตั้ง Anaconda


curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh


bash Anaconda3-2023.09-0-Linux-x86_64.sh

source ~/.bashrc

conda info

conda update --all

conda create --name myenv python=3.8

conda activate myenv



# 4.ติดตั้ง Jupyter

#conda install -c conda-forge jupyterlab

conda install -c anaconda jupyter 

conda update -c conda-forge notebook

jupyter notebook --generate-config

nano  /home/ubuntu/.jupyter/jupyter_notebook_config.py

allow_remote_access='True'

c.NotebookApp.allow_origin = '*'

c.NotebookApp.ip = '0.0.0.0' # listen on all IPs 


# cmd

jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root --no-browser



# 5.ทดสอบ Jupyter Notebook + Python

git clone  https://github.com/project2you/nginx-docker-jupyter.git

cd nginx-docker-jupyter

pip install -r requirements.txt

python3 app.py

#ระบบจะทำการรัน Jupyter Notebook ขึ้นมา เราสามารถ GET ค่า พารามิตเตอร์ ผ่าน Token ได้โดยเรียกผ่าน API

#curl localhost:5000/api

#จะได้ค่า Token : 53a325b714b8787aaefda5cbd4cb68451bda89905f417b38 ซึ่งสามารถนำไปใช้งานต่อได้




# 6 ติดตั้ง nginx และทำการ config

    
sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring

curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
    
    
 echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
    
    
 echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx
    
 
 
sudo apt update

sudo apt install nginx


sudo apt-get install nginx-module-njs


sudo reboot now



sudo nano /etc/nginx/nginx.conf

load_module modules/ngx_http_js_module.so;

load_module modules/ngx_stream_js_module.so;


sudo nginx -s reload && sudo nginx -t
#Output
#nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
#nginx: configuration file /etc/nginx/nginx.conf test is successful


#The njs dynamic modules for nginx have been installed. To enable these modules, add the following to /etc/nginx/nginx.conf and reload nginx:


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


# Option

git clone https://github.com/project2you/nginx-docker-jupyter/

docker build -t project2you/alpine-conda .

docker run -it -d -p 5000:5000 -p 8888:8888 -v /home/ubuntu/tmp:/root/notebooks project2you/alpine-conda



