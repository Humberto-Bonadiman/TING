from ting_file_management.file_management import txt_importer
import sys


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
        instance.enqueue(output_structure)
        return print(str(output_structure), file=sys.stdout)


def remove(instance):
    len_instance = len(instance)
    if(len_instance <= 0):
        return print('Não há elementos', file=sys.stdout)
    dequeue_file = instance.dequeue()
    print(f'Arquivo {dequeue_file} removido com sucesso', file=sys.stdout)



def file_metadata(instance, position):
    """Aqui irá sua implementação"""
