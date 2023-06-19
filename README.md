# Low-Light Enhance Web App

The Low-Light Enhance web app, inspired by the research paper ["A Light Weight Transformer for Image Enhancement and Exposure Correction" by Cui et al. (2022)](https://github.com/cuiziteng/Illumination-Adaptive-Transformer), leverages a compact Transformer model. This app, which incorporates the insights from the mentioned research, allows for efficient low-light image enhancement. The deployment of the app includes creating and containerizing the Flask app, Node website, and Nginx server using Docker Compose, ensuring seamless integration and scalability. 

## Getting Started
To run these containers,
* #### Docker Engine and Docker Compose 
    You need to instal the Docker Engine and Docker Compose. You can reach the official documentation to install Docker Engine [here](https://docs.docker.com/engine/install/) and Docker Compose [here](https://docs.docker.com/compose/install/)
* #### OpenSSL for Localhost
    You should create an OpenSSL certificate for localhost to run this project as https://localhost. To create the certificates;
    
    ```
    git clone https://github.com/FurkanAtass/LightEnhance-WebApp.git
    cd LightEnhance-WebApp
    cd nginx
    ```

    and follow the [How to Get SSL HTTPS for Localhost](https://www.section.io/engineering-education/how-to-get-ssl-https-for-localhost/) tutorial's;
        - Step 1: Generate a CA certificate
        - Step 2: Generating a certificate
        - Step 5: Importing CA Certificate to the browser

* #### Download the Model
    The model that is used for Low-Light Image Enhancement is `best_Epoch_lol.pth`. You can download it from [here](https://github.com/cuiziteng/Illumination-Adaptive-Transformer/blob/main/IAT_enhance/best_Epoch_lol.pth) by clicking the `Download raw file` on the right of the screen.
    
    Put this model file in `./pythonEnhance/best_Epoch_lol.pth`.

## Usage
With the help of Docker Compose, the usage is "A piece of cake."
Go to LightEnhance-WebApp folder and use the command;


`docker compose up -d`

where the -d flag stands for detached mode. It instructs Docker to start the containers defined in the Docker Compose file in the background and detach the terminal from the container's output.


####  * Here is an example usage:
[Low-Light-Enhance.webm](https://github.com/FurkanAtass/LightEnhance-WebApp/assets/79604903/533ffac2-7cf8-494e-84c7-86ad9d18f692)

## Stop and Delete
- To stop containers;


    `docker compose stop`

- To delete the containers; 

    `docker compose down`

- To delete the images that is created by the `docker-compose.yml` file;

    `docker rmi $(docker-compose images -q)`


## Issues

* If you cannot delete images as in the _Stop and Delete_ section (`docker images` command still shows images that should be deleted), you can use 
`$ docker rmi $(docker images | grep lightenhanceapp- | awk '{print $1}')`
