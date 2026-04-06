# Job Search Scraper Sources

A curated list of job boards to be integrated into the Personal Job CRM. Initial focus is on **Google Jobs** as the primary aggregator.

## 🚀 Phase 1: Primary Aggregator
* **Google Jobs**: Acts as a meta-search engine pulling from LinkedIn, Indeed, and various company career pages. Most stable for initial scraping.

---

## 🛠 Phase 2: Tech & Startup Niche (High Signal)
* **[Wellfound](https://wellfound.com/) (formerly AngelList)**: Best for startups. Highly structured data, usually very developer-friendly.
* **[Y Combinator / Work at a Startup](https://www.workatastartup.com/)**: High-quality roles from YC-backed companies.
* **[HackerNews (Who is Hiring)](https://news.ycombinator.com/submitted?id=whoishiring)**: Posted on the 1st of every month. A goldmine for "no-bullshit" remote roles.
* **[Ottotto](https://ottotto.io/)**: Specifically designed for tech roles with great metadata for scrapers.

## 🌍 Phase 3: Remote-First Boards
* **[We Work Remotely](https://weworkremotely.com/)**: The oldest and most reliable remote board.
* **[RemoteOK](https://remoteok.com/)**: Modern tech roles; often provides an API or highly scannable HTML.
* **[Himalayas](https://himalayas.app/)**: Excellent for filtering by timezone and country restrictions (e.g., Remote but must be in India).
* **[Working Nomads](https://www.workingnomads.com/jobs)**: Curated lists for digital nomads.

## 🇮🇳 Phase 4: India-Specific Tech
* **[Instahyre](https://www.instahyre.com/)**: High-quality product-based companies in India.
* **[Cuvette](https://cuvette.tech/)**: Great for early-to-mid career developers in the Indian ecosystem.
* **[Naukri](https://www.naukri.com/)**: High volume; requires strong filtering (e.g., "Product Based only") to avoid spam.

## 🏗 Phase 5: Specialized Engineering
* **[Dice](https://www.dice.com/)**: Purely technology-focused.
* **[Gun.io](https://www.gun.io/)**: Vetted engineering roles, great for high-end full-time and freelance work.
* **[Turing](https://www.turing.com/)**: Large-scale global remote hiring platform.

---

## 📋 Scraper Implementation Notes
- **Strategy**: Use Playwright for dynamic content (LinkedIn/Wellfound) and simple Requests/BeautifulSoup for static boards (HackerNews).
- **Target Frequency**: Every morning at 08:00 IST.
- **Deduplication Logic**: Use a hash of `(company_name + job_title)` in Postgres to prevent duplicate entries from different sources.