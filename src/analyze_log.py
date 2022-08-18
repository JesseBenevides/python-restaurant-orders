import csv


def get_data(path_to_file):
    if '.csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def analyze_log(path_to_file):
    all_data = get_data(path_to_file)
    print(all_data)
