# Projeto E-commerce 
Um projeto de e-commerce feito com Django 6.1.1 e Python 3.14.5.

### Conteúdo educacional
Este conteúdo foi criado no [Curso de Python 3 - Do Básico Ao Avançado (Completo)](https://www.udemy.com/course/python-3-do-zero-ao-avancado/) sem a intenção de 
ser utilizado em produção, mas como recurso educacional ensinado no meu curso.

Isso não impede que você baixe, altere, use e/ou distribua o seu conteúdo conforme preferir.

### Este projeto NÃO inclui
Abaixo uma lista de recursos que não adicionei ainda e que você pode me ajudar a adicionar.

- Combinações de variações de produto (tem apenas uma variação)
- Cupons de desconto no carrinho de compras
- Cálculo de frete
- Métodos de pagamento (MercadoPago, PayPal, PagSeguro, enfim...)

### TODOs
Abaixo uma lista do que adicionei ou ainda pretendo adicionar.

- [x] Model produtos
- [x] Model variações
- [x] Listagem e detalhes de produtos e variações
- [x] Carrinho de compras baseado em session
- [x] Remover produtos do carrinho
- [x] Model perfil (criar e atualizar)
- [x] Login e Logout do cliente
- [x] Registrar pedido do cliente
- [x] Página de pagamento

### Tutorial para iniciantes
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git (Windows, Linux e Mac) e depois:

```
git clone https://github.com/luizomf/django-simple-ecommerce.git
```

- Para **Windows**:

```
cd django-simple-ecommerce
python -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Para **Linux / Mac**:

```
cd django-simple-ecommerce
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Pronto!
Agora abra o link http://127.0.0.1:8000 no seu navegador!