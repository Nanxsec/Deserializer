# Node.js Unsafe Deserialization Payload Generator

Este script gera payloads para exploração de vulnerabilidades de **deserialização insegura no Node.js**, especialmente em aplicações que usam a biblioteca `node-serialize`. retornando um RCE

---

## 📌 Objetivo

Cria entradas maliciosas que injetam funções no backend Node.js por meio de objetos serializados, resultando em **execução remota de comandos (RCE)**.

---

## ⚙️ Funcionamento

Gera uma função JavaScript (Node.js) que estabelece uma reverse shell com o atacante.

1 - A função é formatada com a tag especial "_$$ND_FUNC$$_", usada pela biblioteca node-serialize para interpretar funções serializadas.

    Constrói e exibe dois formatos de payload:
    
    JSON puro – para uso direto em requisições.
    Base64 – ideal para injeção em cookies ou campos codificados.

No payload, ele gera dentro do campo "email" que pode ser alterado para o formato que a aplicação que for testada receberá!

## 🧪 Exemplo de uso

```bash
python3 payload.py host port
