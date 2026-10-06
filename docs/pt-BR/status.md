# Estado do projeto e compatibilidade

[English](../en/status.md) | Português brasileiro

[Documentação](../../README.pt-BR.md)

O Cajuí está em desenvolvimento ativo. As aplicações de firmware são experimentais.
As funcionalidades suportadas e as limitações conhecidas estão listadas abaixo; a
[referência de funcionalidades](inventory.md) apresenta o índice completo por subsistema.

## Versões da documentação

Esta documentação abrange as seguintes revisões de código, verificadas em 06/10/2026:

| Projeto | Revisão | Disponibilidade na atualização da documentação |
| --- | --- | --- |
| Cajuí Central | [`76a9a18`](https://github.com/cajui/cajui-central/tree/76a9a189d9a8101bc74b07f6723f9541f9acb05d) | Incluída pelo [PR #33](https://github.com/cajui/cajui-central/pull/33) integrado |
| Cajuí Firmware | [`a2ce332`](https://github.com/cajui/cajui-firmware/tree/a2ce332b2e3ff704f8e35032381786497c287968) | Branch de desenvolvimento, [PR #25](https://github.com/cajui/cajui-firmware/pull/25) |

Os links de referência técnica apontam para essas revisões. Imagens instaladas e
releases publicadas podem conter um conjunto anterior de funcionalidades.

O firmware de desenvolvimento adiciona o alvo Stick Lite/SHT4x, recuperação da busca
Wi-Fi, persistência independente das configurações de Wi-Fi verificadas e melhorias na
recuperação MQTT. O alvo Stick Lite suporta instalação por USB e está fora dos artefatos
de releases assinadas e instalação web nesta versão.

## Rótulos de funcionalidades

- **Implementado:** disponível na implementação documentada.
- **Em desenvolvimento:** disponível na revisão de desenvolvimento do firmware acima.
- **Validação pendente:** comportamento implementado com verificações físicas ou de integração em aberto.
- **Não suportado:** fora da implementação atual.

Esses rótulos descrevem a disponibilidade do software; os requisitos de compatibilidade
de hardware e validação continuam se aplicando.

## Limitações conhecidas

### Rádio e hardware

Alcance de rádio, operação sob interferência contínua, capacidade em escala, consumo em
sono profundo, calibração da bateria e limiares de baixa tensão exigem mais medições.
Os testes de armazenamento físico para perda arbitrária de energia e durabilidade da
memória flash estão incompletos.

As aplicações atuais suportam os sensores climáticos documentados. Outros modelos
exigem drivers e configuração da aplicação adicionais. O protocolo fornece telemetria
por LoRa direto; LoRaWAN, malha, TDMA e controle de atuadores não são suportados.

### Segurança

O protocolo não passou por auditoria independente de segurança. O pareamento por rádio
não possui autenticação contra atacante ativo. O ponto de acesso temporário de
configuração fica aberto enquanto habilitado, e a receptora usa MQTT sem TLS. Implante
o sistema dentro dos limites de confiança descritos em [rádio e segurança](radio-security.md).

### Testes de integração

As mensagens e os templates de Discovery do Home Assistant foram verificados; os testes
com uma instalação do Home Assistant em execução continuam pendentes. A persistência
de Wi-Fi sem broker após desligar e religar a placa e a continuidade do MQTT durante uma
visita à configuração sem alterações também exigem verificação no hardware para o
firmware de desenvolvimento.

## Referências técnicas

| Assunto | Referência |
| --- | --- |
| Capacidades do firmware | [README](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/README.md) |
| Protocolo de rádio | [Especificação](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/protocol-v1.md) |
| Máquina de estados de entrega | [Runtime](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/runtime.md) |
| Registros duráveis e fila | [Persistência](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/persistence.md) |
| Comportamento da placa e encaminhamento MQTT | [Aplicações](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-applications.md) |
| Stick Lite/SHT4x | [Guia da placa](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/stick-lite.md) |
| Provisionamento e pareamento | [USB](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/provisioning.md), [rádio](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/radio-pairing.md) |
| Gestão MQTT | [Contrato](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/management-v1.md) |
| Home Assistant | [Integração](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/home-assistant.md) |
| Instalação e atualizações | [Atualizações de firmware](https://github.com/cajui/cajui-firmware/blob/a2ce332b2e3ff704f8e35032381786497c287968/docs/updates.md) |
| APIs e configuração do Central | [README do Central](https://github.com/cajui/cajui-central/blob/76a9a189d9a8101bc74b07f6723f9541f9acb05d/README.md) |
