import requests
import os

# List of GitHub usernames to check
usernames = [
    "username1", "username2", "username3", "username4", "username5",
    "username6", "username7", "username8", "username9", "username10",
    "username11", "username12", "username13", "username14", "username15",
    "username16", "username17", "username18", "username19", "username20",
    "username21", "username22", "username23", "username24", "username25",
    "username26", "username27", "username28", "username29", "username30",
    "username31", "username32", "username33", "username34", "username35",
    "username36", "username37", "username38", "username39", "username40",
    "username41", "username42", "username43", "username44", "username45",
    "username46", "username47", "username48", "username49", "username50",
    "username51", "username52", "username53", "username54", "username55",
    "username56", "username57", "username58", "username59", "username60",
    "username61", "username62", "username63", "username64", "username65",
    "username66", "username67", "username68", "username69", "username70",
    "username71", "username72", "username73", "username74", "username75",
    "username76", "username77", "username78", "username79", "username80",
    "username81", "username82", "username83", "username84", "username85",
    "username86", "username87", "username88", "username89", "username90",
    "username91", "username92", "username93", "username94", "username95",
    "username96", "username97", "username98", "username99", "username100",
    "username101", "username102", "username103", "username104", "username105",
    "username106", "username107", "username108", "username109", "username110",
    "username111", "username112", "username113", "username114", "username115",
    "username116", "username117", "username118", "username119", "username120",
    "username121", "username122", "username123", "username124", "username125",
    "username126", "username127", "username128", "username129", "username130",
    "username131", "username132", "username133", "username134", "username135",
    "username136", "username137", "username138", "username139", "username140",
    "username141", "username142", "username143", "username144", "username145",
    "username146", "username147", "username148", "username149", "username150"
]

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
        message = f"Suspended accounts found on Second 50: {', '.join(suspended_accounts)}"
        send_discord_message(message)

if __name__ == "__main__":
    main()
