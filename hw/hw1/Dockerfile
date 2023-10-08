# Използваме slim версия на Python 3.11 като базов образ
FROM python:3.11-slim AS build

# Задаваме работната директория на /app
WORKDIR /app

# Копираме requirements.txt файлът в контейнера
COPY requirements.txt .

# Инсталираме необходимите пакети за приложението
RUN pip install --user -r requirements.txt

# Копираме целия код на приложението в контейнера
COPY . .

# Създаваме нов образ, който ще бъде използван за production
FROM python:3.11-slim AS production

# Задаваме работната директория на /app
WORKDIR /app

# Копираме инсталираните пакети от build образа в production образа
COPY --from=build /root/.local /root/.local

# Копираме целия код на приложението в production образа
COPY --from=build /app .

# Задаваме PATH променливата, за да можем да използваме инсталираните пакети
ENV PATH=/root/.local/bin:$PATH

# Отваряме порт 5001 за връзка с приложението
EXPOSE 5001

# Задаваме команда, която да се изпълни при стартиране на контейнера
CMD ["python", "app.py"]