#!/bin/bash

set -e

php -r "
    require_once '/opt/sip/web/Sip.php';
    \$conexao = BancoSip::getInstance();
    \$conexao->abrirConexao();
    \$r = \$conexao->consultarSql('select texto_log from infra_log');
	print_r(\$r);"

php -r "
    require_once '/opt/sei/web/SEI.php';
    \$conexao = BancoSEI::getInstance();
    \$conexao->abrirConexao();
    \$r = \$conexao->consultarSql('select texto_log from infra_log');
	print_r(\$r);"