#!/bin/bash
echo "Installing XRAY core..."
bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install
systemctl enable xray
systemctl restart xray


echo "Installing RealiTLScanner..."
wget https://github.com/XTLS/RealiTLScanner/releases/download/v0.2.1/RealiTLScanner-linux-64 -O ./RealiTLScanner
