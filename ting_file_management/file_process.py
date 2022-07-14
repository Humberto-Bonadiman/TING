from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    path_list = []
    len_instance = instance.__len__()
    for index in range(0, len_instance):
        path_list.append(instance.search(index))

    if path_file not in path_list:
        content = txt_importer(path_file)
        output_structure = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content
        }
        print(output_structure)
        instance.enqueue(output_structure)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
