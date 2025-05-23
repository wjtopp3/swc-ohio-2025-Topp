from collections import defaultdict
from datetime import datetime
import logging
from cryptography.fernet import Fernet
import os

# Constants
MAX_ATTEMPTS = 3
LOG_FILE = "security_log.txt"
KEY_FILE = "fernet.key"

# Generate and store a key if it doesn't already exist


# Configure logging
#	Configure the logger to write ERROR level messages to "security_log.txt" using
#2025-05-12	10:42:31 - ERROR - User '#encryptedName#' has been locked out after 3 failed attempts.



# Simulated login attempts (can be randomized or expanded)



# Track failed attempts using defaultdict(int)



# Track who is already locked to avoid duplicate log entries
locked_users = set()

# Process login attempts
for user in attempts:
    #add code here


    if login_attempts[user] == MAX_ATTEMPTS and user not in locked_users:
        try:
            #encrypt the user before writing to the log



        except OSError as e:
            print(f"Logging failed: {e}")

# Print summary of all users and their attempt count
print("Login Attempt Summary:")
for user, count in login_attempts.items():
    print(f"{user}: {count} attempt(s)") #user is in plain text here

