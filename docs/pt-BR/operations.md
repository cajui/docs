# Operação e diagnóstico

[English](../en/operations.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

## Diagnóstico

Acompanhe uma amostra com falha desde a leitura do sensor até a entrega por rádio,
o encaminhamento MQTT e a ingestão pela aplicação. Confira o estado de cada etapa
antes de alterar a configuração.

| Sintoma | Verificações | Comportamento relevante |
| --- | --- | --- |
| Sem resposta USB | Cabo de dados, porta e ID estável do dispositivo | Portas seriais podem mudar após a reconexão |
| Erro de sensor com ACK de rádio bem-sucedido | Alimentação, fiação e driver do sensor | A qualidade da medição é independente da entrega por rádio |
| Sem ACK de rádio | Antenas, perfil, vínculo e integridade do armazenamento | A receptora pode aceitar amostras enquanto o MQTT está indisponível |
| Wi-Fi conectado, mas a aplicação não recebe dados | Endereço do broker, credenciais, ACLs e assinaturas | Wi-Fi e MQTT têm estados de conexão separados |
| Busca do broker sem resultados | Anúncio mDNS e alcance do multicast | Há suporte à entrada manual do endereço |
| Fila da receptora cresce | Conexão com o broker e processamento de PUBACKs | A fila é limitada; confira os contadores de amostras descartadas |
| Fila esvazia sem leituras no consumidor | Permissões de tópicos, identidade e logs do consumidor | O MQTT 3.1.1 pode confirmar publicações negadas |
| Estado desconectado demora após falta de energia | Keepalive MQTT e Last Will | A detecção de desconexão depende do timeout do broker |
| Receptora conectada, mas transmissor sem dados recentes | Última amostra única e intervalo de envio | Transmissores em sono profundo são monitorados pela chegada de amostras |
| Novas chegadas contêm condições antigas | Acúmulo na fila e horários | O horário de chegada inclui o atraso de encaminhamento |
| Entidades do HA ausentes | Permissões de Discovery, prefixo, ID de origem e suporte às métricas | Discovery e telemetria usam tópicos separados |
| Itens removidos reaparecem | Novas amostras ou estado ao vivo dos dispositivos | A remoção da lista preserva o acesso do produtor |

## Informações de diagnóstico

O histórico de medições registra leituras ao longo do tempo. O estado dos dispositivos
registra os últimos valores de fila, tempo ligado, firmware e disponibilidade. Os logs
e o buffer de diagnóstico MQTT descrevem eventos recentes de processamento.

Confira os horários ao interpretar o diagnóstico. O último sinal Wi-Fi conhecido ou o
contador de encaminhamentos de uma receptora desconectada pode continuar visível após
a perda da conexão.

## Atualizações

Faça backup do banco do Central antes de atualizar seu esquema. O downgrade do esquema
não é suportado; voltar a uma versão anterior pode exigir o binário antigo e seu backup
correspondente.

Atualizações de firmware devem preservar o vínculo e o estado dos contadores. A receptora
aceita pacotes de atualização assinados enviados pela página de configuração e usa duas
partições de aplicação com tratamento de rollback. Transmissores são atualizados por USB.
O alvo Stick Lite está atualmente fora do fluxo de releases assinadas e instalação web.

Siga as [instruções de atualização do firmware](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md) para compatibilidade
de imagens, organização das partições e procedimentos de recuperação. Uma instalação
em placa nova inicializa o armazenamento dos vínculos e não deve ser usada como
atualização de rotina.

## Verificação de recuperação

Após mudanças de configuração ou firmware, verifique as configurações salvas depois
de reiniciar, o vínculo, a entrega de novas amostras, o andamento da fila da receptora
e a reconexão da aplicação. Reabrir e fechar a configuração deve preservar uma conexão
MQTT estabelecida no firmware com o comportamento de recuperação atualizado.

A cobertura automatizada e as verificações físicas pendentes estão documentadas no
[estado do projeto](status.md). Para detalhes dos campos de log, consulte as
[aplicações de rádio](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md) e a
[operação do Central](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md).
