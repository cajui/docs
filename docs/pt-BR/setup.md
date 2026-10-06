# Instalação e configuração

[English](../en/setup.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

## Requisitos

- Uma placa transmissora e um sensor suportados.
- Uma placa receptora suportada e antenas LoRa adequadas para ambos os dispositivos.
- Fontes de alimentação apropriadas para as placas e os sensores.
- Uma rede Wi-Fi de 2,4 GHz alcançável pela receptora.
- Um broker MQTT e uma aplicação de monitoramento: Cajuí Central, Home Assistant ou outro consumidor compatível.
- Uma conexão USB com transmissão de dados para instalação inicial do firmware e provisionamento opcional.

Confira os [alvos suportados](components.md) e as [versões documentadas](status.md)
antes de selecionar o firmware. O alvo Stick Lite/SHT4x atualmente exige uma compilação
de desenvolvimento instalada por USB.

## 1. Inicie o broker e a aplicação

Siga as [instruções de instalação do Central](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md) para Docker ou Go.
A implantação com Docker inclui um broker; brokers existentes podem ser usados com
as contas e permissões de tópicos documentadas. Para uma implantação com Home Assistant,
configure sua integração MQTT seguindo o [guia de integração](mqtt-integrations.md).

Verifique se a aplicação conecta ao broker e assina os tópicos com sucesso. O endpoint
de saúde do banco de dados do Central não verifica a conectividade MQTT.

## 2. Instale o firmware

Compile ou selecione a imagem correta para cada placa e função. Siga as
[instruções de instalação e atualização](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md) e o
[guia de provisionamento USB](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md).

Use o procedimento de instalação em placa nova apenas para uma placa não inicializada.
Atualizações normais preservam a partição dedicada que contém vínculos, contadores e
amostras na fila. Identifique os dispositivos por ID estável; os nomes das portas
seriais podem mudar após uma reconexão.

## 3. Configure a rede da receptora

1. Segure o botão PRG da receptora por três segundos para abrir a configuração.
2. Entre na rede Wi-Fi temporária dela e abra `http://192.168.4.1`.
3. Selecione uma rede de 2,4 GHz ou informe um SSID oculto e suas credenciais.
4. Informe o endereço, a porta e as credenciais de produtor dedicadas do broker.
5. Confirme os estados de conexão do Wi-Fi e do broker.

O endereço do broker deve ser alcançável pela rede da receptora. Um nome de contêiner
interno pode resolver apenas dentro do Docker. A busca por mDNS está disponível quando
a máquina do broker anuncia o serviço na rede local.

O firmware com persistência independente de Wi-Fi salva as configurações verificadas
da rede antes da configuração do broker. Versões anteriores exigem as configurações
completas de encaminhamento. Consulte as [versões documentadas](status.md) para
identificar qual comportamento se aplica.

O assistente de configuração da receptora no Central fornece os dados de conexão e
verifica o estado recebido do dispositivo. Uma receptora passa a ser visível por meio
de suas publicações MQTT.

## 4. Vincule um transmissor

Escolha o [provisionamento por USB](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md) ou o
[pareamento por rádio](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md). Para parear por rádio, abra uma
janela na receptora, solicite a entrada no transmissor e aprove a identidade candidata.
O Central pode iniciar ações de pareamento suportadas pelo canal de gestão MQTT da
receptora quando ela está conectada.

Verifique separadamente a aceitação pelo rádio e a entrega à aplicação: um ACK de rádio
correspondente confirma a aceitação pela receptora; uma leitura na aplicação confirma
que a amostra chegou ao consumidor.

## 5. Configure o monitoramento

No Central, cadastre os dispositivos observados, atribua nomes e locais e organize o
painel por dispositivo, sensor ou medição. No Home Assistant, verifique as entidades
suportadas publicadas por MQTT Discovery.

## 6. Verifique a instalação

- Confirme que medições válidas chegam no intervalo esperado.
- Confira a fila da receptora e o estado de encaminhamento.
- Reinicie os dispositivos e confirme a preservação das configurações e dos vínculos.
- Teste a reconexão da aplicação e verifique as amostras seguintes.

Consulte [operação](operations.md) para diagnóstico e [estado do projeto](status.md)
para as validações de hardware ainda necessárias.
