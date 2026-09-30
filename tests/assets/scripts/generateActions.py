dbs = ["mysql", "postgres", "sqlserver", "oracle"]
vers = ["4.0.9", "4.0.12", "4.0.12.15", "4.1.5"]

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

body_image_pre="[![sei{}-precarga-{}](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei{}-precarga-{}.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei{}-precarga-{}.yml)"
body_image_carga="[![sei{}-carga-{}](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei{}-carga-{}.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei{}-carga-{}.yml)"

body = ""

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



for v in vers:

    body += f"| {v} "

    for db in dbs:

        img_pre = body_image_pre.format(v, db, v, db, v, db)
        img_carga = body_image_carga.format(v, db, v, db, v, db)
        body += '|' + img_pre + '<br>' + img_carga

    body += "|\n"

body = head + body

print(body)