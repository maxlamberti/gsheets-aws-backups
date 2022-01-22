#!/bin/bash


remove_build_files()
{
  echo "Removing deployment files: deployment.zip, package/"
  rm -f deployment.zip
  rm -rf ./package
}

remove_build_files

pip install --target ./package boto3 gspread
if [ $? -ne 0 ]; then
   echo "Failed to install python deployment dependencies. Check if pip is installed correctly. Aborting build."
   remove_build_files
   exit 1
fi

cd package && zip -r ../deployment.zip . && cd ..
zip -g deployment.zip lambda_function.py

if test -f google_credentials.json;
then
  echo "Adding google_credentials.json to deployment package."
  zip -g deployment.zip google_credentials.json
else
  echo "Required file google_credentials.json is missing, aborting build."
  remove_build_files
  exit 1
fi

remove_build_files
