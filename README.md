# OIKOS-API

Uma das preocupações que um Micro-Emprendedor enfrenta na hora de iniciar um novo emprendimento é o método que utilizará para calcular os custos de produção. A maioria simplesmente calcula os seus lucros com a diferença entre o preço que pagou pelos materiais que utilizou e o preço da venda do seu produto final. Mesmo que esta simples operação aritmetica ajuda na percepção da quantidade do lucro (ou prejuizo), muitas das vezes não é exato porque pode ter um ou mais fatores que podem influir diretamente sobre o lucro assim calculado.

OIKOS foi idealizado para fazer esse cálculo e dependendo da prolixidade do usuário no fornecimento das informações, pode retornar valores muito ajustados à realidade. Esta aplicação não pretende ser "a solução de todos os problemas", porém, pode ser sim uma poderosa ferramenta para fazer o cálculo de custos de produção a partir da informação fornecida pelo usuário.

Para usar OIKOS o usuário precisará fazer um cadastro, com a única finalidade de garantir que a informação só possa ser por ele manipulada.

# Cadastro de usuário

## POST /api/users/signup - Rota responsável pelo CADASTRO do usuário.

#### Não necessita de AUTORIZAÇÃO por token

#### Corpo da requisição:

```json
{
  "name": "Philip",
  "email": "example@gmail.com",
  "password": "1234"
}
```

#### Corpo da resposta:

```json
{
  "id": 1,
  "name": "Philip",
  "email": "example@gmail.com"
}
```

---

> > > > > > > develop

## POST /api/users/signin - Rota responsável pelo LOGIN do usuário.

#### Não necessita de AUTORIZAÇÃO por token -

#### Corpo da requisição:

```json
{
  "email": "example@gmail.com",
  "password": "1234"
}
```

#### Corpo da resposta:

```json
{
  "token": "370e63d575bfsdfsfesasdfa2346c1bfb973b0b61047dae3"
}
```

---

> > > > > > > develop

## GET /api/users - Rota responsável pela BUSCA DO USUÁRIO.

#### Rota necessita de AUTORIZAÇÃO por token -

#### Requisição sem corpo:

##### Obs: para encontrar o usuário é preciso fazer o login e utilizar o token auth.

#### Corpo da resposta:

```json
{
  "id": 1,
  "name": "Philip",
  "email": "example@gmail.com"
}
```

---

> > > > > > > develop

## PUT /api/users - rota responsável pela ATUALIZAÇÃO de todas as informações do usuário.

#### Rota necessita de AUTORIZAÇÃO por token -

#### Corpo da requisição:

##### É possível alterar o nome e a senha.

```json
{
  "name": "Philip02",
  "email": "example@gmail.com",
  "password": "1234567890"
}
```

#### Corpo da resposta:

> > > > > > > develop

```json
{
  "id": 1,
  "name": "Philip02",
  "email": "example@gmail.com"
}
```

---

> > > > > > > develop

## DELETE /api/users - Rota responsável por DELETAR O USUÁRIO.

#### Requisição sem corpo:

##### - Obs: para deletar o usuário é preciso fazer o login e utilizar o token auth.

#### Corpo da resposta:

```json
{
  "message": "User Philip has been deleted."
}
```

---

---

# Produção

## CADASTRO DE PRODUÇÃO

### POST /api/producions

####  Requisição sem corpo:

#####   -     Obs: para crear uma produção preciso fazer o login e utilizar o token auth.

####  Corpo da resposta - STATUS CODE 201 - CREATED:

```json
    {
        "production_date": "Tue, 03 May 2022 00:00:00 GMT",
        "production_id": 32
    }
```

---------------------------------------------------------------

## INCERÇÃO DE RECEITAS NA PRODUÇÃO

### POST /api/producions/<id>

OBS: PASSAR ID DA PRODUÇÃO QUE IRA RECEBER A RECEITA 

####  Corpo da requisição:

```json
	{
		"recipe_id":1,
	 	"recipe_quantity":50
	}
```

#####   -     Obs: para crear uma produção preciso fazer o login e utilizar o token auth.

####  Corpo da resposta - STATUS CODE 201 - CREATED:

```json
    {
        "id": 10,
        "production_id": 30,
        "recipe_id": 1,
        "recipe_quantity": 50.0
    }
```


### Possíveis erros

Caso o nome de uma das chaves esteja incorreta.

FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 
    {
        "expected keys": 
		[
            		"recipe_id",
		    	"recipe_quantity"
        	],
        "recived keys": 
		[
            		"recipe_id",
		   	"recipe_quantity"
        ]
    }
```

Valor invalido:  

FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json 
    {
	    "exeple": 
        {
		    "recipe_id": 1,
		    "recipe_quantity": 1.5
	    },
	    "msg": "values invalid"
    }
```

---------------------------------------------------------------

## BUSCAR TODAS AS PRODUÇÃO

### GET /api/producions

####  Requisição sem corpo:

#####   -     Obs: para buscar uma produção preciso fazer o login e utilizar o token auth.

####  Corpo da resposta - STATUS CODE 200 - OK:

```json
    [
        {
            "production_date": "Sun, 01 May 2022 00:00:00 GMT",
            "production_id": 28,
            "recipes": [
                {
                    "id": 9,
                    "production_id": 28,
                    "recipe_id": 1,
                    "recipe_quantity": 500.0
                }
            ]
        },
        {
            "production_date": "Sun, 01 May 2022 00:00:00 GMT",
            "production_id": 29,
            "recipes": []
        }
    ]
```

---------------------------------------------------------------

## BUSCAR PRODUÇÃO POR INTERVALO

### GET /api/producions/intervalo?initial_date=01-05-2022&final_date=02-05-2022

OBS: PASSAR A DATA INICIAL (initial_date=XX-XX-XXXX) E FINAL (final_date=XX-XX-XXXX) PARA DEFINIR O INTERVALO

####  Requisição sem corpo:

#####   -     Obs: para buscar uma produção preciso fazer o login e utilizar o token auth.

####  Corpo da resposta - STATUS CODE 200 - OK:

```json
    [
        {
            "production_date": "Sun, 01 May 2022 00:00:00 GMT",
            "production_id": 28,
            "recipes": [
                {
                    "id": 9,
                    "production_id": 28,
                    "recipe_id": 1,
                    "recipe_quantity": 500.0
                }
            ]
        },
        {
            "production_date": "Sun, 02 May 2022 00:00:00 GMT",
            "production_id": 29,
            "recipes": []
        }
    ]
```

---------------------------------------------------------------

## BUSCAR PRODUÇÃO POR DATA

### GET /api/producions/date?date=01-05-2022

OBS: PASSAR A DATA (initial_date=XX-XX-XXXX) DEFINIDA

####  Requisição sem corpo:

#####   -     Obs: para buscar uma produção preciso fazer o login e utilizar o token auth.

####  Corpo da resposta - STATUS CODE 200 - OK:

```json
    [
        {
            "production_date": "Sun, 01 May 2022 00:00:00 GMT",
            "production_id": 28,
            "recipes": [
                {
                    "id": 9,
                    "production_id": 28,
                    "recipe_id": 1,
                    "recipe_quantity": 500.0
                }
            ]
        }
    ]
```

---------------------------------------------------------------

## BUSCAR PRODUÇÃO POR ID

### GET /api/producions/<ID>

OBS: PASSAR ID EXPECIFICO

####  Requisição sem corpo:

#####   -     Obs: para buscar uma produção preciso fazer o login e utilizar o token auth.

####  Corpo da resposta - STATUS CODE 200 - OK:

```json
    [
        {
            "production_date": "Sun, 01 May 2022 00:00:00 GMT",
            "production_id": 28,
            "recipes": [
                {
                    "id": 9,
                    "production_id": 28,
                    "recipe_id": 1,
                    "recipe_quantity": 500.0
                }
            ]
        }
    ]
```
### Possíveis erros

Id não encontrado.

FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 
    {
	    "Error": "id not found"
    }
```


---------------------------------------------------------------

## ALTERAR UMA RECEITA PRODUZIDA 

### PTCH /api/producions/recipes/<ID>

OBS: PASSAR ID DA RECEITA PERTECENTE A UMA PRODUÇÃO PARA A ALTERAÇÃO

####  Corpo da requisição:
```json
    {
        "recipe_id": 1,
        "recipe_quantity": 500
    }
```

#####   -     Obs: para alterar uma produção preciso fazer o login e utilizar o token auth.

####  Corpo da resposta - STATUS CODE 200 - OK:

```json
    {
        "id": 9,
        "production_id": 28,
        "recipe_id": 1,
        "recipe_quantity": 500.0
    }
```

### Possíveis erros

Caso o nome de uma das chaves esteja incorreta.

FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 
    {
        "expected keys":
		[
            		"recipe_id",
		    	"recipe_quantity"
		],
        "recived keys": 
		[
            		"recipe_id",
		    	"recipe_quantity"
		]		
    }
```

Valor invalido:  

FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json 
    {
	    "exeple": 
        {
		    "recipe_id": 1,
		    "recipe_quantity": 1.5
	    },
	    "msg": "values invalid"
    }
```

Id não encontrado:  

FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json 
    {
	    "msg":  "id not found"
    }
```
---------------------------------------------------------------

## DELETAR UMA RECEITA PRODUZIDA 

### GET /api/producions/recipes/<ID>

OBS: PASSAR ID DA RECEITA PERTECENTE A UMA PRODUÇÃO PARA A DELEÇÃO

####  Requisição sem corpo:

#####   -     Obs: para deletar uma receita produzida preciso fazer o login e utilizar o token auth.

####  Requisição sem corpo - STATUS CODE 204 - NO CONTENT:

### Possíveis erros

Id não encontrado.

FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 
    {
	    "Error": "id not found"
    }
```
---------------------------------------------------------------

## DELETAR UMA PRODUÇÃO 

### GET /api/producions/recipes/<ID>

OBS: PASSAR ID DA PRODUÇÃO PARA A DELEÇÃO

####  Requisição sem corpo:

#####   -     Obs: para deletar uma produção preciso fazer o login e utilizar o token auth.

####  Requisição sem corpo - STATUS CODE 204 - NO CONTENT:

### Possíveis erros

Id não encontrado.

FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json 
    {
	    "Error": "id not found"
    }
```
---------------------------------------------------------------
---------------------------------------------------------------

# Ingredientes

## CADASTRO DE INGREDIENTES

### POST /api/ingredients - Rota responsável pelo CADASTRO de ingrediente.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json
{
  "ingredient_name": "Fermento",
  "measurement_unit": "G"
}
```

#### Corpo da resposta - STATUS CODE 201 - CREATED:

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
  "expected keys": ["measurement_unit", "ingredient_name"],
  "recived keys": ["measurement_unit", "ingredients_name"]
}
```

Ingrediente já cadastrado:

POST /api/ingredients - FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json
{
  "msg": "ingredient already exists"
}
```

---

## BUSCA DE INGREDIENTES

### GET /api/ingredients - Rota responsável pela BUSCA de ingrediente.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

#### Corpo da resposta - STATUS CODE 200 - OK:

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

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

    [
        {
            "ingredient_id": 1,
            "ingredient_name": "trigo",
            "measurement_unit": "g",
            "purchases": [
                {
                    "purchase_date": "Sun, 01 May 2022 00:00:00 GMT",
                    "purchase_id": 1,
                    "purchase_price": 50.0,
                    "purchase_quantity": 10.0
                },
                {
                    "purchase_date": "Tue, 01 Mar 2022 00:00:00 GMT",
                    "purchase_id": 2,
                    "purchase_price": 30.0,
                    "purchase_quantity": 5.0
                },
                {
                    "purchase_date": "Thu, 02 Jun 2022 00:00:00 GMT",
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
                    "purchase_date": "Sun, 01 May 2022 00:00:00 GMT",
                    "purchase_id": 1,
                    "purchase_price": 36.0,
                    "purchase_quantity": 3.0
                }
            ]
        }
    ]

}
]

````

### Possíveis erros

Ingrediente não encontrado:

GET /api/ingredients/trigosed - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json
{
  "Error": "Ingredient not found"
}
````

## ATUALIZAÇÃO DE INGREDIENTES

### PATCH /api/ingredients - Rota responsável pela ATUALIZAÇÃO do ingrediente.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json
{
  "ingredient_name": "Fermento",
  "measurement_unit": "kg"
}
```

#### Corpo da resposta:

=======
[
{
"ingredient_id": 1,
"ingredient_name": "trigo",
"measurement_unit": "g",
"purchases": [
{
"purchase_date": "Sun, 01 May 2022 00:00:00 GMT",
"purchase_id": 1,
"purchase_price": 50.0,
"purchase_quantity": 10.0
},
{
"purchase_date": "Tue, 01 Mar 2022 00:00:00 GMT",
"purchase_id": 2,
"purchase_price": 30.0,
"purchase_quantity": 5.0
},
{
"purchase_date": "Thu, 02 Jun 2022 00:00:00 GMT",
"purchase_id": 3,
"purchase_price": 35.0,
"purchase_quantity": 5.0
}
]
}
]

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
  "expected keys": ["measurement_unit", "ingredient_name"],
  "recived keys": ["measurement_unit", "ingredients_name"]
}
```

=======
GET /api/ingredients/<name> - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

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

---

## DELEÇÃO DE INGREDIENTES

### DELETE /api/ingredients/<name> - Rota responsável pela DELEÇÃO de ingrediente.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

=======

### PATCH /api/ingredients/<name> - Rota responsável pela ATUALIZAÇÃO do ingrediente.

> > > > > > > develop

#### Não possui corpo de resposta

### Possíveis erros

Caso não exista o ingrediente.

DELETE /api/ingredients/<name> - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json
{
  "Error": "Ingredient not found"
}
```

---

---

# Receitas

## CRIAÇÃO DE RECEITAS

### POST /api/recipes - Rota responsável pelo CRIAÇÃO da receita.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json
{
  "recipe_name": "Massa de biscoito"
}
```

#### Corpo da resposta - STATUS CODE 201 - CREATED:

```json
{
  "recipe_id": 1,
  "recipe_name": "Massa de biscoito"
}
```

### POST /api/recipes/<recipe_id> - Rota responsável pela ADIÇÃO de ingredientes e suas quantidades na receita.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json
{
  "ingredient_id": "2",
  "quantity": "7200"
}
```

#### Corpo da resposta - STATUS CODE 201 - CREATED:

```json
{
  "receitas": [
    [
      {
        "ingredient_id": 3,
        "quantity": 5000.0,
        "recipe_id": 1
      },
      {
        "ingredient_id": 2,
        "quantity": 7200.0,
        "recipe_id": 1
      },
      {
        "ingredient_id": 1,
        "quantity": 12000.0,
        "recipe_id": 1
      }
    ]
  ],
  "recipe_id": 1,
  "recipe_name": "Massa de biscoito"
}
```

### Possíveis erros

Caso o nome de uma das chaves esteja incorreta.

POST /api/recipes - FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json
{
  "expected keys": ["recipe_name"],
  "recived keys": ["recipename"]
}
```

Receita já cadastrada:

POST /api/recipess - FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST

```json
{
  "msg": "Recipe already exists"
}
```

---

## BUSCA DE RECEITAS

### GET /api/recipes - Rota responsável pela BUSCA de todas as receitas.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

#### Corpo da resposta - STATUS CODE 200 - OK:

```json
[
  {
    "ingredients": [
      {
        "ingredient_id": 3,
        "ingredient_name": "farinha",
        "quantity": 90.0,
        "recipe_id": 1
      }
    ],
    "recipe_id": 1,
    "recipe_name": "massa de pao"
  },
  {
    "ingredients": [
      {
        "ingredient_id": 3,
        "ingredient_name": "farinha",
        "quantity": 1000.0,
        "recipe_id": 11
      },
      {
        "ingredient_id": 2,
        "ingredient_name": "trigo",
        "quantity": 1000.0,
        "recipe_id": 11
      },
      {
        "ingredient_id": 1,
        "ingredient_name": "fermento",
        "quantity": 1000.0,
        "recipe_id": 11
      }
    ],
    "recipe_id": 11,
    "recipe_name": "massa de polvilho salgado"
  }
]
```

### GET /api/recipes/<name> - Rota responsável pela BUSCA de receita pelo nome.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

PATCH /api/recipes/<name> - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

#### Não possui corpo de requisição

#### Corpo da resposta - STATUS CODE 200 - OK:

```json
[
  {
    "ingredients": [
      {
        "ingredient_id": 3,
        "ingredient_name": "farinha",
        "quantity": 90000.0,
        "recipe_id": 1
      }
    ],
    "recipe_id": 1,
    "recipe_name": "massa de pao"
  }
]
```

### Possíveis erros

Receita não encontrada:

GET /api/ingredients/masa de pao - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json
{
  "Error": "Recipe not found"
}
```

---

## ATUALIZAÇÃO DE RECEITA

### PATCH /api/recipe - Rota responsável pela ATUALIZAÇÃO da receita.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Corpo da requisição:

```json
{
  "ingredient_id": 3,
  "recipe_id": 11,
  "quantity": 8009
}
```

#### Corpo da resposta:

```json
{
  "ingredient_id": 3,
  "quantity": 8009.0,
  "recipe_id": 11
}
```

### Possíveis erros

Caso o nome de uma das chaves esteja incorreta.

PATCH /api/recipes - FORMATO DA RESPOSTA - STATUS 422 - UNPROCESSABLE ENTITY

```json
{
  "expected keys": ["ingredient_id", "recipe_id", "quantity"],
  "recived keys": ["ingredientes_id", "recipe_id", "quantity"]
}
```

Caso não exista o ingrediente na receita ou a receita.

PATCH /api/recipes - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json
{
  "error": "Recipe or ingredient not found"
}
```

---

## DELEÇÃO DE RECEITAS

### DELETE /api/recipes/<name> - Rota responsável pela DELEÇÃO da receita.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

#### Não possui corpo de resposta

### Possíveis erros

Caso não exista a receita.

DELETE /api/recipe/<name> - FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND

```json
{
  "error": "Recipe not found"
}
```

### DELETE /api/recipes/?recipe_id=<recipe_id>&ingredient_id=<ingredient_id> - Rota responsável pela DELEÇÃO do ingrediente da receita.

\*OBS - NECESSITA DE AUTORIZAÇÃO VIA TOKEN

#### Não possui corpo de requisição

#### Não possui corpo de resposta


