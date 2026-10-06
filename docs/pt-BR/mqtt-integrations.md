# MQTT e integrações

[English](../en/mqtt-integrations.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

O broker MQTT conecta receptoras às aplicações de monitoramento. As receptoras publicam
telemetria, estado dos dispositivos e definições de entidades do Home Assistant.
Clientes autorizados podem solicitar ações administrativas suportadas pelo canal de gestão.

## Tópicos

| Família | Padrão de tópico | Finalidade | Retido |
| --- | --- | --- | --- |
| Telemetria | `telemetry/v1/<source>/<node>/samples` | Leituras de sensores e diagnóstico | Não |
| Disponibilidade | `manage/v1/<source>/<device>/availability` | Estado conectado/desconectado da receptora | Sim |
| Estado | `manage/v1/<source>/<device>/state` | Fila, firmware, pareamento e estado dos nós | Sim |
| Comandos | `manage/v1/<source>/<device>/commands` | Solicitações administrativas | Não |
| Resultados | `manage/v1/<source>/<device>/results` | Resultados de comandos | Não |
| HA Discovery | `homeassistant/sensor/<source>/<object>/config` | Definições de entidades | Sim |

`source` é o nome de usuário MQTT da receptora. Os identificadores precisam atender às
restrições de cada contrato. Em particular, a integração atual com Home Assistant exige
uma origem composta apenas por letras, dígitos, sublinhados e hífens. Um nome de usuário
com ponto pode publicar telemetria, mas desabilita a publicação de Discovery.

## Descoberta do broker

A receptora pode buscar um anúncio mDNS `_mqtt._tcp` na rede local. A descoberta
fornece o endereço e a porta do broker; a autenticação exige credenciais configuradas
separadamente.

A máquina do broker precisa anunciar o serviço em uma rede alcançável pela receptora.
No Docker Desktop, execute o script de anúncio do projeto na máquina hospedeira, pois
o multicast do contêiner não é exposto automaticamente à rede local. A entrada manual
de endereço está disponível quando a descoberta por multicast não funciona.

## Home Assistant

Configure a receptora e o Home Assistant para usar um broker alcançável e habilite a
integração MQTT do Home Assistant com o prefixo padrão de Discovery `homeassistant`.
A receptora publica definições retidas de entidades para as métricas suportadas.
O Central é opcional e pode funcionar junto com o Home Assistant.

As entidades suportadas incluem temperatura, umidade, diagnóstico de rádio, tensão da
bateria e diagnóstico da receptora, conforme os dados disponíveis. A disponibilidade
das entidades segue o estado da receptora e as regras de expiração das medições.
Modelos adicionais de sensores exigem suporte no driver.

As publicações e os templates de Discovery foram testados; a validação com uma instalação
do Home Assistant em execução ainda está pendente. Consulte a [referência da integração](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md)
para definições de entidades, permissões de tópicos e tratamento de configurações retidas antigas.

## Contas e permissões

Use contas separadas para receptoras e aplicações. Conceda a cada receptora acesso aos
seus tópicos de telemetria, gestão e Discovery. Conceda aos consumidores as assinaturas
necessárias; comandos administrativos exigem permissões adicionais.

A distribuição inclui ferramentas para criar, importar e revogar credenciais de
produtores. O assistente de configuração de receptoras do Central usa uma conta de
produtor configurada; ele não cria uma nova conta para cada dispositivo. As conexões
atuais da receptora usam MQTT sem TLS em uma rede confiável.

## Sessões e retenção

O Central usa uma sessão MQTT persistente. A configuração incluída do broker permite
até 1000 mensagens na fila por cliente e expira uma sessão após sete dias de ausência.
Alterações na configuração do broker podem mudar esses limites.

Mensagens retidas fornecem o último estado conhecido e definições de entidades. A
telemetria é publicada sem retenção; o histórico é armazenado pelas aplicações
consumidoras. O MQTT QoS 1 permite entregas duplicadas, tratadas pelo Central por meio
da identidade da amostra.

## Referências

[Gestão MQTT](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md) ·
[Configuração do broker no Central](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md) · [Garantias de entrega](data-flow.md)
