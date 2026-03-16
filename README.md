# Enterprise Budget Governance Platform

> **Transformando R$ 500k+/mês de intuição em decisão orientada por dados — com explicabilidade, audit trail e compliance enterprise.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![dbt](https://img.shields.io/badge/dbt-BigQuery-orange?logo=dbt)
![MLflow](https://img.shields.io/badge/MLflow-tracking-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)
![Status](https://img.shields.io/badge/Sprint-1%2F6-yellow)
![Nível](https://img.shields.io/badge/Nível-Senior%2FLead-purple)

---

## 🧭 Por Que Este Projeto Existe

Este projeto nasce de um problema real vivido em **10+ anos de operação com budget de marketing em e-commerce**:

**O time de dados recomenda uma realocação. O negócio não aprova.**

Não porque a recomendação está errada — mas porque não há resposta para três perguntas simples:

- *Por que você está sugerindo tirar verba do Google?*
- *Se der errado, quem aprovou isso?*
- *Isso respeita a regra de não zerar brand?*

O Enterprise Budget Governance Platform resolve exatamente isso: uma plataforma que une **otimização com ML**, **explicabilidade via SHAP** e **governança real** — com audit trail, RBAC e workflow de aprovação integrado.

> **Contexto:** Baseado em experiência real gerenciando R$ 1.2M em budget de marketing  
> com ROAS médio de 3.2x comprovado em operações de e-commerce.

---

## 💡 O Problema em Números

| Gap | Sintoma | Custo Real |
|-----|---------|-----------|
| **Sem explicabilidade** | Recomendações de dados rejeitadas pelo negócio | Budget alocado no feeling |
| **Sem audit trail** | Ninguém sabe quem aprovou a última mudança | Risco regulatório e operacional |
| **Sem compliance** | Regras como "mínimo de 20% em brand" violadas sem alerta | Perda de posicionamento de marca |
| **Sem monitoramento** | Modelo degrada e ninguém percebe | ROI prometido nunca se materializa |

---

## 🏗️ Arquitetura da Solução

```
┌─────────────────────────────────────────────────────────┐
│                 CAMADA 4 — NEGÓCIO                      │
│   Dashboard Executivo (Power BI) + Workflow de Aprovação│
│              (Dash) — onde o CFO decide                 │
├─────────────────────────────────────────────────────────┤
│               CAMADA 3 — GOVERNANÇA                     │
│         RBAC  |  Audit Trail  |  Compliance Rules       │
├─────────────────────────────────────────────────────────┤
│              CAMADA 2 — INTELIGÊNCIA                    │
│    Modelo de Otimização  |  SHAP  |  Drift Monitoring   │
├─────────────────────────────────────────────────────────┤
│                CAMADA 1 — DADOS                         │
│          BigQuery  |  dbt  |  DuckDB (local dev)        │
└─────────────────────────────────────────────────────────┘
```


## 📊 Impacto Simulado

> Projeções baseadas em operações reais gerenciadas durante o desenvolvimento deste projeto (R$ 1.2M em receita incremental gerada, ROAS médio de 3.2x documentado).

| Métrica | Baseline | Com a Plataforma | Δ |
|---------|----------|------------------|---|
| Budget otimizado por mês | R$ 0 | R$ 87k | **+R$ 87k** |
| Taxa de aprovação das recomendações | 30% | 78% | **+160%** |
| Tempo por ciclo de budget | 3 dias | 2 horas | **-92%** |
| Violações de compliance | Não rastreado | 0 | **100% controlado** |
| Confiança do negócio no modelo | Baixa | Alta (SHAP) | **Adoção garantida** |

---

## 🛠️ Stack e Decisões Técnicas

| Camada | Tecnologia | Decisão |
|--------|------------|---------|
| **Dados** | BigQuery + dbt + DuckDB | BigQuery para escala enterprise; DuckDB para dev local sem custo |
| **ML** | Scikit-Learn + SHAP + MLflow | SHAP é não-negociável: sem explicabilidade, o negócio não aprova |
| **API** | FastAPI | Separação clara de backend; Swagger automático facilita validação |
| **Workflow** | Dash (Plotly) | Controle de estado necessário para aprovação multi-step; Streamlit não dá conta |
| **Visualização** | Power BI | Alavanca expertise existente; padrão nas empresas-alvo |
| **Auth** | Firebase Auth | RBAC enterprise (Admin, Approver, Viewer) sem reinventar a roda |
| **Infra** | Docker + GitHub Actions | Reprodutibilidade local e CI/CD para produção |

> Para os trade-offs detalhados de cada decisão, veja [DECISOES.md](./DECISOES.md).

---

## 📁 Estrutura do Projeto

```
enterprise-budget-governance/
├── README.md                   # Narrativa de negócio (este arquivo)
├── DECISOES.md                 # Por que BigQuery? Por que Dash e não Streamlit?
├── RISCOS.md                   # Matriz de riscos com probabilidade × impacto
├── STAKEHOLDERS.md             # Quem usa, aprova, audita e mantém
├── ENTREVISTA_QA.md            # 10 perguntas técnicas e como responder
├── MODEL_CARD.md               # Documentação do modelo (padrão industry)
├── POLITICA_USO.md             # Governança e regras de compliance
├── dbt/
│   ├── models/
│   │   ├── staging/            # Bronze — dados brutos normalizados
│   │   ├── intermediate/       # Silver — métricas calculadas
│   │   └── marts/              # Gold — visões de negócio
│   └── tests/                  # Testes de qualidade de dados
├── src/
│   ├── api/
│   │   ├── main.py             # FastAPI — endpoints de recomendação
│   │   ├── auth.py             # RBAC e controle de acesso
│   │   └── audit.py            # Logging de decisões
│   ├── ml/
│   │   ├── train.py            # Treinamento do modelo
│   │   ├── explain.py          # SHAP values e explicabilidade
│   │   └── monitor.py          # Drift monitoring
│   └── dashboard/
│       ├── app.py              # Dash — workflow de aprovação
│       └── powerbi/            # Templates e conexões Power BI
├── infra/
│   ├── docker-compose.yml
│   └── github-actions-ci.yml
├── docs/
│   └── guia_usuario.md
├── data/
│   ├── dictionary.md
│   └── raw/
└── notebooks/
    └── exploracao_inicial.ipynb
```

---

## 🗺️ Roadmap do Projeto

| Sprint | Período | Foco | Entregáveis |
|--------|---------|------|-------------|
| **Sprint 1** | Semana 1-2 | Fundações de Dados | DuckDB, dbt, Data Dictionary, testes de qualidade |
| **Sprint 2** | Semana 3-4 | Modelo ML + Explicabilidade | Scikit-Learn, SHAP, MLflow, Model Card |
| **Sprint 3** | Semana 5-6 | Governança | RBAC, Audit Trail, Logging, Política de Uso |
| **Sprint 4** | Semana 7-8 | API + Dashboard | FastAPI, Dash (workflow), Power BI (visualização) |
| **Sprint 5** | Semana 9-10 | Infra + CI/CD | Docker, GitHub Actions, pytest (coverage > 80%) |
| **Sprint 6** | Semana 11-12 | Documentação + Demo | README final, vídeo demo, post LinkedIn |

**Status Atual:** 🟡 Sprint 1 em andamento — [ver backlog no GitHub Projects](../../projects)

---

## 📖 Documentação de Governança

Este projeto trata governança como entregável, não como afterthought.

| Documento | Conteúdo |
|-----------|----------|
| [DECISOES.md](./DECISOES.md) | Por que cada escolha técnica foi feita. Trade-offs documentados. |
| [RISCOS.md](./RISCOS.md) | O que pode dar errado, probabilidade e plano de mitigação. |
| [STAKEHOLDERS.md](./STAKEHOLDERS.md) | Analista, gestor, CFO, auditor — o que cada um vê e aprova. |
| [ENTREVISTA_QA.md](./ENTREVISTA_QA.md) | Perguntas técnicas e de negócio esperadas em processos seletivos. |
| [MODEL_CARD.md](./MODEL_CARD.md) | Métricas, viéses, limitações e uso adequado do modelo. |
| [POLITICA_USO.md](./POLITICA_USO.md) | Regras de compliance e quem pode aprovar o quê. |

---

## 🚀 Como Rodar

### Com Docker (recomendado)

```bash
git clone https://github.com/maryvnagashima/enterprise-budget-governance.git
cd enterprise-budget-governance
cp .env.example .env        # configure suas credenciais
docker-compose up
```

Acesse:
- **API + Swagger:** `http://localhost:8000/docs`
- **Dashboard (Workflow de Aprovação):** `http://localhost:8050`

### Sem Docker

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Pipeline dbt (local com DuckDB)
cd dbt && dbt run && dbt test

# API
python src/api/main.py

# Dashboard
python src/dashboard/app.py
```

---


## 🧠 Sobre Mim

**Marina Vieira Nagashima**  
*Data Analyst | AI Governance & Business Integration*

| Experiência | Resultado |
|-------------|-----------|
| 10+ anos com dado aplicado a negócio | Raro: une visão de negócio com execução técnica |
| R$ 1.2M em budget de marketing gerenciado | ROAS médio 3.2x comprovado |
| R$ 1.2M de impacto financeiro gerado | Resultado mensurável, não estimado |
| Stack: BigQuery, Python, SQL, Power BI, dbt | Alinhado com empresas-alvo |


> *"Não sou quem só constrói o modelo. Sou quem garante que o modelo gera valor, não gera risco, e escala com segurança no enterprise."*

**Contato:**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-marinanagashima-0077B5?logo=linkedin)](https://linkedin.com/in/marinanagashima)
[![GitHub](https://img.shields.io/badge/GitHub-maryvnagashima-181717?logo=github)](https://github.com/maryvnagashima)

---

*Projeto desenvolvido em Março 2026*
