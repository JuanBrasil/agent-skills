# Modelo de pedidos de produto

## O que os exemplos ensinam

Pedidos bem desenvolvidos usam linguagem de produto: o texto funciona como especificação para implementação, não como resumo do pedido. Os padrões observados são:

- Título com verbo e resultado concreto: “Corrigir…”, “Adicionar…”, “Permitir…”, “Reorganizar…”. Não exigir etiquetas entre colchetes.
- Tela/rota quando conhecida, seguida do comportamento atual e de sua consequência prática.
- Comportamento esperado desenvolvido em ações, campos, estados e regras verificáveis.
- Seções com nomes do assunto: “Regras dos status”, “Card expandido”, “Lidas e não lidas”, “Salvamento”, “Hierarquia visual”.
- Exemplos concretos e fluxos com setas; contrastes antes/depois quando esclarecem o erro.
- Preservação de dados, funções e padrão visual pertinente à mudança.
- Detalhes como atualização imediata, persistência e consistência entre telas quando relevantes ao fluxo. Não copiar “sem F5” ou “persistir entre dispositivos” para todo card indiscriminadamente.
- Em bugs: separar sintoma, investigação e resultado esperado. Hipóteses técnicas não substituem prova.

Esses cards são referências de estilo, não prova de autoria por IA nem de funcionamento atual do sistema. A presença na lista concluída também não transforma cada frase em uma regra universal para novos pedidos.

## Transformar relato curto em especificação

Antes de escrever, identifique o que o relato está pedindo e procure contexto relevante já disponível. Para revisar um card, leia a descrição, discussão pertinente e anexos que possam resolver ambiguidades. Não é necessário varrer o board em toda execução; este modelo já preserva o estilo aprendido.

Depois, desenvolva os pontos que mudam a implementação:

1. **Local e escopo:** qual tela, componente, entidade ou conjunto de itens muda?
2. **Interação:** onde o usuário começa, qual ação executa, qual resposta vê?
3. **Condições:** como se comporta em estados diferentes relevantes ao pedido?
4. **Regra:** qual campo, relação, nível, fórmula ou transição orienta o resultado?
5. **Exemplo:** uma sequência, exemplo numérico ou antes/depois torna a regra mais clara?
6. **Preservação:** quais dados/funções poderiam ser afetados por essa mudança?
7. **Conferência:** o que demonstra que o comportamento foi entregue?

Isso é uma lente de elaboração, não sete seções obrigatórias. Um card de ordenação pode ter problema, funcionamento, exemplo e regras; uma página nova pode separar layout, estados e cada área funcional.

## Como aprofundar sem inventar

“Não inventar” não significa repetir o usuário. Separe:

| Tipo | Como escrever |
| --- | --- |
| Relato ou evidência | Descrever como atual, preservando a origem quando importar. |
| Consequência necessária do pedido | Explicitar como comportamento esperado. Ordenar muda a sequência, não o conteúdo dos registros. |
| Escolha de UX ainda não definida | “Sugestão”, “por exemplo”, “preferir o padrão já existente”. Uma proposta marcada pode trazer detalhes concretos. |
| Regra de negócio sem base | Perguntar ou manter decisão em aberto. Não inventar taxa, enum, hierarquia comercial, acesso ou exclusão de registros. |
| Causa técnica possível | “Investigar se…”. Não diagnosticar pela aparência do print ou pelo nome do erro. |

Exemplo: “ordenar por tipo de entrega” permite detalhar opção de ordenação, conjunto afetado, visualização do critério ativo e exemplo ilustrativo. A–Z/Z–A pode ser uma sugestão explícita; não uma política comprovada. Não autoriza filtros novos, agrupamento expansível, exportação ou analytics.

Se o local exato não estiver disponível, mantenha “listagem de entregas” e não invente uma rota. Tipos fictícios servem apenas para demonstrar a ordem; os tipos reais devem vir do cadastro existente.

## Apresentação

Use `###` para seções, **negrito** para campos e ações, listas para regras paralelas e `código inline` para labels, estados e fluxos curtos. Separe título de conteúdo com uma linha em branco.

Evite headings vazios, numeração repetida, caracteres invisíveis, cartões de citação/favicons copiados de IA, conclusões que só repetem o card e blocos de código vazios. Não reproduza links de acesso com tokens, dados pessoais ou identificadores privados nos exemplos reutilizáveis.

Seções de layout devem descrever hierarquia, posição, densidade e interação; “melhorar o visual” sozinho não orienta implementação. Seções de dados devem distinguir referência comercial, evento real e efeitos nos cálculos quando o contexto permitir.
