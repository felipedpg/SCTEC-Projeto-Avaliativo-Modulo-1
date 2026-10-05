# Projeto de Análise de Dados de RH — FreeSQL / HR

Aluno: Felipe de PAiva Garcia  
Turma: QA VDBI 2026/1 3 
Banco: FreeSQL — esquema `HR`

1. Objetivo

O projeto analisa dados de Recursos Humanos do esquema HR, utilizando SQL no FreeSQL para extração e Python/Pandas para análise exploratória. O foco está em salários, cargos, departamentos e distribuição geográfica.

2. Tecnologias

- FreeSQL / SQL
- Python 3
- Pandas
- Matplotlib
- VS Code
- Git e GitHub

3. Tabelas utilizadas

- 'HR.EMPLOYEES': funcionários e salários.
- 'HR.DEPARTMENTS': departamentos e localização.
- 'HR.JOBS': cargos e faixas salariais.
- 'HR.LOCATIONS': cidade, estado e país.
- 'HR.COUNTRIES': países e regiões.
- 'HR.REGIONS': regiões geográficas.

4. Query 1 — Salário por Departamento e Cargo

A consulta usa 'EMPLOYEES' como tabela principal e dois 'LEFT JOIN': com 'DEPARTMENTS' e 'JOBS'.

Filtro aplicado:

sql
WHERE e.SALARY > 0


Resultado real exportado do FreeSQL: 107 funcionários.

Arquivo: 'data/query_01.csv'

5. Query 2 — Funcionários por Região

A consulta relaciona:

EMPLOYEES > DEPARTMENTS > LOCATIONS > COUNTRIES > REGIONS

Foram utilizados quatro 'LEFT JOIN'.

Filtro aplicado:

sql
WHERE r.REGION_NAME IS NOT NULL


Resultado real exportado do FreeSQL: 106 funcionários.

Arquivo: 'data/query_02.csv'

6. EDA e qualidade dos dados

# Query 1

- Registros: 107
- Duplicatas: 0
- Salário médio: 6.461,83
- Mediana: 6.200,00
- Moda: 2.500,00
- Mínimo: 2.100,00
- Máximo: 24.000,00
- Desvio padrão: 3.909,58
- 'DEPARTMENT_ID' e 'DEPARTMENT_NAME': 1 valor nulo

O registro sem departamento corresponde ao funcionário 178 — Kimberely Grant, com salário de 7.000. Isso demonstra um efeito esperado de 'LEFT JOIN': o funcionário é preservado mesmo quando não existe correspondência em 'DEPARTMENTS'.

# Query 2

- Registros: 106
- Duplicatas: 0
- Salário médio: 6.456,75
- Mediana: 6.150,00
- Moda: 2.500,00
- Mínimo: 2.100,00
- Máximo: 24.000,00
- Desvio padrão: 3.927,80
- 'STATE_PROVINCE': 1 valor nulo

O registro com estado/província ausente corresponde a London, Reino Unido, funcionário 203 — Susan Jacobs. O restante da localização está preenchido.

7. Resultados por departamento

| Departamento | Funcionários | Salário médio |
|---|---:|---:|
| Executive | 3 | 19.333,33 |
| Accounting | 2 | 10.154,00 |
| Public Relations | 1 | 10.000,00 |
| Marketing | 2 | 9.500,00 |
| Sales | 34 | 8.955,88 |
| Finance | 6 | 8.601,33 |
| Human Resources | 1 | 6.500,00 |
| IT | 5 | 5.760,00 |
| Administration | 1 | 4.400,00 |
| Purchasing | 6 | 4.150,00 |
| Shipping | 45 | 3.475,56 |

O departamento Executive apresentou o maior salário médio, enquanto Shipping apresentou o maior número de funcionários.

8. Resultados por região

| Região | Funcionários | Salário médio |
|---|---:|---:|
| Europe | 36 | 8.916,67 |
| Americas | 70 | 5.191,66 |

A região Europe apresentou salário médio superior ao da região Americas na base analisada.

9. Cargos

Os cargos com maiores salários médios incluem:

| Cargo | Salário médio |
|---|---:|
| President | 24.000,00 |
| Administration Vice President | 17.000,00 |
| Marketing Manager | 13.000,00 |
| Sales Manager | 12.200,00 |
| Finance Manager | 12.008,00 |
| Accounting Manager | 12.008,00 |
| Purchasing Manager | 11.000,00 |
| Public Relations Representative | 10.000,00 |

10. Principais insights

1. O salário médio geral da Query 1 foi de 6.461,83.
2. A diferença entre o menor salário (2.100) e o maior (24.000) é ampla, indicando dispersão relevante na remuneração.
3. O departamento Executive possui o maior salário médio (19.333,33), enquanto Shipping concentra o maior número de funcionários (45).
4. Europe apresentou salário médio de 8.916,67, acima dos 5.191,66 observados em Americas.
5. A análise encontrou poucos problemas de qualidade: não há duplicatas, mas existem valores nulos decorrentes principalmente da ausência de relacionamento/localização.

11. Gráficos

- Distribuição salarial

[Boxplot dos salários](graficos/boxplot_salarios.png)

- Salário médio por departamento

[Salário médio por departamento](graficos/salario_medio_departamento.png)

- Salário médio por região

[Salário médio por região](graficos/salario_medio_regiao.png)

- Top 10 cargos por salário médio

[Top 10 cargos](graficos/top10_cargos_salario_medio.png)

12. Como executar

 Pré-requisitos

- Python 3.10+
- Git
- VS Code
- Acesso ao FreeSQL

# Instalação

bash
git clone https://github.com/felipedpg/SCTEC-Projeto-Avaliativo-Modulo-1.git
cd projeto-rh-freesql
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


# Executar análise

Os arquivos 'query_01.csv' e 'query_02.csv' já correspondem aos resultados exportados do FreeSQL.

Execute:

bash
python python/analise_rh.py


13. Versionamento GitHub

Branches sugeridas:

main
feature/sql
feature/dados
feature/analise
feature/graficos
docs/readme

Exemplos de commits:

feat(sql): adiciona consultas de salarios e localizacao
feat(dados): adiciona resultados das consultas do FreeSQL
feat(analise): implementa analise exploratoria em Python
feat(graficos): adiciona visualizacoes de salarios
docs: atualiza README com resultados e instrucoes


14. Melhorias futuras

- Dashboard interativo em Power BI.
- Análise histórica usando 'JOB_HISTORY'.
- Automatização da extração.
- Indicadores adicionais de RH.
- Filtros por cargo, departamento, país e região.
- Monitoramento automatizado da qualidade dos dados.