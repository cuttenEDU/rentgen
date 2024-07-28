output=$(xray x25519)
readarray -t keys <<<"$output"
privatekey=${keys[0]:13}
publickey=${keys[1]:12}

private_file=private.key
public_file=pub.key

echo Private key: $privatekey
echo Public key: $publickey

echo Saving private key to $private_file
echo ${privatekey} > $private_file
echo Saving public key to $public_file
echo ${publickey} > $public_file