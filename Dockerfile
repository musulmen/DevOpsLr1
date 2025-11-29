# Используем официальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY app.py requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт, который будет открыт в контейнере
EXPOSE 1234

# Команда запуска Flask
CMD ["python", "app.py"]
