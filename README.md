# Lignin Nanoparticle Lab

![screenshot](docs/screenshot.png)

An interactive population-balance model of lignin nanoparticle (LNP) formation and breakup by
**antisolvent addition**, **dilute-H2SO4 acid precipitation** and **sonication**, with DLS-comparable
Z-average and PDI. UIC colors. One self-contained file, no server or internet needed.

**Live demo (after enabling GitHub Pages on `main` / root):** `https://<user>.github.io/lignin-nanoparticle-lab/`
**Archive DOI:** add after the Zenodo release.

## Use it
Open `index.html` in any modern browser. Pick a solvent (33 built in: 13 classical solvents/amines plus
acetate and nitrate protic ionic liquids of eight amines), set lignin and process parameters, press Replay.

## What is in the model
Sectional population balance on 56 size bins (1.5 nm to about 3 um): classical nucleation, diffusion-limited
growth, DLVO-limited aggregation, stress-based breakage, engulfment micromixing, and charge-balance titration for the
acid route. Equations and validation plan: `docs/Detailed_report_LNP_model.docx`.

## Repository layout
| Path | Contents |
|---|---|
| `index.html` | Built, self-contained viewer (what you host) |
| `src/` | `template.html` (layout, UIC theme), `model.js` (physics), `data.js` (solvents, lignin, openCOSMO-RS dG), `app.js` (interface) |
| `build.py` | Inlines `src/` into `index.html` (`python3 build.py`) |
| `model/lnp_pbm.py` | Python reference implementation |
| `tests/` | Node smoke tests (`node tests/test_model.js`) |
| `docs/` | Detailed report, 33-solvent screening outputs (JSON), screenshot |

## Important limitations
* Only five solvents (EOAN, GVL, dioxane, DMSO, [EMIM][OAc]) plus water have openCOSMO-RS dG; every other
  solvent uses a Hansen-parameter placeholder, and PIL properties marked `est` are estimated. Results for those
  are placeholders until computed dG and measured properties replace them.
* The model does not yet track temperature or solid/supercooled state of PILs that melt near room temperature.
* Outputs are screening-level and must be validated against DLS.

## Citation
See `CITATION.cff` (GitHub's "Cite this repository" button) or the Zenodo record once released.

## License
MIT, see `LICENSE`.
