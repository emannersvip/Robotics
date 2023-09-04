#!/bin/bash

REGULAR_USER=${SUDO_USER:-${USER}}
REGULAR_USER_HOME=/home/${SUDO_USER:-${USER}}
SSH_DIR=/home/${REGULAR_USER}/.ssh
SSH_AUTH=$SSH_DIR/authorized_keys

echo "--Bootstrapping $HOSTNAME..."

echo "--Checking for SSH keys in $SSH_AUTH"
if test -f "$SSH_AUTH"; then
	echo '--No need to setup SSH keys'
else
	echo '--Setting up SSH keys...'
	mkdir $SSH_DIR
	chmod 700 $SSH_DIR
	touch $SSH_AUTH
	cat << EOF > $SSH_AUTH
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXP7oE/7jhnxcQXNVYzTC0ZbtHV2m9sMin7rSel+byUw3jDss5FwpSkjD8/2NKxojjsONybyC0DHNB8pzhuu/oMJuwR/s48t77cW305TfR7z4uwlim1I0BlX7u8oPop1DhFG/M2H6Gequ8Wi2FtlSvmDlclUgireIpHQypgG/8AL8BxujxNZVeK0t9yHDIXESw/btii45KzqXsU3P21zGzBNB4ZR145wcL+/J/lAlRBwD5ex9B08JJvatyLFlTZXOo0gHqO25+tkVLgaWI9Ou7Q5TgrWuFPNJb+M5/kgni0YokzwZ0pG06G4Fk+d9zGT4rv/8RaxKVt3f5czkQRVIp emanners@work_ubuntu
EOF
fi

apt update
echo '--Update apt cache. Pleae run "sudo apt upgrade"'
apt -y upgrade

echo '--Adding Pi camera software...'
apt -y install vim git

echo '--Adding Pi camera software...'
# https://github.com/raspberrypi/picamera2#installation
apt install -y python3-picamera2 --no-install-recommends
 
echo '--Initialize GIT environment'
if test -f "${REGULAR_USER_HOME}/Code"; then
	echo "--No need to setup ${REGULAR_USER_HOME}, it already exists"
else
	echo "--Creating Code directory: ${REGULAR_USER_HOME}/Code"
	sudo --user=${REGULAR_USER} mkdir ${REGULAR_USER_HOME}/Code
	cd ${REGULAR_USER_HOME}/Code
	if test -f "${REGULAR_USER}/Code/Robotics"; then
		echo '--Git environment already setup'
	else
		sudo --user=${REGULAR_USER} git clone https://github.com/emannersvip/Robotics.git 
	fi
fi

if test -f "${SSH_DIR}/id_ecdsa"; then
	echo '--It looks like SSH keys are already in place' 
else
	echo '--It looks like SSH keys are *NOT* setup. Copy SSH keys at first convenience'
fi


UNNEEDED_SVCS='avahi-daemon cups bluetooth'
systemctl stop ${UNNEEDED_SVCS}
systemctl disable ${UNNEEDED_SVCS}


