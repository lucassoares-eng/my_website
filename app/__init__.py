from flask import Flask
from .routes import routes_bp
from sentiment_analysis.app.routes import routes_bp as sentiment_analysis_bp

def create_app():
    app = Flask(
        __name__,
        static_folder="static",            # Configura pasta estática para o módulo principal
        template_folder="templates"        # Configura pasta de templates para o módulo principal
    )

    # Registrar blueprint do app principal
    app.register_blueprint(routes_bp)

    # Registrar blueprint do sentiment_analysis com prefixo
    app.register_blueprint(
        sentiment_analysis_bp,
        url_prefix="/sentiment-analysis",
        static_folder="sentiment_analysis/app/static",  # Pasta estática do módulo sentiment_analysis
        template_folder="sentiment_analysis/app/templates"  # Templates específicos do módulo sentiment_analysis
    )

    return app

app = create_app()