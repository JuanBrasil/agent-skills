# Exemplos de feedback

Todos os exemplos abaixo são fictícios, para demonstrar o modelo de escrita. Use o formato como apoio, preservando a intenção do pedido real. Escolhas sem definição na entrada aparecem como sugestões, não como fatos do sistema.

## Pedido curto: ordenar por tipo de entrega

Entrada: “Falta um ordenar por tipo de entrega.”

O relato identifica o critério, mas não a tela nem a direção. Redija no contexto de listagem de entregas; não invente a localização. Se houver print acessível, use-o para identificar o controle existente.

Título: **Adicionar ordenação por tipo de entrega**

### Problema atual

Falta uma opção para ordenar a listagem pelo **tipo de entrega**. Sem esse critério, não é possível colocar entregas do mesmo tipo em sequência para facilitar a conferência.

### Comportamento esperado

Adicionar **Tipo de entrega** às opções de ordenação da listagem, seguindo o padrão dos controles já existentes.

Ao selecionar esse critério, reorganizar as entregas pelo tipo cadastrado em cada uma.

### Funcionamento da ordenação

**Sugestão de comportamento**, caso ainda não exista uma regra equivalente na tela:

- **Tipo: A–Z** — ordem alfabética crescente.
- **Tipo: Z–A** — ordem alfabética decrescente.
- Mostrar o critério e a direção ativos no controle de ordenação.
- Atualizar a ordem na própria listagem, sem exigir recarregar a página.

Se a tela já possui um padrão de alternância e indicação da direção, reutilizá-lo.

### Exemplo ilustrativo

Antes:

`Vídeo dedicado → Inserção → Stories → Inserção`

Com **Tipo: A–Z**:

`Inserção → Inserção → Stories → Vídeo dedicado`

Os nomes acima são apenas exemplos. Usar os tipos já cadastrados no sistema, sem criar uma lista paralela de categorias.

### Regras importantes

- A alteração reorganiza a exibição; não modifica tipo, dados, status ou quantidade de entregas.
- Ordenar não deve ocultar entregas. Filtros existentes continuam delimitando os itens exibidos.
- Se houver grupos de campanha ou influenciador, definir pelo contexto qual nível recebe a ordenação. Não misturar entregas de grupos diferentes nem ordenar somente os grupos quando o pedido é ordenar as entregas.
- Não transformar essa opção em um novo filtro ou agrupamento expansível.

Critério de aceite: ao selecionar a ordenação por tipo, as entregas ficam na sequência correspondente, mantendo os mesmos registros e filtros aplicados.

O exemplo desenvolve a interação central sem acrescentar plataforma, prioridade de formatos, persistência entre sessões ou regra para valores vazios que a entrada não definiu.

## Fluxo com estados: campanha expansível

Entrada com contexto: “Na aba Campanhas do portal, quero ver as informações na própria listagem. Hoje preciso abrir outra página. Mostrar nome, cliente, período e status no cabeçalho; detalhes com Entregas, Informações e Documentos. Manter as ações atuais e a largura do Painel.”

Título: **Exibir detalhes das campanhas em cards expansíveis no portal**

### Problema atual

Na aba **Campanhas**, consultar os detalhes exige sair da listagem e abrir outra página. A mudança deve permitir consultar essas informações no próprio card.

### Comportamento esperado

Manter a aba Campanhas como página própria e transformar cada campanha em um card expansível.

`Campanha recolhida → clicar → detalhes no próprio card → clicar novamente → recolher`

### Card recolhido

Mostrar no cabeçalho:

- Nome da campanha.
- Cliente.
- Data de início → data de fim.
- Status.
- Controle visual para expandir/recolher.

Exemplo ilustrativo:

**Campanha de setembro**

`Cliente X · 01/09/2026 → 30/09/2026 · Ativa · ⌄`

### Card expandido

Manter o cabeçalho visível e abrir os detalhes dentro do card, separados em:

**Entregas | Informações da campanha | Documentos**

- **Entregas:** mostrar as entregas vinculadas à campanha e manter as ações que o usuário já pode executar.
- **Informações:** mostrar os dados da própria campanha disponíveis para o usuário.
- **Documentos:** mostrar os documentos vinculados à campanha e permitidos para esse usuário.

### Layout e preservação

- Utilizar a mesma largura útil do Painel.
- Manter as ações existentes; mudar o layout não deve eliminar funções.
- Expandir/recolher na mesma página, sem navegar para uma rota adicional.
- Reutilizar a identidade visual do portal.

### Estados propostos

**Sugestão:** iniciar os cards recolhidos para facilitar a leitura da listagem. Se uma campanha não possuir entregas ou documentos, mostrar um estado vazio na aba correspondente, mantendo o cabeçalho e as informações disponíveis.

Não adicionar busca, novas colunas, novos documentos ou novas permissões só porque aparecem em outro exemplo de Campanhas. A entrada deste exemplo não pede essas funções.

## Ordenação em dois níveis

Entrada: “O filtro fica fora da tabela, mas só ordena os itens dentro de cada grupo. Quero ordenar os grupos.”

Saída:

**Ordenar os grupos da listagem principal**

**Problema atual:** o controle aparece no nível da listagem principal, mas altera apenas a ordem dos itens dentro de cada grupo.

**Comportamento esperado:** aplicar esse controle à ordem dos grupos exibidos. Manter a ordenação interna dos itens independente.

**Critério de aceite:** ao mudar a ordenação principal, a sequência dos grupos muda e a ordenação interna permanece conforme sua própria regra.

## Sintoma de login, sem causa confirmada

Entrada: “Depois de um tempo aberto, clico em entrar e ele redireciona sem logar.”

Saída:

**Corrigir login que não conclui após período de inatividade**

**Problema atual:** conforme o relato, após a página ficar aberta por algum tempo, clicar em entrar redireciona sem concluir o login.

**Comportamento esperado:** concluir o login quando válido ou apresentar uma mensagem clara se não for possível autenticar.

**Ponto de investigação:** verificar se o período de inatividade influencia a sessão e o redirecionamento. A causa ainda não foi confirmada.

Não transforme a hipótese em “o token expirou” nem prescreva renovação de token como causa comprovada. Se o usuário quiser só o relato curto, omita a investigação.

## Ajuste simples

Entrada: “Troca ‘Enviar’ por ‘Salvar alterações’ no botão da tela de perfil, só isso.”

Saída: Na tela de perfil, alterar o texto do botão de “Enviar” para “Salvar alterações”.

## Print não prova comportamento

Entrada: um print desktop mostra um botão sobre o último campo do formulário.

Saída: No print enviado, o botão se sobrepõe ao último campo do formulário. Ajustar o posicionamento para que campo e botão permaneçam visíveis sem sobreposição.

Não alegue que o botão está impossível de clicar, que ocorre também em mobile ou que todos os formulários são afetados sem evidência.

## Resultado esperado ainda ambíguo

Entrada: “Esse total está errado”, sem valor esperado ou regra de cálculo.

Prepare o relato com a tela/campo conhecido e peça a regra ou um exemplo do valor esperado se necessário para orientar a correção. Não invente cálculo, exclusão de registros ou impacto financeiro.
