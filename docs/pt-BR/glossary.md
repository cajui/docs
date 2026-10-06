# Glossário

[English](../en/glossary.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

| Termo | Definição |
| --- | --- |
| Cajuí | Ecossistema de telemetria de sensores, incluindo firmware e software de monitoramento |
| Cajuí Central | Servidor de monitoramento e aplicação web |
| Sensor | Componente que mede uma ou mais grandezas físicas |
| Métrica | Identificador de uma grandeza, como temperatura ou umidade relativa |
| Leitura | Valor ou estado de qualidade de uma métrica em uma amostra |
| Amostra | Grupo de leituras que compartilham uma identidade de entrega |
| Transmissor / nó | Dispositivo de rádio vinculado à rede que coleta e envia amostras |
| Receptora | Dispositivo de rádio que aceita amostras e as encaminha por MQTT |
| Firmware | Software instalado em uma placa |
| LoRa | Modulação usada no enlace de rádio |
| LoRaWAN | Protocolo de rede construído sobre LoRa, não suportado pelo firmware atual |
| Perfil de rádio | Configurações de frequência e modulação compartilhadas pelos dispositivos que se comunicam |
| CAD | Detecção de atividade no canal antes da transmissão |
| RSSI | Intensidade do sinal recebido, expressa em dBm |
| SNR | Relação sinal-ruído, expressa em dB |
| Cadastro na rede / vínculo | Associação autorizada entre nó, rede e credenciais |
| ACK de rádio | Confirmação autenticada de aceitação pela receptora |
| MQTT | Comunicação por publicação e assinatura entre receptoras, broker e aplicações |
| Broker | Servidor que distribui mensagens MQTT aos clientes assinantes |
| Tópico | Canal de mensagens dentro do broker |
| QoS 1 | Nível de entrega MQTT com confirmação e possibilidade de duplicatas |
| PUBACK | Confirmação MQTT de uma publicação QoS 1 |
| ACL | Regras de controle de acesso que determinam as permissões de uma conta sobre tópicos |
| Mensagem retida | Último valor de um tópico armazenado pelo broker |
| Last Will | Mensagem publicada pelo broker após uma desconexão inesperada do cliente |
| mDNS | Mecanismo de descoberta de serviços locais usado para localizar um broker anunciado |
| MQTT Discovery | Mensagens de definição de entidades usadas pelo Home Assistant |
| Fila | Amostras que aguardam encaminhamento à próxima etapa de entrega |
| Replay | Reutilização de um quadro anterior, avaliada contra o estado de aceitação persistido |
| Deduplicação | Reconhecimento de identidades de amostra repetidas |
| Vext / Ve | Alimentação externa com controle de liga/desliga para sensores na placa de referência |
| I2C / SDA / SCL | Barramento do sensor e seus sinais de dados e relógio |
| Qwiic / STEMMA QT | Convenções de conectores para fiação I2C compatível |
| SSE | Eventos enviados pelo servidor para atualizar o estado dos dispositivos no navegador |
| SQLite | Banco de dados usado pelo Central |
| Partição OTA | Partição de aplicação usada durante atualizações de firmware e rollback |

Consulte [arquitetura](overview.md) para as relações entre componentes e
[fluxo de dados](data-flow.md) para as garantias de entrega.
