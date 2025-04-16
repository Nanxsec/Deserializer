# Node.js Unsafe Deserialization Payload Generator

Este script gera payloads para exploração de vulnerabilidades de **deserialização insegura no Node.js**, especialmente em aplicações que usam a biblioteca `node-serialize`.


---

## 📌 Objetivo

Cria entradas maliciosas que injetam funções no backend Node.js por meio de objetos serializados, resultando em **execução remota de comandos (RCE)**.

---

## ⚙️ Funcionamento

1. Recebe um **comando shell** como argumento.
2. Constrói um objeto JavaScript malicioso com a sintaxe especial usada por `node-serialize`:  
   `_$$ND_FUNC$$_function() { ... }()`
3. Insere o payload dentro de um campo `email`. --> Pode alterar o campo de acordo com a entrada!
4. Codifica tudo em **Base64**, pronto para ser injetado como valor do cookie de sessão.

---

## 🧪 Exemplo de uso

```bash
python3 payload.py host port
