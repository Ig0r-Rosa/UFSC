import os

def renomear_arquivos_numericamente(diretorio, prefixo='', com_zeros=False):
    """
    Renomeia arquivos em 'diretorio' para 'prefixo1.ext', 'prefixo2.ext', ...
    Se com_zeros=True, adiciona zeros à esquerda (e.g. 001, 002, ...).
    """
    # Lista apenas arquivos, ignorando subpastas
    arquivos = [f for f in os.listdir(diretorio) 
                if os.path.isfile(os.path.join(diretorio, f))]
    arquivos.sort()  # ordena alfabeticamente; adapte se quiser outra ordem

    # Calcula número de dígitos necessários, se for usar zeros à esquerda
    total = len(arquivos)
    largura = len(str(total)) if com_zeros else 0

    for idx, nome in enumerate(arquivos, start=1):
        basename, ext = os.path.splitext(nome)
        if com_zeros:
            numero = str(idx).zfill(largura)
        else:
            numero = str(idx)
        novo_nome = f"{prefixo}{numero}{ext}"
        caminho_antigo = os.path.join(diretorio, nome)
        caminho_novo  = os.path.join(diretorio, novo_nome)

        # Evita sobrescrever arquivo existente
        if not os.path.exists(caminho_novo):
            os.rename(caminho_antigo, caminho_novo)
        else:
            print(f"Aviso: '{caminho_novo}' já existe, pulando.")

if __name__ == "__main__":
    # Exemplo de uso:
    pasta = "/home/manzine/Italo/Faculdade/FeTrans/aulas_23-06_25-06_30-06"
    # Para renomear sem zeros: 1.jpg, 2.png, ...
    renomear_arquivos_numericamente(pasta)

    # Para renomear com zeros: 001.jpg, 002.png, ...
    # renomear_arquivos_numericamente(pasta, prefixo='', com_zeros=True)

    # Para adicionar um prefixo: img001.jpg, img002.png, ...
    # renomear_arquivos_numericamente(pasta, prefixo='img', com_zeros=True)
