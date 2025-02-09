import json


def dict_list_to_json(dict_list, filename):
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)

        return json_str

    except (TypeError, ValueError, IOError) as e:
        error_text = 'Ошибка при преобразовании списка словарей'
        error_text += f' в JSON или записи в файл: {e}'
        print(error_text)
        return None


def json_to_dict_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)

        return dict_list

    except (TypeError, ValueError, IOError) as e:
        error_text = 'Ошибка при чтении JSON из файла'
        error_text += f' или преобразовании в список словарей: {e}'
        print(error_text)
        return None
