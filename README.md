# Numerical modelling of heat and mass transfer with phase change using a sharp-interface two-fluid method

Talk at **Dispersed Two-Phase Flows (DTPF) 2026**, Société Hydrotechnique de France, EDF Lab Chatou -
session 4, Tuesday 24 November 2026, 10:20.

Louis Libat, Vincent Le Chenadec, Can Selçuk, Eric Chénier - MSME, Univ Gustave Eiffel, CNRS.

- Slides (reveal.js): https://fastaxx.github.io/dtpf-2026/
- PDF: https://fastaxx.github.io/dtpf-2026/S4.02_Libat_SharpInterfaceTwoFluid.pdf
- Offline copy (HTML + MathJax, unzip and open the `.html`): https://fastaxx.github.io/dtpf-2026/S4.02_Libat_SharpInterfaceTwoFluid.zip

## Build

`index.qmd` is a Quarto reveal.js deck (Quarto 1.6). `quarto render index.qmd` writes `index.html`, with
figures, videos and fonts embedded; MathJax is loaded from `theme/mathjax/`, which must stay next to the HTML.
The workflow in `.github/workflows/publish.yml` renders the deck, the PDF and the offline package on every
push to `main` and publishes them on GitHub Pages.

Photo credits: `figures/web/CREDITS.md`.
