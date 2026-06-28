"""Verify the local fellowship development environment."""

import platform
import sys


def main() -> None:
    """Print the versions and capabilities required by the fellowship."""
    print("=== Flow Fellowship Environment Check ===")
    print(f"Operating system: {platform.platform()}")
    print(f"Python: {sys.version.split()[0]}")

    try:
        import torch

        print(f"PyTorch: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"Tensor test:\n{torch.rand(2, 3)}")
    except ImportError as error:
        print(f"PyTorch check failed: {error}")

    try:
        import flwr

        print(f"Flower: {flwr.__version__}")
    except ImportError as error:
        print(f"Flower check failed: {error}")


if __name__ == "__main__":
    main()