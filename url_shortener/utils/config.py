import os
from omegaconf import OmegaConf


def load_conf():
    "Load config from file"
    env = os.getenv("PRJ_ENV", "dev")
    config_file = os.path.join(
        os.path.dirname(__file__), "../../conf/{}.yaml".format(env)
    )

    with open(config_file) as f:
        cfg = OmegaConf.create(f.read())
    return cfg, env


cfg, env = load_conf()
