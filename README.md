# KI_Tech_Challenge1

This repo contains the entire files and code used to create the streaming pipeline for No.1 of the tech challenge.

Build the image using the dockerfile provided i.e:

Docker build -t [image-name]

#Running the container

To run the job, make the job accessible through a volume (your local directory) and pass the necessary arguments:

*gitbash
docker run -v \\local_folder:/WORKDIR/ [image-name] /bin/bash -c "$(cat ./docker_entrypoint.sh)" 
*powershell
docker run -v /local_folder:/WORKDIR/ [image-name] /bin/bash -c "$(cat ./docker_entrypoint.sh)"
