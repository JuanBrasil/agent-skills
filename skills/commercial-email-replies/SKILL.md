---
name: commercial-email-replies
description: Prepare ou revise respostas individuais de email comercial, propostas de parceria, pedidos de orçamento, negociação, recusas e follow-ups. Use o histórico real e, quando presente, a personalização da instalação para aplicar voz, preços, restrições e organização da caixa de entrada.
---

# Respostas de email comercial

## Carregar a personalização

- Verificar se existe `personalization/profile.md` nesta instalação e ler antes de redigir ou avaliar elegibilidade. A pasta é opcional: sua ausência não bloqueia o core e não autoriza presumir políticas, preços, nomes ou preferências de outro usuário.
- Quando presente, carregar também as seções aplicáveis de `personalization/commercial-rules.md`; usar `personalization/style-examples.md` apenas para exemplos pertinentes. Esses arquivos contêm dados pessoais/comerciais e ficam fora da exportação pública.
- Seguir a instrução explícita atual, os acordos vigentes da conversa e a personalização aplicável. Impedimentos confirmados prevalecem sobre tabelas e exemplos; um exemplo nunca cria condição para outra campanha. O histórico da negociação não revoga uma restrição atual.
- Manter procedimentos reutilizáveis neste arquivo e nos scripts. Guardar identidade, estilo individual, contatos, fontes de preços, limites de creators, descontos autorizados, etiquetas, prazos internos e casos reais exclusivamente em `personalization/`. Não promover uma exceção pessoal ao core.
- Para configurar outra instalação, usar [o modelo de personalização](references/personalization.example.md). Sem perfil, adaptar-se ao pedido e ao histórico; esclarecer só dados essenciais ausentes.

## Entender e decidir

1. Ler a versão atual do rascunho, a mensagem pendente e o histórico relevante inteiro. Conferir quem propôs cada condição e quais perguntas já foram respondidas; procurar outras threads relacionadas e o canal ativo antes de retomar a negociação.
2. Identificar a intenção: contratação de conteúdo, apresentação de creator/agência, programa, teste, pedido de dados, recusa ou prospecção de patrocinadores. Não transformar toda mensagem em oferta nem confundir os modelos de remuneração.
3. Conferir identidade e elegibilidade segundo evidências reais e regras do perfil. Não acusar fraude nem fazer afirmação jurídica por inferência. Verificar fatos atuais nas fontes adequadas quando a decisão depender deles.
4. Pedir somente informação ausente que realmente muda a avaliação ou cotação. Se o formato e o preço já puderem ser apresentados, não adiar a resposta com perguntas genéricas. Distinguir dados necessários para precificar de detalhes de execução que cabem depois da aprovação.
5. Preservar acordo vigente de moeda, escopo, valores, direitos, prazo e pagamento. Usar somente fonte de preços confirmada e descontos autorizados. Preço ausente não significa zero; não inventar conversão, disponibilidade, métricas, bônus ou condições.
6. Escrever na voz e idioma pertinentes. Usar cumprimento, blocos curtos de ideias e fechamento; agrupar frases relacionadas. Mostrar formatos/valores de modo legível e colocar o próximo passo junto da oferta quando houver uma.
7. Em follow-ups, respeitar prazo de retorno prometido, política do perfil e o último ponto realmente pendente. Rascunho não conta como envio. Não reiniciar conversa que segue em outro canal nem afirmar ações não realizadas.

## Gravar e verificar

- Rascunho não autoriza envio. Executar somente as ações externas autorizadas pelo pedido ou perfil ativo; preservar conta, participantes externos pertinentes e cabeçalhos da thread. Não adicionar contatos por suposição.
- Corrigir o rascunho existente, preservando edições do titular, links, condições, assinaturas e anexos. Substituir o corpo MIME pode remover anexos: preservá-los explicitamente quando houver. Não reconstruir a resposta a partir de uma cópia antiga.
- Salvar somente a resposta nova, sem histórico citado ou cabeçalho de mensagem recebida. Não inventar assinatura nem declarar envio de materiais ou contato por outro canal sem confirmação.
- No HTML novo, usar `<div>texto</div>` para cada bloco e exatamente `<div><br></div>` entre blocos. Não simular a linha em branco com margens de `<p>`; não adicionar separador no início ou depois do fechamento. Usar `<br>` dentro de um bloco só para linhas relacionadas, como formatos e valores.
- Executar `python scripts/check_gmail_html.py /caminho/corpo.html` antes de salvar e com o corpo recuperado depois da gravação. Acrescentar opções de voz apenas quando determinadas pelo perfil. Validar cada item de um lote; não considerar o texto do chat prova de espaçamento no Gmail. O script verifica formato, não fatos comerciais.
- Validar somente o corpo novo, sem histórico e assinatura automática. Não apagar assinatura/anexos do titular para fazer um teste passar. Se o serviço normalizar o HTML, conferir a estrutura equivalente e o espaçamento real sem reescrever por estética; preservar texto e condições.
- Ao concluir, aplicar apenas o fluxo de etiquetas configurado e autorizado no perfil, na conta certa. Conferir mensagens antigas que possam manter uma etiqueta na thread. Sem configuração, não inventar nomes ou transições de etiquetas.
- Rever pedido, estágio, restrições, compromissos, texto e corpo salvo. Se houver divergência que indique edição concorrente do titular, não sobrescrever; preservar a versão atual e resolver o trecho afetado.

## Manter e compartilhar

- Alterar a skill dentro do escopo autorizado. Revisar não significa enviar emails ou publicar conteúdo. Validar alterações e usar o mecanismo de persistência autorizado do ambiente; não presumir que outra instalação utiliza Git, branch ou servidor remoto.
- Para preparar uma cópia pública, executar `python scripts/export_core.py /destino/vazio`. O exportador inclui somente o core, scripts e modelo genérico, sem `personalization/`, casos reais, ícones privados ou histórico Git. Ele não publica nem altera a instalação ativa.
- Não publicar diretamente a pasta instalada nem seu histórico como se fossem a cópia exportada: a personalização permanece guardada nela para uso privado. Usar a exportação limpa em um repositório novo quando o titular solicitar publicação.
