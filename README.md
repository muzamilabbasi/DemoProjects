# Introduction

This challenge is to do a simple REST implementation of https://macaddress.io/. The first and foremost step is to sign up at https://macaddress.io/ .After a sign up it provides you an api-key which is used in order to manipulate the rest api calls

# Directory Structure
The Directory structure for this project is as defined.

![201507431-6f4d95b3-07c7-4404-92b1-978b2b757134](https://user-images.githubusercontent.com/2918618/201507624-71b8019a-5d33-45c2-958c-c52bf1ff595b.png)


- api_key.env: This file contains the api_key as an environment variable
- Dockerfile: The Dockerfile has all the dependencies it requires to spin it up in a container
- getMacAddressInfo.sh: Takes one parameter which is a MAC Address and returns CompanyName with MAC Address
- set_env.sh: This is environment setup if you running the 'getMacAddressInfo.sh' locally without Docker

# Dependecies:

- Linux / Unix
- [Curl] (http://help.ubidots.com/en/articles/2165289-learn-how-to-install-run-curl-on-windows-macosx-linux)
- [jq] (https://stedolan.github.io/jq/download/)
- [api_key] (https://macaddress.io/api/documentation/making-requests)
  
# How to run

## To run locally follow the steps:
**Assuming you have cloned the repository and have an api-key** 

- Open **api_key.env** file and add your api_key to `export API_KEY="YourApiKey"` and save the file, then 
- source `api_key.env`
- `./set_env.sh`
- `./getMacAddressInfo.sh "Your Mac Address"`
  
**The output is written down on terminal and also a file called companyName is created which contains the OUI and CompanyName details as well**

## To run on Docker
**Assuming you have cloned the repository and have an api-key** 

- Open **api_key.env** file and add your api_key to `export API_KEY="YourApiKey"` and save the file, then 
- source `api_key.env`
- `docker build . --build-arg API_KEY=$API_KEY -t brightsigndemo`
- `docker run -it brightsigndemo /bin/bash ./getMacAddressInfo.sh "You Mac Address"`
  
**The output is written down on terminal and also a file called companyName is created which contains the OUI and CompanyName details as well**

# Security
There are many ways to improve security here, one of it that I will mention is setting a Rate Limit.
Implement a code that actually errors out if you have constant submission of the API request. For example doing a CURL twice or hitting the api endpoint using same credentials from different systems. There are many ways and many algorithms to implement a rate limiter if I were to implement one, I would following something similar in python https://akshayranganath.github.io/Rate-Limiting-With-Python/#:~:text=control%20the%20rate%20of%20requests,the%20limit%20are%20generally%20documented. with restAPI implementation.

