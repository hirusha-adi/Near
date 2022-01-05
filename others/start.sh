mkdir NearBot
cd NearBot
curl "https://raw.githubusercontent.com/hirusha-adi/Near/main/others/1-dependencies.sh" >> "1-dependencies.sh"
curl "https://raw.githubusercontent.com/hirusha-adi/Near/main/others/2-install-bot.sh" >> "2-install-bot.sh"
curl "https://raw.githubusercontent.com/hirusha-adi/Near/main/others/3-install-lavalink.sh" >> "3-install-lavalink.sh"
curl "https://raw.githubusercontent.com/hirusha-adi/Near/main/others/remove.sh" >> "remove.sh"
chmod +x "1-dependencies.sh" "2-install-bot.sh" "3-install-lavalink.sh" "remove.sh"
