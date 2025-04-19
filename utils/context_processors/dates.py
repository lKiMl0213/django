# myapp/context_processors.py
from datetime import datetime


def dates(request):
    current_year = datetime.now().year
    days = range(1, 32)
    months = range(1, 13)
    years = range(current_year - 80, current_year + 20)

    return {
        "current_year": current_year,
        "days": days,
        "months": months,
        "years": years,
    }
