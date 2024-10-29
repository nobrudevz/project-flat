# Project File Collector

Um script Python para coletar e organizar arquivos de projetos Laravel (ou similares) em uma única pasta, mantendo a estrutura de diretórios através da nomenclatura dos arquivos. Útil para revisão de código, análise de estrutura do projeto ou quando você precisa compartilhar apenas parte do projeto.

## 🎯 Características

- Coleta arquivos de forma recursiva baseado em padrões configuráveis
- Converte caminhos de diretórios em nomes de arquivos com pontos
- Suporta padrões de inclusão e exclusão específicos
- Mantém as permissões originais dos arquivos
- Logging detalhado do processo
- Alta performance com otimização de busca
- Configuração flexível via arquivo .ini

## 📋 Pré-requisitos

- Python 3.6+
- Bibliotecas Python listadas em `requirements.txt`

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/USER/REPO.git
cd REPO

# Instale as dependências
pip install -r requirements.txt
```

## ⚙️ Configuração

Crie um arquivo `config.ini` com suas configurações:

```ini
[paths]
# Diretório raiz do projeto
source_dir = "C:\projects\laravel\meu-projeto"
# Diretório onde os arquivos serão copiados
output_dir = "output"

[patterns]
# Padrões para incluir arquivos
include =
    .env
    composer.json
    app/*.php
    config/*.php
    routes/*.php
    resources/views/*.blade.php

# Padrões para excluir (opcional)
exclude =
    config/enums/*
```

### Padrões Suportados

- Arquivos específicos: `.env`, `composer.json`
- Padrões por diretório: `app/*.php`
- Padrões recursivos: `app/**/*.php`
- Wildcards: `*.blade.php`
- Exclusões: `config/enums/*`

## 🖥️ Uso

```bash
# Uso básico
python main.py

# Usando arquivo de configuração alternativo
python main.py /caminho/para/config.ini
```

## 📋 Exemplo de Saída

Estrutura original:

```text
meu-projeto/
├── app/
│   ├── Models/
│   │   └── User.php
│   └── Controllers/
│       └── UserController.php
└── resources/
    └── views/
        └── user.blade.php
```

Saída gerada:

```text
output/
├── app.Models.User.php
├── app.Controllers.UserController.php
└── resources.views.user.blade.php
```

## 📝 Logging

O script gera logs detalhados incluindo:

- Início do processo
- Padrões utilizados
- Arquivos processados
- Erros encontrados
- Estatísticas finais

## ⚠️ Tratamento de Erros

- Validação de configuração
- Verificação de permissões
- Tratamento de erros de I/O
- Logs detalhados para debugging

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add: alguma funcionalidade'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 🔍 Resolução de Problemas

### Arquivos não estão sendo coletados

- Verifique se os padrões em `config.ini` estão corretos
- Confirme os caminhos dos diretórios
- Verifique as permissões dos arquivos
- Examine os logs para mais detalhes

### Erros de permissão

- Verifique as permissões do diretório fonte
- Confirme o acesso ao diretório de saída
- Execute o script com as permissões adequadas

### Performance

- Use padrões específicos em vez de wildcards genéricos
- Evite padrões recursivos desnecessários
- Limite a profundidade da busca quando possível

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
