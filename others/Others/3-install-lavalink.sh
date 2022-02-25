mkdir LavalinkServer
cd LavalinkServer
wget "https://github.com/freyacodes/Lavalink/releases/download/3.4/Lavalink.jar"
curl "https://raw.githubusercontent.com/hirusha-adi/Near/main/others/application.yml" >> "application.yml"
cd ..
clear
echo "You can now start Lavalink, run the commands below"
echo "cd LavalinkServer"
echo "java -jar ./Javalink.jar"
echo "Ctrl+Z"
echo "bg"
echo "disown -h"
