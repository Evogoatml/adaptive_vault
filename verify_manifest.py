# verify_manifest.py
import json, base64, os
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

def verify_manifest(manifest_path, sig_path, pubkey_path="keys/pubkey.pem"):
    if not os.path.exists(manifest_path) or not os.path.exists(sig_path):
        raise FileNotFoundError("manifest or signature missing")
    with open(manifest_path, "rb") as f:
        manifest = f.read()
    with open(sig_path, "rb") as f:
        sig = base64.b64decode(f.read())
    pub = Ed25519PublicKey.from_public_bytes(open(pubkey_path,"rb").read())
    try:
        pub.verify(sig, manifest)
        return json.loads(manifest)
    except Exception as e:
        raise ValueError("Manifest signature invalid") from e
