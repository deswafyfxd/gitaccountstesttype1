import requests
import os

# List of GitHub usernames to check
usernames = ["username1", "username2", "username3"]

# Discord webhook URL
webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

def check_account_status(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 404:
        return "Suspended"
    else:
        return "Active"

def send_discord_message(message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        raise Exception(f"Failed to send message to Discord: {response.status_code}")

def main():
    suspended_accounts = []
    for username in usernames:
        status = check_account_status(username)
        if status == "Suspended":
            suspended_accounts.append(username)
    
    if suspended_accounts:
        message = f"Suspended accounts found: {', '.join(suspended_accounts)}"
        send_discord_message(message)

if __name__ == "__main__":
    main()
