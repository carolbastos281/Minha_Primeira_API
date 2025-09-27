import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pathlib import Path
import uvicorn

"""API FastAPI para servir dados de crocodilos."""

CSV_PATH = Path(__file__).resolve().parent / "dados" / "crocodile_dataset.csv"
try:
    dados = pd.read_csv(CSV_PATH)
    dados_dict = dados.to_dict("records")
except Exception as e:
    print(f"Erro ao carregar o CSV: {e}")
    dados_dict = []

# Crie o app fora do try/except!
app = FastAPI(title="API Crocodilos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    """Informações básicas da API"""
    return {
        "projeto": "API Crocodilos",
        "autor": "Carolina Mendes Bastos",
        "descricao": "API para servir dados de crocodilos",
        "total_registros": len(dados_dict)
    }

@app.get("/dados")
def listar_todos():
    """Retorna todas as observações de crocodilos"""
    return dados_dict

@app.get("/observacao/{obs_id}")
def buscar_por_observacao(obs_id: int):
    """
    Busca uma observação específica pelo Observation ID
    Exemplo: /observacao/5
    """
    for item in dados_dict:
        try:
            if int(item.get("Observation ID")) == int(obs_id):
                return item
        except Exception:
            continue
    raise HTTPException(status_code=404, detail="Observação não encontrada para o ID informado")

@app.get("/pais/{pais}")
def buscar_por_pais(pais: str):
    """
    Filtra observações por país/região
    Exemplo: /pais/Brazil
    """
    resultados = [
        item for item in dados_dict
        if str(item.get("Country/Region", "")).lower() == pais.lower()
    ]
    return {
        "pais": pais,
        "total": len(resultados),
        "resultados": resultados,
    }

@app.get("/buscar")
def buscar_com_filtros(
    nome: Optional[str] = Query(None, description="Nome comum do crocodilo"),
    pais: Optional[str] = Query(None, description="País ou região"),
    comprimento_min: Optional[float] = Query(None, ge=0, description="Comprimento mínimo (m)"),
    peso_min: Optional[float] = Query(None, ge=0, description="Peso mínimo (kg)"),
    sexo: Optional[str] = Query(None, description="Sexo"),
    limite: int = Query(10, ge=1, le=100, description="Limite de resultados"),
):
    """
    Busca com filtros:
    - /buscar?nome=Morelet&pais=Mexico
    - /buscar?comprimento_min=3.0
    - /buscar?peso_min=100
    - /buscar?sexo=Female
    """
    resultados = dados_dict

    if nome:
        termo = nome.lower()
        resultados = [
            item for item in resultados
            if termo in str(item.get("Common Name", "")).lower()
        ]

    if pais:
        resultados = [
            item for item in resultados
            if str(item.get("Country/Region", "")).lower() == pais.lower()
        ]

    if comprimento_min is not None:
        def to_float(value):
            try:
                return float(value)
            except Exception:
                return None
        resultados = [
            item for item in resultados
            if to_float(item.get("Observed Length (m)")) is not None and to_float(item.get("Observed Length (m)")) >= comprimento_min
        ]

    if peso_min is not None:
        def to_float(value):
            try:
                return float(value)
            except Exception:
                return None
        resultados = [
            item for item in resultados
            if to_float(item.get("Observed Weight (kg)")) is not None and to_float(item.get("Observed Weight (kg)")) >= peso_min
        ]

    if sexo:
        resultados = [
            item for item in resultados
            if str(item.get("Sex", "")).lower() == sexo.lower()
        ]

    resultados = resultados[:limite]

    return {
        "filtros": {
            "nome": nome,
            "pais": pais,
            "comprimento_min": comprimento_min,
            "peso_min": peso_min,
            "sexo": sexo,
            "limite": limite,
        },
        "total": len(resultados),
        "resultados": resultados,
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
