from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="templates")
    
    # Importar e registrar o blueprint principal
    from .routes import routes_bp
    app.register_blueprint(routes_bp)

    # Importar e registrar o blueprint de sentiment_analysis
    from sentiment_analysis.app.routes import routes_bp as sentiment_analysis_bp
    app.register_blueprint(sentiment_analysis_bp, url_prefix='/sentiment-analysis')

    return app

# Instanciar a aplicação
app = create_app()
