# Validação de comportamento

Comece com cenários que a skill realmente atende. Anote entrada, decisão/resultado observável, ações permitidas e o que não pode acontecer. Compare a versão original e a lapidada; mudança de decisão precisa ser intencional e sustentada.

Exemplos fictícios úteis:

- Pedido de rascunho não deve publicar.
- Revisão de entrega usa a última pendência do solicitante, não toda a descrição antiga.
- Aprovação com melhoria nova conclui a entrega e só cria novo item se solicitado.
- Perfil ausente permite comportamento genérico; corrupção de memória não autoriza zerar dados.
- Dependência opcional indisponível não quebra o fluxo básico; dependência necessária impede só o trabalho que depende dela.
- Retorno externo incerto exige verificar antes de repetir.
- Redução de latência mantém qualidade e persistência, não apenas resposta curta no lugar do trabalho.

Teste mecanismos em cópias sintéticas: links quebrados, YAML inválido, campos vazios, política preservada, duplicidade, configuração ausente, caminho privado e credenciais fictícias. Execute helpers sem rede e sem gravar no sistema real. Limpe somente a pasta temporária verificada, nunca uma raiz calculada sem checagem.

Separe resultados: teste automatizado executado; simulação de decisões; teste real de integração; inspeção manual. Não promova simulação a teste de produção nem um caso a cobertura total. Um scan pode ter falsos positivos/negativos; inspecione achados sem divulgar valores.
