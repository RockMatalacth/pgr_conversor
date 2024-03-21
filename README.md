# pgr_conversor
-- Consultas API + Json -- 

Aplicação de RPA(Robotic Process Automation), cujo propósito foi uma consulta de cotações de moedas. 
A moeda referida no código foi o Dólar(USD) para Real(R$), sucedido por uma conversão de Bitcoin(BTC) para Real.

O módulo requests do Python é utilizado para enviar solicitações HTTP a APIs da web e obter informações de cotação de moedas. Quando se faz solicitações HTTP, o módulo requests demonstra a simplicidade e eficácia, facilitando e tornando mais eficiente a interação com APIs externas. Entender o código é fácil e conciso, facilitando a compreensão de seu funcionamento e sua manutenção futura. Além disso, o método .json() é usado para automaticamente analisar as respostas JSON fornecidas pelas APIs, simplificando o processo de extração de dados. De forma simplificada, o uso do módulo requests torna mais fácil a comunicação com APIs da web em projetos de desenvolvimento de software.


Este código realiza as seguintes etapas:

-Importação de módulos: 
+Importa o módulo requests, que é uma biblioteca em Python usada para fazer solicitações HTTP, e também importa dois módulos locais chamados Json_dolar e Json_Bitcoin (não fornecidos no código).

-Requisições HTTP:
+Realiza duas requisições GET para duas URLs diferentes: uma para obter a cotação do dólar em reais (USD-BRL) e outra para obter a cotação do bitcoin em dólares (BTC-USD).
+As requisições são feitas usando o método requests.get(), que faz uma solicitação HTTP GET para o servidor especificado na URL e retorna a resposta.

-Extração de dados JSON:
+Converte o conteúdo da resposta HTTP para formato JSON usando o método json().
+Os dados JSON contêm informações sobre as cotações do dólar e do bitcoin.

-Cálculo do valor do bitcoin em reais:
+Extrai os valores de oferta (bid) do dólar e do bitcoin das respostas JSON.
+Multiplica o valor do bitcoin em dólares pelo valor do dólar em reais para obter o valor do bitcoin em reais.

-Impressão dos resultados:
+Imprime as informações sobre a cotação do dólar e do bitcoin, incluindo o nome da moeda e o valor da cotação.
+Imprime o valor do bitcoin em reais.
