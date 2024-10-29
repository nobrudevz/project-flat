<div align="center">

# Project Flat

🗃️ Colete e organize arquivos de projetos Laravel em uma estrutura plana

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

## ✨ Features

- 🚀 **Alta Performance**: Busca otimizada de arquivos
- 🎯 **Seletivo**: Padrões de inclusão/exclusão configuráveis
- 🔄 **Conversão Inteligente**: `app/Models/User.php` → `app.Models.User.php`
- 📝 **Logging Detalhado**: Rastreamento completo das operações

## ⚡ Quickstart

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
    app/*.php

# Execute
python main.py
```

## 🛠️ Configuração

### Padrões Suportados

| Tipo | Exemplo | Descrição |
|------|---------|-----------|
| Arquivo específico | `.env` | Match exato |
| Diretório específico | `app/*.php` | Arquivos PHP no diretório app |
| Recursivo | `app/**/*.php` | Arquivos PHP em todo diretório app |
| Wildcard | `*.blade.php` | Qualquer arquivo blade.php |
| Exclusão | `config/enums/*` | Ignora arquivos neste padrão |

### Exemplo Completo

```ini
[paths]
source_dir = "C:\projects\laravel\meu-projeto"
output_dir = "output"

[patterns]
include =
    .env
    composer.json
    package.json
    app/**/*.php
    config/*.php
    routes/*.php
    resources/views/*.blade.php

exclude =
    config/enums/*
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

## 🔍 Troubleshooting

<details>
<summary>Arquivos não encontrados</summary>

- Verifique os padrões no `config.ini`
- Confirme os caminhos dos diretórios
- Examine os logs para detalhes
</details>

<details>
<summary>Erros de permissão</summary>

- Verifique permissões do diretório fonte
- Confirme acesso ao diretório de saída
- Execute com privilégios adequados
</details>

<details>
<summary>Problemas de performance</summary>

- Use padrões específicos
- Evite recursão desnecessária
- Limite a profundidade da busca
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
Made with ❤️ by <a href="https://github.com/nobrudevz">NobruDev</a>
</div>
