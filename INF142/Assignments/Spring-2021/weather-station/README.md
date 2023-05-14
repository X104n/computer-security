# Inf142M1

**First mandatory assignment in inf142**

Team members:

	- Gard Kalland
	- Østen Edvardsen
	- Stian Munkejord
	- Oskar Michalski
	- Lars Bysheim

Some Information:

We have built a program collecting data from three fictional weather stations. The weather stations "reads" the weather and transfers it to one of two storages. Using our web-page, a client can access data from both of the storages.
The "README.png" is from an older version, but it still shows how it is all connected.

Some of the files are nearly duplicates and best commented in "Storage_Bergen_Karmøy" and "Weather_Station_Bergen" 

**Running**

On Windows:

	1. Run "start.py"
	2. Run "website-start.py"
	3. Go to "localhost:5000"

On others:

	1. Run "tcp_server.py" and "udp_server.py" in both of the storage folders
	2. Run "tcp_client.py" in all three of the weather_station folders (try to start them as close to eachother as possible for higher realism)
	3. Run "web-server.py" in FMI/webserver/
	4. Go to "localhost:5000"


If you want to try it in a terminal just follow the above steps, but instead of "web-server.py" you should run "udp_client.py" in the FMI folder.
The commands:

	1. help
	2. {location name}		- returns the average for each day at this location
	3. {location name} {(1-31)} 	- returns data for each hour of the chosen day and location

Locations = bergen,karmøy and oslo

**Extensions**

1. sqlite:

We created a sqlite database called "weather-data.db" and placed it in both of the storages. The db holds a single table called "WEATHER" with 6 coloumns: 

	1. id (autoincrementing, mostly there for debugging)
	2. location
	3. day (day of the month)
	4. month
	5. temperature
	6. rain
	
When the storage tcp_server recives this data it executes a line of SQL, inserting it into the db.
The udp_server fetches a piece of that db based on the client command.
Using a sqlite database made it easy to fetch the wanted data without having to loop through all the data on each client request.

Since we are collecting data from a simulation and not real weather data, we can not restart the program without clearing the database. The "station.py" script starts over from May 1. 00:00 every time we restart, and we dont want duplicated data. That is why, when we start running the tcp_servers, we clear out the database.

NB:
We have had no problem with this, but
if should experience a problem with duplicated data (ex: two May 2. or 48 hour in a day), try this:

	1. Shut down everything
	2. Download and run "DB BROWSER FOR SQLITE"
	3. Open the weather-data.db in db browser. 
	4. Execute the file "clear.sql" in the "Execute SQL" tab
	5. Do this with both the database files and try running it again.

This was a problem, but it has never happened to any of us after we fixed it. However, if it does happen to you, this is the way we fixed it then.
	
2. flask:

short on how it works

	1. If a site i clicked that there exsits an route for, the function beneath wil start
	2. The function calls a function that is in the receive script and the r.{{name}}temps will be filled with information
	3. it returns a render_template that takes in different variables, one is the html file that it needs to find, then the weather which uses the r.{{name}}temps, then the title which changes the title of the website, and last the style which chooses the .ccs file that is going to be used
	4. layout.html runs and and the website is posted, layout.html takes in the information that the render_template gives, but in the render_template it dosent specify that layout.html is the one that is being ran, beacuse in each of the html files that the render_template defines is an extension of the layout.html file, and everything that is posted inside the {{name}}.html file will either lay inside the {% block content %}{% endblock %} or   {% block information %}{% endblock %}


more detalied explanation
↓
↓
↓
↓
↓


The Flask script does several different things, it routes new pages by using the @app.route function, this makes it so that if you type in that route you will not get an 404 error page.

Each route have an function, that function request the information stored in the database, its using the udp-server sorting system to get the information from the database, there are three different functions that the flask script uses to get the information, and that is: one that request Oslo, one that request Bergen and one that request Karmøy. The functions in each route requests the one that they need. 

The function return a render_template, this does inside the template folder and accesses the html file that the template defines, it also has three other statements, the r.{{name}}temps is a list of the day, temp, rain, month that is in the database. Then it return a title and style, the style is a path to the correct css file that stores how the site looks

The Day function request the information that is stored in the url and the two first numbers will be put in a variable named day, then it checks which location is stored in the url, when it has found that it starts the udp function where it uses the day as a variable so that the r.{{name}}temps will get the correct day, then you will be sent to a new site that shows every temp of that day.

The layout.html is the layout of the website, it takes in two different variables and that is title and style, the layout uses the style variable to link to the correct .ccs file so that the background of each site will change. The title variable makes it so that at the tab it wont say “localhost:5000/{{name}}” but INF vær – {{name}}.
Then there are the navbar that has the name of the website and three hyperlink with names that allow the user to click on ex: Bergen, and that will take you that page. 

There are two places where it says {% block content %}{% endblock %} and  {% block information %}{% endblock %} these two can you find in the html file that the return render_template  link to “{{name}}.html”
inside each “{{name}}.html” at the top it says {% extends "layout.html" %} this means that it is a “subfile” of the layout.html file and everything that everything that is inside the block content and block information will be posted to the website.


