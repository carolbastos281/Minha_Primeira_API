Projeto: API Avançada de Dados de Crocodilos com FastAPI
Esta é uma API REST robusta desenvolvida com FastAPI para consultar um dataset sobre observações de crocodilos. A API oferece múltiplos endpoints para pesquisa e filtragem de dados, permitindo consultas simples e complexas.

🎯 Objetivo
O objetivo é fornecer uma interface de programação (API) rápida e bem documentada para acessar e filtrar dados sobre crocodilos, demonstrando o uso de Path Parameters, Query Parameters e boas práticas de desenvolvimento com FastAPI.

📂 Estrutura do Projeto
Para que a API funcione corretamente, a estrutura de pastas e arquivos deve ser a seguinte:

seu_projeto/
├── README.md          # Esta documentação
├── main.py            # O seu código principal da API
├── dados/
│   └── crocodile_dataset.csv  # O dataset utilizado
└── requirements.txt   # As dependências do projeto

🚀 Como Executar o Projeto
Organize os Arquivos: Certifique-se de que seus arquivos estão na estrutura mostrada acima.

Abra o Terminal: Navegue com o terminal (Prompt de Comando, PowerShell, etc.) até a pasta principal do seu projeto (a pasta seu_projeto).

Crie e Ative um Ambiente Virtual (Recomendado):

# Criar o ambiente
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Mac/Linux
source venv/bin/activate

Instale as Dependências: Com o ambiente virtual ativo, instale todas as bibliotecas necessárias com um único comando:

pip install -r requirements.txt

Execute a API:

uvicorn main:app --reload

O terminal indicará que o servidor está rodando, geralmente em http://127.0.0.1:8000.

Acesse a Documentação Interativa:

Abra seu navegador e vá para http://127.0.0.1:8000/docs.

Nesta página, você pode ver, testar e interagir com todos os endpoints da API de forma visual.

📖 Endpoints Disponíveis
A API oferece os seguintes endpoints para consulta:

GET /
Descrição: Endpoint inicial que retorna informações básicas sobre a API.

Exemplo de Resposta:

{
  "projeto": "API Crocodilos",
  "autor": "Carolina Mendes Bastos",
  "descricao": "API para servir dados de crocodilos",
  "total_registros": 1000
}

GET /dados
Descrição: Retorna a lista completa com todas as observações de crocodilos do dataset.

GET /observacao/{obs_id}
Descrição: Busca uma única observação pelo seu Observation ID específico.

Parâmetro:

obs_id (inteiro): O ID da observação.

Exemplo de Uso: http://127.0.0.1:8000/observacao/5

GET /pais/{pais}
Descrição: Retorna uma lista de todas as observações registradas em um país ou região específica. A busca não diferencia maiúsculas de minúsculas.

Parâmetro:

pais (texto): O nome do país.

Exemplo de Uso: http://127.0.0.1:8000/pais/Brazil

GET /buscar
Descrição: Endpoint de busca avançada que permite combinar múltiplos filtros. Todos os parâmetros são opcionais.

Parâmetros de Query:

nome (texto, opcional): Parte do nome comum do crocodilo. Ex: American.

pais (texto, opcional): Nome exato do país/região. Ex: Mexico.

comprimento_min (número, opcional): Filtra por comprimento mínimo em metros. Ex: 3.5.

peso_min (número, opcional): Filtra por peso mínimo em kg. Ex: 200.

sexo (texto, opcional): Filtra por sexo (Male ou Female).

limite (inteiro, opcional): Limita a quantidade de resultados retornados (padrão: 10, máximo: 100).

Exemplos de Uso:

Buscar crocodilos "American" no México: /buscar?nome=American&pais=Mexico

Buscar crocodilos fêmeas com pelo menos 300kg: /buscar?sexo=Female&peso_min=300

Buscar os 5 maiores crocodilos (em comprimento) da Austrália: /buscar?pais=Australia&comprimento_min=5.0&limite=5

📄 Fonte dos Dados
Nome do Dataset: Crocodile Datase
thttps://www.kaggle.com/datasets/aniruddhass/crocodile-dataset

Fonte: Kaggle

Link: https://www.kaggle.com/datasets
