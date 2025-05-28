import logging

logging.basicConfig(
    level=logging.INFO,  # Muestra info, warning, error
    format="%(asctime)s [%(levelname)s] %(message)s",  # Formato del mensaje
)
logger = logging.getLogger(__name__)  # Crea el logger
