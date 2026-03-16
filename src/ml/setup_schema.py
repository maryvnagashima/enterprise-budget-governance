"""
Setup inicial do schema DuckDB para Enterprise Budget Governance
Baseado no Plano de Carreira — Projeto 1: BudgetMind v2
"""

import duckdb
import os

# Criar banco de dados local
DB_PATH = "data/enterprise_budget.db"
os.makedirs("data", exist_ok=True)

# Conectar ao DuckDB
con = duckdb.connect(DB_PATH)

# Criar tabelas
con.execute("""
CREATE TABLE IF NOT EXISTS marketing_spend (
    date DATE,
    channel VARCHAR,
    spend_usd DOUBLE,
    impressions INTEGER,
    clicks INTEGER
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS revenue_attribution (
    date DATE,
    channel VARCHAR,
    orders INTEGER,
    revenue_usd DOUBLE,
    cac_usd DOUBLE
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS budget_approved (
    month DATE,
    channel VARCHAR,
    budget_usd DOUBLE,
    approved_by VARCHAR,
    approved_at TIMESTAMP
)
""")

# Validar
tables = con.execute("SHOW TABLES;").fetchall()
print(f"Sucesso: {len(tables)} tabelas criadas!")
for table in tables:
    print(f"   - {table[0]}")

# Fechar conexão
con.close()
