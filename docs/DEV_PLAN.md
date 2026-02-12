# Development Plan & Roadmap

## Vision: "Lab in a Box"
A self-contained, offline-capable personal trainer for STEM. The goal is to have a portable environment that generates infinite practice problems, tracks progress, and allows for digital handwriting/notes.

## Technical Architecture
- **Frontend**: Streamlit (Dashboard, Analytics, Scratchpad)
- **Backend Logic**: Python `src/core`
- **Data Storage**: Local CSV (`data/dashboard.csv`) and Images (`data/notes/`)
- **Math Engine**: `sympy` (Symbolic Comp) and `numpy` (Linear Algebra)

## Future Scalability Architecture
- **Core Engine (Python)**: The `generator.py` and logic will remain pure Python (no UI dependencies) so it can be wrapped in an API (FastAPI) later.
- **Desktop (Mac/Windows)**: Currently running via local Python. Future: Package as an executable (PyInstaller) or Electron app.
- **Web/Mobile**: The core logic can be exposed via a REST API, allowing a React/React Native frontend to consume problems and submit answers.
- **New Modules**: The modular structure (`src/core/modules/`) allows plugins like "Chemistry" or "Biology" to be added without rewriting the platform.

## Modules
1.  **Math Foundations**: The core engine.
2.  **Physics**: Simulation & Dynamics.
3.  **Engineering**: Signals & Control.
4.  **Machine Learning**: Algorithms from scratch.
5.  **Pure Math**: Logic & Theory.
6.  **Financial**: Quant modeling.
7.  **Future Modules**: Chemistry, Biology, etc.

## Roadmap

### Phase 1: Foundation (Current)
- [x] Project Structure Refactor
- [x] Logging & Error Handling
- [x] Dashboard UI (Streamlit - Rapid Prototyping)
- [x] Handwriting Support

### Phase 2: The Engine (Next)
- [ ] Build `src/core/generator.py` (Platform Agnostic)
- [ ] Implement Calculus problems
- [ ] Implement Linear Algebra problems
- [ ] Add "Practice" tab to Dashboard

### Phase 3: Expansion & Intelligence
- [ ] API Layer (FastAPI) to decouple UI from Logic.
- [ ] "Smart" difficulty adjustment.
- [ ] Automated checking of handwritten answers.

