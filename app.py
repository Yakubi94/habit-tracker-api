from flask import Flask, request, jsonify

from storage import load_data, save_data

app = Flask(__name__)

habits = load_data()
next_id = max([h["id"] for h in habits], default=0) + 1


# ---------- GET ALL ----------
@app.route("/habits", methods=["GET"])
def get_habits():
    return jsonify(habits)


# ---------- ADD ----------
@app.route("/habits", methods=["POST"])
def add_habit():
    global next_id

    data = request.json
    if not data:
        return {"error": "Request body is required"}, 400

    title = data.get("title")
    if not title:
        return {"error": "Title is required"}, 400

    # запрет дубликатов
    for habit in habits:
        if habit["title"].lower() == title.lower():
            return {"error": "Habit already exists"}, 400

    habit = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    habits.append(habit)
    next_id += 1

    save_data(habits)

    return {"message": "Habit added", "habit": habit}, 201


# ---------- COMPLETE ----------
@app.route("/habits/<int:habit_id>/complete", methods=["PUT"])
def complete_habit(habit_id):
    for habit in habits:
        if habit["id"] == habit_id:
            if habit["completed"]:
                return {"error": "Habit already completed"}, 400

            habit["completed"] = True
            save_data(habits)
            return {"message": "Completed", "habit": habit}

    save_data(habits)

    return {"error": "Habit not found"}, 404


# ---------- RESET ----------
@app.route("/habits/reset", methods=["PUT"])
def reset_habits():
    for habit in habits:
        habit["completed"] = False
        save_data(habits)

    return {"message": "All habits reset"}


# ---------- DELETE ----------
@app.route("/habits/<int:habit_id>", methods=["DELETE"])
def delete_habit(habit_id):
    for habit in habits:
        if habit["id"] == habit_id:
            habits.remove(habit)
            save_data(habits)
            return {"message": "Habit deleted"}

    return {"error": "Habit not found"}, 404


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)