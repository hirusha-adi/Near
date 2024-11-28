# Near - A discord bot for Team SDS

<p align="center">
    <img src="https://raw.githubusercontent.com/hirusha-adi/Near-Data/refs/heads/main/images/github/github-banner.png" alt="Lisence">
    <br>
    <img src="https://img.shields.io/github/license/hirusha-adi/Near?style=for-the-badge" alt="Lisence">
    <img src="https://img.shields.io/github/last-commit/hirusha-adi/Near?style=for-the-badge" alt="Last Commit">
    <img src="https://img.shields.io/github/contributors/hirusha-adi/Near?style=for-the-badge" alt="Contributors">
</p>

# Architechture

![Untitled Diagram](https://github.com/user-attachments/assets/571eaac5-9003-40f1-b3b5-0a7a8fb704e5)

# Docker

```bash
docker-compose build # build the image 
docker-compose up -d # start application
docker-compose down  # shut down application
docker-compose logs  # view application logs
```

# Debian

```bash
# Update repositories and update all pakcges
# ---
sudo apt update && sudo apt upgrade 

# Install dependencies
# ---
sudo apt install python3 python3-pip wget htop curl git ffmpeg default-jdk nano -y

# Create required directories
# ---
mkdir ~/nearbot
mkdir ~/nearbot/lavalink

# Setup Lavalink
# ---
cd ~/nearbot/lavalink
wget "https://github.com/lavalink-devs/Lavalink/releases/download/4.0.7/Lavalink.jar"
curl 'https://raw.githubusercontent.com/hirusha-adi/Near/main/lavalink.yml' >> 'application.yml'
java -jar ./Lavalink.jar    # run normally
java -jar ./Lavalink.jar &  # run in background

# Setup Nearbot
# ---
cd ~/nearbot
git clone https://github.com/hirusha-adi/Near
cd Near
mv .env.example .env
nano .env       # fill the environment file
# optionally, create a venv and source it before doing the below step
python3 -m pip install -r requirements.txt
python3 nearbot.py      # run normaly
python3 nearbot.py &    # run in background


# Optionally, you can also keep running it in the background
# ---
bg
disown -h
```

