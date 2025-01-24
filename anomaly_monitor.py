from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('anomaly_monitor.log'),  # Логи в файл
        logging.StreamHandler()  # Логи в консоль
    ]
)

app = Flask(__name__)

# Хранилище для аномалий (в памяти)
anomalies = []

# Хранилище для логов (в памяти)
logs = []

# Кастомный обработчик для логирования в память
class MemoryHandler(logging.Handler):
    def emit(self, record):
        logs.append(self.format(record))

# Добавляем кастомный обработчик
memory_handler = MemoryHandler()
memory_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(memory_handler)

@app.route('/')
def index():
    """Главная страница с интерфейсом."""
    logging.info("Главная страница запрошена.")
    return render_template('index.html', anomalies=anomalies, logs=logs[-10:])  # Показываем последние 10 логов

@app.route('/log', methods=['POST'])
def log_anomaly():
    """Логирование новой аномалии."""
    description = request.form.get('description', '').strip()
    if description:
        anomaly = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description
        }
        anomalies.append(anomaly)
        logging.info(f"Зарегистрирована новая аномалия: {description}")
    else:
        logging.warning("Попытка зарегистрировать аномалию без описания.")
    return index()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logging.info(f"Запуск Flask-приложения на порту {port}...")
    app.run(host='0.0.0.0', port=port)