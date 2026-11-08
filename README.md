# Автотест LemanaPro

Автоматизированный тест проверки перехода в раздел «Клиентская поддержка» на сайте https://yaroslavl.lemanapro.ru/.

## Требования
- **Python 3.13**
- Остальное установится само.

## Установка
```bash
pip install -r requirements.txt
```

## Запуск
```bash
pytest test_support.py -s
```

*Примечание: используется SeleniumBase в режиме Pure CDP для обхода защиты сайта. Драйверы (yandexdriver.exe и т.д.) не нужны, SeleniumBase сам скачает нужную сборку Chromium при первом запуске.*
