from graphviz import Digraph

dot = Digraph(comment='ML Lab Map', format='png')
dot.attr(rankdir='TB', bgcolor='white')

# Core
dot.node('C', 'ML LAB', shape='oval', style='filled', fillcolor='#FADADD')

# Foundations
dot.node('F1', 'Linear Regression', fillcolor='#B3E5FC', style='filled')
dot.node('F2', 'Logistic Regression', fillcolor='#B3E5FC', style='filled')
dot.node('F3', 'Loss & Gradients', fillcolor='#B3E5FC', style='filled')

# Representation
dot.node('R1', 'PCA', fillcolor='#FFE082', style='filled')
dot.node('R2', 'Neural Network', fillcolor='#FFE082', style='filled')

# Attention
dot.node('A1', 'Attention', fillcolor='#CE93D8', style='filled')
dot.node('A2', 'Vision Transformer', fillcolor='#CE93D8', style='filled')

# Explainability
dot.node('E1', 'Explainable AI', fillcolor='#F48FB1', style='filled')

# Connections
dot.edges([
    ('C', 'F1'), ('C', 'F2'), ('C', 'F3'),
    ('C', 'R1'), ('C', 'R2'),
    ('R2', 'A1'), ('A1', 'A2'),
    ('A2', 'E1')
])

dot
