import os
import zipfile

VERSAO = "3.3.1"

PASTA_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DIST = os.path.join(PASTA_PROJETO, "dist")

ARQUIVO_ZIP = os.path.join(
    PASTA_DIST,
    f"TechBairro-{VERSAO}.zip"
)

PASTAS_FORA = ["dist", "__pycache__"]
EXTENSOES_FORA = [".db", ".pyc"]

os.makedirs(PASTA_DIST, exist_ok=True)

incluidos = []
fora = []

with zipfile.ZipFile(ARQUIVO_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:

    for raiz, pastas, arquivos in os.walk(PASTA_PROJETO):

        pastas[:] = [
            pasta for pasta in pastas
            if pasta not in PASTAS_FORA
        ]

        for arquivo in arquivos:

            caminho = os.path.join(raiz, arquivo)

            if caminho == ARQUIVO_ZIP:
                continue

            if os.path.splitext(arquivo)[1] in EXTENSOES_FORA:
                fora.append(caminho)
                continue

            caminho_relativo = os.path.relpath(
                caminho,
                PASTA_PROJETO
            )

            zipf.write(caminho, caminho_relativo)
            incluidos.append(caminho_relativo)

print("=== ARQUIVOS INCLUÍDOS ===")

for arquivo in incluidos:
    print(arquivo)

print("\n=== ARQUIVOS DE FORA ===")

for arquivo in fora:
    print(os.path.relpath(arquivo, PASTA_PROJETO))

print("\nPacote criado com sucesso!")
print(ARQUIVO_ZIP)