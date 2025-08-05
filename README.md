# Cat App
 A simple Flask web application that manages cat and owner data using a SQLite database (pets_database.db). This project demonstrates basic CRUD operations and table relationships (one-to-many) using Flask and SQLite, built as part of Phase 4 learning for Flask and SQL integration.

# Table of Contents
 Project Overview
 Features
 Setup
 Usage
 API Endpoints
 Resources

## Project Overview
 This Flask app connects to a SQLite database (pets_database.db) to manage cat and owner records. It uses primary and foreign keys to establish a one-to-many relationship (one owner can have many cats). The app provides RESTful endpoints to retrieve and create cat data, integrating SQL queries with Flask routes.

## Features
 Retrieve all cats for a specific owner (GET /cats).
 Retrieve a single cat by ID (GET /cat/<id>).
 Create a new cat (POST /cats).
 Retrieve cats with their owner names using a LEFT JOIN (GET /cats_with_owners).
 Error handling for missing tables, invalid data, and non-existent records.

## Setup
 Prerequisites
 Python 3.7+
 SQLite 3.31.1+
 Flask (pip install flask)

## Installation
 Clone the Repository:
 git clone <https://github.com/mathiasmunene/cat_names.db>
 cd <cats_names.db>


Set Up Virtual Environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # Linux/WSL
### or: .\venv\Scripts\activate  # Windows

## Install Dependencies:
 pip install flask

## Create Database:
Create pets_database.db with the following SQL:sqlite3 pets_database.db

PRAGMA foreign_key=ON;
CREATE TABLE owners (
  id INTEGER PRIMARY KEY,
  name TEXT
);
CREATE TABLE cats (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  breed TEXT,
  owner_id INTEGER,
  FOREIGN KEY (owner_id) REFERENCES owners(id)
);
INSERT INTO owners (name) VALUES ('mugumogu');
INSERT INTO cats (name, age, breed, owner_id) VALUES ('Maru', 3, 'Scottish Fold', 1);
INSERT INTO cats (name, age, breed, owner_id) VALUES ('Hana', 1, 'Tabby', 1);
.quit


## Verify Database:
 sqlite3 pets_database.db "SELECT * FROM cats;"

## Usage
 Run the Flask App:
 python3 app.py

 The server runs on http://127.0.0.1:5000 with debug mode enabled.


## Test Endpoints:
 se a browser, curl, or Postman to interact with the API.
 Examples:curl http://127.0.0.1:5000/cats
 curl -X POST -H "Content-Type: application/json" -d '{"name":"Moe","age":10,"breed":"Tabby","owner_id":1}' http://127.0.0.1:5000/cats

## Resources
 Flask Documentation
 SQLite Documentation
 HTTP Verbs (MDN)
 SQL Joins (W3Schools)
