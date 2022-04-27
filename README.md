# Ko-Bang Cosmetic Demo App
Supporting code for containerisation of a Python Flask application using Docker and deploying it to Heroku

This repo contains a sample code to show how to create a Flask API server by deploying our PyTorch model. This is a sample code which goes with [tutorial](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html).

The deployment of flask application to Heroku through Docker is with the reference of [Flask-Docker-Heroku](https://medium.com/@ashok7067/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43).

## Requirements

Install them from 'requirements.txt':

    pip install -r requirements.txt

## Local Deployment

Run the server:

    python app.py

## Demo App

Click this link to run our demo app

[Ko-Bang Cosmetic Demo App](https://kobang-cosmetic1.herokuapp.com/)

## How it works
Screen 1: Homepage             |  Screen 2: Take photo with camera or choose image from gallery              
:-------------------------:|:-------------------------:
<img src="https://github.com/sinhong96/Ko-Bang-Cosmetic-App/blob/main/app_screen/S1.jpg" width="250" height="500">   |   <img src="https://github.com/sinhong96/Ko-Bang-Cosmetic-App/blob/main/app_screen/S2.jpg" width="250" height="500">   
Screen 3: Preview uploaded image             |  Screen 4: Retrieve prediction of food and corresponding nutrient content                  
<img src="https://github.com/sinhong96/Ko-Bang-Cosmetic-App/blob/main/app_screen/S3.jpg" width="250" height="500"> | <img src="https://github.com/sinhong96/Ko-Bang-Cosmetic-App/blob/main/app_screen/S4.jpg" width="250" height="500">                  
 

## Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://kobang-cosmetic1.herokuapp.com/)

## Training Dataset 
- The data is collected by web-crawling and has 5 face skin types, and the total number of images in this dataset is 1000 images.
- Face types 
* Dry Skin
* Normal Skin
* Oily Skin
* Pimples 
* Sensitve Skin

![dataset](https://github.com/sinhong96/Ko-Bang-Cosmetic-App/blob/main/app_screen/dataset.png?raw=true )

## Flow of the Deplopyment of App to Heroku through Docker
- The flow of how Ko-Bang-Cosmetic-App is deployed is as shown in the figure below. 
![app_deploy](https://github.com/sinhong96/Ko-Bang-Cosmetic-App/blob/main/app_screen/app_deploy.png?raw=true )

## License

Please check 'LICENSE' for more details.
