from flask import Blueprint, request, jsonify, redirect
from .services import gerar_codigo_curto
from .database import db, URL

bp = Blueprint('rotas', __name__)


@bp.route('/encurtar', methods=['POST'])
def encurtar_url():
    dados = request.get_json()

    if not dados or 'url' not in dados:
        return jsonify({"erro": "O campo 'url' é obrigatório"}), 400

    url_original = dados['url']

    codigo_curto = gerar_codigo_curto()
    while URL.query.filter_by(codigo_curto=codigo_curto).first() is not None:
        codigo_curto = gerar_codigo_curto()

    #INSERT
    nova_url = URL(codigo_curto=codigo_curto, url_original=url_original)
    db.session.add(nova_url)
    db.session.commit()

    url_encurtada = request.host_url + codigo_curto

    return jsonify({
        "url_original": url_original,
        "url_encurtada": url_encurtada,
        "codigo": codigo_curto
    }), 201


@bp.route('/<codigo_curto>', methods=['GET'])
def redirecionar(codigo_curto):
    #SELECT
    registro = URL.query.filter_by(codigo_curto=codigo_curto).first()

    if registro:
        return redirect(registro.url_original)

    return jsonify({"erro": "URL não encontrada"}), 404