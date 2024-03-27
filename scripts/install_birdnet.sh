#!/usr/bin/env bash
# Install BirdNET script
set -x # Debugging
exec > >(tee -i installation-$(date +%F).txt) 2>&1 # Make log
set -e # exit installation if anything fails

my_dir=$HOME/BirdNET-Pi
export my_dir=$my_dir

cd $my_dir/scripts || exit 1

if [ "$(uname -m)" != "aarch64" ];then
  echo "BirdNET-Pi requires a 64-bit OS.
It looks like your operating system is using $(uname -m),
but would need to be aarch64.
Please take a look at https://birdnetwiki.pmcgui.xyz for more
information"
  exit 1
fi

#Install/Configure /etc/birdnet/birdnet.conf
./install_config.sh || exit 1
sudo -E HOME=$HOME USER=$USER ./install_services.sh || exit 1
source /etc/birdnet/birdnet.conf

install_birdnet() {
  cd ~/BirdNET-Pi || exit 1
  echo "Establishing a python virtual environment"
  python3 -m venv birdnet
  source ./birdnet/bin/activate
  pip3 install -U -r $HOME/BirdNET-Pi/requirements.txt

  # Define the lines to be added to rc.local
  lines_to_add=(
    "~/BirdNET-Pi/birdnet/bin/python /home/sparrow/BirdNET-Pi/scripts/utils/power_on.py
    "~/BirdNET-Pi/birdnet/bin/python /home/sparrow/BirdNET-Pi/scripts/utils/open.py"
  )

  # Loop through the lines and add them to rc.local
  for line in "${lines_to_add[@]}"; do
    # Check if the line already exists in rc.local
    if grep -Fxq "$line" /etc/rc.local; then
        echo "Line already exists in rc.local"
    else
        # Add the line to rc.local
        sudo sed -i '$i '"$line"'' /etc/rc.local
        echo "Line added to rc.local"
    fi
  done

}


[ -d ${RECS_DIR} ] || mkdir -p ${RECS_DIR} &> /dev/null

install_birdnet

cd $my_dir/scripts || exit 1

./install_language_label_nm.sh -l $DATABASE_LANG || exit 1

exit 0
