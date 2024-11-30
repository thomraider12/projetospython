import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Rota principal
@app.route("/")
def index():
    return render_template("index.html")

# API para listar scripts
@app.route("/list-scripts", methods=["GET"])
def list_scripts():
    projects_dir = "projects"
    scripts = {}

    for root, dirs, files in os.walk(projects_dir):
        # Apenas considera arquivos com extensão .py
        python_files = [f for f in files if f.endswith(".py")]
        if python_files:
            project_name = os.path.relpath(root, projects_dir)
            scripts[project_name] = python_files

    return jsonify(scripts)

# Rota para carregar o conteúdo de um script
@app.route("/get-script/<path:project>/<script>", methods=["GET"])
def get_script(project, script):
    script_path = os.path.join("projects", project, script)
    if not os.path.isfile(script_path):
        return {"error": "Script not found"}, 404

    with open(script_path, "r") as f:
        content = f.read()

    return jsonify({"content": content})

if __name__ == "__main__":
    app.run(debug=True)
