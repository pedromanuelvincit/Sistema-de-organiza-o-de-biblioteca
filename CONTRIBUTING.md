# Guia de Contribuição

Este documento explica como contribuir para o projeto Sistema de Organização de Biblioteca Digital.

## Configuração Inicial

1. Faça um **fork** do repositório
2. Clone seu fork localmente:
   ```bash
   git clone https://github.com/SEU-USERNAME/Sistema-de-organiza-o-de-biblioteca.git
   ```
3. Adicione o repositório original como remote:
   ```bash
   git remote add upstream https://github.com/pedromanuelvincit/Sistema-de-organiza-o-de-biblioteca.git
   ```

## Fazendo Alterações

### Commits
1. Mantenha commits pequenos e focados
2. Use mensagens claras e descritivas:
   ```bash
   git commit -m "Feat: Adiciona função de busca por data"
   ```
3. Padrão para mensagens de commit:
   - Adiciona: para novas funcionalidades
   - Corrige: para correções de bugs
   - Atualiza: para atualizações em funcionalidades
   - Remove: para remoção de código

### Branches
1. Crie uma branch para sua alteração:
   ```bash
   git checkout -b nome-da-funcionalidade
   ```
2. Mantenha sua branch atualizada:
   ```bash
   git pull upstream main
   ```

### Push
1. Faça push das suas alterações:
   ```bash
   git push origin nome-da-funcionalidade
   ```

## Pull Requests

1. Acesse seu fork no GitHub
2. Clique em "New Pull Request"
3. Selecione:
   - Base repository: pedromanuelvincit/Sistema-de-organiza-o-de-biblioteca
   - Base: main
   - Head repository: seu-fork
   - Compare: nome-da-funcionalidade

### Descrição do Pull Request
- Explique o que foi alterado
- Mencione se resolve alguma issue
- Adicione capturas de tela se necessário

### Após o Pull Request
1. Aguarde a revisão
2. Faça as alterações solicitadas se necessário
3. Responda aos comentários

## Boas Práticas
- Teste suas alterações antes de enviar
- Mantenha o código organizado
- Siga o estilo de código do projeto
- Atualize a documentação quando necessário