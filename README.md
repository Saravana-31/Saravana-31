<div align="center">

<img src="assets/profile-banner.png" width="100%" alt="Saravana P | AI Engineering and Full-Stack Development. Building intelligent systems. Engineering useful products." />

<br/>

<a href="https://saravana-p.me">Portfolio</a> &nbsp;·&nbsp;
<a href="https://www.linkedin.com/in/saravana-p-kec">LinkedIn</a> &nbsp;·&nbsp;
<a href="https://github.com/saravana-31">GitHub</a> &nbsp;·&nbsp;
<a href="https://leetcode.com/u/Saravana_P/">LeetCode</a>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=22D3EE&center=true&vCenter=true&width=760&lines=AI+Engineering+%C3%97+Full-Stack+Development;Building+intelligent+systems.+Engineering+useful+products.;LLM+apps%2C+APIs+and+interfaces%2C+built+end+to+end" alt="Animated headline: AI Engineering and Full-Stack Development. Building intelligent systems. Engineering useful products." />

</div>

<br/>

## About

I build AI-powered applications end to end. In **SmartSpend AI** that is a chat assistant backed by a Flask API and Firebase. In the **Intelligence Extraction Agent** it is a FastAPI pipeline that tries rules before it asks an LLM. In **SaviAI** it is an interview-practice app wired to local models.

I'm a final-year B.Tech Artificial Intelligence and Machine Learning student at **Kongu Engineering College** (graduating 2027), based in Tamil Nadu, India.

The problems I like are the ones where a model is one part of a larger system: deciding when ordinary code is enough, what happens when the model isn't available, and how the result reaches a person through an interface they can use. I label prototypes as prototypes and credit team work as team work.

---

## Engineering focus

<div align="center">
<img src="assets/ai-engineering-visual.png" width="100%" alt="Five layers from data to models to services to storage to interface, each annotated with the projects where it appears. AI engineering covers data and models; full-stack engineering covers services, storage and interface." />
</div>

<br/>

<table>
<tr>
<td width="50%" valign="top">

**AI-powered applications and LLM integration**

Groq-hosted Llama in SmartSpend AI, Ollama behind the Intelligence Agent, local `llama.cpp` models in SaviAI. Rules come first where they are reliable, and the app degrades gracefully when no model key is configured.

</td>
<td width="50%" valign="top">

**Backend services and data workflows**

Flask, FastAPI and Express APIs. Deterministic parsing and validation (Pydantic schemas in the Intelligence Agent, bid rules in BidBank) with Firebase, MongoDB and Supabase for persistence.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Full-stack product development**

React and Next.js interfaces over those APIs: sign-in flows, dashboards, listing and bidding screens, and storefront, payment and admin screens in my Mahamitra contribution.

</td>
<td width="50%" valign="top">

**Applied machine learning**

CNN image classification (Deception Detection) and fraud detection with logistic regression, random forest and SMOTE (Credit Card Fraud Detection), kept as notebook experiments.

</td>
</tr>
</table>

---

## Featured projects

<div align="center">
<img src="assets/project-showcase.png" width="100%" alt="Priority projects in order: 1 SmartSpend AI, 2 Mahamitra, 3 SaviAI, 4 BidBank, each with status and stack." />
</div>

<sub>Screenshots below come from local runs of the public repositories (or from the project's own README) with external services not connected, so data-driven screens are empty or gated. Diagrams are labelled as diagrams.</sub>

<br/>

### 1. SmartSpend AI

**Conversational expense tracking** &nbsp;|&nbsp; Working prototype &nbsp;|&nbsp; Team project

<div align="center">
<img src="assets/smartspend-architecture.png" width="100%" alt="Architecture diagram: the React and Vite UI sends a chat message and user id to a Flask API. The API detects a transaction with regex and keyword rules and saves it to Firebase Firestore, otherwise it asks Groq. The dashboard reads Firestore directly." />
</div>

**Problem.** Logging every expense by hand is the step people skip.

**Approach.** Type a message such as an amount and what it was for. A Flask API matches amount patterns, assigns a keyword-based category (Food, Travel, Health, Investment, Other), and writes the transaction to Firestore. Messages that aren't transactions go to a Groq-hosted Llama 3.1 model.

**Also in the app.** Dashboard, budget planner, calculators, and an OCR bill scanner built on Tesseract.js.

**Current limits.** Intent detection is pattern-based, so unusual phrasing is missed. It needs your own Firebase project and Groq key, the front end calls the API at `localhost:5000`, and there are no automated tests. No live demo is linked because I haven't verified one.

`React` `Vite` `Flask` `Groq` `Firebase`

[**Repository**](https://github.com/Saravana-31/Smart-Spend) &nbsp;|&nbsp; [Earlier Next.js iteration](https://github.com/Saravana-31/Smart_Spend)

<div align="center">
<img src="assets/screenshots/smartspend-signin.png" width="55%" alt="SmartSpend AI sign-up screen with email, password and Google sign-in options." />
</div>

<sub>Sign-up screen from a local run. Every other page sits behind Firebase sign-in, so the chat and dashboard are not shown here.</sub>

<sub>**Two versions, on purpose.** [`Smart-Spend`](https://github.com/Saravana-31/Smart-Spend) is the current Vite and React app with the Flask API above. [`Smart_Spend`](https://github.com/Saravana-31/Smart_Spend) is the earlier Next.js "SmartSpend+" iteration, whose Flask endpoint returns a placeholder reply instead of calling a model. The repository history shows other contributors alongside me.</sub>

<!-- TODO (Saravana): add one line naming exactly which parts of SmartSpend AI you built, e.g. "I built the Flask API and the chat page." -->

<br/>

### 2. Mahamitra

**E-commerce platform** &nbsp;|&nbsp; **Team contribution** &nbsp;|&nbsp; Repository owned by Sanjay N at Neovate

<div align="center">
<img src="assets/screenshots/mahamitra-home.png" width="80%" alt="Mahamitra storefront home page: a pink hero banner for women's, girls' and baby clothing with shop buttons and a chat assistant button." />
</div>

<sub>Storefront home page from a local run of the public repository. Product data comes from Supabase, which wasn't connected.</sub>

**What it is.** A boutique storefront with shopping, orders, wallet top-up and favorites, plus an admin area for dashboard, inventory, coupons, orders and analytics. Payments go through Razorpay, and a shopping assistant runs on Groq behind a Supabase Edge Function.

**My part.** Feature development and testing, as credited in the project README. 15 of the repository's 90 commits are under my GitHub account; most of the rest are Sanjay N's. I don't own this codebase.

`React` `TypeScript` `Supabase` `Razorpay` `Groq`

[**Original repository**](https://github.com/sanjayn29/Mahamitra-E-commence)

<!-- TODO (Saravana): name the specific Mahamitra features you built or tested (for example a checkout, wallet or admin screen). -->

<br/>

### 3. SaviAI

**AI interview preparation** &nbsp;|&nbsp; Prototype

<div align="center">
<img src="assets/screenshots/saviai-home.png" width="70%" alt="SaviAI home page on a dark starfield background with mock interview and formal interview options." />
</div>

<sub>Home page from a local run (no database connected).</sub>

**What it does.** Aptitude practice, coding practice in several languages, and AI mock interviews with speech input, a live face-detection preview for emotion feedback, evaluation, history and reports.

**Architecture.** Next.js and TypeScript with NextAuth and MongoDB. Question generation is designed for local models (Mistral 7B and CodeLlama through `llama.cpp`).

**To run it.** Download the model files named in the repository README (roughly 4 GB each); Docker Compose files are included. Not production-ready.

`Next.js` `TypeScript` `MongoDB` `NextAuth` `llama.cpp`

[**Repository**](https://github.com/Saravana-31/Savi_AI)

<br/>

### 4. BidBank

**Online auction platform** &nbsp;|&nbsp; Full-stack prototype

<div align="center">
<img src="assets/screenshots/bidbank-auctions.png" width="70%" alt="BidBank auction listings with item photos, end dates, prices, Bid Now buttons and Sold badges." />
</div>

<sub>Auction listings, from the screenshots in the project's own README.</sub>

**What it does.** Sign-up and login with hashed passwords and MongoDB-backed sessions, item listings with images and an end date, bids the API validates (must beat the highest bid, meet the starting price and arrive before the end date), countdown timers and a bid-activity feed.

**Be precise.** Socket.IO live updates were started but are commented out, so the app does not push real-time updates. The data model has no user roles, and there is no payment code. No live demo is linked because I haven't verified one.

`React` `Express` `MongoDB` `Node.js`

[**Repository**](https://github.com/Saravana-31/online-auction-platform)

<br/>

### More projects

| Project | What it is | Stack | Status |
|:--|:--|:--|:--|
| [**Intelligence Extraction Agent**](https://github.com/Saravana-31/Autonomous-Intel-Agent) | Extracts contacts, services and certifications from offline website snapshots: rule-based parsing first, then an Ollama-served LLM to classify and normalize, plus a knowledge-graph pipeline and React view. Runs locally. | `FastAPI` `Pydantic` `Ollama` `React` | Working prototype |
| [**PM Internship Recommender**](https://github.com/Saravana-31/SIH_PMIRS) | Skill-first internship matching for Smart India Hackathon problem 25034, with learning-path suggestions when nothing matches and a Groq chat on each listing. Uses sample data. | `React` `Express` `Flask` `Groq` | Hackathon build |
| [**Udyam Registration Portal**](https://github.com/Saravana-31/Udyam_Frontend) ([backend](https://github.com/Saravana-31/Udyam_Backend)) | Two-step registration-flow clone with validation and OTP steps, backed by a TypeScript API with Jest and Supertest tests and a Dockerfile. | `React` `Express` `TypeScript` `Jest` | Self-built |
| [**Form Builder**](https://github.com/Saravana-31/Form_Builder) | MERN form editor with Categorize, Cloze and Comprehension question types, image upload and a fill-in view. | `MongoDB` `Express` `React` `Next.js` | Self-built |
| [**Deception Detection**](https://github.com/Saravana-31/Deception-Detection) | CNN classifier for facial images, with augmentation and a confusion-matrix evaluation. | `TensorFlow` `Keras` | Notebook experiment |
| [**Credit Card Fraud Detection**](https://github.com/Saravana-31/Credit-Card-Fraud-Detection) | Logistic regression and random forest on imbalanced data using SMOTE. | `Python` | Notebook experiment |
| [**Hostel Room Allocation**](https://github.com/Saravana-31/Hostel-Room-Allocation-Application) | Java application for assigning student accommodation. | `Java` | Application |

<sub>[Browse all repositories](https://github.com/saravana-31?tab=repositories)</sub>

---

## Technical toolkit

<table>
<tr><td width="150"><b>Languages</b></td><td>
<img src="https://img.shields.io/badge/Python-173A6B?style=flat-square" alt="Python" />
<img src="https://img.shields.io/badge/Java-173A6B?style=flat-square" alt="Java" />
<img src="https://img.shields.io/badge/JavaScript-173A6B?style=flat-square" alt="JavaScript" />
<img src="https://img.shields.io/badge/TypeScript-173A6B?style=flat-square" alt="TypeScript" />
<img src="https://img.shields.io/badge/C-173A6B?style=flat-square" alt="C" />
<img src="https://img.shields.io/badge/SQL-173A6B?style=flat-square" alt="SQL" />
</td></tr>
<tr><td><b>AI / ML</b></td><td>
<img src="https://img.shields.io/badge/Groq-173A6B?style=flat-square" alt="Groq" />
<img src="https://img.shields.io/badge/Ollama-173A6B?style=flat-square" alt="Ollama" />
<img src="https://img.shields.io/badge/llama.cpp-173A6B?style=flat-square" alt="llama.cpp" />
<img src="https://img.shields.io/badge/TensorFlow-173A6B?style=flat-square" alt="TensorFlow" />
<img src="https://img.shields.io/badge/Keras-173A6B?style=flat-square" alt="Keras" />
<img src="https://img.shields.io/badge/Tesseract.js-173A6B?style=flat-square" alt="Tesseract.js" />
</td></tr>
<tr><td><b>Frontend</b></td><td>
<img src="https://img.shields.io/badge/React-173A6B?style=flat-square" alt="React" />
<img src="https://img.shields.io/badge/Next.js-173A6B?style=flat-square" alt="Next.js" />
<img src="https://img.shields.io/badge/Vite-173A6B?style=flat-square" alt="Vite" />
<img src="https://img.shields.io/badge/Tailwind_CSS-173A6B?style=flat-square" alt="Tailwind CSS" />
</td></tr>
<tr><td><b>Backend</b></td><td>
<img src="https://img.shields.io/badge/Node.js-173A6B?style=flat-square" alt="Node.js" />
<img src="https://img.shields.io/badge/Express-173A6B?style=flat-square" alt="Express" />
<img src="https://img.shields.io/badge/Flask-173A6B?style=flat-square" alt="Flask" />
<img src="https://img.shields.io/badge/FastAPI-173A6B?style=flat-square" alt="FastAPI" />
<img src="https://img.shields.io/badge/Pydantic-173A6B?style=flat-square" alt="Pydantic" />
</td></tr>
<tr><td><b>Databases</b></td><td>
<img src="https://img.shields.io/badge/MongoDB-173A6B?style=flat-square" alt="MongoDB" />
<img src="https://img.shields.io/badge/Firebase-173A6B?style=flat-square" alt="Firebase" />
<img src="https://img.shields.io/badge/Supabase-173A6B?style=flat-square" alt="Supabase" />
<img src="https://img.shields.io/badge/MySQL-173A6B?style=flat-square" alt="MySQL" />
</td></tr>
<tr><td><b>Testing and tooling</b></td><td>
<img src="https://img.shields.io/badge/Jest-173A6B?style=flat-square" alt="Jest" />
<img src="https://img.shields.io/badge/Docker-173A6B?style=flat-square" alt="Docker" />
<img src="https://img.shields.io/badge/Git-173A6B?style=flat-square" alt="Git" />
</td></tr>
</table>

## Experience and education

| | Period |
|:--|:--|
| **Generative AI Internship**, Generative AI Consortium | Mar to Apr 2025 |
| **Software Development Intern**, Codtech IT Solutions | Dec 2024 to Jan 2025 |
| **B.Tech Artificial Intelligence and Machine Learning**, Kongu Engineering College | 2023 to 2027 |

<!-- TODO (Saravana): add one or two factual responsibilities for each internship; none were available to verify. -->

## Certifications

- Oracle Certified Professional: Java SE 17 Developer
- MongoDB Associate Developer
- Oracle APEX Cloud Developer
- NPTEL: Edge Computing
- NPTEL: Affective Computing

<!-- TODO (Saravana): link each certification to its public credential page when available. -->

---

## GitHub activity

<div align="center">

<a href="https://github.com/saravana-31">
  <img src="https://streak-stats.demolab.com/?user=saravana-31&hide_border=true&background=0B1220&ring=22D3EE&fire=60A5FA&currStreakNum=E6F1FF&currStreakLabel=22D3EE&sideNums=E6F1FF&sideLabels=9FB3C8&dates=6F8AA8" width="70%" alt="GitHub contribution streak" />
</a>

<br/>

<a href="https://github.com/saravana-31">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=saravana-31&show_icons=true&hide_border=true&bg_color=0B1220&title_color=22D3EE&text_color=9FB3C8&icon_color=60A5FA&ring_color=22D3EE" alt="GitHub profile statistics" />
</a>
<a href="https://github.com/saravana-31?tab=repositories">
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=saravana-31&layout=compact&langs_count=6&hide=html,jupyter%20notebook&hide_border=true&bg_color=0B1220&title_color=22D3EE&text_color=9FB3C8" alt="Most-used languages across public repositories" />
</a>

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=saravana-31&bg_color=0B1220&color=9FB3C8&line=22D3EE&point=E6F1FF&area=true&hide_border=true" width="100%" alt="GitHub contribution activity graph" />

</div>

<sub>These cards use community-run services and can be rate-limited or briefly unavailable. The language card estimates code composition across public repositories (notebooks and HTML hidden), not proficiency. GitHub's own contribution calendar is on my <a href="https://github.com/saravana-31">profile</a>.</sub>

## LeetCode

<div align="center">

<a href="https://leetcode.com/u/Saravana_P/">
  <img src="https://leetcard.jacoblin.cool/Saravana_P?theme=dark&font=JetBrains_Mono&colors=0B1220,0F2447,9FB3C8,E6F1FF,22D3EE,60A5FA,38BDF8,67E8F9" width="75%" alt="LeetCode statistics for Saravana_P" />
</a>

<br/>

<a href="https://leetcode.com/u/Saravana_P/">
  <img src="https://img.shields.io/badge/LeetCode-View%20live%20profile-0B1728?style=for-the-badge&logo=leetcode&logoColor=22D3EE" alt="View LeetCode profile" />
</a>

</div>

<sub>The card depends on a third-party service. If it fails to load, my <a href="https://leetcode.com/u/Saravana_P/">LeetCode profile</a> always shows the current numbers.</sub>

---

## Connect

<div align="center">

<a href="https://saravana-p.me">Portfolio</a> &nbsp;·&nbsp;
<a href="https://www.linkedin.com/in/saravana-p-kec">LinkedIn</a> &nbsp;·&nbsp;
<a href="https://leetcode.com/u/Saravana_P/">LeetCode</a> &nbsp;·&nbsp;
<a href="https://github.com/saravana-31">GitHub</a>

<br/><br/>

<sub>Thanks for reading. The repositories above are the best record of how I work.</sub>

</div>
