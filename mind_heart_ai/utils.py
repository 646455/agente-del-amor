import re

def validate_query(query: str) -> bool:
    """
    Valida si la consulta es razonable para un agente de IA.
    Ahora acepta cualquier consulta no vacía.
    """
    if not query or len(query.strip()) < 1:
        return False

    # Aceptar cualquier consulta que tenga al menos un carácter
    return True