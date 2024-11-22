from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib


# Inicializar o aplicativo FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Classe do modelo de entrada
class Dados(BaseModel):
    ano: float
    municipio: str
    ideb: float
    ensino_fundamental_docentes: float
    ensino_fundamental_escolas: float
    ensino_fundamental_matriculas: float
    ensino_infantil_docentes: float
    ensino_infantil_escolas: float
    ensino_infantil_matriculas: float
    ensino_medio_docentes: float
    ensino_medio_escolas: float
    ensino_medio_matriculas: float

# Lista dos municípios com Label Encoding
municipios = [
    'abreu e lima', 'afogados da ingazeira', 'agrestina', 'altinho',
    'amaraji', 'angelim', 'araripina', 'arcoverde', 'barra de guabiraba',
    'barreiros', 'belo jardim', 'bezerros', 'bom conselho', 'bom jardim',
    'bonito', 'brejo da madre de deus', 'buenos aires',
    'cabo de santo agostinho', 'cachoeirinha', 'camaragibe', 'camutanga',
    'canhotinho', 'capoeiras', 'carpina', 'caruaru', 'casinhas', 'catende',
    'cedro', 'condado', 'correntes', 'cumaru', 'cupira', 'dormentes', 'escada',
    'exu', 'feira nova', 'ferreiros', 'flores', 'floresta', 'frei miguelinho',
    'gameleira', 'garanhuns', 'goiana', 'granito', 'iati', 'ibimirim',
    'ibirajuba', 'igarassu', 'ipojuca', 'ipubi', 'itacuruba', 'itapissuma',
    'itaquitinga', 'jaqueira', 'joaquim nabuco', 'jucati', 'jupi', 'jurema',
    'lagoa do carro', 'lagoa do ouro', 'lagoa dos gatos', 'lagoa grande',
    'lajedo', 'limoeiro', 'macaparana', 'machados', 'maraial', 'mirandiba',
    'moreno', 'olinda', 'ouricuri', 'palmares', 'palmeirina', 'panelas',
    'paranatama', 'parnamirim', 'passira', 'paudalho', 'paulista', 'pedra',
    'pesqueira', 'petrolina', 'pombos', 'primavera', 'recife',
    'riacho das almas', 'rio formoso', 'salgueiro', 'santa cruz',
    'santa cruz da baixa verde', 'santa cruz do capibaribe',
    'santa filomena', 'santa maria da boa vista', 'serra talhada', 'serrita',
    'surubim', 'tabira', 'tacaratu', 'taquaritinga do norte', 'terezinha',
    'terra nova', 'toritama', 'trindade', 'triunfo', 'tupanatinga',
    'venturosa', 'verdejante', 'brejinho', 'carnaubeira da penha',
    'itapetim', 'manari', 'quixaba', 'santa terezinha', 'tuparetama',
    'ingazeira', 'salgadinho'
]

# Rota para previsão
@app.post("/previsao-total-crimes/")
def previsao_total_crimes(dados: Dados):
    # Converter município para inteiro com Label Encoding
    if dados.municipio.lower() not in municipios:
        return {"error": f"Município '{dados.municipio}' inválido"}
    municipio_codificado = municipios.index(dados.municipio.lower())

    # Criar DataFrame para o modelo
    input_data = pd.DataFrame({
        'Ano': [dados.ano],
        'Municipio': [municipio_codificado],
        'IDEB': [dados.ideb],
        'Ensino fundamental_docentes': [dados.ensino_fundamental_docentes],
        'Ensino fundamental_escolas': [dados.ensino_fundamental_escolas],
        'Ensino fundamental_matrículas': [dados.ensino_fundamental_matriculas],
        'Ensino infantil_docentes': [dados.ensino_infantil_docentes],
        'Ensino infantil_escolas': [dados.ensino_infantil_escolas],
        'Ensino infantil_matrículas': [dados.ensino_infantil_matriculas],
        'Ensino médio_docentes': [dados.ensino_medio_docentes],
        'Ensino médio_escolas': [dados.ensino_medio_escolas],
        'Ensino médio_matrículas': [dados.ensino_medio_matriculas],
    })

    # Carregar modelo e fazer previsão
    try:
        model = joblib.load('src/resources/model.pkl')
        previsao = model.predict(input_data)
        return {"TotalCrimesPrevisto": round(previsao[0], 2)}
    except Exception as e:
        return {"error": str(e)}
