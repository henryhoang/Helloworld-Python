Helloworld-Python
=================

cd Helloworld-Python
docker build -t henryhoang/myapp-py .
docker run -d -P henryhoang/myapp-py
docker ps
CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS              PORTS                     NAMES
a989919d7f98        myapp-py:latest     "/usr/bin/python2.7    6 seconds ago       Up 5 seconds        0.0.0.0:49153->8080/tcp   agita
curl localhost:49153
<h1> Hey Docker from j2 Cloud!</h1>root@Docker:~/Helloworld-Python#
========================================================================
Please login prior to push:
Username: henryhoang
Password:
Email: henry.hoang@j2.com

docker pull henryhoang/myapp-py
