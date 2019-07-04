# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:03:37 2019

@author: Deepak
"""

from flask import Flask, render_template,redirect,url_for,request
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def index():
    client = MongoClient() 
    client = MongoClient('mongodb://localhost:27017/')
    db = client['IMDB']
    collection = db['movies_data']
    d=[]
    curr = collection.find()
    for i in curr:
        d.append(i["movie_name"])
    mydata={}
    mydata["list"]=d
    return render_template("index.html",data=mydata)

@app.route("/movie1/<ids>")
def movie1(ids):
    client = MongoClient() 
    client = MongoClient('mongodb://localhost:27017/')
    db = client['IMDB']
    collection = db['movies_data']
    curr = collection.find({'id':ids})
    data={}
    for i in curr:
            data['id'] = i['id']
            data["movie"]=i['movie_name']
            data["rating"]=str(i['rating'])
            data["cast"]=i['cast']
            data["genre"]=i['genre']
            data["runtime"]=str(i['runtime'])
            
    return render_template("show_data.html",**data)

@app.route("/movie_name",methods=['POST'])
def movie_name():
    if(request.method=="POST"):
        name = request.form['movie_title']
        client = MongoClient() 
        client = MongoClient('mongodb://localhost:27017/')
        db = client['IMDB']
        collection = db['movies_data']
        curr = collection.find({'movie_name':name})
        data={}
        for i in curr:
                data['id'] = i['id']
                data["movie"]=i['movie_name']
                data["rating"]=str(i['rating'])
                data["cast"]=i['cast']
                data["genre"]=i['genre']
                data["runtime"]=str(i['runtime'])
                
        return render_template("show_data.html",**data)

@app.route("/movie",methods=["POST"])
def my_from():
    text =  request.form['movieID']
    return redirect(url_for('movie1',ids=text))

@app.route("/api2")
def api2():
    client = MongoClient() 
    client = MongoClient('mongodb://localhost:27017/')
    db = client['IMDB']
    collection = db['movies_data']
    d=[]
    curr = collection.find()
    for i in curr:
        d.append(i["id"])
    mydata={}
    mydata["list"]=d
    return render_template("API_2.html",data=mydata)
    

if __name__ == "__main__":
    app.run()