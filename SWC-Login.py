from collections import defaultdict
from datetime import datetime
import logging
from cryptography.fernet import Fernet
import os

# Constants
MAX_ATTEMPTS = 3
LOG_FILE = "security_log.txt"
DKEY_FILE = "fernet.key"

# Initialize defaultdict with int — default value is 0
login_attempts = defaultdict(int)

# Simulated login attempts (from user input or logs)
attempts = ["alice", "bob", "alice", "charlie", "alice", "bob", "charlie", "david", "bob", "charlie"]

# Generate and store a key if it doesn't already exist

key = Fernet.generate_key()
with open(DKEY_FILE, "wb") as key_file:
    key_file.write(key)

# To use the key later, read it back securely and initialize the cipher object:

# Load the key
#with open(DKEY_FILE, "rb") as key_file:
#    key = key_file.read()

#cipher = Fernet(key)

# Configure logging
#	Configure the logger to write ERROR level messages to "security_log.txt" using
#    2025-05-12	10:42:31 - ERROR - User '#encryptedName#' has been locked out after 3 failed attempts.

# Track who is already locked to avoid duplicate log entries
num_locked = 0
locked_users = set()

# Simulated login attempts (can be randomized or expanded)
# security_log.txt will contain lockout entries
def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# simulated login handler
def login(user, success):
    if login_attempts[user] >= MAX_ATTEMPTS:
        print(f"***Account for '{user}' is locked!***")
        log_event(f"LOCKOUT: {user} attempted login while locked.")
        locked_users.add = user
        num_locked += 1
        return

    if success:
        print(f"{user} logged in successfully.")
        login_attempts[user] = 0  # Reset on success
    else:
        login_attempts[user] += 1
        print(f"Failed login attempt for {user} ({login_attempts[user]})")
        if login_attempts[user] >= MAX_ATTEMPTS:
            print(f"{user} has been locked out after {MAX_ATTEMPTS} failed attempts.")
            log_event(f"LOCKOUT: {timestamp} - ERROR - {user} locked out after {MAX_ATTEMPTS} failed attempts.")


# Track failed attempts using defaultdict(int)





# Process login attempts
for user in attempts:
    login_attempts[user] += 1


    if login_attempts[user] == MAX_ATTEMPTS and user not in locked_users:
        try:
            #encrypt the user before writing to the log



        except OSError as e:
            print(f"Logging failed: {e}")

# Print summary of all users and their attempt count
print("Login Attempt Summary:")
for user, count in login_attempts.items():
    print(f"{user}: {count} attempt(s)") #user is in plain text here

