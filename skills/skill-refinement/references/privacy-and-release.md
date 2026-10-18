# Separação privada e publicação

Classifique informação pela função, não só pelo nome do arquivo:

| Informação | Destino |
| --- | --- |
| Método, critérios e comportamento reutilizáveis | Núcleo público |
| Preferência de uma pessoa, identidade e destinos | Perfil local externo |
| Contatos, tabelas de valores, clientes, registros e capturas reais | Dados privados, fora da distribuição |
| Token, senha, cookie e chave privada | Gestor de credenciais/sessão autorizada; nunca perfil ou exemplos |
| Exemplo fictício necessário | Público, identificado como fictício e sem cópia disfarçada de dados reais |

Use uma raiz privada resolvida por configuração ou convenção explícita sob CODEX_HOME/ambiente local; não fixe caminho com o usuário do computador nos arquivos públicos. Para um pacote sem perfil, prossiga com o contexto da sessão e peça apenas dados essenciais ausentes. Perfil não amplia autorização nem vira anexo automático a um card.

## Antes de exportar

Revise frontmatter, prompts, comentários de código, fixtures, nomes de arquivos, imagens/metadados, links com query ou credencial no caminho e exports compactados. Trocar só o nome da pessoa não anonimiza um caso único com valores, datas e links intactos. Termos pessoais usados num scanner/denylist também são dados: essa lista precisa ficar privada.

Inspecione arquivos rastreados e o diff completo da seleção. Ignore e remoção do arquivo atual não limpam commits antigos. Se houver exposição prévia, interrompa a nova divulgação, comunique o tipo de dado e o alcance sem reproduzi-lo; não reescreva histórico ou revogue credenciais sem autorização. Nunca prometa que a remoção atual apaga cópias externas.

Publicação permitida não implica tornar repositório público, criar remote, subir assets privados ou publicar skills adicionais. Preserve licenças de terceiros e marque derivações. Use allowlist positiva; não exporte tudo e tente filtrar depois. Confirme o conteúdo remoto, não só o retorno do upload.

## Comunicação

Relate “nenhum indício encontrado nos arquivos revisados”, não garantia absoluta. Cite contagens/categorias e ações concluídas sem imprimir valores detectados. Não cole segredos em logs, mensagens de commit, issues ou relatórios. Logs locais com paths/nomes reais também ficam privados.
