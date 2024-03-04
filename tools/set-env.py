import sys
import os

# Get the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Add the current directory to the Python path
sys.path.append(current_directory)

# Replace the following values with your actual MySQL database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "medibot"

# Set the environment variables
os.environ["DB_HOST"] = DB_HOST
os.environ["DB_USER"] = DB_USER
os.environ["DB_PASSWORD"] = DB_PASSWORD
os.environ["DB_NAME"] = DB_NAME
