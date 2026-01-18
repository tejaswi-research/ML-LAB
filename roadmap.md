```mermaid
flowchart LR

%% FOUNDATIONS
A[Linear Regression] --> B[Logistic Regression]
B --> C[Loss Functions and Gradients]
C --> D[Bias Variance]
D --> E[K Means]
E --> F[KNN]
F --> G[Decision Tree]
G --> H[PCA]
H --> I[Neural Network]

%% REPRESENTATION LEARNING
I --> J[Representation Learning]
J --> J1[Autoencoders]
J --> J2[Contrastive Learning]
J --> J3[Self Supervised Learning]

%% ATTENTION AND TRANSFORMERS
J --> K[Attention Mechanism]
K --> K1[Vision Transformer]
K --> K2[Swin Transformer]
K --> K3[CLIP]
K --> K4[Masked Autoencoder]

%% MULTIMODAL
K --> L[Multimodal Learning]
L --> L1[Vision and Text Models]
L --> L2[Foundation Models]

%% EXPLAINABILITY
L --> M[Explainable AI]
M --> M1[Attribution Methods]
M --> M2[Counterfactuals]
M2 --> N[Human in Loop ML]

%% STYLING
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
style L fill:
