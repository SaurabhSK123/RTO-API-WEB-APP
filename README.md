# RTO-API-WEB-APP

In This task I created One Web Portal in Which we have to upload one car image
after that behind the scene that car image process in the model I created I recognize the 
number plate. for Recognizing number on the number plate here I use tesseract 
ocr tool which has some pre-created models help to reconize the exact numbers on the plate.
After Recongnizing the exact number of the car it will go to RTO API server and Retrieve all 
information and details about the car like car description and all..


In Prediction.py file line no. 43 we have to give the proper username instead of the {username} according 
your registration in the api server 
Link of that api server👇👇


For This Task I use Flask Framework. 

Here is the Task Description 📄

📌 In this task :
👉Create a model that will detect a car in a live stream or video and recognize characters on number plate of the car .

👉Secondly , it will use the characters and fetch the owners information using RTO API’s .

👉Create a Web portal where all this information will be displayed (using html,css,and js)

Requirements :

☘ install and import all the libraries given in the code.

☘ install the tesseracr-ocr model which help in recongnizing number on the numperplate of image.
