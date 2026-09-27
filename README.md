# Aula4_Sistemas_distribuido_Cliente-servidor
Nesta aula, foi realizada uma atividade prática sobre **RPC (Remote Procedure Call)** utilizando Python e a biblioteca `xmlrpc`. Foi desenvolvido um servidor RPC responsável por disponibilizar funções de soma, subtração e multiplicação na porta 8000.

Em seguida, foi criado um cliente RPC utilizando `xmlrpc.client`, responsável por se conectar ao servidor e executar remotamente as funções disponibilizadas. A comunicação foi testada utilizando dois terminais: um para executar o servidor e outro para executar o cliente.

Ao final, foram obtidos os resultados das operações 10 + 5 = 15, 10 - 5 = 5 e 10 × 5 = 50, comprovando o funcionamento da comunicação entre cliente e servidor.

A atividade permitiu compreender na prática o conceito de **chamada de procedimentos remotos**, no qual o cliente solicita a execução de funções disponibilizadas por um servidor.
