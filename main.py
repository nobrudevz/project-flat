from pathlib import Path
import shutil
import fnmatch
import logging
from typing import Set
import configparser
import sys
import os

class ProjectFileCollector:
    def __init__(self, config_path: str = 'config.ini'):
        self.config = self._load_config(config_path)
        self.source_dir = self._parse_path(self.config['paths']['source_dir'])
        self.output_dir = self._parse_path(self.config['paths']['output_dir'])
        self.include_patterns = [p.strip() for p in self.config['patterns']['include'].split('\n') if p.strip()]
        self.exclude_patterns = [p.strip() for p in self.config['patterns']['exclude'].split('\n') if p.strip()]

        # Configuração do logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _parse_path(self, path: str) -> Path:
        """Processa o caminho mantendo aspas duplas e normalizando separadores"""
        # Remove espaços em branco extras
        path = path.strip()

        # Remove aspas se existirem
        if path.startswith('"') and path.endswith('"'):
            path = path[1:-1]

        # Remove a barra final se existir
        path = path.rstrip('\\').rstrip('/')

        # Normaliza o caminho para o sistema operacional atual
        path = os.path.normpath(path)

        return Path(path)

    def _clear_directory_contents(self, directory: Path) -> None:
        """Limpa o conteúdo do diretório mantendo o diretório em si"""
        try:
            if directory.exists():
                self.logger.info(f"Limpando conteúdo do diretório: {directory}")
                # Remove cada item dentro do diretório
                for item in directory.glob('*'):
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
                self.logger.info("Conteúdo do diretório limpo com sucesso")
        except Exception as e:
            self.logger.error(f"Erro ao limpar conteúdo do diretório: {str(e)}")
            raise

    def _ensure_directory(self, directory: Path) -> None:
        """Garante que o diretório existe"""
        try:
            if not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)
            elif not directory.is_dir():
                raise NotADirectoryError(f"{directory} existe mas não é um diretório")
        except Exception as e:
            self.logger.error(f"Erro ao criar/verificar diretório {directory}: {str(e)}")
            raise

    def _load_config(self, config_path: str) -> configparser.ConfigParser:
        """Carrega as configurações do arquivo .ini"""
        config = configparser.ConfigParser()

        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config.read_file(f)

            # Validar seções obrigatórias
            required_sections = ['paths', 'patterns']
            for section in required_sections:
                if section not in config:
                    raise ValueError(f"Seção '{section}' não encontrada no arquivo de configuração")

            return config

        except Exception as e:
            self.logger.error(f"Erro ao carregar configurações: {str(e)}")
            sys.exit(1)

    def should_include_file(self, file_path: Path) -> bool:
        """Verifica se o arquivo deve ser incluído baseado nos padrões definidos."""
        file_str = str(file_path)

        # Primeiro verifica se o arquivo deve ser excluído
        for pattern in self.exclude_patterns:
            if fnmatch.fnmatch(file_str, f'*{pattern}'):
                return False

        # Depois verifica se o arquivo deve ser incluído
        for pattern in self.include_patterns:
            if fnmatch.fnmatch(file_str, f'*{pattern}'):
                return True

        return False

    def get_output_filename(self, file_path: Path) -> str:
        """Gera o nome do arquivo de saída no formato desejado."""
        try:
            relative_path = file_path.relative_to(self.source_dir)
            # Converte separadores de caminho para pontos
            return str(relative_path).replace('\\', '.').replace('/', '.')
        except ValueError as e:
            self.logger.error(f"Erro ao gerar nome do arquivo de saída para {file_path}: {str(e)}")
            return str(file_path.name)

    def collect_files(self) -> Set[Path]:
        """Coleta todos os arquivos que correspondem aos padrões definidos."""
        collected_files = set()

        self.logger.info(f"Iniciando coleta de arquivos em: {self.source_dir}")
        self.logger.info("Padrões de inclusão: %s", ', '.join(self.include_patterns))
        self.logger.info("Padrões de exclusão: %s", ', '.join(self.exclude_patterns))

        try:
            for file_path in self.source_dir.rglob('*'):
                if file_path.is_file() and self.should_include_file(file_path):
                    collected_files.add(file_path)
        except Exception as e:
            self.logger.error(f"Erro durante a coleta de arquivos: {str(e)}")

        self.logger.info(f"Total de arquivos coletados: {len(collected_files)}")
        return collected_files

    def copy_files(self, collected_files: Set[Path]) -> None:
        """Copia os arquivos coletados para o diretório de saída."""
        try:
            # Garante que o diretório de saída existe
            self._ensure_directory(self.output_dir)

            # Limpa o conteúdo do diretório
            self._clear_directory_contents(self.output_dir)

            for source_file in collected_files:
                output_filename = self.get_output_filename(source_file)
                destination = self.output_dir / output_filename

                # Garante que o diretório pai do arquivo de destino existe
                self._ensure_directory(destination.parent)

                try:
                    shutil.copy2(source_file, destination)
                    self.logger.info(f"Arquivo copiado: {output_filename}")
                except Exception as e:
                    self.logger.error(f"Erro ao copiar {source_file}: {str(e)}")

        except Exception as e:
            self.logger.error(f"Erro ao processar diretório de saída: {str(e)}")
            raise

    def run(self) -> None:
        """Executa o processo completo de coleta e cópia dos arquivos."""
        try:
            self.logger.info("Iniciando processo de coleta de arquivos")
            collected_files = self.collect_files()
            if collected_files:
                self.copy_files(collected_files)
                self.logger.info("Processo concluído com sucesso!")
            else:
                self.logger.warning("Nenhum arquivo encontrado para copiar!")

        except Exception as e:
            self.logger.error(f"Erro durante a execução: {str(e)}")
            raise

def main():
    # Permite especificar um arquivo de configuração diferente via linha de comando
    config_path = sys.argv[1] if len(sys.argv) > 1 else 'config.ini'
    collector = ProjectFileCollector(config_path)
    collector.run()

if __name__ == '__main__':
    main()
