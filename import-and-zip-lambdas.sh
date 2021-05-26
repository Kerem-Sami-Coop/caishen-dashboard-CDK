#!/bin/sh

#variables for where to get lambda functions
owner=Kerem-Sami-Coop
repo=caishen-lambda
# use main in the long run
tag_or_branch=develop
lambda_function_list=lambda-function-list-dev.txt

#remove and remake the artifacts file
sudo rm -r artifacts
mkdir artifacts
cd artifacts

#for each lambda function, download and zip
# TODO: for the future: remove for in the future, think of different layers etc.
for i in $(cat ../${lambda_function_list}); do
    #save the file
    wget https://raw.githubusercontent.com/${owner}/${repo}/${tag_or_branch}/${i}
    #get the filename from the i using regex
    filename=$(printf ${i} | grep  -oE "[^\/]+$" | grep -oE "[^\.py]*")
    #zip
    zip -j ${filename}.zip ${filename}.py
    #remove the unzipped file 
    rm ${filename}.py
done

#aws shenanigans
cdk synth
cdk bootstrap
cdk deploy