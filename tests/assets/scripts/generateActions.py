dbs = ["oracle", "sqlserver", "postgres", "mysql"]
vers = ["4.0.9", "4.1.5"]

cont_pre = """name: sei{}-precarga-{}

on:
  push:
  workflow_dispatch:

jobs:
  test:
    uses: ./.github/workflows/testCargaPre.yml
    secrets: inherit
    with:
      sei-version: {}
      db: {}

"""

cont_carga = """name: sei{}-carga-{}

on:
  push:
  workflow_dispatch:

jobs:
  test:
    uses: ./.github/workflows/testCarga.yml
    secrets: inherit
    with:
      sei-version: {}
      db: {}
"""

head="""|Versão| Mysql | Postgres | SqlServer | Oracle
|--|--|--|--|--|
"""

body = """| 4.1.5 | [![sei{}-precarga-{}](actions/workflows/badge-sei{}-precarga-{}.yml/badge.svg)](actions/workflows/badge-sei{}-precarga-{}.yml) [![sei{}-carga-{}](actions/workflows/badge-sei{}-carga-{}.yml/badge.svg)](actions/workflows/badge-sei{}-carga-{}.yml) | [![sei{}-precarga-{}](actions/workflows/badge-sei{}-precarga-{}.yml/badge.svg)](actions/workflows/badge-sei{}-precarga-{}.yml) | [![sei{}-precarga-{}](actions/workflows/badge-sei{}-precarga-{}.yml/badge.svg)](actions/workflows/badge-sei{}-precarga-{}.yml) | [![sei{}-precarga-{}](actions/workflows/badge-sei{}-precarga-{}.yml/badge.svg)](actions/workflows/badge-sei{}-precarga-{}.yml) |"""

for v in vers:
    for db in dbs:

        print(f"Criando arquivo de precarga {v} db: {db}")

        with open(f"generated/badge-sei{v}-precarga-{db}.yml", "w", encoding="utf-8") as f:
            c = cont_pre.format(v, db, v, db)
            f.write(c)

        print(f"Criando arquivo de carga {v} db: {db}")

        with open(f"generated/badge-sei{v}-carga-{db}.yml", "w", encoding="utf-8") as f:
            c = cont_carga.format(v, db, v, db)
            f.write(c)




