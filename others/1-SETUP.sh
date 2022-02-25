sudo apt update && sudo apt upgrade -y
sudo apt install htop wget curl git ffmpeg python3 python3-pip default-jdk nano -y
cd ~
mkdir NearBot && cd NearBot
https://github.com/hirusha-adi/Near
cd Near
pip3 install -r requirements.txt
nano token.txt
cd ..
mkdir Lavalink && cd Lavalink
wget "https://github.com/freyacodes/Lavalink/releases/download/3.4/Lavalink.jar"
curl "https://raw.githubusercontent.com/hirusha-adi/Near/main/others/application.yml" >> "application.yml"
