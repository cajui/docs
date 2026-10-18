# Referência de funcionalidades

[English](../en/inventory.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

As funcionalidades estão agrupadas por subsistema. Os rótulos de estado se referem às
versões listadas em [estado do projeto](status.md); as aplicações de firmware continuam
experimentais.

## Sensores e alimentação

| Funcionalidade | Estado | Detalhes |
| --- | --- | --- |
| Leituras DHT22/AM2302 | Implementado | Temperatura e umidade no transmissor WiFi LoRa 32 V3 |
| Leituras SHT4x | Implementado | Driver I2C e alvo Wireless Stick Lite V3 |
| Validação CRC do SHT4x | Implementado | Verifica as duas palavras da resposta e informa erros de medição |
| Controle da alimentação do sensor e sono profundo | Implementado | Alimentação do sensor desligada entre ciclos de envio |
| Medição de bateria e ajuste de envio por baixa tensão | Validação pendente | Calibração do divisor e limiares exigem medição no hardware |

Referências: [aplicações dos sensores](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/radio-applications.md),
[Stick Lite](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/stick-lite.md).

## Rádio e vínculo com a rede

| Funcionalidade | Estado | Detalhes |
| --- | --- | --- |
| Identidades estáveis e chaves por vínculo | Implementado | IDs de rede e nó identificam dispositivos; chaves autorizam a comunicação |
| Provisionamento USB, retomada e revogação | Implementado | Ferramenta de provisionamento com suporte à recuperação |
| Pareamento por rádio iniciado pelo operador | Implementado | Janela de dois minutos e aprovação de candidato; autenticação contra atacante ativo pendente |
| Proteção AES-128-GCM de DATA/ACK | Implementado | Conteúdo autenticado com credenciais por vínculo |
| Contadores duráveis e tratamento de replay | Implementado | Reserva de contadores e registros de aceitação persistidos |
| Avaliação de canal e tentativas limitadas | Implementado | Atrasos aleatórios e limites de tentativas reduzem a disputa pelo canal |
| Teto configurável de potência de transmissão | Implementado | Configuração por dispositivo dentro da faixa do rádio |
| Comando de potência no ACK da versão 2 | Implementado | O protocolo suporta o comando; a receptora atualmente solicita manter a potência |
| Leituras de RSSI e SNR | Implementado | A receptora informa diagnóstico dos quadros de rádio aceitos |

Referências: [protocolo](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/protocol-v1.md), [runtime](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/runtime.md),
[provisionamento USB](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/provisioning.md), [pareamento](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/radio-pairing.md).

## Configuração e encaminhamento da receptora

| Funcionalidade | Estado | Detalhes |
| --- | --- | --- |
| Aceitação durável antes do ACK de rádio | Implementado | Registro de aceitação e amostra gravados antes da confirmação |
| Fila persistente de amostras | Implementado | Guarda as 128 amostras mais recentes; conta os descartes das mais antigas |
| Encaminhamento MQTT QoS 1 | Implementado | Remove uma amostra da fila após o PUBACK correspondente ao publicador |
| Página de configuração por Wi-Fi temporário | Implementado | Ponto de acesso iniciado por botão, configuração e estado |
| Seletor de redes e recuperação da busca | Implementado | Tentativas de busca limitadas e entrada manual de redes ocultas |
| Persistência independente do Wi-Fi | Implementado | Salva Wi-Fi verificado antes da configuração MQTT |
| Recuperação MQTT após tentativas de Wi-Fi | Implementado | Restaura conexões suspensas com tentativas limitadas |
| Descoberta do broker | Implementado | Descoberta de endereço por mDNS com anúncio na máquina do broker |
| Disponibilidade e estado dos dispositivos | Implementado | Estado MQTT retido e Last Will da receptora |
| Comandos MQTT de pareamento e revogação | Implementado | Disponíveis a clientes autorizados pelo canal de gestão |
| MQTT Discovery do Home Assistant | Implementado; validação de integração pendente | Publica definições de entidades suportadas |

Referências: [aplicações](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/radio-applications.md),
[gestão](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/management-v1.md), [Home Assistant](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/home-assistant.md).

## Monitoramento

| Funcionalidade | Estado | Detalhes |
| --- | --- | --- |
| Armazenamento atômico e deduplicação de amostras | Implementado | Identidade de origem/dispositivo/amostra com detecção de conflito |
| Sessão MQTT persistente do consumidor | Implementado | O broker guarda mensagens dentro dos limites configurados |
| Cadastro de dispositivos e sensores | Implementado | Nomes de exibição e locais |
| Organização do painel | Implementado | Seções com dispositivos, sensores ou medições individuais |
| Histórico e exportação CSV | Implementado | Histórico por período com leituras originais paginadas; CSV cobre dados recentes da visão geral |
| Detecção de ausência de dados | Implementado | Baseada em amostras novas e únicas e nos intervalos de envio esperados |
| Assistente de configuração da receptora | Implementado | Dados de conexão e verificação do estado recebido |
| Remoção de receptoras e sensores da lista | Implementado | Preserva histórico; novas observações que atendam aos critérios restauram os itens |
| Tabela de diagnóstico MQTT | Implementado | Últimas 100 observações dos tópicos assinados, em memória |
| Atualização de estado da conexão em tempo real | Implementado | SSE com recuperação após interrupções |
| Internacionalização da interface | Implementado | Inglês e português brasileiro |

Referência: [configuração e interface do Central](https://github.com/cajui/cajui-central/blob/23ee539454c133fee42e020975e7d3dc662937e9/README.md).

## Manutenção

| Funcionalidade | Estado | Detalhes |
| --- | --- | --- |
| Atualizações assinadas da receptora | Implementado | Pacotes enviados localmente com verificação |
| Rollback da aplicação | Implementado | Duas partições de aplicação e validação de inicialização |
| Instalação e atualizações por USB | Implementado | Procedimentos separados para placa nova e atualização que preserva armazenamento |

Referência: [atualizações de firmware](https://github.com/cajui/cajui-firmware/blob/de9ddaa602faa6507a686a9f468d8f7377fd09dd/docs/updates.md).

## Capacidades não suportadas

As aplicações atuais não oferecem seleção arbitrária de drivers de sensores, fila de
amostras no transmissor entre ciclos de envio, atualização de firmware do transmissor
por LoRa, LoRaWAN, roteamento em malha, TDMA ou controle de atuadores. Consulte o
[estado do projeto](status.md) para os requisitos de compatibilidade e validação.
