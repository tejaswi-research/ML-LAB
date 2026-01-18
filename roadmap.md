```mermaid
flowchart LR

A[Learning<br/>Dynamics] --> B[Structure<br/>Formation]
B --> C[Representation<br/>Learning]
C --> D[Attention &<br/>Transformers]
D --> E[Explainability &<br/>Human Loop]

subgraph A1[ ]
    A11[Linear Regression]
    A12[Loss Landscape]
end

subgraph B1[ ]
    B11[K-Means]
    B12[Decision Tree]
end

subgraph C1[ ]
    C11[PCA]
    C12[Neural Network]
end

subgraph D1[ ]
    D11[Attention]
    D12[Vision Transformer]
end

subgraph E1[ ]
    E11[XAI]
    E12[Counterfactuals]
end

A --> A11
A --> A12
B --> B11
B --> B12
C --> C11
C --> C12
D --> D11
D --> D12
E --> E11
E --> E12

style A fill:#E3F2FD,stroke:#1E88E5
style B fill:#E8F5E9,stroke:#43A047
style C fill:#FFF3E0,stroke:#FB8C00
style D fill:#F3E5F5,stroke:#8E24AA
style E fill:#FCE4EC,stroke:#D81B60
