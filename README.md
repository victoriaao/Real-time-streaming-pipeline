# KI_Tech_Challenge1

This repo contains the entire files and code used to create a streaming pipeline in 2 envs for data transformation and aggregation running on spark.

To test pipeline solution -
Run python main.py in the terminal to generate streaming data.

Build the image using the dockerfile provided i.e:

Docker build -t [image-name]

## Running the container

To run , make the job accessible through a volume (your local directory) and pass the necessary directories:

*gitbash
docker run -v \\local_folder:/WORKDIR/ [image-name] /bin/bash -c "$(cat ./docker_entrypoint.sh)" 

*powershell
docker run -v /local_folder:/WORKDIR/ [image-name] /bin/bash -c "$(cat ./docker_entrypoint.sh)"

This would run the first pipeline prodenv.py file in the background and
then run the second prod env file in the foreground concurrently.
*Apache Airflow would have been a preferred orchestration tool to run the second env after data files have been ingested from the first. It would be a great tool for monitoring of the pipeline for breaks as well.
