from .base import bp


@bp.route('/ping')
def index():
    return 'pong'
