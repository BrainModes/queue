import os
import requests
from requests.models import HTTPError
from pydantic import BaseSettings, Extra
from typing import Dict, Set, List, Any
from functools import lru_cache
from common import VaultClient
from dotenv import load_dotenv

# load env var from local env file
load_dotenv()

SRV_NAMESPACE = os.environ.get("APP_NAME", "service_queue")
CONFIG_CENTER_ENABLED = os.environ.get("CONFIG_CENTER_ENABLED", "false")

def load_vault_settings(settings: BaseSettings) -> Dict[str, Any]:
    if CONFIG_CENTER_ENABLED == "false":
        return {}
    else:
        vc = VaultClient(os.getenv("VAULT_URL"), os.getenv("VAULT_CRT"), os.getenv("VAULT_TOKEN"))
        return vc.get_from_vault(SRV_NAMESPACE)


class Settings(BaseSettings):
    port: int = 6060
    host: str = "127.0.0.1"
    env: str = "test"
    version: str = "0.1.0"
    
    gm_queue_endpoint: str
    gm_username: str
    gm_password: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = Extra.allow

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                load_vault_settings,
                env_settings,
                init_settings,
                file_secret_settings,
            )
    

@lru_cache(1)
def get_settings():
    settings =  Settings()
    return settings

ConfigClass = Settings()