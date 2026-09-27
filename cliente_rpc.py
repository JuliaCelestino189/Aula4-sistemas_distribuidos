import xmlrpc.client

servidor = xmlrpc.client.ServerProxy(
    "http://localhost:8000/"
)

print("10 + 5 =", servidor.soma(10, 5))
print("10 - 5 =", servidor.subtracao(10, 5))
print("10 x 5 =", servidor.multiplicacao(10, 5))




TERMINAL 1 — SERVIDOR

python servidor_rpc.py


Servidor RPC ativo na porta 8000...


TERMINAL 2 — CLIENTE

python cliente_rpc.py

10 + 5 = 15
10 - 5 = 5
10 x 5 = 50
