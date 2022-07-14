import sys


def txt_importer(path_file):
    try:
        if ".txt" not in path_file:
            print("Formato inválido", file=sys.stderr)
        with open(path_file, 'r', encoding='utf-8') as file:
            info = file.readlines()
            return [line.replace('\n', '') for line in info]
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)


print(txt_importer("ting_file_management/text.txt"))
