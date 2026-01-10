from pathlib import Path
from omegaconf import OmegaConf

_CURRENT_DIR = Path(__file__).parent

def _load_config(filename: str):
    """
    Loads a config by searching both the installed package location
    and the local development location.
    """
    installed_path = _CURRENT_DIR / "configs" / filename
    dev_path = _CURRENT_DIR.parent / "configs" / filename

    if installed_path.exists():
        return OmegaConf.load(installed_path)
    else:
        return OmegaConf.load(dev_path)

DEFAULT_CONFIG = _load_config("default.yaml")
DEFAULT_DATASET_CONFIG = DEFAULT_CONFIG.dataset
DEFAULT_MODALITY_CONFIG = DEFAULT_CONFIG.dataset.modality_config
DEFAULT_DATALOADER_CONFIG = DEFAULT_CONFIG.dataloader

BENCHMARKING_CONFIG = _load_config("throughput_f16_prenorm.yaml")