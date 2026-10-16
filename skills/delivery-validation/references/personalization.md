# Personalização local, fora da distribuição pública

Estas skills são reutilizáveis. Dados de pessoas, clientes, valores/taxas reais, regras comerciais particulares, contatos, IDs de boards/projetos, links reais e exemplos históricos devem ficar fora dos arquivos públicos.

Quando o ambiente definir CODEX_HOME, procure `personalization/product-workflows/profile.md` sob essa pasta. Caso contrário, procure sob `~/.codex/`. O caminho é local, não uma URL de publicação. Leia somente o perfil e referências privadas necessárias ao pedido. Se não existir, use a sessão atual e peça apenas contexto essencial ausente.

O perfil pode definir identidade do solicitante, idioma, ferramenta/perfil de navegador, destinos e estados, exigência de prints e regras comerciais particulares. Preferências de estilo generalizáveis pertencem às skills; dados e decisões particulares pertencem ao perfil. Nunca armazene senhas, cookies ou tokens nele: use a sessão autenticada e integrações autorizadas.

Um perfil privado não é um artefato para anexar a cards/issues. Uma solicitação explícita pode exigir publicar dados específicos num item autorizado; inclua só o necessário e nunca credenciais. Isso não autoriza incorporar esses dados aos exemplos ou repositório das skills.

Ao preparar exportação ou Git, use somente arquivos públicos revisados. Não copie perfis, backups, logs, capturas ou relatórios de teste reais. Regras de ignore não removem arquivos já rastreados; revise o diff e, se houver suspeita de exposição anterior, o histórico pertinente. Não prometa ausência absoluta de dados só por um scan automático.
