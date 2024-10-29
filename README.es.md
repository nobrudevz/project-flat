<div align="center">

# Project Flat

🗃️ Recopila y organiza archivos de proyectos Laravel en una estructura plana

[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](./README.pt-br.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](./README.es.md)

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/nobrudevz/project-flat/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

</div>

## 📖 Acerca de

Un script Python optimizado para recopilar archivos de proyectos Laravel y convertirlos en una estructura plana, ideal para:

- Revisión de código
- Compartir parcialmente proyectos
- Análisis de estructura
- Backup selectivo

## ✨ Características

- 🚀 **Alto Rendimiento**: Búsqueda optimizada de archivos
- 🎯 **Selectivo**: Patrones de inclusión/exclusión configurables
- 🔄 **Conversión Inteligente**: `app/Models/User.php` → `app.Models.User.php`
- 📝 **Registro Detallado**: Seguimiento completo de operaciones

## ⚡ Inicio Rápido

```bash
# Instalar
git clone https://github.com/nobrudevz/project-flat.git
cd project-flat
pip install -r requirements.txt

# Configurar (config.ini)
[paths]
source_dir = "C:\projects\laravel\mi-proyecto"
output_dir = "output"

[patterns]
include =
    .env
    composer.json
    app/*.php

# Ejecutar
python main.py
```

## 🛠️ Configuración

### Patrones Soportados

| Tipo | Ejemplo | Descripción |
|------|---------|-------------|
| Archivo específico | `.env` | Coincidencia exacta |
| Directorio específico | `app/*.php` | Archivos PHP en directorio app |
| Recursivo | `app/**/*.php` | Archivos PHP en todo directorio app |
| Comodín | `*.blade.php` | Cualquier archivo blade.php |
| Exclusión | `config/enums/*` | Ignora archivos en este patrón |

### Ejemplo Completo

```ini
[paths]
source_dir = "C:\projects\laravel\mi-proyecto"
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

## 📊 Ejemplo de Uso

```text
Entrada:                          Salida:
mi-proyecto/                     output/
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

## 🔍 Solución de Problemas

<details>
<summary>Archivos no encontrados</summary>

- Verifique los patrones en `config.ini`
- Confirme las rutas de directorios
- Examine los registros para más detalles

</details>

<details>
<summary>Errores de permisos</summary>

- Verifique permisos del directorio fuente
- Confirme acceso al directorio de salida
- Ejecute con privilegios adecuados

</details>

<details>
<summary>Problemas de rendimiento</summary>

- Use patrones específicos
- Evite recursión innecesaria
- Limite la profundidad de búsqueda

</details>

## 👥 Contribuyendo

¡Las contribuciones son bienvenidas! Por favor, lea nuestra guía de contribución.

1. Fork
2. Feature Branch (`feature/AmazingFeature`)
3. Commit (`git commit -m 'Add: feature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Pull Request

## 📄 Licencia

[MIT](LICENSE) © [NobruDev](https://github.com/nobrudevz)

---

<div align="center">
Hecho con ❤️ por <a href="https://github.com/nobrudevz">NobruDev</a>
</div>
