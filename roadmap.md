```mermaid
flowchart LR

%% ===== CORE SPINE =====
A[Linear Regression] --> B[Logistic Regression]
B --> C[Loss and Gradients]
C --> D[Bias Variance]
D --> E[K Means]
E --> F[KNN]
F --> G[Decision Tree]
G --> H[PCA]
H --> I[Neural Network]

%% ===== GROUPED EXTENSIONS =====
I --> J[Representation Learning]
J --> K[Attention Models]
K --> L[Explainable AI]

%% ===== TRENDING MODELS (GROUPED, NOT EXPANDED) =====
J -.-> J1[Autoencoders]
J -.-> J2[Contrastive Learning]
K -.-> K1[Vision Transformer]
K -.-> K2[CLIP]
L -.-> L1[Counterfactuals]

%% ===== STYLING =====
style A fill:#1976D2,stroke:#FFFFFF,color:#FFFFFF
style B fill:#1976D2,stroke:#FFFFFF,color:#FFFFFF
style C fill:#1976D2,stroke:#FFFFFF,color:#FFFFFF
style D fill:#1976D2,stroke:#FFFFFF,color:#FFFFFF

style E fill:#2E7D32,stroke:#FFFFFF,color:#FFFFFF
style F fill:#2E7D32,stroke:#FFFFFF,color:#FFFFFF
style G fill:#2E7D32,stroke:#FFFFFF,color:#FFFFFF

style H fill:#F9A825,stroke:#FFFFFF,color:#000000
style I fill:#F9A825,stroke:#FFFFFF,color:#000000

style J fill:#7B1FA2,stroke:#FFFFFF,color:#FFFFFF
style K fill:#7B1FA2,stroke:#FFFFFF,color:#FFFFFF
style L fill:#C2185B,stroke:#FFFFFF,color:#FFFFFF
