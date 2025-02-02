import camelot

# Caminho para o arquivo PDF
pdf_path = "2020.pdf"

# Ler tabelas
tables = camelot.read_pdf(pdf_path, pages="all")

# Salvar as tabelas em CSV
for i, table in enumerate(tables):
    csv_path = f"tabela_{i + 1}.csv"
    table.to_csv(csv_path)
    print(f"Tabela {i + 1} salva em {csv_path}")
