# Calculate survival rate for passenger of Titanic 2
 
Train a machine learning (ML) model based on the data from Titanic disaster
and apply it to calculate the survival rate for passenger of the Titanic 2.
Details of this challenge and data set for ML model trainig can be found
[here](https://www.kaggle.com/c/titanic).

## ML model training

Train data preparation and ML model training was done using Jupyter notebook **titanic2_train.ipynb**.
*PassengerId*, *Name*, *Ticket* and *Cabin* columns from the original data set were not used for model training. Several columns (*Pclass*, *Sex*, *Embarked*) have been quantified or normalized for training.
*Survived* column was used as a data flag.
TensorFlow Sequential model consisted of four fully connected layers was used. In the last layer sigmoid activation function was used to obtain result in the range from 0 to 1. Trained model was saved in the **ML_model_titanic2** directory. Finally directory with ML model was packed to archive by:

    tar -cvzf ML_model.tar.gz ML_model_titanic2

## REST API

REST API was developed using Flask and saved as **app.py** file. It consists of two requests:
* GET request at **localhost:5000/example** which returns json file which can be used as a template for POST request with passenger data
* POST request at **localhost:5000/predict** which will accept json file with passenger data and return json file with calculated survival rate
To calculate the survival rate **prediction** function from the **calculate.py** script will be called.

## Docker image

Dockerfile was created to build the Docker image. All neccessary files were copied to the work direcory (in case of the ML model archive ADD method was used to unpack it). Library dependencies were defined in the **dependencies.txt** file. Image was build from inside of the Visual Studio Code with Docker extension and saved as **titanic2_restapi**. Docker documentation about build process can be found [here](https://docs.docker.com/engine/reference/commandline/build/).

## Running and testing

Docker image can be run as a container using the following command:

    docker run -p 5000:5000 titanic2_restapi

Test request can be send by running the **titanic_request.py** script.