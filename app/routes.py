import os
from flask import Blueprint, render_template, send_from_directory

# Definir o Blueprint
routes_bp = Blueprint("main_routes", __name__)

# Página inicial
@routes_bp.route('/')
def index():
    return render_template('home.html')

# Página de projetos
@routes_bp.route('/projects')
def projects():
    project_list = [
        {"name": "Project 1", "description": "Description of Project 1", "link": "https://github.com/yourusername/project1"},
        {"name": "Project 2", "description": "Description of Project 2", "link": "https://github.com/yourusername/project2"},
    ]
    return render_template('projects.html', projects=project_list)

# Página de currículo
@routes_bp.route('/resume')
def resume():
    return render_template('resume.html')

# Rota para servir o arquivo PDF
@routes_bp.route('/Resume.pdf')
def serve_resume():
    return send_from_directory(os.path.join("static"), "Resume.pdf")