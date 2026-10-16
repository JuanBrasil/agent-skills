# Product Requests

Crie e detalhe pedidos de produto para implementação.

## Uso

Use $product-requests para transformar este relato e suas referências em um pedido implementável; publique somente conforme eu solicitar.

Instale esta pasta no diretório de skills do seu assistente. Ferramentas de navegador, Trello ou GitHub e sessões autenticadas são fornecidas pelo ambiente, não pela skill. Não cria credenciais nem implementa correções no produto.

## Uso conjunto

Instale **Product Requests** e **Delivery Validation** como pastas irmãs para habilitar os links relativos. Delivery Validation entende a rodada e testa; Product Requests desenvolve o pedido ou a pendência. As autorizações, evidências e exclusões passam de uma para outra sem nova conversa nem segunda aprovação da mesma ação. Product Requests também funciona sem uma validação prévia.

Exemplo: validar entrega → usuário aponta só uma pendência → redigir essa pendência com Product Requests → comentar no item original → devolver para correção. Ideia nova independente vira outro item somente quando solicitada.

## Dados privados

Configuração particular fica fora da distribuição, em `personalization/product-workflows/profile.md` sob CODEX_HOME (ou `~/.codex/`). Consulte [personalização](references/personalization.md). Sem perfil, use o contexto fornecido na sessão. Não copie dados reais para exemplos, testes ou arquivos públicos.

## Verificação do pacote

Na raiz do repositório: `python scripts/check_product_skills.py`. O check confere estrutura, links locais, metadados e padrões de dados sensíveis. Não substitui revisão humana nem comprova execução do produto, acesso às ferramentas ou ausência absoluta de segredos.
