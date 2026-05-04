# Habit Tracker API

## 🇬🇧 English

Simple API for tracking habits.

### Features
- Add habit
- Get habits
- Complete habit
- Reset habits

### Endpoints

POST /habits
{
  "title": "run"
}

GET /habits

PUT /habits/complete
{
  "title": "run"
}

PUT /habits/reset

### How to run

pip install -r requirements.txt  
python app.py  

---

## 🇷🇺 Русский

Простое API для отслеживания привычек.

### Возможности
- Добавление привычки
- Получение списка привычек
- Отметка выполнения
- Сброс всех привычек

### Эндпоинты

POST /habits
{
  "title": "run"
}

GET /habits

PUT /habits/complete
{
  "title": "run"
}

PUT /habits/reset

### Как запустить

pip install -r requirements.txt  
python app.py