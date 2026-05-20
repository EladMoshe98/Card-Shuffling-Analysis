# Card Shuffling Analysis

Mathematical analysis of collision probability and shuffle sufficiency in the riffle shuffle — a project for the Advanced Algorithms & Combinatorics course in my CS Master's at IE Business School.

## Topics Covered

- **Riffle shuffle model** – Gilbert-Shannon-Reeds (GSR) formulation
- **Collision probability** – how likely two cards end up adjacent after k shuffles
- **Shuffle sufficiency** – the minimum number of riffle shuffles needed to achieve near-uniform randomness (the classic "7 shuffles" result)
- Theoretical derivations with empirical validation

## Structure

```
├── analysis.ipynb   # Main notebook with proofs and experiments
├── report.pdf       # Written report submitted for the course
└── utils.py         # Shuffle simulation helpers
```

## Running the Notebook

```bash
pip install numpy matplotlib jupyter
jupyter notebook analysis.ipynb
```
