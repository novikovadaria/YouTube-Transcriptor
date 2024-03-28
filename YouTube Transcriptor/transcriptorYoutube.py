from youtube_transcript_api import YouTubeTranscriptApi

def save_transcript(line_length=100):
    # Запрос ссылки на видео у пользователя
    video_url = input("Введите ссылку на видеоролик: ")
    # Извлечение ID видео из URL
    video_id = video_url.split('v=')[1]

    # Запрос предпочтительного языка транскрипта
    language_code = input("Выберите язык транскрипта (русский - ru, английский - eng): ").strip().lower()
    # Сопоставление ввода пользователя с кодами языков
    language = 'ru' if language_code == 'ru' else 'en'

    # Получение транскрипта
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    except Exception as e:
        print(f"Произошла ошибка при получении транскрипта: {e}")
        return

    # Создание или открытие текстового файла для записи
    with open('transcript.txt', 'w', encoding='utf-8') as file:
        line = ""  # Начальное значение текущей строки
        for item in transcript:
            # Предварительно добавляем пробел перед текстом, кроме начала строки
            text = ' ' + item['text'] if line else item['text']
            # Проверяем, не превысит ли добавление текста лимит по длине строки
            if len(line + text) > line_length:
                # Если да, записываем текущую строку в файл и начинаем новую
                file.write(line + "\n")
                line = item['text']  # Начинаем новую строку с текущего текста
            else:
                # Если нет, просто добавляем текст к текущей строке
                line += text
        # Записываем оставшуюся строку в файл, если она не пустая
        if line:
            file.write(line)

# Пример использования
save_transcript()

