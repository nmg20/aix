from app.providers.registry import PlaylistProviderRegistry
from app.providers.local import LocalProvider

providers_registry = PlaylistProviderRegistry()
providers_registry.register(LocalProvider())
