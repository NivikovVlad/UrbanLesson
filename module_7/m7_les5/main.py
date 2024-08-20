import os
import time


directory = '..\\..\\'
dirs_ignore = ['.git', '.idea', '.venv']
files_ignore = ['.gitignore']

if __name__ == "__main__":

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in dirs_ignore]
        files[:] = [f for f in files if f not in files_ignore]

        for file in files:

            filepath = os.path.join(root, file)
            # filetime = time.ctime(os.path.getmtime(filepath))
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)

            print(
                f'\nОбнаружен файл: {file},'
                f'\nПуть: {filepath},'
                f'\nРазмер: {filesize} байт,'
                f'\nВремя изменения: {formatted_time},'
                f'\nРодительская директория: {parent_dir}')
