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
- 🎯 **Selective**: Configurable include patterns with optional exclusions
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
    app/*.php      # Only files directly in app/
    app/**/*.php   # Files in all subdirectories
```

## 🛠️ Configuration

### Pattern Matching Rules

- Patterns are relative to the source directory
- Patterns must match the exact path structure
- `*` matches any characters within a directory level
- `**` matches across directory levels

### Supported Patterns

| Type | Example | Description |
|------|---------|-------------|
| Specific file | `.env` | Exact file match from project root |
| Directory specific | `app/*.php` | PHP files directly in app directory only |
| Recursive | `app/**/*.php` | PHP files in app and all subdirectories |
| Multiple extensions | `resources/views/*{.php,.blade.php}` | Multiple file types in directory |
| Optional exclusion | `exclude = app/cache/*` | Optionally ignore specific patterns |

### Basic Example

```ini
[paths]
source_dir = "C:\projects\laravel\my-project"
output_dir = "output"

[patterns]
include =
    .env
    composer.json
    app/*.php          # Only PHP files directly in app/
    app/**/*.php       # PHP files in all app subdirectories
    config/*.php       # Only PHP files directly in config/
```

### Example with Exclusions

```ini
[paths]
source_dir = "C:\projects\laravel\my-project"
output_dir = "output"

[patterns]
include =
    app/**/*.php       # All PHP files in app directory tree

exclude =              # Optional section
    app/cache/*        # Exclude everything in app/cache
    app/tests/**/*.php # Exclude PHP files in tests directory
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

- Check if patterns exactly match your directory structure
- Confirm paths are relative to source directory
- Review logs to see which files were evaluated

</details>

<details>
<summary>Permission errors</summary>

- Check source directory permissions
- Confirm output directory access
- Run with proper privileges

</details>

<details>
<summary>Performance issues</summary>

- Use specific patterns instead of broad ones
- Avoid deep recursion when possible
- Be explicit about which files you need

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
