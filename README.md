<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->
<div align="center">

# Project Flat

🗃️ Collect and organize Laravel project files into a flat structure

[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](./README.pt-br.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](./README.es.md)

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nobrudevz/project-flat/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

</div>

## 📖 About

An optimized Python script to collect Laravel project files and convert them into a flat structure, perfect for:

- Code review
- Partial project sharing
- Structure analysis
- Selective backup

## ✨ Features

- 🚀 **High Performance**: Optimized file search
- 🎯 **Selective**: Configurable include/exclude patterns
- 🔄 **Smart Conversion**: `app/Models/User.php` → `app.Models.User.php`
- 📝 **Detailed Logging**: Complete operation tracking

## ⚡ Quickstart

```bash
# Install
git clone https://github.com/nobrudevz/project-flat.git
cd project-flat
pip install -r requirements.txt

# Configure (config.ini)
[paths]
source_dir = "C:\projects\laravel\my-project"
output_dir = "output"

[patterns]
include =
    .env
    composer.json
    app/*.php

# Run
python main.py
```

## 🛠️ Configuration

### Supported Patterns

| Type | Example | Description |
|------|---------|-------------|
| Specific file | `.env` | Exact match |
| Directory specific | `app/*.php` | PHP files in app directory |
| Recursive | `app/**/*.php` | PHP files in all app subdirectories |
| Wildcard | `*.blade.php` | Any blade.php file |
| Exclusion | `config/enums/*` | Ignore files matching this pattern |

### Complete Example

```ini
[paths]
source_dir = "C:\projects\laravel\my-project"
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

## 📊 Usage Example

```text
Input:                            Output:
my-project/                      output/
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
<summary>Files not found</summary>

- Check patterns in `config.ini`
- Confirm directory paths
- Check logs for details

</details>

<details>
<summary>Permission errors</summary>

- Check source directory permissions
- Confirm output directory access
- Run with proper privileges

</details>

<details>
<summary>Performance issues</summary>

- Use specific patterns
- Avoid unnecessary recursion
- Limit search depth

</details>

## 👥 Contributing

Contributions are welcome! Please read our contribution guide.

1. Fork
2. Feature Branch (`feature/AmazingFeature`)
3. Commit (`git commit -m 'Add: feature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Pull Request

## 📄 License

[MIT](LICENSE) © [NobruDev](https://github.com/nobrudevz)

---

<div align="center">
Made with ❤️ by <a href="https://github.com/nobrudevz">NobruDev</a>
</div>
