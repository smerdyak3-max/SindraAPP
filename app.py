import os
import sys
import webview

def get_resource_path(relative_path):
    """Возвращает путь к файлу, учитывая режим работы (exe или скрипт)"""
    if getattr(sys, 'frozen', False):
        # Если запущено как exe
        base_path = sys._MEIPASS
    else:
        # Если запущено как скрипт
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    # Путь к HTML должен быть полным и правильным
    html_path = get_resource_path('index.html')
    
    # Запускаем окно
    window = webview.create_window(
        title='Синдра: Эджинг-Марафон v5.0',
        url=f'file:///{html_path.replace(os.sep, "/")}', # Добавляем file:/// для локального доступа
        width=1250,
        height=880
    )
    
    webview.start()