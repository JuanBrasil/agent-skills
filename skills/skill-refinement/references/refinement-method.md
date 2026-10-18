# Método de lapidação

## Inventário mínimo

Identifique ponto de entrada, metadados/UI, referências alcançáveis, scripts e dependências, assets, configuração, dados de execução, testes e licença. Veja como cada recurso é chamado antes de removê-lo. Scripts podem receber caminhos por configuração/CLI; uma busca só em Markdown não identifica todos os callers.

## Duplicidade e conflito

- Mesma regra e mesmas condições: mantenha uma fonte e referências claras.
- Mesma frase em dois pacotes independentes pode ser necessária para cada pacote funcionar sozinho; não crie dependência artificial só para economizar linhas.
- Regra geral e exceção específica: preserve ambas com precedência clara.
- Duas regras incompatíveis: encontre instrução vigente e evidência da intenção. Sem resolução, descreva o conflito e peça só a decisão necessária.
- Exemplo longo: mantenha apenas o que ensina decisão relevante; substitua dados reais por um exemplo fictício que preserve a dificuldade.

Não reúna duas skills só porque se encadeiam. Intenções de entrada distintas podem usar um padrão de escrita compartilhado. Não separe uma skill curta em vários arquivos sem ganho de leitura/manutenção.

## Organização

O SKILL.md mantém ativação, objetivo, caminho principal, limites e roteamento. Referências guardam procedimentos condicionais e exemplos substanciais. Scripts guardam automação determinística realmente reutilizada. Assets servem ao artefato final, não à memória pessoal. Não crie placeholders ou diretórios vazios para parecer completo.

Prompts e nomes devem comunicar a função real. Preserve invocação implícita/explicita existente; sensibilidade não significa proibição automática. Ao renomear, atualize calls, links, UI e instaladores; aposente cópias antigas fora da descoberta e preserve rollback privado. Não edite outros pacotes sem necessidade/autorização.

## Critério de parada

Termine quando mudanças autorizadas estiverem aplicadas, contrato preservado, testes pertinentes concluídos e publicação solicitada confirmada ou bloqueio exato explicado. Não acrescente uma auditoria sem fim por detalhes cosméticos ou métricas de tamanho.
