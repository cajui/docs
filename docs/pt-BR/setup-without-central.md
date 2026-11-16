# Instalação sem o Central

[English](../en/setup-without-central.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

O Central é opcional. Esta página cobre uma instalação com o Home Assistant ou outro
consumidor MQTT, um broker existente ou a configuração por USB. Para o caminho com o
Central, consulte a [instalação](setup.md).

## 1. Prepare o broker

Use um broker alcançável pela rede da receptora. Crie uma conta de produtor para a
receptora, com escrita nos espaços de telemetria, gestão e Discovery dela, e contas
separadas para os consumidores; consulte [contas e permissões](mqtt-integrations.md#contas-e-permissões).
A implantação do Central com Docker também oferece um broker e ferramentas de
credenciais, sem usar o painel.

**Resultado esperado:** o consumidor conecta ao broker com a própria conta.

## 2. Instale o firmware

Siga a etapa 2 do [guia de instalação](setup.md#2-instale-o-firmware).

## 3. Configure a receptora

1. Segure o botão PRG da receptora por três segundos para abrir a configuração.
2. Entre na rede Wi-Fi temporária dela e abra `http://192.168.4.1`.
3. Selecione uma rede de 2,4 GHz ou informe um SSID oculto e suas credenciais.
4. Quando o Wi-Fi conectar, toque em **Refresh** até a busca terminar, o que leva até
   cerca de um minuto. Na seção **MQTT broker**, escolha um broker encontrado na rede ou
   informe o endereço, depois a porta e as credenciais de produtor, e salve.
5. Toque em **Refresh** até o estado mostrar o Wi-Fi conectado e **Broker: online**.

O endereço do broker deve ser alcançável pela rede da receptora. Um nome de contêiner
interno pode resolver apenas dentro do Docker. A receptora lista os brokers anunciados
por mDNS e os que respondem na porta 1883, ou na porta já informada, na própria
sub-rede; consulte as observações da [instalação](setup.md#3-adicione-a-receptora).

**Resultado esperado:** a página informa **Broker: online**.

### Por USB

A [ferramenta de provisionamento USB](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/provisioning.md#receiver-uplink-settings)
grava as configurações de rede da receptora sem a página de configuração. Ela exige
todos os campos, inclusive a rede Wi-Fi e a senha, mesmo para trocar só o broker. Para
trocar só o broker, use a página de configuração, que mantém o Wi-Fi salvo.

## 4. Vincule um transmissor

Use o [pareamento por rádio](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/radio-pairing.md)
pela página de configuração da receptora: toque em **Search for transmitters**, segure o
botão PRG do transmissor por três segundos e toque em **Add**. Outra opção é o
[provisionamento por USB](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/provisioning.md#enroll-resume-and-verify).

Verifique separadamente a aceitação pelo rádio e a entrega à aplicação: um ACK de rádio
correspondente confirma a aceitação pela receptora; uma leitura na aplicação confirma
que a amostra chegou ao consumidor.

**Resultado esperado:** o transmissor aparece na lista de transmissores vinculados da
página da receptora.

## 5. Configure o Home Assistant

Ative a integração MQTT do Home Assistant com o prefixo de Discovery padrão
`homeassistant` e verifique as entidades suportadas; consulte o
[Home Assistant](mqtt-integrations.md#home-assistant).

**Resultado esperado:** as medições do transmissor aparecem como entidades.

## 6. Verifique a instalação

Siga a etapa 6 do [guia de instalação](setup.md#6-verifique-a-instalação).
