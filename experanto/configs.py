from pathlib import Path
from omegaconf import OmegaConf

_CURRENT_DIR = Path(__file__).parent


def _load_config(filename: str):
    """
    1. Installed Mode: 'experanto/resources/<filename>' (renamed to avoid collision)
    2. Dev Mode:       '../configs/<filename>' (sibling to experanto source)
    """
    installed_path = _CURRENT_DIR / "resources" / filename
    dev_path = _CURRENT_DIR.parent / "configs" / filename
    if installed_path.exists():
        return OmegaConf.load(installed_path)
    elif dev_path.exists():
        return OmegaConf.load(dev_path)
    else:
        # Debugging aid: print paths if not found
        raise FileNotFoundError(
            f"Config '{filename}' not found.\n"
            f"Checked installed path: {installed_path}\n"
            f"Checked dev path: {dev_path}"
        )

DEFAULT_CONFIG = _load_config("default.yaml")
DEFAULT_DATASET_CONFIG = DEFAULT_CONFIG.dataset
DEFAULT_MODALITY_CONFIG = DEFAULT_CONFIG.dataset.modality_config
DEFAULT_DATALOADER_CONFIG = DEFAULT_CONFIG.dataloader

BENCHMARKING_CONFIG = _load_config("throughput_f16_prenorm.yaml")