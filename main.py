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

        # Torna o exclude opcional
        self.exclude_patterns = []
        if 'exclude' in self.config['patterns']:
            self.exclude_patterns = [p.strip() for p in self.config['patterns']['exclude'].split('\n') if p.strip()]

        # Configuração do logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _parse_path(self, path: str) -> Path:
        """Processa o caminho mantendo aspas duplas e normalizando separadores"""
        path = path.strip()
        if path.startswith('"') and path.endswith('"'):
            path = path[1:-1]
        path = path.rstrip('\\').rstrip('/')
        path = os.path.normpath(path)
        return Path(path)

    def _clear_directory_contents(self, directory: Path) -> None:
        """Limpa o conteúdo do diretório mantendo o diretório em si"""
        try:
            if directory.exists():
                self.logger.info(f"Limpando conteúdo do diretório: {directory}")
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

            # Validar apenas as seções e configurações obrigatórias
            required_sections = ['paths', 'patterns']
            required_options = {
                'paths': ['source_dir', 'output_dir'],
                'patterns': ['include']
            }

            for section in required_sections:
                if section not in config:
                    raise ValueError(f"Seção '{section}' não encontrada no arquivo de configuração")

                for option in required_options[section]:
                    if option not in config[section]:
                        raise ValueError(f"Opção '{option}' não encontrada na seção '{section}'")

            return config

        except Exception as e:
            self.logger.error(f"Erro ao carregar configurações: {str(e)}")
            sys.exit(1)

    def should_include_file(self, file_path: Path) -> bool:
        """Verifica se o arquivo deve ser incluído baseado nos padrões definidos."""
        # Obtém o caminho relativo ao diretório fonte
        try:
            relative_path = str(file_path.relative_to(self.source_dir))
            relative_path = relative_path.replace('\\', '/')  # Normaliza separadores para o matching

            # Primeiro verifica se o arquivo corresponde a algum padrão de include
            included = False
            for pattern in self.include_patterns:
                # Normaliza o padrão para usar forward slashes
                pattern = pattern.replace('\\', '/')

                # Se o padrão não começa com /, adiciona-o para garantir match do início
                if not pattern.startswith('/'):
                    pattern = '/' + pattern

                # Se o caminho relativo não começa com /, adiciona-o para o matching
                relative_path_for_matching = relative_path
                if not relative_path_for_matching.startswith('/'):
                    relative_path_for_matching = '/' + relative_path_for_matching

                # Converte o padrão glob para regex
                pattern = pattern.replace('*', '[^/]*')
                pattern = pattern.replace('?', '[^/]')

                # Se termina com /, adiciona ** para incluir todo conteúdo do diretório
                if pattern.endswith('/'):
                    pattern += '**'

                # Verifica se o caminho corresponde ao padrão
                import re
                if re.match(f"^{pattern}$", relative_path_for_matching):
                    included = True
                    break

            # Se não foi incluído por nenhum padrão, retorna False
            if not included:
                return False

            # Se foi incluído e não há padrões de exclusão, retorna True
            if not self.exclude_patterns:
                return True

            # Verifica os padrões de exclusão
            for pattern in self.exclude_patterns:
                pattern = pattern.replace('\\', '/')
                if fnmatch.fnmatch(relative_path, pattern):
                    return False

            return True

        except ValueError:
            # Se não conseguir obter o caminho relativo, não inclui o arquivo
            return False

    def get_output_filename(self, file_path: Path) -> str:
        """Gera o nome do arquivo de saída no formato desejado."""
        try:
            relative_path = file_path.relative_to(self.source_dir)
            return str(relative_path).replace('\\', '.').replace('/', '.')
        except ValueError as e:
            self.logger.error(f"Erro ao gerar nome do arquivo de saída para {file_path}: {str(e)}")
            return str(file_path.name)

    def collect_files(self) -> Set[Path]:
        """Coleta todos os arquivos que correspondem aos padrões definidos."""
        collected_files = set()

        self.logger.info(f"Iniciando coleta de arquivos em: {self.source_dir}")
        self.logger.info("Padrões de inclusão: %s", ', '.join(self.include_patterns))
        if self.exclude_patterns:
            self.logger.info("Padrões de exclusão: %s", ', '.join(self.exclude_patterns))
        else:
            self.logger.info("Nenhum padrão de exclusão definido")

        try:
            for file_path in self.source_dir.rglob('*'):
                if file_path.is_file():
                    if self.should_include_file(file_path):
                        relative_path = str(file_path.relative_to(self.source_dir)).replace('\\', '/')
                        self.logger.debug(f"Incluindo arquivo: {relative_path}")
                        collected_files.add(file_path)
                    else:
                        relative_path = str(file_path.relative_to(self.source_dir)).replace('\\', '/')
                        self.logger.debug(f"Ignorando arquivo: {relative_path}")
        except Exception as e:
            self.logger.error(f"Erro durante a coleta de arquivos: {str(e)}")

        self.logger.info(f"Total de arquivos coletados: {len(collected_files)}")
        return collected_files

    def copy_files(self, collected_files: Set[Path]) -> None:
        """Copia os arquivos coletados para o diretório de saída."""
        try:
            self._ensure_directory(self.output_dir)
            self._clear_directory_contents(self.output_dir)

            for source_file in collected_files:
                output_filename = self.get_output_filename(source_file)
                destination = self.output_dir / output_filename
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
    config_path = sys.argv[1] if len(sys.argv) > 1 else 'config.ini'
    collector = ProjectFileCollector(config_path)
    collector.run()

if __name__ == '__main__':
    main()
