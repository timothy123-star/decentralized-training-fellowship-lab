## Environment Setup

### Development environment

- Operating system: Windows 11 Pro
- Python version: 3.14.5
- pip version: 26.1.2
- PyTorch version: 2.12.1+cpu
- Flower version: 1.32.0
- CUDA available: No
- Execution device: CPU
- Virtual environment: `fellowship-env`

### Verification performed

I verified the environment using both direct terminal commands and a reusable Python verification script.

The following checks succeeded:

- Git is installed and available from the terminal.
- Python and pip are running from the project virtual environment.
- PyTorch imports successfully.
- PyTorch can create and perform operations on tensors.
- Flower imports successfully.
- The Flower command-line interface is available.
- The installed dependency versions have been exported to `requirements.txt`.

### CUDA result

`torch.cuda.is_available()` returned `False`.

This project currently uses CPU-based PyTorch. The early fellowship exercises involve small controlled experiments, so CPU execution is sufficient for the initial learning and simulation work.

### Compatibility note

The current environment uses Python 3.14 and successfully runs the core PyTorch and Flower packages. Before beginning Flower’s simulation-based exercises, I will prepare a Python 3.11 simulation environment to reduce compatibility risks involving Flower’s Ray-based simulation runtime.

### Reproducing the check

Run:

```powershell
python scripts/verify_environment.py
```

### Problems encountered

I initially ran:

```powershell
pytorch --version
```

PowerShell reported that `pytorch` was not a recognised command. PyTorch is a Python package imported using the module name `torch`, not a standalone `pytorch` command.

The correct version check is:

```powershell
python -c "import torch; print(torch.__version__)"
```

## Verification Result

Python, PyTorch, torchvision, and Flower were successfully installed and imported.

## Problems Encountered

## Resource Title

### Source

Add the title and public link.

### What I understood

Explain the main ideas in your own words.

### What confused me

List the concepts you still do not understand.

### Why it matters

Explain how it relates to decentralized training.

### PayShield connection

Explain whether it could affect collaborative fintech fraud detection.

### Questions for the meeting

Write specific questions to raise with the mentor or group.
