
import getpass
import os

username = input("Choose your Admin username: ").strip()
password = getpass.getpass("Choose an Admin password (12+ characters): ")
confirm = getpass.getpass("Confirm Admin password: ")

if password != confirm:
    raise SystemExit("Passwords do not match.")

if len(password) < 12:
    raise SystemExit("Password must be at least 12 characters.")

os.environ["BOOTSTRAP_ADMIN_USERNAME"] = username
os.environ["BOOTSTRAP_ADMIN_PASSWORD"] = password

try:
    from dashboard.auth import initialize_database, bootstrap_first_admin

    initialize_database()

    if bootstrap_first_admin():
        print("Initial Admin created successfully.")
    else:
        print("No Admin created. A user may already exist in the database.")
finally:
    os.environ.pop("BOOTSTRAP_ADMIN_USERNAME", None)
    os.environ.pop("BOOTSTRAP_ADMIN_PASSWORD", None)
