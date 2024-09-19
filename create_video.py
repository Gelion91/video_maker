import os
import re
import sys
import ffmpeg


def make_video(path=None, name=None, file_name=None):
    """
    Функция принимает 3 аргумента
    path - Путь до папки с секвенциями
    name - Имя секвенции без цифрового значения и формата
    file_name - Имя готового видео
    ВАЖНО!
    ------------------------------------------------------------------
    Если аргумент содержит пробелы, необходимо обернуть его в ""
    ------------------------------------------------------------------
    """
    pattern = None
    for root, dirs, files in os.walk(path):
        answer = name
        for file in files:
            if answer in file:
                re_file = re.match(fr'{answer}.\d+.jpg', file)
                if re_file:
                    result = re.sub(r'\d+', '*', re_file.group(0))
                    pattern = os.path.join(root, result)

    output = os.getcwd() + '/static/' + file_name

    if path and name and file_name:
        if os.path.exists(output):
            os.remove(output)
        if pattern:
            ffmpeg.input(f'{pattern}', pattern_type='glob', vcodec='mjpeg', framerate=24).output(output).run()
            return file_name
        else:
            return 'Нет секвенций с таким именем'
    else:
        return "Нужны все параметры"


if __name__ == '__main__':
    if len(sys.argv) <= 3:
        raise IndexError('Необходимо указать все аргументы(path, name, file_name')
    make_video(sys.argv[1], sys.argv[2], sys.argv[3])