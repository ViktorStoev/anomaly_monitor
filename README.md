# Anomaly Monitor

Микросервис для регистрации и мониторинга аномалий. Проект создан на базе Flask и предназначен для демонстрации работы автономного микросервиса.

## Особенности
- Регистрация аномалий через веб-интерфейс.
- Отображение зарегистрированных аномалий и логов в реальном времени.
- Простая интеграция с Replit.

## Как запустить проект в Replit

### Шаг 1: Импорт проекта из GitHub
1. Перейдите в [Replit](https://replit.com/).
2. Нажмите **"Create"** → **"Import from GitHub**.
3. Вставьте URL репозитория: ([https://github.com/ViktorStoev/anomaly_monitor](https://github.com/ViktorStoev/anomaly_monitor/tree/main))
4. Нажмите **"Import**".

### Шаг 2: Настройка команды запуска
После импорта Replit может запросить команду для запуска проекта. Если это произошло:
1. Перейдите в раздел **"Configure Repl"**, нажав на **"Configuration"**.
![image](https://github.com/user-attachments/assets/8f26041c-7e15-487e-9952-5634ee119492)

2. В поле **"Run command"** введите следующую команду:
```bash
python -m ensurepip --upgrade && pip install -r requirements.txt && python anomaly_monitor.py
```
### Шаг 3: Запуск проекта
1. Нажмите "Run".
