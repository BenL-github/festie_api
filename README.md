# Festie API

## About

Festie API is a project to help me learn about API development, RESTful principles, SQL queries, continuous development, and containerization. The main idea behind Festie API is a music festival application that connects users to music festivals with artists that they love. Using SQL joins and aggregate functions, the API can find out music festivals that a client might be interested in. The music festival API can also find out other interesting information as well, such as the genre composition of specific music festivals.

## The Stack 

I used FastAPI because I found it very intuitive and I liked how to readily produces documentation for the API. As I was creating the API, I was also learning about development principles such as CI/CD, so I incorporated an automated test suite using GitHub workflows. The workflow creates a docker container for a PostgreSQL database so I did not need to alter the actual database hosted on Heroku.

In order to collect more data for the API, I learned how to write a Python script using the BeautifulSoup and Selenium libraries to scrape websites, specifically music festival pages, in order to find artists going to a music festival. 

## Database Design

The queries were made possible because of my knowledge from a database course I took in Oregon State University. The database has 7 tables - 2 of which are intersection tables in order to create a relation between entities. 

## Improvements 

I personally love live music so the idea of this application is very interesting to me. I would love to transform this into an actual product, or integrate this feature for a music streaming company, so more people will be connected to live music. 