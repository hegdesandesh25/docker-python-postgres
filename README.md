# docker-python-postgres
Program to demonstrate python container connect to Postgres container

Execution steps to run the demo:

|steps|description|
| --- | --- |
|docker build .|to build the Docker file consisting of python code|
|docker images <br><p> <br>REPOSITORY TAG  IMAGE ID  CREATED  SIZE <br> none none 7cfd81808987  38 minutes ago  895MB <br> </p>| to check if the images is built ok|
|docker tag image-id custom-name <br><p><br> REPOSITORY TAG IMAGE ID CREATED SIZE <br> python-nov2 latest 7cfd81808987 38 minutes ago 895MB <br> </p>| pick up the image ID and tag it to ease the use|
| docker-compose up |To build the docker file, this file contains all details (username/password/database name/port/network/host)|
| docker network ls <br><p><br>NETWORK ID NAME DRIVER SCOPE <br> 876d62db9a62 postgres_node_net bridge local <br> </p> | check the bridge network created by postgres (postgres_node_net) as defined in the code, this will help python container connect in further steps|
|docker run --name=custom-name --network=postgres_node_net| run the container to see output, notice that we tagged the network so that container will know which network to connect|


 Docker-compose file:
 - the below env are used to set in the compose file
    - Username
    - Password
    - database name
    - port(5432)
    - network 
    -  host 
 
 Dockerfile:
 - Set the workdir
 - copy the file to container 
 - install the psycopg2 library
 - command to execute the python script inside container
