# webappnorthwind
##connect server
ssh -p 4567 ubuntu@ip_of_real_machine

#docker 
https://docs.docker.com/v17.09/get-started/part2/#dockerfile
https://docs.docker.com/install/linux/docker-ce/ubuntu/

#backend
sudo docker build -t backend .
sudo docker run -d --name backend --env db_ip=10.0.2.15 -p 8080:8080 backend 
sudo docker stop backend
sudo docker rm backend 
sudo docker exec -it coredb bash

#deploy db
sudo docker load --input postgres_11.2-alpine.tar

sudo docker run -d --restart unless-stopped --name coredb -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -v ~/northwind_db:/var/lib/postgresql/data -p 5432:5432 postgres:11.2-alpine

#postgres
psql -U postgres
\l
create database xyz;
\c xyz;
