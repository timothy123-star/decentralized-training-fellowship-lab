# Week 1 Vocabulary

## Centralized Training

### My explanation

Centralized training is a machine-learning setup in which one organisation controls the data, model, computing infrastructure, training process, and final output. Training data is collected or moved into a centrally controlled environment where the model is trained and evaluated.

Centralized training does not necessarily mean that only one computer is used. The training workload may run across many GPUs or servers, but the system remains centralized when those resources are controlled by one organisation.

### Real-world example

A fintech company collects transaction records from its customers and stores them in its central infrastructure. It uses those records to train a fraud-detection model on its own servers or cloud environment.

Another example would be PayShield NG receiving permitted transaction datasets from several fintech partners, storing them centrally, and training one shared fraud-detection model.

### What stays centralized?

- Raw training data
- Model parameters
- Training code
- Computing infrastructure
- Evaluation process
- Access control
- Deployment decisions

### What may be distributed?

The computation may be distributed across several GPUs, machines, or cloud servers. However, this does not make the system decentralized when one organisation still owns and controls the entire training environment.

### Main advantages

- Easier system coordination
- Faster communication between training machines
- Easier debugging and monitoring
- Direct access to the complete dataset
- More straightforward model evaluation
- Fewer untrusted external participants
- Greater control over the training environment

### Main limitations

- Raw data must usually be moved into the central environment
- Creates privacy and regulatory concerns
- Produces a single point of control
- Produces a possible single point of failure
- Requires significant central computing resources
- Participating organisations may lose control over how their data is used

### PayShield NG connection

Centralized training could be useful during an early PayShield NG machine-learning pilot, especially if one partner provides a permitted and properly protected dataset.

However, it becomes difficult when multiple banks or fintech companies want to collaborate but cannot transfer their raw customer transaction records to PayShield. This limitation motivates the exploration of cross-silo federated learning.

### Key takeaway

Distributed computation is not automatically decentralized training. A system can use many machines while remaining centralized if one organisation controls the data, infrastructure, model, and training process.

## Distributed Data Parallel Training

### My explanation

### Example

### How it differs from decentralization

## Federated Learning

### My explanation

### Example

### What is shared

### What remains local

## Cross-Device Federated Learning

## Cross-Silo Federated Learning

## Split Learning

## Swarm Learning

## Volunteer Computing

## Decentralized Compute Markets
