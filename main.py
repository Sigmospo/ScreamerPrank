# Самый простой скрипт, чтобы напугать человека.

# ! Создано в развлекательных целях.
# ! Всю ответственность вы перекладываете на себя.

# * Информация
# Скрипт не добавляется в автозапуск
# Автоматически устанавливается громкость 100%

# * Если подкинуть однокласснику на уроке информатики, вообще ржачка будет.
# * всем советую.

# * P.S Вы можете скачать EXE файл в репозитории, и не собирать его при помощи pyinstaller'a.

# Получаем папку со скриптом/EXE.
folder = '\\'.join(__file__.split('\\')[:-1:1])

# 1. Модули

# pip install simpleaudio
from simpleaudio import WaveObject

# pip install keyboard
import keyboard

# 2. Устанавливаем громкость 100%
for x in range(50):
    keyboard.press('volume up')

# 3. Блокируем все клавиши
for x in range(1, 150):
    keyboard.block_key(x)

# 4. Играем звук (бесконечно)
wave_obj = WaveObject.from_wave_file(folder + "\\ScreamerSound.wav")

while True:
    play_obj = wave_obj.play()
    play_obj.wait_done()
