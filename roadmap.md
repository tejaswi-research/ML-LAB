```mermaid
flowchart LR

subgraph A[Learning Dynamics]
    A1[Linear Regression]
    A2[Loss Landscape]
    A3[Bias Variance]
    A1 --> A2 --> A3
end

subgraph B[Structure Formation]
    B1[K-Means]
    B2[Decision Tree]
    B3[KNN]
    B1 --> B2 --> B3
end

subgraph C[Representation Learning]
    C1[PCA]
    C2[Neural Network]
    C3[Feature Space]
    C1 --> C2 --> C3
end

subgraph D[Attention and Transformers]
    D1[Attention Weights]
    D2[Vision Transformer]
    D3[Multimodal Fusion]
    D1 --> D2 --> D3
end

subgraph E[Explainability and Human Loop]
    E1[Explainable AI]
    E2[Counterfactuals]
    E3[Human in Loop]
    E1 --> E2 --> E3
end

A3 --> B1 --> C1 --> D1 --> E1

style A fill:#E3F2FD,stroke:#1E88E5
style B fill:#E8F5E9,stroke:#43A047
style C fill:#FFF3E0,stroke:#FB8C00
style D fill:#F3E5F5,stroke:#8E24AA
style E fill:#FCE4EC,stroke:#D81B60
