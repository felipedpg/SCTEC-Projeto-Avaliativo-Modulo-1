from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
GRAFICOS_DIR = BASE_DIR / "graficos"
GRAFICOS_DIR.mkdir(exist_ok=True)

q1 = pd.read_csv(DATA_DIR / "query_01.csv")
q2 = pd.read_csv(DATA_DIR / "query_02.csv")

for df in (q1, q2):
    df.columns = df.columns.str.strip().str.upper()
    df["SALARY"] = pd.to_numeric(df["SALARY"], errors="coerce")

def estatisticas(df, nome):
    s = df["SALARY"].dropna()
    print(f"\n{'='*60}\n{nome}\n{'='*60}")
    print(f"Registros: {len(df)}")
    print(f"Média: {s.mean():.2f}")
    print(f"Mediana: {s.median():.2f}")
    print(f"Moda: {s.mode().iloc[0]:.2f}")
    print(f"Mínimo: {s.min():.2f}")
    print(f"Máximo: {s.max():.2f}")
    print(f"Desvio padrão: {s.std():.2f}")
    print(f"Duplicatas: {df.duplicated().sum()}")
    print("\nNulos por coluna:")
    print(df.isna().sum())

estatisticas(q1, "QUERY 1 - Departamento e Cargo")
estatisticas(q2, "QUERY 2 - Região e Localização")

print("\nSALÁRIO MÉDIO POR DEPARTAMENTO")
print(q1.groupby("DEPARTMENT_NAME")["SALARY"].agg(["count","mean","median","min","max"]).sort_values("mean", ascending=False))

print("\nTOP 10 CARGOS POR SALÁRIO MÉDIO")
print(q1.groupby("JOB_TITLE")["SALARY"].agg(["count","mean"]).sort_values("mean", ascending=False).head(10))

print("\nSALÁRIO MÉDIO POR REGIÃO")
print(q2.groupby("REGION_NAME")["SALARY"].agg(["count","mean","median","min","max"]).sort_values("mean", ascending=False))

# Boxplot
plt.figure(figsize=(8,5))
plt.boxplot(q1["SALARY"].dropna())
plt.title("Distribuição dos salários - Query 1")
plt.ylabel("Salário")
plt.tight_layout()
plt.savefig(GRAFICOS_DIR / "boxplot_salarios.png", dpi=160)
plt.close()

# Departamento
dept = q1.groupby("DEPARTMENT_NAME")["SALARY"].mean().sort_values()
plt.figure(figsize=(9,6))
dept.plot(kind="barh")
plt.title("Salário médio por departamento")
plt.xlabel("Salário médio")
plt.ylabel("Departamento")
plt.tight_layout()
plt.savefig(GRAFICOS_DIR / "salario_medio_departamento.png", dpi=160)
plt.close()

# Região
reg = q2.groupby("REGION_NAME")["SALARY"].mean().sort_values()
plt.figure(figsize=(8,5))
reg.plot(kind="barh")
plt.title("Salário médio por região")
plt.xlabel("Salário médio")
plt.ylabel("Região")
plt.tight_layout()
plt.savefig(GRAFICOS_DIR / "salario_medio_regiao.png", dpi=160)
plt.close()

# Cargos
job = q1.groupby("JOB_TITLE")["SALARY"].mean().sort_values().tail(10)
plt.figure(figsize=(10,6))
job.plot(kind="barh")
plt.title("Top 10 cargos por salário médio")
plt.xlabel("Salário médio")
plt.ylabel("Cargo")
plt.tight_layout()
plt.savefig(GRAFICOS_DIR / "top10_cargos_salario_medio.png", dpi=160)
plt.close()

print(f"\nGráficos salvos em: {GRAFICOS_DIR}")
