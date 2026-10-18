# Cajuí Central

[English](../en/central.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

O Cajuí Central é um servidor de monitoramento em Go com armazenamento SQLite e
interface web incorporada. Ele aceita amostras MQTT e leituras HTTP, valida os dados
recebidos e oferece cadastro de dispositivos, painéis e histórico. A interface web
é servida pela aplicação Go e não exige um serviço de frontend separado.

## Ingestão de dados

Amostras MQTT são validadas e gravadas atomicamente. O Central deduplica entregas pela
identidade de origem, dispositivo e amostra, rejeitando conteúdo conflitante sob a
mesma identidade. As leituras preservam seu estado de qualidade e horário de chegada.

A disponibilidade da receptora e o estado dos dispositivos são armazenados separadamente
do histórico de medições. Esses registros fornecem informações de conexão, fila,
firmware e pareamento.

## Cadastro de dispositivos e sensores

O cadastro atribui nomes de exibição e locais aos dispositivos e sensores observados.
Os nomes são independentes das identidades de rádio e das credenciais MQTT. Um cadastro
de sensor pode conter várias medições, como temperatura e umidade.

O painel suporta seções nomeadas com dispositivos, sensores completos ou medições
individuais. Mudanças no arranjo preservam os cadastros e o histórico. Os gráficos
consultam leituras armazenadas por canal e data, com as linhas originais em tabela
paginada. O CSV cobre apenas leituras recentes da visão geral. A interface suporta
inglês e português brasileiro.

## Histórico

Escolha períodos predefinidos de até 30 dias ou um intervalo personalizado de até
366 dias por consulta. Os dados não são apagados automaticamente por idade. O
histórico usa a chegada ao Central, sem inferir o horário de aquisição de amostras
que ficaram em fila. Gráficos grandes selecionam pontos originais; a tabela
paginada mostra leituras originais, mais recentes primeiro. Faça backup antes de
atualizar: iniciar um binário antigo não desfaz as migrações do banco.

## Estado da conexão e das medições

| Estado | Interpretação |
| --- | --- |
| Receptora desconectada | A disponibilidade MQTT informa uma receptora desconectada |
| Transmissor sem dados recentes | Nenhuma amostra nova e única chegou em três intervalos de envio esperados |
| Erro de sensor | Uma amostra chegou com falha na medição |
| Estado desconhecido ou antigo | Não há valor atual disponível ou a idade do estado armazenado é incerta |

Atualizações de estado da receptora e do painel usam eventos enviados pelo servidor
(SSE). O navegador pausa as conexões de eventos quando a página está oculta e reconecta
após interrupções. Uma perda abrupta de energia da receptora ainda depende do timeout
MQTT do broker para que um evento de desconexão fique disponível.

## Administração

O Central pode solicitar pareamento e revogação de transmissores quando uma receptora
conectada informa suporte a essas funções. O vínculo de rádio é gerenciado pela receptora.

Remover uma receptora ou um sensor da lista preserva seu histórico e suas credenciais.
Novas observações que atendam aos critérios podem trazê-los de volta à lista. A revogação
de rádio e a revogação de uma conta MQTT são ações administrativas separadas.

## Diagnóstico MQTT

A página do broker exibe os estados da conexão e das assinaturas, configurações somente
para leitura e as últimas 100 observações recebidas. As entradas podem ser filtradas,
pausadas e expandidas para inspecionar o JSON normalizado. O buffer cobre as assinaturas
do Central e é limpo ao reiniciar. A configuração do broker é fornecida por variáveis
de ambiente e arquivos de segredos.

## Acesso e escopo

A interface do navegador usa restrições de acesso local e verificações de autorização
por capacidade. Mantenha a interface no computador local e siga a
[política de acesso](https://github.com/cajui/cajui-central/blob/23ee539454c133fee42e020975e7d3dc662937e9/README.md). A funcionalidade atual cobre monitoramento e a administração
suportada de dispositivos; controle de atuadores e um mecanismo geral de automação
não estão implementados.

## Referência

[README do Central](https://github.com/cajui/cajui-central/blob/23ee539454c133fee42e020975e7d3dc662937e9/README.md) · [Código da API e da interface](https://github.com/cajui/cajui-central/tree/23ee539454c133fee42e020975e7d3dc662937e9/internal/httpapi)
