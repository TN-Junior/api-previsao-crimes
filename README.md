## Previsão Total de Crimes - Projeto FastAPI

Este projeto é uma API desenvolvida com FastAPI para prever o número total de crimes em municípios com base em dados educacionais e o IDEB (Índice de Desenvolvimento da Educação Básica). A API utiliza um modelo treinado de Machine Learning para fazer as previsões.

# Funcionalidades

Previsão de crimes: Recebe dados relacionados a um município específico e retorna a previsão do número total de crimes.
Validação de entrada: Verifica a consistência dos dados fornecidos, incluindo o nome do município.
Interface RESTful: Fornece uma rota POST para enviar dados e receber previsões.


## Requisitos

Certifique-se de ter instalado:

Docker (para rodar via container)
Python 3.9+ (para rodar localmente)
Dependências Python (listadas em requirements.txt):

FastAPI
Uvicorn
Pandas
Pydantic
Joblib
Scikit-learn

## Uso

1. Clonando o Repositório
git clone https://github.com/plat07/api-previsao-crimes.git
cd src/app

2. Executando com Docker

docker build -t previsao-total-crimes .
docker run -d -p 8000:8000 previsao-total-crimes

3. Executando Localmente

Instalando as Dependências:
pip install -r requirements.txt

Iniciando a API:
uvicorn src.app.main:app


## Rota Disponível 

# POST  /previsao-total-crimes/

Exemplo de Requisição:
{
    "ano": 2024,
    "municipio": "Recife",
    "ideb": 5.2,
    "ensino_fundamental_docentes": 1000,
    "ensino_fundamental_escolas": 200,
    "ensino_fundamental_matriculas": 30000,
    "ensino_infantil_docentes": 500,
    "ensino_infantil_escolas": 100,
    "ensino_infantil_matriculas": 15000,
    "ensino_medio_docentes": 800,
    "ensino_medio_escolas": 150,
    "ensino_medio_matriculas": 25000
}
