from flask import Flask, render_template   
from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for job postings (use the API's database)
job_postings = [
    {"id": 1, "title": "Web Developer", "description": "Full-stack web developer position"},
    {"id": 2, "title": "Data Scientist", "description": "Data science role"},
    {"id": 3, "title": "UX Designer", "description": "User experience designer needed"},
]

@app.route('/')
def index():
    return render_template("index.html", job_postings=job_postings)

@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        # In the real application, you would save the job posting to a database.
        # we added it to the dummy data.
        job_id = len(job_postings) + 1
        job_postings.append({"id": job_id, "title": title, "description": description})
        return redirect(url_for('index'))
    return render_template('post_job.html')

if __name__ == '__main__':
    app.run(debug=True)
