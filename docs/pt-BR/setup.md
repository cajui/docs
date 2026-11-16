# Instalação e configuração

[English](../en/setup.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

Este guia instala uma receptora e um transmissor com o Cajuí Central e o broker que
vem com ele. Cada etapa termina com o que você deve ver antes de continuar. Para usar
o Home Assistant sem o Central, um broker existente ou a configuração por USB, consulte
a [instalação sem o Central](setup-without-central.md).

## Requisitos

- Uma placa transmissora e um sensor suportados.
- Uma placa receptora suportada e antenas LoRa adequadas para ambos os dispositivos.
- Fontes de alimentação apropriadas para as placas e os sensores.
- Uma rede Wi-Fi de 2,4 GHz. A receptora e o computador do Central precisam estar na
  mesma rede: a receptora procura o broker apenas na própria sub-rede.
- Um computador com Docker que fique ligado para receber e guardar as leituras.
- Um celular ou outro computador com Wi-Fi, para abrir a página de configuração da receptora.
- Um cabo USB com transmissão de dados para instalar o firmware.

Confira os [alvos suportados](components.md) e as [versões documentadas](status.md)
antes de selecionar o firmware.

## 1. Inicie o Central

Siga a [instalação do Central com Docker](https://github.com/cajui/cajui-central/blob/05f58ba12b6c2542018f9cbc7ee2d913b4e4a27f/docs/installation.md#docker)
e abra http://127.0.0.1:8080 no computador onde ele roda. O painel não tem login, por
isso só abre nesse computador. Num servidor sem tela, abra-o de outro computador por um
[encaminhamento local de porta pelo SSH](https://github.com/cajui/cajui-central/blob/05f58ba12b6c2542018f9cbc7ee2d913b4e4a27f/docs/installation.md#server-without-a-screen).

Se quiser, defina `CAJUI_RECEIVER_HOST` com o endereço do computador na rede local para
o assistente da receptora mostrá-lo; consulte o
[endereço do broker para receptoras](https://github.com/cajui/cajui-central/blob/05f58ba12b6c2542018f9cbc7ee2d913b4e4a27f/docs/installation.md#broker-address-for-receivers).

**Resultado esperado:** o painel abre, e **Sistema → Broker MQTT** mostra o Central
conectado ao broker.

## 2. Instale o firmware

Instale a imagem de receptora na placa receptora e a imagem de transmissor na placa
transmissora. O [instalador web](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/updates.md#web-installer-usb)
instala as imagens publicadas da Heltec WiFi LoRa 32 V3 pelo Chrome ou pelo Edge. As
versões publicadas são anteriores à busca do broker pela receptora, usada na etapa 3,
e não incluem as outras placas. Nesses casos,
[compile e instale a partir do código-fonte](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/provisioning.md#build-and-install)
por USB.

Use o procedimento de instalação em placa nova apenas para uma placa não inicializada.
Atualizações normais preservam a partição dedicada que contém vínculos, contadores e
amostras na fila. Identifique os dispositivos por ID estável; os nomes das portas
seriais podem mudar após uma reconexão.

**Resultado esperado:** a instalação termina sem erros. Uma receptora sem transmissores
começa a escutar; um transmissor sem vínculo aguarda o pareamento.

## 3. Adicione a receptora

No Central, abra **Equipamentos → Receptores → Adicionar receptor** e siga as três etapas.

1. **Conectar ao receptor.** Segure o botão PRG da receptora por três segundos, conecte
   o celular à rede Wi-Fi `Cajui-XXXX` dela e abra `http://192.168.4.1`. Escolha sua rede
   de 2,4 GHz e salve a senha. A página informa o Wi-Fi conectado e as configurações salvas.
2. **Dados de conexão.** Na seção **MQTT broker** da página, escolha o broker encontrado
   na rede. Se aparecer mais de um, use o do computador do Central.
   Preencha o usuário e a senha mostrados pelo assistente e salve. A página informa
   **Broker: online**.
3. **Encontrar receptor.** O assistente lista a receptora quando ela se conecta. Confirme-a.

**Resultado esperado:** a receptora aparece em **Equipamentos → Receptores** como conectada.

Antes de depender da página de configuração, saiba como ela funciona:

- A página responde apenas na rede Wi-Fi da própria receptora, que o botão PRG abre por
  até 30 minutos. Trocar o broker depois exige alguém ao lado da receptora, ou USB.
- A rede de configuração fica aberta enquanto está ativa; consulte
  [rádio e segurança](radio-security.md).
- Escolher outra rede Wi-Fi apaga as configurações do broker salvas, para que a senha
  nunca seja enviada a um broker numa rede desconhecida. Escolha o broker e informe as
  credenciais de novo.
- A lista mostra os brokers que respondem na porta 1883 da sub-rede da receptora, sem
  depender do anúncio por mDNS do Central. Firmware mais antigo lista só os brokers
  anunciados por mDNS. Se o broker não aparecer, informe o endereço do computador na
  rede local.

Se a receptora não aparecer, as linhas de estado da página separam Wi-Fi e broker:

| A página da receptora mostra | Confira |
| --- | --- |
| Wi-Fi sem conseguir conectar | Nome e senha da rede; a rede precisa oferecer 2,4 GHz |
| Wi-Fi conectado, broker offline | Endereço, porta, usuário e senha; receptora e Central na mesma rede. No computador do Central, `docker compose logs broker` mostra se as tentativas de conexão chegam ao broker |
| Broker online, mas o assistente não lista nada | O assistente lista as receptoras que se conectam depois de ele abrir. Uma que já estava conectada aparece em **Equipamentos → Receptores** |

## 4. Pareie um transmissor

Abra **Equipamentos → Transmissores → Adicionar transmissor**, toque em **Buscar
transmissores**, segure o botão PRG do transmissor por três segundos e toque em
**Adicionar** quando ele aparecer. A receptora precisa estar conectada. O pareamento
por rádio não é autenticado contra um atacante ao alcance durante a busca de dois
minutos; consulte o
[pareamento por rádio](https://github.com/cajui/cajui-firmware/blob/47a6a652e788f99d3d6406dae837ba99223fe036/docs/radio-pairing.md).

**Resultado esperado:** o Central informa o transmissor pareado e, em seguida, enviando
leituras. Dê um nome a ele.

## 5. Organize o painel

Nomeie os sensores, atribua locais e organize o painel por dispositivo, sensor ou
medição. Consulte o [guia do Central](central.md).

**Resultado esperado:** a visão geral mostra cada medição com o seu nome.

## 6. Verifique a instalação

- Confirme que medições válidas chegam no intervalo esperado.
- Confira a fila da receptora e o estado de encaminhamento.
- Reinicie os dispositivos e confirme a preservação das configurações e dos vínculos.
- Teste a reconexão da aplicação e verifique as amostras seguintes.

Consulte [operação](operations.md) para diagnóstico e [estado do projeto](status.md)
para as validações de hardware ainda necessárias.
