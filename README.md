**To test the project use the excel that is present in assets folder**


To start the Backend run ensure that system has docker installed and use the following command

    sudo docker-compose up --build

    This command will start the backend server, redis, and celery. it will also applies all the migrations


LLD 

![LLD_image_processing_BE](https://github.com/C0deGeek007/image_processing/assets/45477155/4f2e4ecf-ad94-4804-a2a8-eaaf96a6b719)

Components:

  API Endpoints: <br>
    1. upload<br>
    2. checkStatus<br>

  Celery:<br>
    1. To process images and download excel output in required format<br>

postman collection and demo video are attached in repo
