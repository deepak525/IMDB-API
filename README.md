# IMDB-API

### Requirements:
- Install Python 3
- Install BeautifulSoup
- Install Flask Using "pip install flask"
- Install MongoDB Server
- Install pyMongo in Python with "pip"

### Scraping Data
- Send a HTTP request to the webpage using third party python library "request". The webpage respond to the request by returning HTML content. Using this library, I fatched 1000 Movie data from 10 different IMDB pages. Data includes Movie Id, Movie title, Rating, Starcast, Genre and Runtime.
- Once we have accessed the HTML content, we are left with parsing the content. For this we will use another third party, python library "BeautifulSoup".

### MongoDB DataBase

- In mongoDB database I created a Database named "IMDB" and a collection named "movies_data" inside "IMDB" Database. 

### API 1 (Search Movie)

- Collected data from MongoDB database and made a javascript for checking the Longest Common Subsequence(LCS). And completed the Autocomplete function which was asked in the Question. The rendering was done using flask.

### API 2 (Search Movie by ID)

- Implemented the api as per the specified norms as mentioned in the question. Pass the Movie ID in the input field and it will return the details of the movie with the related ID.
