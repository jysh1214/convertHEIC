# ConvertHEIC to png

1. Put your HEIC files into the folder `HEIC`

2. Build the docker image
    ```
    docker build -t convert_image .
    ```

2. Run the docker container
    ```
    docker run --name convert_container convert_image
    ```

3. Copy the result from conatiner to host.
    ```
    docker cp convert_container:/home/user/HEIC .
    ```
