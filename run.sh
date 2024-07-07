#!/bin/bash

# Check if the project name argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <project_name>"
  exit 1
fi

# Set the project name
PROJECT_NAME=$1

# Define the base directory containing your Streamlit apps
APP_BASE_DIR="./src"

# Determine the path to the main.py file based on the project name
case $PROJECT_NAME in
  data_analysis)
    APP_FILE="${APP_BASE_DIR}/data_analysis/main.py"
    ;;
  building_bonds)
    APP_FILE="${APP_BASE_DIR}/building_bonds/main.py"
    ;;
  resume_screening)
    APP_FILE="${APP_BASE_DIR}/resume_screening/main.py"
    ;;
  ingredient_to_recipe)
    APP_FILE="${APP_BASE_DIR}/ingredient_to_recipe/main.py"
    ;;
  *)
    echo "Unknown project name: $PROJECT_NAME"
    exit 1
    ;;
esac

# Check if the Streamlit app file exists
if [ ! -f "$APP_FILE" ]; then
  echo "Streamlit app file not found: $APP_FILE"
  exit 1
fi

# Run the Streamlit application
streamlit run "$APP_FILE"