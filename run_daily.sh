#!/bin/bash

# Path to your Python environment (if using virtualenv or conda)
# Uncomment and modify the next line if needed
# source /path/to/your/virtualenv/bin/activate

# Set the working directory
cd /Users/ivkin/my/heltmet_checker

# Replace with your target email address
EMAIL="your_email@example.com"

# Set email credentials as environment variables
# Replace these with your actual credentials
export EMAIL_ADDRESS="your_sender_email@gmail.com"
export EMAIL_PASSWORD="your_app_password"

# Run the script with the URL and email address
python helmet_checker.py https://www.motoland.rs/proizvod/31153/shoei-nxr-ii-white --email $EMAIL 