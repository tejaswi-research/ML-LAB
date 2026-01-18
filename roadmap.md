```mermaid
flowchart TD

A[Raw Data] --> B[Linear Regression<br>Line moves each epoch]
B --> C[Loss Landscape<br>Learning rate effects]
C --> D[Bias Variance Tradeoff<br>Underfit vs Overfit]

D --> E[K Means Clustering<br>Centroids move]
E --> F[Decision Tree<br>Splits grow step by step]
F --> G[KNN<br>Neighbourhood influence]

G --> H[Representation Learning<br>Features transform]
H --> I[Neural Network<br>Hidden representation]
I --> J[PCA<br>Data compression]

J --> K[Attention Mechanism<br>Weight flow]
K --> L[Vision Transformer<br>Patches to Attention]
L --> M[Multimodal Fusion<br>Vision and Text]

M --> N[Explainable AI<br>Why this decision]
N --> O[Counterfactuals<br>What if input changed]

O --> P[Human in the loop ML<br>User feedback]
P --> Q[Interactive Learning System<br>Model adapts with user]
