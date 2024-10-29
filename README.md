# Project File Collector

Um script Python para coletar e organizar arquivos de um projeto Laravel (ou similar) em uma única pasta, mantendo a estrutura de diretórios através da nomenclatura dos arquivos.

## 🎯 Funcionalidades

- Varre recursivamente todas as pastas do projeto
- Filtra arquivos baseado em padrões configuráveis de inclusão/exclusão
- Converte caminhos de arquivo para formato com pontos (ex: `app/Models/User.php` → `app.Models.User.php`)
- Mantém permissões originais dos arquivos
- Logging detalhado do processo
- Configuração flexível via arquivo .ini

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas Python listadas em `requirements.txt`

## 🚀 Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:

```shell
pip install -r requirements.txt
```

## ⚙️ Configuração

O arquivo `config.ini` contém todas as configurações necessárias:

```ini
[paths]
source_dir = .               # Diretório raiz do projeto
output_dir = ./collected_files  # Diretório de saída

[patterns]
# Padrões para incluir arquivos
include =
    *.blade.php
    *.php
    .env
    lara-*-log.ini

# Padrões para excluir arquivos
exclude =
    *ide*helper.php
    *.lock
    *vendor*
    *node_modules*
    *.git*
```

### Personalizando Padrões

- Use `*` como curinga para qualquer sequência de caracteres
- Um padrão por linha
- Linhas em branco são ignoradas
- Não é necessário usar aspas

## 🖥️ Uso

### Uso Básico

```shell
python main.py
```

### Usando Arquivo de Configuração Alternativo

```shell
python main.py caminho/para/outro_config.ini
```

## 📁 Estrutura do Projeto

```text
.
├── config.ini          # Configurações do projeto
├── main.py            # Script principal
├── requirements.txt    # Dependências do projeto
└── README.md          # Esta documentação
```

## 📋 Exemplo de Saída

Se você tiver um projeto com esta estrutura:

```text
meu_projeto/
├── app/
│   ├── Models/
│   │   └── User.php
│   └── Controllers/
│       └── UserController.php
└── resources/
    └── views/
        └── user.blade.php
```

O script irá gerar:

```text
collected_files/
├── app.Models.User.php
├── app.Controllers.UserController.php
└── resources.views.user.blade.php
```

## 📝 Logs

O script gera logs detalhados com:

- Início do processo
- Padrões de inclusão/exclusão utilizados
- Cada arquivo copiado
- Quaisquer erros encontrados
- Total de arquivos processados

## ⚠️ Tratamento de Erros

O script inclui tratamento robusto de erros para:

- Arquivo de configuração ausente ou inválido
- Problemas de permissão
- Erros de cópia de arquivo
- Diretórios inexistentes

## 🤝 Contribuindo

Sinta-se à vontade para:

1. Reportar bugs
2. Sugerir novas funcionalidades
3. Enviar pull requests

## 🔍 Resolução de Problemas

### Arquivos não estão sendo copiados

- Verifique se os padrões em `config.ini` estão corretos
- Confirme se o diretório fonte está correto
- Verifique as permissões dos arquivos

### Erros de permissão

- Verifique se você tem permissão para ler os arquivos fonte
- Confirme se você tem permissão para escrever no diretório de saída

### Conflitos de nome

- Arquivos com mesmo nome em diretórios diferentes serão sobrescritos
- Use diretórios de saída diferentes para diferentes execuções
