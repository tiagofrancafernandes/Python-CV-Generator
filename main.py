from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import json
import os
import argparse

def carregar_dados_curriculo(arquivo_json, idioma):
    with open(arquivo_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    if idioma not in dados['idiomas']:
        raise ValueError(f"Idioma '{idioma}' não disponível no arquivo JSON.")
    return dados['curriculos'][idioma]

# Caminho do arquivo JSON e idioma desejado
ARQUIVO_JSON = './curriculum_data.json'
IDIOMA = 'pt'  # ou 'en' para inglês

def main():
    parser = argparse.ArgumentParser(description="Gerador de Currículos Multi-idioma")
    parser.add_argument('-i', '--idioma', help='Idioma do currículo a ser gerado (ex: pt, en)')
    args = parser.parse_args()

    with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)
    idiomas_disponiveis = dados_json['idiomas']

    idiomas_para_gerar = [args.idioma] if args.idioma else idiomas_disponiveis

    for idioma in idiomas_para_gerar:
        if idioma not in idiomas_disponiveis:
            print(f"Idioma '{idioma}' não disponível. Pulando...")
            continue
        dados = dados_json['curriculos'][idioma]
        doc = Document()
        # --- Cabeçalho ---
        nome = doc.add_paragraph(dados['nome'])
        nome.style = doc.styles["Heading 1"]
        nome.alignment = WD_ALIGN_PARAGRAPH.CENTER
        funcao = doc.add_paragraph(dados['funcao'])
        funcao.alignment = WD_ALIGN_PARAGRAPH.CENTER
        contatos = doc.add_paragraph(dados['contatos'])
        contatos.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph("")
        # --- Apresentação ---
        doc.add_heading(dados['apresentacao_titulo'], level=2)
        doc.add_paragraph(dados['apresentacao'])
        # --- Competências Técnicas ---
        doc.add_heading(dados['competencias_titulo'], level=2)
        for skill in dados['competencias']:
            doc.add_paragraph(f"• {skill}")
        # --- Experiência Profissional ---
        doc.add_heading(dados['experiencia_titulo'], level=2)
        for exp in dados['experiencia']:
            doc.add_paragraph(f"{exp['cargo']} - {exp['empresa']} ({exp['periodo']})").bold = True
            for desc in exp["descricao"]:
                doc.add_paragraph(f"• {desc}")
        # --- Formação ---
        doc.add_heading(dados['formacao_titulo'], level=2)
        for formacao in dados['formacao']:
            doc.add_paragraph(formacao)
        # --- Certificações ---
        doc.add_heading(dados['certificacoes_titulo'], level=2)
        for cert in dados['certificacoes']:
            doc.add_paragraph(f"• {cert}")
        # --- Idiomas ---
        doc.add_heading(dados['idiomas_titulo'], level=2)
        for idioma_item in dados['idiomas_lista']:
            doc.add_paragraph(idioma_item)
        # Salvar arquivo
        output_dir = './output'
        os.makedirs(output_dir, exist_ok=True)
        caminho_cv = f"{output_dir}/CV-{idioma}-Tiago-Franca-Fernandes.docx"
        doc.save(caminho_cv)
        print(f"Currículo gerado: {caminho_cv}")

if __name__ == "__main__":
    main()
