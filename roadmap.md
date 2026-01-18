```mermaid
flowchart LR

%% =========================
%% BASIC FOUNDATIONS
%% =========================
subgraph A[Optimization and Learning]
    A1[Linear Regression] --> A2[Logistic Regression]
    A2 --> A3[Loss and Gradients]
    A3 --> A4[Bias Variance]
end

subgraph B[Classical Machine Learning]
    B1[K Means] --> B2[KNN]
    B2 --> B3[Decision Tree]
end

subgraph C[Feature and Representation]
    C1[PCA] --> C2[Neural Network]
end

A4 --> B1
B3 --> C1

%% =========================
%% MODERN LEARNING
%% =========================
C2 --> D[Representation Learning]
D --> E[Attention Models]
E --> F[Explainable AI]

%% =========================
%% TRENDING MODELS (HINTED)
%% =========================
D -.-> D1[Autoencoders]
D -.-> D2[Contrastive Learning]

E -.-> E1[Vision Transformer]
E -.-> E2[CLIP]

F -.-> F1[Counterfactuals]

%% =========================
%% STYLING
%% =========================
style A fill:#1E88E5,stroke:#FFFFFF,color:#FFFFFF
style B fill:#2E7D32,stroke:#FFFFFF,color:#FFFFFF
style C fill:#F9A825,stroke:#FFFFFF,color:#000000

style D fill:#7B1FA2,stroke:#FFFFFF,color:#FFFFFF
style E fill:#8E24AA,stroke:#FFFFFF,color:#FFFFFF
style F fill:#C2185B,stroke:#FFFFFF,color:#FFFFFF
