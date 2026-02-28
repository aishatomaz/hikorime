from pathlib import Path

from fastapi import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

class HikorimeUI:

    @staticmethod
    def render(template: str, request: Request, usr: dict, **kwargs) -> Response:
        """
        Renderiza um template HTML utilizando Jinja2 e injeta automaticamente
        o objeto ``request`` no contexto do template.

        Utilitário para evitar repetição ao retornar ``TemplateResponse``
        nas rotas que exibem páginas.

        Args:
            template (str):
                Caminho do template dentro do diretório de templates.

            request (Request):
                Objeto da requisição atual. Necessário para funcionamento de
                ``url_for``, arquivos estáticos e middlewares no Jinja2.

            usr (dict):
                Dados do usuário da sessão. Necessário para mantê-lo
                autenticado.

            **kwargs:
                Variáveis adicionais que serão incluídas no contexto do template.

        Returns:
            Response:
                Resposta HTTP contendo o template renderizado.
        """
        return templates.TemplateResponse(
            template,
            {"request": request, "usr": usr, **kwargs}
        )