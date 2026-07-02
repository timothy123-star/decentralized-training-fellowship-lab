# Week 1 Report

**Name:** Timothy Okolo
**Track:** AI Research - Decentralized Training
**Week:** Week 1
**Focus:** Orientation, terminology, environment setup, and initial research direction

## 1. Summary of the Week

My Week 1 focus was building a correct foundation for understanding decentralized training. I created a public research repository, configured the development environment, began building an AI and machine-learning glossary, and studied the distinctions between centralized, distributed, federated, and decentralized training.

I also examined the major failure modes identified in the fellowship material and developed an initial position that non-IID data may be the most persistent problem in permissioned cross-silo federated-learning systems.

## 2. Work Completed

- Created the public `decentralized-training-fellowship-lab` repository.
- Created a structured folder system for weekly notes, reports, research, references, experiments, and reusable code.
- Created and activated a Python virtual environment.
- Installed and verified PyTorch and Flower.
- Created a reusable environment-verification script.
- Exported installed dependencies to `requirements.txt`.
- Began an AI and machine-learning glossary.
- Documented centralized training and the distinction between distributed computation and decentralized control.
- Studied the basic meanings of AI, machine learning, deep learning, algorithms, models, training, inference, and prediction.
- Wrote a one-page memo on the failure mode I currently expect to dominate cross-silo decentralized-training systems.
- Recorded a provisional research direction connected to secure collaborative fraud-model training.

## 3. Evidence Links

### Repository

https://github.com/timothy123-star/decentralized-training-fellowship-lab

### Main evidence

- `README.md`
- `scripts/verify_environment.py`
- `requirements.txt`
- `docs/glossary/ai-ml-glossary.md`
- `docs/week-01/01-vocabulary.md`
- `docs/week-01/02-study-notes.md`
- `docs/week-01/03-failure-mode-memo.md`
- `research/research-directions.md`

## 4. Environment Verification

- Python: 3.14.5
- PyTorch: 2.12.1+cpu
- Flower: 1.32.0
- CUDA available: No
- Execution mode: CPU
- Operating system: Windows 11

PyTorch successfully performed tensor operations, and the Flower Python package and command-line interface were verified.

## 5. Key Concepts Learned

### Centralized training

One organisation controls the data, model, infrastructure, training process, and final output. The computation may use several machines while remaining centrally governed.

### Distributed training

Training computation is divided across multiple machines or processes. Distributed computation does not automatically mean decentralized control.

### Federated learning

Participants train locally using their own data and share model updates rather than transferring their raw datasets to the central coordinator.

### Cross-device federated learning

This involves a large number of personal devices that may be unreliable, resource-constrained, and temporarily available.

### Cross-silo federated learning

This involves a smaller number of relatively reliable organisations, such as banks, fintechs, or hospitals, that cannot freely share their datasets.

### Major failure modes

The main failure modes I identified are:

- Non-IID data
- Unreliable clients
- Communication cost
- Privacy leakage
- Malicious updates
- Weak evaluation

## 6. Initial Research Direction

My broad research interest is secure collaborative fraud-model training across financial institutions.

The broad question is:

> How can multiple financial institutions collaboratively train a fraud-detection model while keeping raw transaction data local and reducing the influence of malicious, unreliable, or low-quality participants?

A possible focused investigation is:

> How does non-IID financial data affect the robustness of cross-silo federated fraud-detection models when one or more participating institutions submit malicious model updates?

This direction is still provisional and requires mentor feedback before becoming my final research problem.

## 7. Blockers and Questions

My main current knowledge gap is that I am still building the machine-learning foundation required to understand model training, gradients, optimisers, and aggregation algorithms properly.

I also need guidance on:

- How deeply Week 2 expects us to understand model training before implementing FedAvg.
- Whether Flower simulations should be run on native Windows or through WSL2.
- Which model and dataset the team will use for the first simulation.
- Whether fellows should begin narrowing their final research direction now or wait until the gap-analysis stage.

## 8. Week 2 Plan

- Strengthen my understanding of model training, parameters, loss, gradients, and optimisation.
- Understand the FedAvg algorithm step by step.
- Prepare a Python 3.11 simulation environment if required.
- Run the first local training baseline.
- Implement or reproduce the first Flower federated-learning simulation.
- Document the client-server training round.
- Record the experiment settings, results, failures, and questions.
