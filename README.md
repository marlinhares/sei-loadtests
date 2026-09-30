# SEI Load Tests

Projeto com scripts no jmeter para testes de carga e stress no SEI.

Testado em SEI: 4.0.9, 4.0.12, 4.0.12.15, 4.1.3, 4.1.4 e 4.1.5.

|Versão| Mysql | Postgres | SqlServer | Oracle
|--|--|--|--|--|
| 4.0.9 |[![sei4.0.9-precarga-oracle](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-oracle.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-oracle.yml)<br>[![sei4.0.9-carga-oracle](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-oracle.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-oracle.yml)|[![sei4.0.9-precarga-sqlserver](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-sqlserver.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-sqlserver.yml)<br>[![sei4.0.9-carga-sqlserver](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-sqlserver.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-sqlserver.yml)|[![sei4.0.9-precarga-postgres](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-postgres.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-postgres.yml)<br>[![sei4.0.9-carga-postgres](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-postgres.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-postgres.yml)|[![sei4.0.9-precarga-mysql](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-mysql.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-precarga-mysql.yml)<br>[![sei4.0.9-carga-mysql](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-mysql.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.0.9-carga-mysql.yml)|
| 4.1.5 |[![sei4.1.5-precarga-oracle](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-oracle.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-oracle.yml)<br>[![sei4.1.5-carga-oracle](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-oracle.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-oracle.yml)|[![sei4.1.5-precarga-sqlserver](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-sqlserver.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-sqlserver.yml)<br>[![sei4.1.5-carga-sqlserver](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-sqlserver.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-sqlserver.yml)|[![sei4.1.5-precarga-postgres](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-postgres.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-postgres.yml)<br>[![sei4.1.5-carga-postgres](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-postgres.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-postgres.yml)|[![sei4.1.5-precarga-mysql](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-mysql.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-precarga-mysql.yml)<br>[![sei4.1.5-carga-mysql](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-mysql.yml/badge.svg)](https://github.com/marlinhares/sei-loadtests/actions/workflows/badge-sei4.1.5-carga-mysql.yml)|

Um aspecto importante a se levar em conta é que a instalação de módulos pode acarretar falha nos testes caso mude as chamadas das requisições.



## Divisão do Projeto

Primeiro escolha a versão do SEI selecionando a pasta correspondente.
**Na pasta selecionada, existe um readme com as orientações para rodar o teste.**

Ao entrar em cada pasta existe um README específico:

- **testes de carga e stress:**
	aqui ficam os testes em jmeter para fazer carga e stress nos ambientes, abordando diversos cenários de uso do SEI.

- **testes de monitoramento:**
	aqui ficam testes em jmeter que ao implantar o sistema nos deparamos com alguma lentidão. Foram necessários para o profissional da sustentação identificar possíveis gargalos relacionados a nó de aplicação ou ingress.
	Apenas SEI4.0.x.

	- **monitoramento-cookies-nagios:**
		esse teste faz inicialmente um apanhado dos cookies ofertados pela url com o  intuito de levantar os possíveis nós(ou pods) de entrada possíveis. Depois disso faz uma chamada ao sistema, logando com o usuário robô disponibilizado, e faz algumas operações simples para informar se o sistema está no ar.
		Segue junto um script para ser disponibilizado no Nagios para monitorar a disponiblidade


	- **monitoramento-nodes-ingress:**
		nesse teste você informa os possíveis nós físicos onde residem seus ingress kubernetes (ou seus balanceadores cattle, ou até mesmo as vms internas q ofertam o tráfego http ou https para o sistema) e dispara uma chamada independente para cada um deles testando o login e pesquisa simples de processo e documentos. A execução do teste em loop vai mostrar possíveis erros aleatórios que possam acontecer e listá-los para análise
