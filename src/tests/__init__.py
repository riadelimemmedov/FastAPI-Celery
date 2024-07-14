# Local modules
from src.core.setup import CommonConfig, DockerLocal, DockerProd, ENVIRONMENT

# !Translation between Docker environment and their classes.
_setup = {"local": DockerLocal, "prod": DockerProd}

if ENVIRONMENT == "dev":
    config = CommonConfig()

else:
    _docker_env = _setup[ENVIRONMENT]().model_dump()
    config = CommonConfig().model_copy(update=_docker_env)
