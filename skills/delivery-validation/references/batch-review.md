# Conferência em lote

Use somente com pedido explícito de lote ou conferência autônoma. Percorra a fila no recorte e ordem autorizados; a última rodada de cada item define o que conferir.

- Teste o produto antes de concluir; relato da equipe não substitui evidência atual.
- Com entrega comprovada e autorização do lote para agir, mova para conclusão sem comentário positivo.
- Com falha comprovada no escopo e autorização para agir, use Product Requests para publicar a pendência e devolver para correção.
- Em dúvida de UX, aceite ou limitação de teste, preserve referência e tela no ponto alcançado, continue em novas abas e deixe os pares para avaliação ao final. Não force conclusão para reduzir pendências.
- Não interrompa a cada dúvida quando o usuário pediu avaliar os casos só no final. Diferencie dúvida visual de teste incompleto por sessão, dados, carregamento ou automação.
- Antes de marcar inconclusivo, ative a aba, aguarde carregamento real com timeout finito e confirme o estado após navegação. UI vazia em segundo plano pode ainda não ter carregado.
- Não envie cadastros, emails, pagamentos ou outros dados reais só para comprovar entrega. Upload limitado pela automação ou input oculto não comprovam bug do produto. Sem cenário apropriado, mantenha inconclusivo.
- Registre localmente item, resultado, evidência e ponto pendente para não confundir abas. O registro é privado; não guarde URLs com credenciais nem o inclua na distribuição.

Se o pedido de lote for só apresentar resultados, não presuma permissão para mover ou comentar. Um recorte como “deixe UX/site para mim” prevalece. Uma pausa ou mudança de instrução do usuário interrompe o trabalho dependente imediatamente.
