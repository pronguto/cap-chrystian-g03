# OIKOS-API

Uma das preocupações que um Micro-Emprendedor enfrenta na hora de iniciar um novo emprendimento é o método que utilizará para calcular os custos de produção. A maioria simplesmente calcula os seus lucros com a diferença entre o preço que pagou pelos materiais que utilizou e o preço da venda do seu produto final. Mesmo que esta simples operação aritmetica ajuda na percepção da quantidade do lucro (ou prejuizo), muitas das vezes não é exato porque pode ter um ou mais fatores que podem influir diretamente sobre o lucro assim calculado.

OIKOS foi idealizado para fazer esse cálculo e dependendo da prolixidade do usuário no fornecimento das informações, pode retornar valores muito ajustados à realidade. Esta aplicação não pretende ser "a solução de todos os problemas", porém, pode ser sim uma poderosa ferramenta para fazer o cálculo de custos de produção a partir da informação fornecida pelo usuário.

Para usar OIKOS o usuário precisará fazer um cadastro, com a única finalidade de garantir que a informação só possa ser por ele manipulada.

# Cadastro de usuário



## POST /api/users/signup - Rota responsável pelo CADASTRO do usuário.

####  Não necessita de AUTORIZAÇÃO por token 

####  Corpo da requisição:

    {
        "name": "Philip",
        "email": "example@gmail.com",
        "password": "1234"
    }

####  Corpo da resposta:


    { 
        "id": 1,
        "name": "Philip",
        "email": "example@gmail.com",
    }



---------------------------------------------------------------



## POST /api/users/signin - Rota responsável pelo LOGIN do usuário.

####  Não necessita de AUTORIZAÇÃO por token -

####  Corpo da requisição:

    {
        "email": "example@gmail.com",
        "password": "1234"
    }

####  Corpo da resposta:

    {
        "token": "370e63d575bfsdfsfesasdfa2346c1bfb973b0b61047dae3"
    }



---------------------------------------------------------------



## GET /api/users - Rota responsável pela BUSCA DO USUÁRIO.


####  Rota necessita de AUTORIZAÇÃO por token -
 

####  Requisição sem corpo:

#####  Obs: para encontrar o usuário é preciso fazer o login e utilizar o token auth.


####  Corpo da resposta:

    {

        "id": 1,
        "name": "Philip"
        "email": "example@gmail.com"

    }



---------------------------------------------------------------



## PUT /api/users - rota responsável pela ATUALIZAÇÃO de todas as informações do usuário.


####  Rota necessita de AUTORIZAÇÃO por token -
 

####  Corpo da requisição:

#####  É possível alterar o nome e a senha.

    {
        "name": "Philip02",
        "email": "example@gmail.com",
        "password": "1234567890"
    }


####  Corpo da resposta:

    {
    	"id": 1,
    	"name": "Philip02",
    	"email": "example@gmail.com"
    }



---------------------------------------------------------------



## DELETE /api/users - Rota responsável por DELETAR O USUÁRIO.


####  Requisição sem corpo:

#####   -     Obs: para deletar o usuário é preciso fazer o login e utilizar o token auth.

####  Corpo da resposta:

    
    {
        "message": "User Philip has been deleted."
    }
    

---------------------------------------------------------------
---------------------------------------------------------------

# Ingredientes

## CADASTRO DE INGREDIENTES

### POST /api/ingredients - Rota responsável pelo CADASTRO de ingrediente.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json 

    {
        "ingredient_name":"Fermento",
        "measurement_unit":"G"
    }

```

####  Corpo da resposta - STATUS CODE 201 - CREATED:


```json 

    {
        "ingredient_id": 1,
        "ingredient_name": "fermento",
        "measurement_unit": "g"
    }

```

1- A unidade de medida passada deve ser apenas a sigla

### Possíveis erros

Caso o nome de uma das chaves esteja incorreta.

POST /api/ingredients - FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 
    {
        "expected keys": [
            "measurement_unit",
            "ingredient_name"
        ],
        "recived keys": [
            "measurement_unit",
            "ingredients_name"
        ]
    }

```

Ingrediente já cadastrado:  

POST /api/ingredients - FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json 

    {
        "msg": "ingredient already exists"
    }

```
---------------------------------------------------------------

## BUSCA DE INGREDIENTES

### GET /api/ingredients - Rota responsável pela BUSCA de ingrediente.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

####  Corpo da resposta - STATUS CODE 200 - OK:

```json 

    [
        {
            "ingredient_id": 1,
            "ingredient_name": "trigo",
            "measurement_unit": "g",
            "purchases": [
                {
                    "purchase_id": 1,
                    "purchase_price": 50.0,
                    "purchase_quantity": 10.0
                },
                {
                    "purchase_id": 2,
                    "purchase_price": 30.0,
                    "purchase_quantity": 5.0
                },
                {
                    "purchase_id": 3,
                    "purchase_price": 35.0,
                    "purchase_quantity": 5.0
                }
            ]
        },
        {
            "ingredient_id": 2,
            "ingredient_name": "fermento",
            "measurement_unit": "g",
            "purchases": [
                {
                    "purchase_id": 1,
                    "purchase_price": 36.0,
                    "purchase_quantity": 3.0
                }
            ]
        }
    ]

```

### GET /api/ingredients/trigo - Rota responsável pela BUSCA de ingrediente.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

####  Corpo da resposta - STATUS CODE 200 - OK:

```json 

    [
        {
            "ingredient_id": 1,
            "ingredient_name": "trigo",
            "measurement_unit": "g",
            "purchases": [
                {
                    "purchase_id": 1,
                    "purchase_price": 50.0,
                    "purchase_quantity": 10.0
                },
                {
                    "purchase_id": 2,
                    "purchase_price": 30.0,
                    "purchase_quantity": 5.0
                },
                {
                    "purchase_id": 3,
                    "purchase_price": 35.0,
                    "purchase_quantity": 5.0
                }
            ]
        }
    ]

```
### Possíveis erros


Ingrediente não encontrado:  

GET /api/ingredients/trigosed - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json 

    {
        "Error": "Ingredient not found"
    }

```

---------------------------------------------------------------

## ATUALIZAÇÃO DE INGREDIENTES

### PATCH /api/ingredients - Rota responsável pela ATUALIZAÇÃO do ingrediente.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json 

    {
        "ingredient_name":"Fermento",
        "measurement_unit":"kg"
    }

```
####  Corpo da resposta:

```json 

    {
        "ingredient_id": 1,
        "ingredient_name": "fermento",
        "measurement_unit": "kg"
    }

```
### Possíveis erros

Caso o nome de uma das chaves esteja incorreta.

PATCH /api/ingredients - FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 
    {
        "expected keys": [
            "measurement_unit",
            "ingredient_name"
        ],
        "recived keys": [
            "measurement_unit",
            "ingredients_name"
        ]
    }

```

Ingrediente não encontrado:  

PATCH /api/ingredients - FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json 

    {
        "msg": "error, ingredient not found"
    }

```

Caso não exista o ingrediente.

PATCH /api/ingredients - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json 

    {
        "Error": "Ingredient not found"
    }

```

---------------------------------------------------------------

## DELEÇÃO DE INGREDIENTES

### DELETE /api/ingredients/<name> - Rota responsável pela DELEÇÃO de ingrediente.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

####  Não possui corpo de resposta

### Possíveis erros

Caso não exista o ingrediente.

DELETE /api/ingredients/<name> - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json 

    {
        "Error": "Ingredient not found"
    }

```

---------------------------------------------------------------
---------------------------------------------------------------


# Purchases

## REGISTRANDO UMA COMPRA 

### POST /api/purchases - Rota responsável pelo REGISTRO de uma compra.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json 

```

####  Corpo da resposta - STATUS CODE 201 - CREATED:


```json 

    {   
	    "purchase_date": "Tue, 03 May 2022 00:00:00 GMT",
	    "purchase_id": 1
    }

```

---------------------------------------------------------------

## REGISTRANDO UMA COMPRA

### POST /api/purchases/purchase_id - Rota responsável pelo REGISTRO de uma compra pelo ID.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN
*OBS - NECESSITA DE UM ID DO PURCHASE

#### Corpo da requisição:

```json 

    {
        "ingredient_name": "trigo",
        "purchase_quantity": 3,
        "purchase_price": 25
    }

```

####  Corpo da resposta - STATUS CODE 201 - CREATED:


```json 

    {
        "compras": [
            [
                {
                    "ingredient_id": 1,
                    "purchase_id": 1,
                    "purchase_price": 25.0,
                    "purchase_quantity": 3.0
                }
            ]
        ],
        "purchase_date": "Tue, 03 May 2022 00:00:00 GMT",
        "purchase_id": 1
    }

```
### Possíveis erros

Caso a compra for utilizando um purchase_id que não exista:

POST /api/purchase/purchase_id - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json

    {

	    "detail": "id not found"

    }

```

Caso o nome de uma das chaves esteja incorreta.

POST /api/purchase/purchase_id - FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 

    {
        "expected keys": [
            "ingredient_name",
            "purchase_price",
            "purchase_quantity"
        ],
        "recived keys": [
            "purchase_price",
            "ingrediente_nome",
            "purchase_quantity"
        ]
    }

```

Caso seja feita a compra do mesmo ingredient no mesmo id

POST /api/purchase/purchase_id - FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json

    {
	    "detail": "o mesmo ingredient vem sendo comprado mais de uma vez"
    }  

```

## BUSCA DE COMPRAS

### GET /api/purchases - Rota responsável pela BUSCA de compras.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

####  Corpo da resposta - STATUS CODE 200 - OK:

```json
    ]
            {
            "Purchases": [
                {
                    "ingredient_id": 1,
                    "ingredient_name": "trigo",
                    "purchase_id": 19,
                    "purchase_price": 25.0,
                    "purchase_quantity": 3.0
                },
                {
                    "ingredient_id": 1,
                    "ingredient_name": "manteiga",
                    "purchase_id": 19,
                    "purchase_price": 25.0,
                    "purchase_quantity": 3.0
                }
            ],
            "price_total": 50.0,
            "purchase_date": "Tue, 03 May 2022 00:00:00 GMT",
            "purchase_id": 19
        }
    ]

```

### GET /api/purchases/?initial_date=25-04-2022&final_date=30-05-2022 - Rota responsável pela BUSCA de compras.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

####  Corpo da resposta - STATUS CODE 200 - OK:

```json

    [
        {
            "ingredient_id": 1,
            "ingredient_name": "trigo",
            "purchase_date": "Tue, 03 May 2022 00:00:00 GMT",
            "purchase_id": 1,
            "purchase_price": 25.0,
            "purchase_quantity": 3.0
        },
        {
            "ingredient_id": 4,
            "ingredient_name": "manteiga",
            "purchase_date": "Tue, 03 May 2022 00:00:00 GMT",
            "purchase_id": 1,
            "purchase_price": 8.0,
            "purchase_quantity": 3.0
        },
        {
            "ingredient_id": 5,
            "ingredient_name": "ovo",
            "purchase_date": "Tue, 03 May 2022 00:00:00 GMT",
            "purchase_id": 1,
            "purchase_price": 20.0,
            "purchase_quantity": 30.0
        }
    ]


```

### Possíveis erros


parametros diferentes de data:  

GET /api/purchases/?initial_date=qualquercoisa&final_date=30-05-2022- FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json 

   {
	    "detail": "start date or end date is not valid"
   }

```

---------------------------------------------------------------

## ATUALIZAÇÃO DE UMA COMPRA

### PATCH /api/purchases/id - Rota responsável pela ATUALIZAÇÃO do ingrediente.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json 

    {
   	    "purchase_price": 22,
	    "purchase_quantity": 10
    }

```
####  Corpo da resposta:

```json 

    {
        "ingredient_id": 1,
        "purchase_id": 3,
      	"purchase_price": 22.0,
	    "purchase_quantity": 10.0
    }

```

### Possíveis erros

Caso seja passado id que não exista:

POST /api/purchase/purchase_id - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json

    {

	    "detail": "purchases not found"

    }

```

Caso o nome de uma das chaves esteja incorreta ou contenha chaves a mais ele as ignora

POST /api/purchase/purchase_id - FORMATO DA RESPOSTA - STATUS 200 - OK

#### Corpo da requisição:

```json

    {
        "purchase_quantity": 100,
        "compra_preco": 25	
    }

```
####  Corpo da resposta:

```json 

    {
    	"ingredient_id": 2,
        "purchase_id": 30,
        "purchase_price": 20.0,
        "purchase_quantity": 100.0
    }

```

## DELEÇÃO DE UMA COMPRA

### DELETE /api/purchases/id - Rota responsável pela DELEÇÃO da compra.

*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

####  Não possui corpo de resposta

### Possíveis erros

Caso não exista a compra.

DELETE /api/purchases/id - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json 

    {
        "Error": "purchases not found"
    }

```