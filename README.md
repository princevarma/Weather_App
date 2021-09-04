# Weather_App
This is GUI(turtle)  based Python Project .

"The GUI app will tell us the current weather of a particular city along with temperature details along with other details. "

Modules required:
Tkinter: It is a built-in python library for making GUI using tkinter toolkit.
Requests: It is a library which helps in fetching the data with the help of URL. It can be installed using the below command:
    --->"pip install requests"
    
Firstly, we have to use a weather API for fetching the data from the Open Weather Map website by generating an API key, and then we need to create a configuration file to store the key. And finally using that configuration file in the python script.

Steps to generate an API key:
Login in the Open Weather Map
Go to the API section. Then in the Current Weather Data section click on the Api doc.
Now in the API Call section, we have the link of api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
Click on the API key on the link it will direct to the page from where you can get the key.

