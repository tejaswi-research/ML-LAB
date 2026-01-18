```mermaid
flowchart LR

%% ===== Main flow =====
A[Learning Dynamics] --> B[Structure Formation]
B --> C[Representation Learning]
C --> D[Attention & Transformers]
D --> E[Explainability & Human Loop]

%% ===== Details =====
A --> A1[Linear Regression]
A --> A2[Loss Landscape]

B --> B1[K-Means]
B --> B2[Decision Tree]

C --> C1[PCA]
C --> C2[Neural Network]

D --> D1[Attention]
D --> D2[Vision Transformer]

E --> E1[XAI]
E --> E2[Counterfactuals]

%% ===== Styling (IMPORTANT) =====
style A fill:#1976D2,stroke:#FFFFFF,color:#FFFFFF
style B fill:#2E7D32,stroke:#FFFFFF,color:#FFFFFF
style C fill:#F9A825,stroke:#FFFFFF,color:#000000
style D fill:#7B1FA2,stroke:#FFFFFF,color:#FFFFFF
style E fill:#C2185B,stroke:#FFFFFF,color:#FFFFFF

style A1 fill:#1E1E1E,stroke:#90CAF9,color:#FFFFFF
style A2 fill:#1E1E1E,stroke:#90CAF9,color:#FFFFFF

style B1 fill:#1E1E1E,stroke:#A5D6A7,color:#FFFFFF
style B2 fill:#1E1E1E,stroke:#A5D6A7,color:#FFFFFF

style C1 fill:#1E1E1E,stroke:#FFE082,color:#FFFFFF
style C2 fill:#1E1E1E,stroke:#FFE082,color:#FFFFFF

style D1 fill:#1E1E1E,stroke:#CE93D8,color:#FFFFFF
style D2 fill:#1E1E1E,stroke:#CE93D8,color:#FFFFFF

style E1 fill:#1E1E1E,stroke:#F48FB1,color:#FFFFFF
style E2 fill:#1E1E1E,stroke:#F48FB1,color:#FFFFFF

%% ===== Make the main path brighter =====
linkStyle 0 stroke:#FFFFFF,stroke-width:2px
linkStyle 1 stroke:#FFFFFF,stroke-width:2px
linkStyle 2 stroke:#FFFFFF,stroke-width:2px
linkStyle 3 stroke:#FFFFFF,stroke-width:2px
