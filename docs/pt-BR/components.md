# Componentes

[English](../en/components.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

## Componentes do sistema

| Componente | Localização | Responsabilidades | Dependências |
| --- | --- | --- | --- |
| Sensor | Ponto de medição | Mede grandezas do ambiente | Alimentação, fiação e driver compatíveis |
| Transmissor | Placa de rádio remota | Lê sensores, criptografa quadros, envia amostras e processa ACKs | Sensor, alimentação, antena e vínculo com a rede |
| Receptora | Placa de rádio com acesso à rede | Valida quadros, enfileira amostras, envia ACKs e publica via MQTT | Antena, armazenamento persistente, Wi-Fi e configuração do broker |
| Broker MQTT | Máquina na rede | Distribui mensagens e aplica permissões de tópicos | Serviço de rede, contas e ACLs |
| Cajuí Central | Computador ou servidor | Armazena leituras, oferece monitoramento e solicita ações de gestão | SQLite e MQTT para o tráfego da receptora |
| Navegador | Computador ou tablet cliente | Apresenta a interface web do Central | Acesso permitido pela política da interface do Central |
| Home Assistant | Serviço separado | Consome telemetria e definições de entidades | Integração MQTT e permissões no broker |

## Alvos de firmware

| Alvo | Placa | Função | Sensor |
| --- | --- | --- | --- |
| `runtime_tx` | Heltec WiFi LoRa 32 V3 | Transmissor | DHT22/AM2302 |
| `runtime_rx` | Heltec WiFi LoRa 32 V3 | Receptora | Recebe nós vinculados |
| `runtime_tx_stick_lite` | Heltec Wireless Stick Lite V3 | Transmissor | SHT4x por I2C |

O alvo Stick Lite está em desenvolvimento e suporta instalação apenas por USB.
Consulte as [versões documentadas](status.md) antes de selecionar uma imagem. Os perfis
de placa definem a pinagem e o comportamento da tela; use a imagem compilada para a
placa correspondente.

## Interfaces dos sensores

O DHT22/AM2302 usa um sinal de dados e um driver DHT. O SHT4x usa I2C, com SDA, SCL,
alimentação e terra. O modelo do sensor determina o driver e as medições suportadas.

Adaptadores passivos Qwiic/STEMMA QT fornecem conexões I2C compatíveis. Uma ligação
direta com as mesmas conexões elétricas usa o mesmo driver. A compatibilidade do
conector, por si só, não garante tensão compatível, endereço disponível ou suporte
no firmware.

O perfil experimental da Stick Lite usa GPIO33 para SDA e GPIO34 para SCL, reservando
GPIO35 para o LED da placa. Consulte o [guia da placa](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md) para
fiação e sequência de alimentação. As [aplicações de referência](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md)
documentam a pinagem do DHT22 e a configuração da receptora.

## Alimentação e antenas

Os transmissores controlam a alimentação do sensor e entram em sono profundo entre
os ciclos de envio. A receptora permanece disponível para receber pelo rádio e
encaminhar dados por Wi-Fi. Ambos os papéis transmitem: receptoras enviam confirmações
e mensagens de pareamento. Instale uma antena LoRa adequada em cada placa antes de
operar o rádio.

A medição de tensão da bateria e o ajuste do intervalo de envio por bateria baixa estão
implementados. A calibração do divisor, os limiares e o consumo em sono profundo precisam
de validação adicional no hardware. A proteção da bateria é um requisito do circuito,
separado da gestão de energia pelo firmware. Consulte as [limitações do projeto](status.md)
para verificar o estado da validação.
