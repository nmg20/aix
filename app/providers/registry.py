from app.providers.base_provider import PlaylistProvider

class PlaylistProviderRegistry:
    """
    Clase para registrar los providers de las playlists por su nombre.
    """
    def __init__(self):
        self.providers: dict[str, PlaylistProvider] = {}
    
    def register(self, provider: PlaylistProvider):
        self.providers[provider.name] = provider
    
    def get(self, name: str) -> PlaylistProvider:
        return self.providers[name]