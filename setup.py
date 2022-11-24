import os

# if os.name == 'posix':
os.system("sudo apt update && sudo apt upgrade -y")
os.system(
    "sudo apt install htop wget curl git ffmpeg python3 python3-pip default-jdk nano -y")
if not (os.path.isdir("/nearbot")):
    os.makedirs("/nearbot")
    os.makedirs("/nearbot/lavalink")


os.chdir("/nearbot/lavalink")
os.system(
    'wget "https://github.com/freyacodes/Lavalink/releases/download/3.4/Lavalink.jar"')
os.system("wget ")

# Setup Near
os.chdir("/nearbot")
os.system("git clone https://github.com/hirusha-adi/Near")  # /nearbot/Near
os.chdir("/nearbot/Near")
TOKEN = input("[?] Please enter your bot token: ")
with open("/nearbot/Near/token.txt", "w", encoding="utf-8") as token_file:
    token_file.write(TOKEN)
