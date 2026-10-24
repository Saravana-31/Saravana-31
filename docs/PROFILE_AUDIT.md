# GitHub profile audit: Saravana-31

Audit date: 24 Oct 2026. Sources: public GitHub pages and raw files, the portfolio at saravana-p.me, public search results. Items marked **not verified** could not be tested from the sandbox.

## Profile snapshot
- Name on profile: Saravana P. Links on profile: portfolio (saravana-p.me), LinkedIn (`saravana-p-kec`), LeetCode (`leetcode.com/u/saravana_p`), Instagram.
- 25 public repositories. Pinned: `eit-assignment`, `23ALR092-OGMS`, `Hostel-Room-Allocation-Application`, `Task-Manager`, `RealTimeChatApp`, `RagaAI-Catalyst` (a fork). The pins are your oldest and weakest work.
- **The profile README repository `saravana-31/saravana-31` does not exist (404).** It has to be created before anything shows on the profile.

## Featured repositories and why
| Repo | Why selected | Evidence checked |
| :-- | :-- | :-- |
| `Smart-Spend` (SmartSpend AI) | Most complete AI + full-stack project | Flask API, Groq `llama-3.1-8b-instant` call, transaction-intent extraction, Firestore writes, React 19 + Vite front end |
| `Autonomous-Intel-Agent` | Strongest AI engineering depth | FastAPI endpoints, deterministic + LLM tiers, Ollama provider, Pydantic schema, knowledge-graph builder, React UI |
| `SIH_PMIRS` | Recommender with real service code | Express server with `/recommend`, `/chat_with_card` (Groq), learning-path service, Flask fallback |
| `Savi_AI` | Substantial Next.js app | Next 16, MongoDB, NextAuth, local-LLM design in README |
| `sanjayn29/Mahamitra-E-commence` | Shows client / team work | README credits "Saravana P, Feature Development & Testing"; repo owned by Sanjay N, forked into your account |
| `Udyam_Frontend` + `Udyam_Backend` | Self-built, tested | Express + TypeScript, Jest + Supertest, Dockerfile |
| `Smart_Spend` (SmartSpend+) | Linked as the earlier iteration | Next.js 15 front end; its Flask `/api/chat` returns a **hard-coded mock reply**, so it is not featured as the main project |

Not featured: course/template repos (`skills-copilot-codespaces-vscode`, `copilot-codespaces-vscode`, `cts-handson`, `pipeline-handson`, `23ALR092`), `eit-assignment`, `Task-Manager`, `RealTimeChatApp`, and the `RagaAI-Catalyst` fork.

## Issues found
1. **Secret exposure risk:** `Udyam_Backend` has a `.env` file committed to a public repo. I did not open it. Treat any keys or database credentials in it as leaked: rotate them, then remove the file from git history.
2. **Inaccurate README:** `Smart-Spend/README.md` says FastAPI, ML categorization and CSV import. The code is Flask with rule-based categorization, and I found no CSV import in the backend (front end not fully checked). It also tells readers to `cd SmartSpendAI-main`. The repo description says "deployed on 06th June 2026" but gives no URL.
3. **Two SmartSpend repos** (`Smart_Spend`, `Smart-Spend`) split attention. Your brief links `Smart_Spend` as SmartSpend+; its `package.json` is named "Full Stack SmartSpend+ APP". Pick one canonical repo and say so in the other's description.
4. **README vs code drift:** `Autonomous-Intel-Agent` README promises a Phi-2 offline fallback, but `llm/router.py` states the fallback is disabled.
5. **Portfolio vs repository mismatch:** the portfolio describes SaviAI as facial-emotion detection with 92% resume-match accuracy; the repo README describes an interview-prep platform. The portfolio also lists 99.2% (fraud), 87% (deception), 150+ concurrent users (BidBank) and a "Competency Score Evaluator" with no matching repository or measurements in the code. **None of these figures are used in the new README.**
6. The portfolio says the Mahamitra code is not listed due to client terms, but the repository is public under `sanjayn29`.
7. Several repos have no README (`Smart_Spend`, `Saravana_P`, `Udyam_Backend`, `Hostel-Room-Allocation-Application`); `Saravana-31.github.io` holds only a CNAME and README.
8. The portfolio publishes a personal phone number and email in plain text (useful for recruiters, also for scrapers). The README deliberately omits both.
9. Domain inconsistency: the portfolio's metadata and your LeetCode page point to `saravana-p.tech`, while you link `saravana-p.me`. Confirm which is canonical.

## LeetCode
- Verified account: **https://leetcode.com/u/Saravana_P/**. The public page lists GitHub `Saravana-31`, LinkedIn `saravana-p-kec` and your portfolio, and your GitHub profile links to it.
- A search-cached copy of the page showed a global rank around 534,356 and Java as the most-used language; the cache date is unknown, so **no numbers are hard-coded**. The README uses a live card plus a link.

## Not verified
- Live demos (Mahamitra, Udyam, BidBank, portfolio sub-demos) and the LinkedIn URL: the sandbox could only reach GitHub and a few package hosts. The portfolio itself loaded and its text was read.
- Rendering of all four external stats images. Parameters were taken from each project's current documentation excerpts; the activity-graph parameters were written from memory of its documentation and not re-checked.
- Experience entries (two internships) and certifications come only from your own portfolio. Certifications are left commented out in the README until you have credential links.

## Manual steps
1. Create a **public** repository named exactly `saravana-31/saravana-31`, push this folder's contents to `main`.
2. Rotate and remove the `.env` from `Udyam_Backend`.
3. Re-pin: Smart-Spend, Autonomous-Intel-Agent, SIH_PMIRS, Savi_AI, Udyam_Frontend, online-auction-platform.
4. Fix the `Smart-Spend` README so it matches the code, and add a screenshot.
5. Confirm project status labels and your contribution to each team project (SIH, SaviAI) and edit the README text if needed.
6. Optional: self-host `github-readme-stats` on your own Vercel account if the public cards rate-limit.

---

# Update 3: minimal README

- README cut from 322 lines / 17 KB / 43 images / 12 sections to 93 lines / 5 KB / 7 images / 7 sections.
- Removed: `README-test.md`, `README-test2.md`, `README_ASSET_NOTES.md`, and four illustrations that repeated the text (`ai-engineering-visual`, `project-showcase`, `smartspend-architecture`, plus unused screenshots). Git history keeps all of them.
- Removed widgets: typing headline, GitHub stats card, top-languages card, activity graph, 30 shields.io badges (stack is now plain text). Kept: contribution streak and LeetCode card, both unchanged from the previous version and untested from this environment.
- Banner re-rendered with the wording "AI Engineering × Full-Stack Development / Building intelligent systems into useful products."
- GIF: only `assets/saviai-demo.gif` (6.4 s, 588 KB), a real recording of SaviAI's landing-page carousel from a local run. SmartSpend, Mahamitra and BidBank workflows need Firebase, Supabase or MongoDB, which could not be reached, so they use genuine static screenshots.
- SaviAI's guest mode only reaches the landing-style /welcome page; mock interview, aptitude and coding redirect back to sign-in, so no deeper workflow could be recorded.
