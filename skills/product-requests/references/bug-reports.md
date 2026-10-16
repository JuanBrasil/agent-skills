# Relatos de bugs prontos para investigação

Use quando o pedido tiver intermitência, logs, inconsistência entre telas ou risco de efeito parcial. A finalidade é escrever o card; não executar um workflow de debugging.

## Evidência e reprodução

Preserve o erro exato e a sequência conhecida: tela → ação → resultado. Inclua horário, rota, ambiente, frequência e solução temporária somente quando fornecidos ou efetivamente observados.

Distinga uma situação em que o usuário percebe o problema de passos que o reproduzem de forma consistente. “Depois de um tempo aberto” é uma condição relatada, não uma reprodução determinística.

- Sem reprodução conhecida: registrar o sintoma e indicar o que capturar na próxima ocorrência.
- Tentativa que não reproduziu: dizer somente que aquela tentativa não reproduziu; não concluir que o bug inexiste ou já foi corrigido.
- Print ou código de erro: sustenta o sintoma mostrado, mas normalmente não prova a causa técnica.

Não exigir logs ou acesso ao código para escrever um relato útil. Não criar seções de evidência vazias nem pedir dados que já estão no card.

## Investigação direcionada

Indique uma pergunta concreta e o dado que ajudaria a respondê-la, em vez de listar toda a stack como suspeita.

Exemplo: “Verificar qual requisição falha ao retornar à aba e se a sessão permanece válida nesse momento. Capturar rota, horário, status da resposta e identificador da requisição, quando disponíveis.”

Não afirmar que o sistema usa uma biblioteca, endpoint, tabela ou mecanismo de autenticação sem evidência. Não converter `CONFLICT`, `UnknownError` ou uma falha visual em diagnóstico fechado.

Quando uma tela divergir de outra, identificar a entidade e os valores conflitantes conhecidos. Pedir que se confira a regra ou origem compartilhada e a atualização das duas telas; não prescrever migração ou arquitetura sem diagnóstico.

## Resultado e verificação esperados

O card deve explicar qual comportamento correto substitui o sintoma. Se houve perda de estado, relacionar a recuperação aos campos e filtros afetados. Se existe solução temporária, distingui-la da correção: “F5 resolve” não significa que reload automático seja a solução.

Critérios de aceite devem conferir:

- a situação relatada e o resultado correto;
- uma variação pertinente ou caminho que já funcionava, quando houver risco concreto de regressão;
- erro/recuperação e preservação de estado quando fizerem parte do problema.

Não inventar um tempo arbitrário para provar correção de intermitência. Descrever condições a exercitar e evidência a observar; não garantir ausência de erro em todas as páginas por uma única tentativa bem-sucedida.

Em operações com possível gravação parcial, como cadastro, pagamento ou envio, recomendar verificar o que foi efetivamente registrado antes de repetir. Não presumir que a mensagem de erro implica ausência de gravação. Explicitar no comportamento esperado a prevenção de duplicidade e a preservação de registros legítimos, quando esse risco for pertinente ao caso.

## Exemplo fictício

Entrada: “Quando volto para a aba, às vezes aparece ‘Não foi possível carregar esta seção’. F5 resolve, mas perco o filtro.”

### Problema atual

Ao retornar à aba do navegador, a seção às vezes exibe **“Não foi possível carregar esta seção”**. Conforme o relato, F5 recupera o conteúdo, mas o filtro selecionado é perdido. Não há uma sequência de reprodução consistente informada.

### Comportamento esperado

Ao voltar à aba, manter a seção utilizável ou permitir recuperar o carregamento na própria tela, preservando o filtro selecionado. Uma falha temporária não deve obrigar o usuário a recomeçar a consulta.

### Investigação

Verificar qual requisição falha no retorno à aba e registrar seu horário, status e identificador quando disponíveis. Conferir se a falha coincide com perda de conexão ou mudança de sessão, sem assumir uma dessas causas como confirmada.

### Verificação esperada

Selecionar um filtro, alternar entre abas e conferir o retorno à seção. Se ocorrer a falha, a recuperação deve restaurar o conteúdo sem perder o filtro. Conferir também que o carregamento normal continua funcionando.
