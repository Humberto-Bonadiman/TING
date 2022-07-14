from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    result_word = []
    len_instance = instance.__len__()
    for index in range(0, len_instance):
        frequency = []
        result = instance.search(index)
        content = txt_importer(result)
        for line in range(0, len(content)):
            if word.upper() in content[line].upper():
                frequency.append({"linha": line + 1})

        if len(frequency) > 0:
            result_word.append({
                "palavra": word,
                "arquivo": result,
                "ocorrencias": frequency,
            })
    return result_word


def search_by_word(word, instance):
    result_word = []
    len_instance = instance.__len__()
    for index in range(0, len_instance):
        frequency = []
        result = instance.search(index)
        content = txt_importer(result)
        for line in range(0, len(content)):
            if word.upper() in content[line].upper():
                frequency.append({
                    "linha": line + 1, "conteudo": content[line]
                })

        if len(frequency) > 0:
            result_word.append({
                "palavra": word,
                "arquivo": result,
                "ocorrencias": frequency,
            })
    return result_word
