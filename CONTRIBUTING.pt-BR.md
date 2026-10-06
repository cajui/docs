# Contribuindo com a documentação do Cajuí

[English](CONTRIBUTING.md) | Português brasileiro

Contribuições são bem-vindas, incluindo correções, orientações de instalação,
procedimentos de diagnóstico e explicações da arquitetura.

## Convenções de escrita

- Escreva para usuários e contribuidores do projeto em inglês e português brasileiro.
- Apresente a finalidade de um componente antes dos detalhes de implementação.
- Use nomes consistentes para dispositivos, serviços e tipos de mensagem.
- Documente requisitos, resultados esperados e casos de falha relevantes.
- Distinga funcionalidades implementadas de trabalho em desenvolvimento e validação pendente.
- Mantenha as especificações técnicas nos repositórios de implementação e use links para elas.
- Use exemplos fictícios e omita credenciais ou dados que identifiquem uma instalação.

## Traduções

Os guias em inglês ficam em `docs/en`; os guias em português brasileiro, em `docs/pt-BR`.
Use nomes de arquivo correspondentes nos dois diretórios e um seletor de idioma que
ligue cada página à sua equivalente. Mantenha a navegação interna no idioma selecionado.
O README e o guia de contribuição da raiz também têm uma versão `.pt-BR.md`.

O inglês é a referência técnica. Atualize os dois idiomas no mesmo pull request,
incluindo os rótulos dos diagramas. Preserve comandos, caminhos, chaves de configuração,
identificadores e tópicos MQTT. Referências técnicas externas podem permanecer em inglês.

## Atualizando a documentação

1. Confira a implementação e as versões listadas em [estado do projeto](docs/pt-BR/status.md).
2. Atualize juntos os guias afetados, a referência de funcionalidades e os diagramas.
3. Mantenha os links de código fixados nas revisões documentadas. Atualize a tabela de
   versões ao mudar a implementação de referência.
4. Execute `python3 scripts/check_docs.py` e `python3 -m unittest discover -s tests -v`.
5. Confira a apresentação do Markdown e dos diagramas Mermaid e envie um pull request.

O script de validação verifica links locais de arquivos e títulos, fechamento dos
blocos de código, paridade de páginas, seletores de idioma, navegação interna, quantidade
de diagramas e marcadores de referência não resolvidos. Essas verificações não avaliam
a qualidade da tradução nem comprovam que o conteúdo está sincronizado. Revise o
significado técnico, a renderização dos diagramas e as referências externas separadamente.

## Licença

As contribuições são licenciadas sob a [Apache-2.0](LICENSE).
