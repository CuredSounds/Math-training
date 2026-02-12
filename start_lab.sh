#!/bin/bash

# Define colors
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Lab in a Box...${NC}"

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first."
    exit 1
fi

# Check for venv directory
if [ ! -d ".venv" ]; then
    echo -e "${GREEN}Creating virtual environment...${NC}"
    python3 -m venv .venv
fi

# Activate venv
source .venv/bin/activate

# Install dependencies
echo -e "${GREEN}Checking dependencies...${NC}"
pip install -r requirements.txt --quiet

# Run the dashboard
echo -e "${GREEN}Launching Dashboard...${NC}"
streamlit run src/app/dashboard.py
