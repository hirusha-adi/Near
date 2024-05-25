# DO NOT RUN THIS FILE!
#
#
#  #####  ####### ####### ######  
# #     #    #    #     # #     # 
# #          #    #     # #     # 
#  #####     #    #     # ######  
#       #    #    #     # #       
# #     #    #    #     # #       
#  #####     #    ####### #       
#
# 
# DO NOT RUN THIS FILE!
# THIS FILE DOES NOT WORK.                                 
# THIS FILE WILL BE REMOVED IN THE NEXT RELEASE!
# DO NOT RUN THIS FILE!
#

import os


def setup_base():
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system(
        "sudo apt install htop wget curl git ffmpeg python3 python3-pip default-jdk nano -y")
    os.makedirs("/nearbot")
    os.makedirs("/nearbot/lavalink")


def setup_lavalink():
    os.chdir("/nearbot/lavalink")
    os.system(
        'wget "https://github.com/lavalink-devs/Lavalink/releases/download/4.0.5/Lavalink.jar"')
    os.system(
        "curl 'https://raw.githubusercontent.com/hirusha-adi/Near/main/lavalink.yml' >> 'application.yml'")
    os.system("java -jar ./Lavalink.jar &")


def setup_near():
    os.chdir("/nearbot")
    os.system("git clone https://github.com/hirusha-adi/Near")  # /nearbot/Near
    os.chdir("/nearbot/Near")
    TOKEN = input("[?] Please enter your bot token: ")
    with open("/nearbot/Near/token.txt", "w", encoding="utf-8") as token_file:
        token_file.write(TOKEN)
    os.system("python3 -m pip install -r requirements.txt")
    os.system("python3 nearbot.py &")


def finalize():
    os.system("bg")
    os.system("disown -h")


def main():
    setup_base()
    setup_lavalink()
    setup_near()
    finalize()
