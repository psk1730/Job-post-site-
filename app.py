from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'data scientist',
        'location': 'India Delhi',
    },
    {
        'id': 2,
        'title': 'data analyst',
        'location': 'India Gurugram',
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'India Bengluru',
    },
    {
        'id': 4,
        'title': 'Electrical Engineer',
        'location': 'India Pune',
    },
]


@app.route("/")
def hello_world():
  return render_template("home.html", var=JOBS, name="Pravesh")

@app.route("/api/jobs")
def H_world():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

{{ }}
