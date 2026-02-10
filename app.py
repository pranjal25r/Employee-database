from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Preloaded employee data (acts like DB)
employees = [
    {"id": 101, "name": "Rahul", "age": 25, "department": "IT", "salary": 50000},
    {"id": 102, "name": "Ananya", "age": 28, "department": "HR", "salary": 45000},
    {"id": 103, "name": "Karthik", "age": 30, "department": "Finance", "salary": 60000}
]

@app.route("/")
def index():
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        new_emp = {
            "id": int(request.form["id"]),
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "department": request.form["department"],
            "salary": int(request.form["salary"])
        }
        employees.append(new_emp)
        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/search", methods=["GET", "POST"])
def search_employee():
    employee = None
    if request.method == "POST":
        emp_id = int(request.form["id"])
        for emp in employees:
            if emp["id"] == emp_id:
                employee = emp
                break
    return render_template("search.html", employee=employee)

@app.route("/delete/<int:emp_id>")
def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp["id"] != emp_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
