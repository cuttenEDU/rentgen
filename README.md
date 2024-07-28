## Steps

*recommended to run everything with sudo*

1. Install everything with install.sh
2. Find acceptable (tls v1.3) masking domain with scan-domains.sh
3. Generate UUID with gen_uuid.sh (saves it into uuid.txt in the working directory, used for later scripts)
4. Generate keypair with gen_keypair.sh (saves them in the working directory, used for later scripts)
5. Generate config with genconfig-vless-xtls-reality.sh (puts it into appropriate xray system directory)
6. Verify that Xray is working with ```sudo systemctl status xray```
7. Generate Client URL with gen_vless_url.sh
8. Enjoy the radiation waves :)

*horribly undertested btw*
