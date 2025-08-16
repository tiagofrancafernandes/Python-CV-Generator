# Changelog

## [1.1.0] - 2024-06-13
### Added
- Detecção automática de idiomas disponíveis no JSON e geração de todos os currículos de uma vez.
- Parâmetro de linha de comando `--idioma` (`-i`) para gerar currículo de idioma específico.
- Estrutura do projeto adaptada para multi-idioma via JSON externo.

### Example
Para gerar todos os currículos:
```
python main.py
```
Para gerar apenas o currículo em inglês:
```
python main.py --idioma en
```

## [1.0.0] - 2024-06-12
### Added
- Geração de currículo a partir de dados fixos no código.
