# Saucedemo UI Tests

Проект содержит автоматизированные UI-тесты для сайта https://www.saucedemo.com/, реализованные на Python с использованием Selenium WebDriver и Pytest. Архитектура проекта построена по паттерну Page Object Model. Тесты интегрированы с Jenkins и поддерживают генерацию Allure-результатов.

## Требования

- Python 3.10+
- Google Chrome
- Git

## Установка и запуск локально

1. Клонировать репозиторий:

git clone [https://github.com/bessonovagalina/Saucedemo.git](https://github.com/bessonovagalina/Saucedemo.git)
cd Saucedemo


2. Создать и активировать виртуальное окружение:

python -m venv venv
venv\Scripts\activate


3. Установить зависимости:

pip install -r requirements.txt

4. Запустить тесты:

pytest --alluredir=allure-results

## Структура проекта

- `pages/` — Page Object классы
- `tests/` — тестовые сценарии
- `conftest.py` — фикстуры Pytest
- `Jenkinsfile` — Jenkins pipeline
- `requirements.txt` — зависимости проекта
- `allure-results/` — результаты выполнения тестов

## CI / Jenkins

Проект содержит Jenkinsfile с декларативным pipeline. Jenkins выполняет следующие шаги:
- checkout репозитория
- установка зависимостей
- запуск Pytest
- сохранение Allure-артефактов сборки

Для запуска в Jenkins достаточно создать Pipeline job и указать репозиторий GitHub.

## Тестируемые сценарии

- Успешная авторизация
- Логин с неверным паролем
- Логин заблокированного пользователя
- Логин с пустыми полями
- Логин пользователя performance_glitch_user


