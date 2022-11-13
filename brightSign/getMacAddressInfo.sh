#!/bin/bash

export address=$1


echo "Printing out Company Name for Mac Address"
curl https://api.macaddress.io/v1\?apiKey\=$API_KEY\&output\=json\&search\=$address  | jq ."vendorDetails | .oui, .companyName" 


echo "Writing it down inside a file in $PWD"
curl https://api.macaddress.io/v1\?apiKey\=$API_KEY\&output\=json\&search\=$address  | jq ."vendorDetails | .oui, .companyName" > companyName
