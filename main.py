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

        # --- Customização de estilos ---
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Calibri'
        font.size = Pt(11)

        heading1 = doc.styles['Heading 1']
        heading1.font.name = 'Calibri'
        heading1.font.size = Pt(26)
        heading1.font.bold = True
        heading1.font.color.rgb = RGBColor(0, 102, 204)  # Azul (não sei se fiz certo aqui. Parece que não)

        heading2 = doc.styles['Heading 2']
        heading2.font.name = 'Calibri'
        heading2.font.size = Pt(16)
        heading2.font.bold = True
        heading2.font.color.rgb = RGBColor(0, 153, 76)  # Verde (não sei se fiz certo aqui. Parece que não)

        # --- Cabeçalho ---
        nome = doc.add_paragraph(dados['nome'])
        nome.style = doc.styles["Heading 1"]
        nome.alignment = WD_ALIGN_PARAGRAPH.CENTER
        nome.paragraph_format.space_after = Pt(8)
        funcao = doc.add_paragraph(dados['funcao'])
        funcao.style = doc.styles['Heading 2']
        funcao.alignment = WD_ALIGN_PARAGRAPH.CENTER
        funcao.paragraph_format.space_after = Pt(10)
        contatos = doc.add_paragraph(dados['contatos'])
        contatos.alignment = WD_ALIGN_PARAGRAPH.CENTER
        contatos.paragraph_format.space_after = Pt(12)
        # Linha separadora discreta
        sep = doc.add_paragraph()
        sep_run = sep.add_run("\u2014" * 30)
        sep.alignment = WD_ALIGN_PARAGRAPH.CENTER
        sep_run.font.size = Pt(8)
        sep_run.font.color.rgb = RGBColor(220, 220, 220)
        doc.add_paragraph("")
        # --- Apresentação ---
        doc.add_heading(dados['apresentacao_titulo'], level=2)
        p = doc.add_paragraph(dados['apresentacao'])
        p.paragraph_format.space_after = Pt(16)
        # --- Competências Técnicas ---
        doc.add_heading(dados['competencias_titulo'], level=2)
        for skill in dados['competencias']:
            item = doc.add_paragraph(f"• {skill}")
            item.paragraph_format.left_indent = Pt(12)
        doc.add_paragraph("")
        # --- Experiência Profissional ---
        doc.add_heading(dados['experiencia_titulo'], level=2)
        for exp in dados['experiencia']:
            cargo_paragraph = doc.add_paragraph()
            cargo_run = cargo_paragraph.add_run(f"{exp['cargo']} - {exp['empresa']} ({exp['periodo']})")
            cargo_run.bold = True
            cargo_run.font.size = Pt(14)

            #############
            cargo_run = doc.styles['Heading 2']
            cargo_run.font.name = 'Calibri'
            cargo_run.font.size = Pt(16)
            cargo_run.font.bold = True
            cargo_run.font.color.rgb = RGBColor(0, 153, 76)  # Verde
            #############

            cargo_paragraph.paragraph_format.space_before = Pt(8)
            for desc in exp["descricao"]:
                item = doc.add_paragraph(f"  - {desc}")
                item.paragraph_format.left_indent = Pt(18)
        doc.add_paragraph("")
        # --- Formação ---
        doc.add_heading(dados['formacao_titulo'], level=2)
        for formacao in dados['formacao']:
            item = doc.add_paragraph(formacao)
            item.paragraph_format.left_indent = Pt(12)
        doc.add_paragraph("")
        # --- Certificações ---
        doc.add_heading(dados['certificacoes_titulo'], level=2)
        for cert in dados['certificacoes']:
            item = doc.add_paragraph(f"• {cert}")
            item.paragraph_format.left_indent = Pt(12)
        doc.add_paragraph("")
        # --- Idiomas ---
        doc.add_heading(dados['idiomas_titulo'], level=2)
        for idioma_item in dados['idiomas_lista']:
            item = doc.add_paragraph(idioma_item)
            item.paragraph_format.left_indent = Pt(12)
        # Salvar arquivo
        output_dir = './output'
        os.makedirs(output_dir, exist_ok=True)
        caminho_cv = f"{output_dir}/CV-{idioma}-Tiago-Franca-Fernandes.docx"
        doc.save(caminho_cv)
        print(f"Currículo gerado: {caminho_cv}")

if __name__ == "__main__":
    main()
