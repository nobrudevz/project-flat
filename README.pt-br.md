<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->
<div align="center">

# Project Flat

🗃️ Colete e organize arquivos de projetos Laravel em uma estrutura plana

[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](./README.pt-br.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](./README.es.md)

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nobrudevz/project-flat/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

</div>

## 📖 Sobre

Um script Python otimizado para coletar arquivos de projetos Laravel e convertê-los em uma estrutura plana, ideal para:

- Revisão de código
- Compartilhamento parcial de projetos
- Análise de estrutura
- Backup seletivo

## ✨ Recursos

- 🚀 **Alta Performance**: Busca otimizada de arquivos
- 🎯 **Seletivo**: Padrões de inclusão com exclusões opcionais
- 🔄 **Conversão Inteligente**: `app/Models/User.php` → `app.Models.User.php`
- 📝 **Logging Detalhado**: Rastreamento completo das operações

## ⚡ Início Rápido

```bash
# Instale
git clone https://github.com/nobrudevz/project-flat.git
cd project-flat
pip install -r requirements.txt

# Configure (config.ini)
[paths]
source_dir = "C:\projects\laravel\meu-projeto"
output_dir = "output"

[patterns]
include =
    .env
    composer.json
    app/*.php      # Apenas arquivos diretamente em app/
    app/**/*.php   # Arquivos em todos os subdiretórios
```

## 🛠️ Configuração

### Regras de Correspondência de Padrões

- Padrões são relativos ao diretório fonte
- Padrões devem corresponder à estrutura exata do caminho
- `*` corresponde a qualquer caractere dentro de um nível de diretório
- `**` corresponde através de níveis de diretório

### Padrões Suportados

| Tipo | Exemplo | Descrição |
|------|---------|-----------|
| Arquivo específico | `.env` | Match exato do arquivo a partir da raiz |
| Diretório específico | `app/*.php` | Arquivos PHP diretamente no diretório app |
| Recursivo | `app/**/*.php` | Arquivos PHP no app e subdiretórios |
| Múltiplas extensões | `resources/views/*{.php,.blade.php}` | Múltiplos tipos de arquivo no diretório |
| Exclusão opcional | `exclude = app/cache/*` | Opcionalmente ignora padrões específicos |

### Exemplo Básico

```ini
[paths]
source_dir = "C:\projects\laravel\meu-projeto"
output_dir = "output"

[patterns]
include =
    .env
    composer.json
    app/*.php          # Apenas arquivos PHP diretamente em app/
    app/**/*.php       # Arquivos PHP em todos os subdiretórios
    config/*.php       # Apenas arquivos PHP diretamente em config/
```

### Exemplo com Exclusões

```ini
[paths]
source_dir = "C:\projects\laravel\meu-projeto"
output_dir = "output"

[patterns]
include =
    app/**/*.php       # Todos os arquivos PHP na árvore do diretório app

exclude =              # Seção opcional
    app/cache/*        # Exclui tudo em app/cache
    app/tests/**/*.php # Exclui arquivos PHP em tests
```

## 📊 Exemplo de Uso

```text
Entrada:                          Saída:
meu-projeto/                     output/
├── app/                        ├── app.Models.User.php
│   ├── Models/                 ├── app.Http.Controllers.UserController.php
│   │   └── User.php           └── resources.views.user.blade.php
│   └── Http/
│       └── Controllers/
│           └── UserController.php
└── resources/
    └── views/
        └── user.blade.php
```

## 🔍 Resolução de Problemas

<details>
<summary>Arquivos não encontrados</summary>

- Verifique se os padrões correspondem exatamente à sua estrutura de diretórios
- Confirme se os caminhos são relativos ao diretório fonte
- Revise os logs para ver quais arquivos foram avaliados

</details>

<details>
<summary>Erros de permissão</summary>

- Verifique permissões do diretório fonte
- Confirme acesso ao diretório de saída
- Execute com privilégios adequados

</details>

<details>
<summary>Problemas de performance</summary>

- Use padrões específicos em vez de genéricos
- Evite recursão profunda quando possível
- Seja explícito sobre quais arquivos você precisa

</details>

## 👥 Contribuindo

Contribuições são bem-vindas! Por favor, leia nosso guia de contribuição.

1. Fork
2. Feature Branch (`feature/AmazingFeature`)
3. Commit (`git commit -m 'Add: feature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Pull Request

## 📄 Licença

[MIT](LICENSE) © [NobruDev](https://github.com/nobrudevz)

---

<div align="center">
Feito com ❤️ por <a href="https://github.com/nobrudevz">NobruDev</a>
</div>
