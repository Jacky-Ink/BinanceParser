Парсер считывающий пару XRP/USDT на платформе Binance

Для запуска необходимо:
1. Клонировать репозиторий:
    git clone git@github.com:Jacky-Ink/BinanceParser.git

2. Установить виртуальное окружение:
    python -m venv venv

3. Запустить виртуально окружение:
    source venv/Scripts/activate

4. Обновить pip install
    python -m pip install --upgrade pip

5. Установить зависимости файла requirements.txt:
    pip install -r requirements.txt

6. Запустить код

Второре задание:
Создать отдельные потоки для других пар и проверять необходимые пары асинхронно
Для удобства можно вывести конечный результат в телеграмм бот и отправлять его конкретному юзеру/юзерам