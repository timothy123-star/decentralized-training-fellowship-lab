# AI and Machine-Learning Foundations

## Artificial Intelligence

Artificial intelligence is the broad field of building computer systems that perform tasks commonly associated with human intelligence, such as understanding language, recognising patterns, making decisions, planning actions, and solving problems.

AI systems do not always learn from data. Some AI systems follow manually created rules.

### PayShield NG connection

PayShield NG's current risk engine uses manually assigned risk factors, weights, and thresholds. It is currently a rule-based decision system rather than a machine-learning model.

---

## Machine Learning

Machine learning is a part of artificial intelligence where a system learns patterns from data instead of being given every decision rule manually.

A machine-learning system studies examples and uses the patterns it discovers to make predictions about new data.

### PayShield NG connection

A future PayShield machine-learning model could study historical transactions labelled as legitimate or fraudulent and learn which combinations of transaction features are associated with fraud.

---

## Deep Learning

Deep learning is a type of machine learning that uses neural networks with multiple layers to learn complex patterns.

It is commonly used for language, images, audio, video, and other large or complicated forms of data.

### PayShield NG connection

PayShield NG may not need deep learning for its first fraud-detection model because its primary inputs are structured transaction records. Simpler machine-learning models may be easier to train, evaluate, and explain.

---

## Algorithm

An algorithm is an organised set of steps used to solve a problem or perform a task.

An algorithm describes the process that should be followed.

Examples include:

- Gradient descent
- FedAvg
- FedProx
- Sorting algorithms
- Fraud-risk calculation procedures

---

## Model

A model is a mathematical system that has learned patterns from data and can use those patterns to produce predictions.

The algorithm is the process used to train or operate the system. The model is the learned result produced by the training process.

### Simple analogy

- Training algorithm: the teaching method
- Training data: the study material
- Model: the student's learned understanding
- Inference: the student answering a new question

---

## Training

Training is the process of teaching a model using data.

During training, the model produces predictions, measures how wrong those predictions are, adjusts its internal parameters, and repeats the process.

A simplified training cycle is:

1. Receive input data.
2. Produce a prediction.
3. Compare the prediction with the correct answer.
4. Calculate the error.
5. Update the model.
6. Repeat.

---

## Inference

Inference is the process of using an already trained model to make predictions on new data.

Training is when the model learns. Inference is when the trained model is used.

### PayShield NG connection

During training, PayShield could use historical transactions to teach a fraud-detection model.

During inference, PayShield could send a new transaction to the trained model and receive a fraud probability or risk prediction.

---

## Prediction

A prediction is the output produced by a trained model.

Examples include:

- `Fraudulent`
- `Legitimate`
- `Fraud probability: 0.87`
- `Risk score: 78`

A model prediction does not always directly determine the final action. An application may apply policies, thresholds, human review, or trusted-contact approval after receiving the prediction.

---

## Key Distinctions

### AI versus machine learning

AI is the broad field of building systems that perform intelligent tasks. Machine learning is one method of building AI systems by learning from data.

### Machine learning versus deep learning

Machine learning includes many methods for learning from data. Deep learning is a subset that primarily uses multi-layer neural networks.

### Algorithm versus model

An algorithm is the process or set of steps. A model is the learned mathematical system produced through training.

### Training versus inference

Training teaches the model using historical data. Inference uses the trained model to make predictions about new data.
