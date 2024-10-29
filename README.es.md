<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->
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
- 🎯 **Selectivo**: Patrones de inclusión con exclusiones opcionales
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
    app/*.php      # Solo archivos directamente en app/
    app/**/*.php   # Archivos en todos los subdirectorios
```

## 🛠️ Configuración

### Reglas de Coincidencia de Patrones

- Los patrones son relativos al directorio fuente
- Los patrones deben coincidir con la estructura exacta del camino
- `*` coincide con cualquier carácter dentro de un nivel de directorio
- `**` coincide a través de niveles de directorio

### Patrones Soportados

| Tipo | Ejemplo | Descripción |
|------|---------|-------------|
| Archivo específico | `.env` | Coincidencia exacta desde la raíz |
| Directorio específico | `app/*.php` | Archivos PHP directamente en directorio app |
| Recursivo | `app/**/*.php` | Archivos PHP en app y subdirectorios |
| Múltiples extensiones | `resources/views/*{.php,.blade.php}` |
