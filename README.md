# Python CV Generator

> Projeto criado para demonstrar uma aplicação em Python e implementar evoluções mesmo Python não sendo uma de minhas tecnologias principais.
>
> Mais projetos em https://github.com/ministracao-aulas/
>
> Versão resumida em https://github.com/ministracao-aulas/Python-CV-Generator
>
> Me reservo o direito de errar kk afinal não sou especialista Python, mas aceito de bom grado sugestões e issues. Desde já, obrigado.
>
> Nota: mantive as chaves e variáveis em português mesmo para fim de demonstração e para evitar confusão à quem era demonstrado.

## Commands

### Load env

```sh
python3 -m venv ./venv
```

- After init `venv`, put this on path:

```sh
export PATH=$(realpath ./venv/bin/):$PATH
```

Or load venv running:

```sh
source ./load-env.sh
```

### Install requirements

```sh
pip install -r requirements.txt
```

### Copy JSON data example file

```sh
cp curriculum_data.example.json curriculum_data.json
```

- Edit the `curriculum_data.json` file with your info.

### Generate file

```sh
python3 ./main.py
```

-----

## OR run all in a single script

```sh
./generate-cv.sh
```

-----

## [CHANGELOG](./CHANGELOG.md)

-----

## ROADMAP

- [x] supports data from JSON file
- [x] supports multi language
- [ ] auto release final file
