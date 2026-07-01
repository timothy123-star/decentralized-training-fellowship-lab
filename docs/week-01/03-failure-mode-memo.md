# Which Failure Mode Will Dominate Real-World Decentralized AI Systems?

My current position is that non-IID data will be one of the most persistent failure modes in real-world decentralized AI systems, particularly in cross-silo federated-learning environments.

Non-IID data means that the data held by different participants does not follow the same distribution. This is likely to happen naturally because participants serve different users, operate in different regions, and collect data under different conditions. Even when every participant is honest, their local models may learn very different patterns. When those model updates are aggregated, the global model may converge slowly, become unstable, or perform well for some participants while performing poorly for others.

A financial-services example makes this problem clear. One fintech may mainly process small student transfers, another may serve merchants, while another handles high-value business transactions. The transaction amounts, customer behaviour, fraud patterns, and class balance across these institutions will be different. A global fraud-detection model created by averaging their updates may fail to represent all the institutions fairly. It may produce more false positives for one fintech and more false negatives for another.

I believe non-IID data is especially important because it exists even without attackers, network failures, or dishonest participants. Communication systems can be improved, and unreliable clients can sometimes be excluded or retried, but natural differences between participants’ data cannot simply be removed without changing the problem itself.

The strongest counterargument is that malicious updates may dominate open and permissionless decentralized-training networks. If unknown participants can join cheaply, create multiple identities, and submit manipulated updates, model poisoning or Sybil attacks may become more dangerous than data heterogeneity. In very large cross-device systems, communication cost and client dropout may also become the main limitations.

Therefore, my conclusion depends on the architecture. In permissioned cross-silo systems involving institutions such as banks or hospitals, I expect non-IID data to be the most persistent problem. In open permissionless networks, malicious participation may become the dominant failure mode instead.
