#!/bin/bash
echo -n "Enter Reality masking domain: "
read REALITY_DOMAIN

export REALITY_DOMAIN
export REALITY_PRIVATE=$(cat private.key)
export USER_ID=$(cat uuid.txt)

cat templates/xray-config-temp.json | envsubst > /usr/local/etc/xray/config.json
systemctl restart xray