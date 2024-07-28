import json
import argparse

URL_TEMPLATE = '''
vless://%(uuid)s@%(ip)s:443/?encryption=none&type=tcp&sni=%(reality_domain)s&fp=chrome&security=reality&alpn=h2&flow=xtls-rprx-vision&pbk=%(reality_pubkey)s&packetEncoding=xudp
'''

DEFAULT_XRAY_PATH = "/usr/local/etc/xray/config.json"


parser = argparse.ArgumentParser(
    prog="VLESS URL Generator",
    description="Generates URL for VLESS clients from XRay config file"
)


parser.add_argument("--config_path",type=str,default=DEFAULT_XRAY_PATH,
                    help=f"Path for XRay config (default is {DEFAULT_XRAY_PATH})")
parser.add_argument("server_ip",type=str,help="External server address")
parser.add_argument("pubkey",type=str,help="Reality public key")


if __name__ == "__main__":
    args = parser.parse_args()

    url_args = {"ip":args.server_ip,"reality_pubkey":args.pubkey}

    with open(args.config_path) as file:
        config = json.load(file)
    
    url_args["uuid"] = config["inbounds"][0]["settings"]["clients"][0]["id"]
    url_args["reality_domain"] = config["inbounds"][0]["streamSettings"]["realitySettings"]["serverNames"][0]

    print(URL_TEMPLATE % url_args)

