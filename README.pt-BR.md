# Cajuí

[English](README.md) | Português brasileiro

**Rede de sensores sem fio feita com placas ESP32/LoRa de prateleira: pontos de
medição a bateria, uma única placa como receptora e as medições guardadas no seu
computador.**

Um transmissor Cajuí é uma placa Heltec com um sensor e uma bateria. A cada cinco
minutos ele acorda, lê o sensor, envia a medição por LoRa e volta a dormir. A
receptora é outra placa da mesma família, ligada ao Wi-Fi: recebe as medições de
todos os transmissores e as entrega a um broker MQTT na sua rede. Dali, o Cajuí
Central guarda o histórico e mostra o painel, ou o Home Assistant consome os dados
diretamente. Coleta e monitoramento ficam na sua rede, sem serviço em nuvem.

O rádio usa um protocolo próprio, ponto a ponto entre transmissores e receptora.
Por isso basta uma placa dessas, rodando o firmware Cajuí, para receber: não há
gateway nem servidor de rede LoRaWAN no caminho.

Hoje o firmware de referência lê temperatura e umidade (SHT4x ou DHT22/AM2302) em
duas placas Heltec. É o primeiro exemplo completo, do sensor ao painel.

```mermaid
flowchart LR
    S[Sensor] --> T[Transmissor]
    T <-->|LoRa| R[Receptora]
    R -->|Wi-Fi| B[Broker MQTT]
    B --> C[Cajuí Central]
    B --> H[Home Assistant]
    C --> V[Painel e histórico]
```

[Experimente o Central](#experimente-o-painel-sem-placas) · [Monte um enlace de sensores](#monte-seu-primeiro-enlace-de-sensores) ·
[Leia os guias](#documentação) · [Contribua](#contribuições)

**O Cajuí é experimental.** Montagem e instalação do firmware ainda exigem
trabalho técnico, e os limites da próxima seção valem para qualquer instalação.

## Para onde o projeto vai

A arquitetura foi desenhada para uma rede de sensores de uso geral, não só para
clima. Três objetivos orientam o desenvolvimento:

- outros tipos de sensor, como umidade do solo, nível de água e chuva;
- vários sensores no mesmo transmissor;
- meses de bateria entre recargas.

Nenhum dos três está pronto. Cada transmissor lê um sensor de clima; outro sensor
exige driver e suporte na aplicação; a autonomia real ainda não foi medida e
depende da placa, do sensor, da bateria e do intervalo de envio. Alcance e
capacidade da rede também não foram estabelecidos. O
[estado do projeto](docs/pt-BR/status.md) separa o que está implementado, o que
falta validar e o que ainda não existe.

## O que cada parte faz

| Parte | Função |
| --- | --- |
| Sensor | Mede uma grandeza física e se conecta ao transmissor por uma interface compatível. |
| Transmissor | Lê o sensor e envia medições por LoRa. Pode dormir entre leituras. |
| Receptora | Aceita transmissores pareados, confirma mensagens de rádio e encaminha amostras por Wi-Fi. |
| Broker MQTT | Distribui mensagens às aplicações inscritas. A instalação Docker do Central inclui um. |
| Cajuí Central | Armazena leituras, apresenta painel e histórico e ajuda no diagnóstico dos dispositivos. |
| Home Assistant | Consome os dados MQTT da receptora como alternativa; o Central é opcional. |

Broker e Central podem rodar no mesmo computador; precisam continuar ligados para
receber e armazenar novos dados. A interface atual do Central é restrita ao
computador local porque ainda não tem autenticação de usuários.

## Experimente o painel sem placas

O [Cajuí Central](https://github.com/cajui/cajui-central/blob/main/README.pt-BR.md#experimente-sem-hardware)
inclui uma instalação com Docker Compose e uma amostra simulada. Inicie o sistema,
cadastre o dispositivo de demonstração e explore o painel e o histórico antes
de montar o hardware.

A interface oferece português brasileiro e inglês. Você pode nomear dispositivos
e sensores, organizar medições em seções e distinguir falhas de sensor de
dispositivos que pararam de enviar. O [guia do Central](docs/pt-BR/central.md)
explica histórico, estados e administração.

## Monte seu primeiro enlace de sensores

Comece com uma receptora e um transmissor:

| Você precisa de | Montagem de referência atual |
| --- | --- |
| Receptora | Heltec WiFi LoRa 32 V3 com antena LoRa adequada |
| Transmissor | Heltec WiFi LoRa 32 V3 com DHT22/AM2302 ou Wireless Stick Lite V3 com SHT4x; também precisa de antena |
| Alimentação e ligação | Alimentação para as duas placas, cabo USB de dados e ligação do sensor adequada à sua tensão e interface |
| Rede | Wi-Fi de 2,4 GHz para a receptora e um broker MQTT acessível |
| Monitoramento | Computador executando o Central ou uma instalação existente do Home Assistant com MQTT |

1. Confira a [compatibilidade e a ligação das placas](docs/pt-BR/components.md).
2. Siga a [instalação](docs/pt-BR/setup.md): prepare o broker, instale o firmware
   correto, configure a rede da receptora e cadastre o transmissor.
3. Confirme a chegada de uma leitura à aplicação e nomeie o dispositivo e o sensor.
4. Confira recepção e recuperação no local de uso com o [guia de operação](docs/pt-BR/operations.md).

Cada transmissor de referência lê um sensor de clima. Outros modelos de sensor
exigem suporte no firmware. Adeque frequência, potência e antena à sua região.
O ponto de acesso aberto, o MQTT sem criptografia de transporte e os limites do
pareamento descritos em [rádio e segurança](docs/pt-BR/radio-security.md) exigem
um ambiente confiável para configuração.

## Repositórios

| Repositório | Comece aqui para… |
| --- | --- |
| [cajui-central](https://github.com/cajui/cajui-central) | Executar o painel, trabalhar na aplicação ou integrar um produtor HTTP/MQTT |
| [cajui-firmware](https://github.com/cajui/cajui-firmware) | Instalar o firmware, adicionar suporte a sensores ou estudar o protocolo de rádio |
| [docs](https://github.com/cajui/docs) | Entender o conjunto, a instalação e a operação |

## Documentação

| Guia | Conteúdo |
| --- | --- |
| [Arquitetura](docs/pt-BR/overview.md) | Topologia, serviços e caminho de uma medição |
| [Componentes](docs/pt-BR/components.md) | Placas, alimentação, antenas e interfaces dos sensores |
| [Instalação](docs/pt-BR/setup.md) | Do firmware e broker à primeira leitura |
| [Cajuí Central](docs/pt-BR/central.md) | Painel, histórico, cadastro e estado dos dispositivos |
| [MQTT e integrações](docs/pt-BR/mqtt-integrations.md) | Permissões, Home Assistant e descoberta |
| [Operação](docs/pt-BR/operations.md) | Diagnosticar leituras ausentes, atualizar e recuperar |
| [Fluxo de dados](docs/pt-BR/data-flow.md) | Confirmações, filas e limites de entrega |
| [Rádio e segurança](docs/pt-BR/radio-security.md) | Pareamento, criptografia e limites de confiança |
| [Inventário de funções](docs/pt-BR/inventory.md) | Capacidades e estado da implementação |
| [Desenvolvimento](docs/pt-BR/development.md) | Organização do código e testes |
| [Glossário](docs/pt-BR/glossary.md) | Termos e abreviações |
| [Estado e compatibilidade](docs/pt-BR/status.md) | Revisões documentadas e validações pendentes |

## Contribuições

Experimente as instruções e relate onde elas falham ou deixam uma etapa pouco
clara. Correções de documentação e traduções ficam aqui; mudanças no firmware
e na aplicação pertencem aos respectivos repositórios. Consulte
[CONTRIBUTING.pt-BR.md](CONTRIBUTING.pt-BR.md) para editar e validar. Mantenha as
páginas em inglês e português brasileiro sincronizadas.

## Licença

Esta documentação está sob a [Apache-2.0](LICENSE).
