from datetime import datetime
from functools import wraps

def dates(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        current_year = datetime.now().year
        days = range(1, 32)
        months = range(1, 13)
        years = range(current_year - 30, current_year + 20)

        # Executa a view normalmente
        response = view_func(request, *args, **kwargs)

        # Se for uma renderização (não JSON), adiciona os dados ao contexto
        if hasattr(response, 'context_data'):
            response.context_data.update({
                'current_year': current_year,
                'days': days,
                'months': months,
                'years': years,
            })
        return response
    return wrapper
