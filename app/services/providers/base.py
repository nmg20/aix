from typing import List
from app.models import Song


class ProviderBase:
    name: str = "base"

    def supports(self, url: str) -> bool:
        """
        True si el servicio da soporte a ese tipo de URL.
        """
        raise NotImplementedError
    
    def parse(self, url: str) -> List[Song]:
        """
        Analiza una playlist apuntada por la URL y devuelve la lista de canciones.
        """
        raise NotImplementedError
    
    def download(self, songs: List[Song], output_dir: str = "./downloads"):
        """
        Descarga la lista de canciones en el directorio designado.
        """
        raise NotImplementedError
