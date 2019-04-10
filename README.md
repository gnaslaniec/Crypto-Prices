# Crypto-Prices
Site feito em Django que consome a API do CryptoCompare e exibe notícias e preços de algumas criptomoedas.

### Pré-requisitos e uso

Os requisistos são o Python na versão 3+ e instalar O Django e a biblioteca Requests através do requiriments.txt
 
Criar um ambiente virtual
```
$ virtualenv venv
```
Instalar as dependências
```
$ pip install -r requirements.txt
```
E para executar basta executar
```
$ python manage.py runserver
```

Para pesquisar uma moeda, deve digitar a abreviação da moeda no campo de pesquisa, por exemplo "BTC" para Bitcoin, "ETH" para Ethereum...
