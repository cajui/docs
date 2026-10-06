# Documentação do Cajuí

[English](README.md) | Português brasileiro

O Cajuí é um sistema open source para coletar medições de sensores por LoRa e
disponibilizá-las em uma rede local. Inclui firmware para transmissores e receptores,
integração MQTT e o Cajuí Central, uma aplicação de monitoramento com interface web
e armazenamento persistente.

Os transmissores enviam medições a uma receptora, que as encaminha a um broker MQTT.
O Cajuí Central e o Home Assistant podem consumir essas mensagens de forma independente.

## Primeiros passos

1. Leia a [visão geral do sistema](docs/pt-BR/overview.md) para conhecer a arquitetura e o papel de cada componente.
2. Confira o [hardware e as interfaces compatíveis](docs/pt-BR/components.md) e o [estado do projeto](docs/pt-BR/status.md).
3. Siga o [guia de instalação](docs/pt-BR/setup.md) para configurar uma receptora, um transmissor e a aplicação.

## Documentação

| Seção | Conteúdo |
| --- | --- |
| [Arquitetura](docs/pt-BR/overview.md) | Topologia física, serviços e terminologia |
| [Componentes](docs/pt-BR/components.md) | Hardware, firmware, alimentação e interfaces dos sensores |
| [Funcionalidades](docs/pt-BR/inventory.md) | Capacidades e estado de implementação por subsistema |
| [Fluxo de dados](docs/pt-BR/data-flow.md) | Identificação de amostras, confirmações, filas e garantias de entrega |
| [Rádio e segurança](docs/pt-BR/radio-security.md) | Cadastro na rede, transmissão, criptografia e limites de confiança |
| [MQTT e integrações](docs/pt-BR/mqtt-integrations.md) | Tópicos, permissões, descoberta e Home Assistant |
| [Instalação](docs/pt-BR/setup.md) | Requisitos, provisionamento e configuração inicial |
| [Cajuí Central](docs/pt-BR/central.md) | Cadastro, painéis, histórico e administração |
| [Operação](docs/pt-BR/operations.md) | Diagnóstico, atualizações e recuperação |
| [Desenvolvimento](docs/pt-BR/development.md) | Organização do código, responsabilidades dos módulos e testes |
| [Glossário](docs/pt-BR/glossary.md) | Termos e abreviações |
| [Estado do projeto](docs/pt-BR/status.md) | Versões documentadas e limitações conhecidas |

## Estado do projeto

O Cajuí está em desenvolvimento ativo. As aplicações de firmware são experimentais,
e algumas funcionalidades estão disponíveis apenas em branches de desenvolvimento.
Consulte o [estado do projeto](docs/pt-BR/status.md) para identificar as versões
abrangidas pela documentação e os limites atuais de validação.

## Repositórios

| Repositório | Finalidade |
| --- | --- |
| [cajui-firmware](https://github.com/cajui/cajui-firmware) | Protocolo de rádio, firmware das placas e ferramentas de provisionamento |
| [cajui-central](https://github.com/cajui/cajui-central) | Servidor de monitoramento, armazenamento e interface web |
| [docs](https://github.com/cajui/docs) | Arquitetura, instalação e documentação entre projetos |

## Contribuições

Contribuições à documentação são bem-vindas. Consulte [CONTRIBUTING.pt-BR.md](CONTRIBUTING.pt-BR.md)
para conhecer as convenções de escrita e os comandos de validação.

## Licença

Esta documentação é licenciada sob a [Apache-2.0](LICENSE).
