from fastapi import Request
from starlette.responses import TemplateResponse

from main import templates


class UIUtils:

    @staticmethod
    def render(template: str, request: Request, **kwargs) -> TemplateResponse:
        """
        Renderiza um template HTML utilizando Jinja2 e injeta automaticamente
        o objeto ``request`` no contexto do template.

        Este método serve como utilitário para evitar repetição ao retornar
        ``TemplateResponse`` nas rotas que exibem páginas.

        Args:
            template (str):
                Caminho do template dentro do diretório de templates.

            request (Request):
                Objeto da requisição atual. Necessário para funcionamento de
                ``url_for``, arquivos estáticos e middlewares no Jinja2.

            **kwargs:
                Variáveis adicionais que serão incluídas no contexto do template.

        Returns:
            TemplateResponse:
                Resposta HTTP contendo o template renderizado.
        """
        return templates.TemplateResponse(
            template,
            {"request": request, **kwargs}
        )