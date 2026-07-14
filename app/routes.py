from flask import Blueprint, request, jsonify, redirect
from .services import gerar_codigo_curto
from .database import db, URL

bp = Blueprint('rotas', __name__)


@bp.route('/encurtar', methods=['POST'])
def encurtar_url():
    """
        Encurta uma URL original e salva no banco de dados.
        ---
        tags:
          - URLs
        parameters:
          - in: body
            name: body
            required: true
            schema:
              id: URLInput
              required:
                - url
              properties:
                url:
                  type: string
                  description: A URL original que será encurtada.
                  example: "SUA URL AQUI"
        responses:
          201:
            description: URL encurtada com sucesso.
            schema:
              properties:
                url_curta:
                  type: string
                  example: "http://127.0.0.1:5000/A1b2C3"
          400:
            description: Erro na requisição (JSON inválido ou URL ausente).
        """
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

#SELECT
@bp.route('/<codigo_curto>', methods=['GET'])
def redirecionar(codigo_curto):

    """
        Redireciona o usuário para a URL original.
        ---
        tags:
          - URLs
        parameters:
          - name: codigo_curto
            in: path
            type: string
            required: true
            description: O código de 6 dígitos gerado pela API.
            example: "A1b2C3"
        responses:
          302:
            description: Redirecionamento HTTP nativo para o site de destino.
          404:
            description: Código curto não encontrado no banco de dados.
        """

    if codigo_curto in['apidoc', 'apispec_1.json', 'flasgger_static']:
        return jsonify({"erro": "Rota ignorada"}), 404

    registro = URL.query.filter_by(codigo_curto=codigo_curto).first()

    if registro:
        return redirect(registro.url_original)

    return jsonify({"erro": "URL não encontrada"}), 404