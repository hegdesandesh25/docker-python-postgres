# docker-python-postgres
Program to demonstrate python container connect to Postgres container

Steps to run the demo:

|steps|description|
| --- | --- |
|docker build .|to build the Docker file consisting of python code|
|docker images | to check if the images is built ok|
|docker tag image-id custom-name| pick up the image ID and tag it to ease the use|
| docker-compose up |To build the docker file|
| docker network ls  | check the bridge network created by postgres (postgres_node_net) as defined in the code|
|docker run --name=custom-name --network=postgres_node_net| run the container to see output|
