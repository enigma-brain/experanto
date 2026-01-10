from pathlib import Path
from omegaconf import OmegaConf
from importlib.resources import files, as_file


def _load_config(filename: str):
    """Load a config file from the package."""
    try:
        config_files = files("experanto.configs")
        with as_file(config_files / filename) as config_path:
            return OmegaConf.load(config_path)
    except (TypeError, FileNotFoundError):
        dev_path = Path(__file__).parent.parent / "configs" / filename
        return OmegaConf.load(dev_path)

DEFAULT_CONFIG = _load_config("default.yaml")
DEFAULT_DATASET_CONFIG = DEFAULT_CONFIG.dataset
DEFAULT_MODALITY_CONFIG = DEFAULT_CONFIG.dataset.modality_config
DEFAULT_DATALOADER_CONFIG = DEFAULT_CONFIG.dataloader

BENCHMARKING_CONFIG = _load_config("throughput_f16_prenorm.yaml")