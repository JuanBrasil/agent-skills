---
name: delivery-validation
description: Confere entregas em cards ou issues, testa primeiro no produto e compara o pedido vigente com evidências atuais. Apresenta o resultado e conduz aprovação ou devolução após o veredito do usuário, usando Product Requests para redigir pendências. Não implementa correções.
---

# Delivery Validation

Conduza a revisão assistida: entender a rodada vigente → fazer a primeira conferência no produto → apresentar resultado e referências → agir conforme o veredito. Use o idioma do usuário; português brasileiro por padrão. A primeira tentativa é sempre do agente; o usuário avalia depois, sobretudo aceite visual e pontos inconclusivos.

## Contexto e destino

Leia [references/personalization.md](references/personalization.md) para localizar um perfil privado opcional com board/repositório, identidade de quem aprova, estados e preferências. Nunca publique dados desse perfil como parte da skill. Instruções da sessão prevalecem e o perfil sozinho não autoriza mutações.

Quando não houver item indicado, pegue o primeiro na fila de aprovação configurada, na ordem atual. Trabalhe um por vez, salvo lote/recorte explícito. Use o destino indicado pelo usuário, sem priorizar silenciosamente por data, tamanho ou urgência. Se a fila estiver vazia, informe e pare. Se faltar destino essencial, peça apenas a identificação necessária.

Leia [references/workflow-routing.md](references/workflow-routing.md) para Trello ou GitHub. Confirme os estados reais no mesmo board/projeto; não crie listas, projetos ou mapeamentos por aproximação. No GitHub, encerrar uma issue e alterar o status em Projects são operações distintas: aplique somente a transição configurada e autorizada.

## Rodada vigente

Leia título, descrição quando necessária, comentários e referências pertinentes, verificando autoria e datas. A posição visual não define cronologia: comentários novos podem aparecer acima.

1. Havendo comentário de quem solicita/aprova, o último comentário dessa pessoa define a rodada atual. Compare com as respostas da equipe posteriores a ele e com a evidência atual.
2. Se o último comentário for confirmação ou resposta curta, use o antecedente mínimo para interpretá-lo; não procure simplesmente o último pedido longo.
3. Descrição e discussões anteriores servem para localizar a tela ou interpretar referências. Não some critérios antigos nem recobre partes já aceitas.
4. Sem comentário do solicitante, use título, descrição e critérios pertinentes. Comentários apenas da equipe não substituem o pedido.
5. Separe pedido, entrega declarada e resultado observado ou relatado pelo usuário. Silêncio, testes da equipe, PRs e deploy não provam aceite nem teste próprio.

Se a identidade de quem define o escopo estiver ambígua, resolva antes de selecionar comentários por suposição. Leia [references/learned-patterns.md](references/learned-patterns.md) somente quando exemplos de rodada ajudarem; são fictícios, não evidência atual.

## Primeira conferência

Abra o produto e exercite os comportamentos do pedido vigente com interações proporcionais e reversíveis. Inspecione a imagem/arte quando a rodada pedir fidelidade visual; se o papel da imagem for incerto, descreva-a como referência anexada sem inventar sua origem.

Use o navegador e perfil autorizado, reutilizando sessões existentes. Quando a preferência for Chrome local, use Playwright em extensão ou ferramenta conectada equivalente; se desconectar, ajude a reconectar, sem trocar silenciosamente para perfil isolado. Não extraia senhas ou cookies.

Use uma janela de revisão separada da janela pessoal do usuário. Reutilize abas da revisão; redescubra identificadores quando o usuário mover páginas ou abas forem fechadas. Deixe card/issue ou sua referência e a tela exata do produto abertos para avaliação. Feche ou reutilize abas de casos encerrados; preserve os pares ainda inconclusivos. Não feche abas pessoais.

Antes de declarar falha de carregamento, ative a aba, aguarde o conteúdo esperado com timeout finito e releia após navegação. Uma aba ainda hidratando não comprova bug. Faça tentativas pertinentes sem insistência ilimitada; se ainda faltar evidência, diga exatamente o que ficou inconclusivo. Restaure filtros/buscas de teste e não declare interações que não executou.

Conferir não autoriza alterar dados reais, registrar pagamentos, enviar formulários/mensagens nem implementar código. Para teste de formulário sem envio, bloqueie a transmissão antes da submissão; validação visual não comprova persistência. Se não for possível garantir ausência de gravação, não envie. Um teste real explicitamente autorizado deve ser identificado e restrito ao escopo combinado.

## Apresentação e veredito

Entregue um resumo curto com link Markdown comum e clicável do item:

- **Pedido vigente:** o que precisa estar feito nesta rodada.
- **Entrega informada:** o que a equipe declarou depois desse pedido, incluindo lacunas; diga se não há resposta posterior.
- **Minha conferência:** o que foi efetivamente testado e o resultado: comprovado, falha reproduzida ou inconclusivo.
- **Para conferir:** somente aceite visual ou ponto que ainda depende do usuário, com as páginas prontas.

Não exiba o card inteiro, payload, snapshot ou prévia de recurso no chat. Por padrão, indique onde está a imagem pelo link do item; não incorpore anexos nem baixe mídia só para exibi-la. Mostre imagem no chat apenas se solicitado. Não prometa que o formato do link controla o navegador em que o app abrirá.

Se houver dúvida visual, apresente diferenças como pontos a avaliar, não reprovações automáticas. Não force conclusão. Se o usuário disser “só falta a sidebar, o resto está bom”, cobre só a sidebar. Não adicione paleta, contadores ou outras diferenças excluídas.

No fluxo individual, aguarde o veredito depois de apresentar sua checagem. Autorização para testar não equivale a concluir/reprovar. Não avance enquanto o usuário avalia, salvo sequência já autorizada. Para lote explicitamente autorizado, leia [references/batch-review.md](references/batch-review.md).

## Agir conforme a resposta

- **Aprovado/funcionou/pode concluir:** mover ao estado de conclusão configurado, sem comentário positivo por padrão. Mover a uma lista chamada Archived não significa arquivar realmente.
- **Reprovado/faltou/parcial:** escrever e publicar a pendência usando Product Requests, confirmar a gravação e devolver ao estado de correção configurado. Preserve no texto o que funciona, quando necessário para delimitar o escopo.
- **Ainda não testei/dúvida/resposta ambígua:** continue ajudando; não mova nem publique reprovação.

O relato do usuário é suficiente para agir; não exija print ou teste próprio adicional. Não atribua a você a reprodução feita por ele. Se houver mais de um item plausível, peça só a identificação; se a reprovação não esclarecer a falha, peça o que faltou. Não peça autorização novamente para o mesmo fluxo já solicitado.

Antes de alterar, releia o estado quando houver intervalo relevante ou sinal de mudança. Se já está no destino, não mova de novo. Uma nova entrega material ainda não avaliada deve ser apresentada antes de agir sobre uma versão anterior.

## Encadear com Product Requests

**Ao redigir/revisar a pendência, leia e aplique [Product Requests](../product-requests/SKILL.md) e seu [modelo de escrita](../product-requests/references/writing-model.md).** É uma dependência para escrever, não para iniciar ou concluir toda validação. Não exige subagent ou nova conversa. Se faltar essa skill, procure no ambiente e informe a limitação antes de alegar que a usou.

Se Product Requests continuar indisponível após a busca, preserve a conferência e informe a limitação. Não publique a pendência nem execute a devolução que depende desse comentário até resolver a dependência. Isso não impede concluir uma entrega aprovada que não exige redação.

Passe a ela: identidade/link do item, pedido vigente, entrega declarada, evidências/relato do usuário, pendências autorizadas e exclusões. O resumo ao usuário pode ser curto; a cobrança deve explicar a interação e as regras pertinentes sem expandir o escopo. Não substitua um pedido de comentário por alteração da descrição. Se o usuário pediu ajuste de um comentário já publicado, edite-o em vez de duplicar.

Se a validação revelar uma ideia nova e independente, não a misture com critérios já aprovados. Crie um pedido separado somente quando solicitado, com link/caminho e print conforme o perfil. A passagem entre skills conserva autorização, preferências de acesso e os limites de teste; não peça de novo informações já observadas.

Para publicar, siga [references/publication.md](../product-requests/references/publication.md). Em retorno incerto, verifique antes de repetir. Se comentar funcionar mas mover falhar, conclua somente o movimento pendente, sem republicar. Confirme brevemente nome/link e destino; diga quando comentou. Só passe ao próximo se solicitado ou já autorizado.
