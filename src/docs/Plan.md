# 🗺️ Job-Hunt-Command-Center: Execution Roadmap

## Phase 1: The Foundation (Infrastructure)
* [ ] **Project Scaffolding**: Create a monorepo with `/backend` (FastAPI), `/frontend` (React/Next.js), and `/scrapers` (Playwright).
* [ ] **Docker Orchestration**: Write a `docker-compose.yml` to spin up a PostgreSQL instance and a Redis instance for background tasks.
* [ ] **Database Schema**: Define the `jobs` table. Ensure columns exist for:
    * `ID` (Primary Key)
    * `Job Title`, `Company`, `Description` (Text)
    * `Link` (Unique Index - to prevent duplicates)
    * `Tech Stack` (Array/JSONB for chips)
    * `Job Type` (Remote/Office/Hybrid)
    * `Status` (Enum: New, Applied, Rejected, etc.)
    * `Created_at` (Timestamp)

## Phase 2: The Engine (Backend & Scraper)
* [ ] **The Tech-Tag Extractor**: Build a utility function that scans text against a "Keyword Dictionary" (React, FastAPI, etc.) to generate tech chips.
* [ ] **The Playwright Scraper**: Build a script that navigates Google Jobs. 
    * Instruct it to pull the Title, Company, and Link.
    * Instruct it to click each job to extract the full Description.
* [ ] **API Development (FastAPI)**:
    * Build a `POST /sync` endpoint to trigger the scraper.
    * Build a `GET /jobs` endpoint with query parameters for searching (Title, Tech, Type).
    * Build a `PATCH /jobs/{id}` endpoint to update the status (the "Action Area").
* [ ] **The Purge Logic**: Implement a background function that deletes jobs with `status="new"` if they were created more than 10 days ago.

## Phase 3: The Cockpit (Frontend UI)
* [ ] **The Data Table**: Implement a high-density table (using TanStack Table or similar).
    * Connect the `ID`, `Title`, and `Description` columns.
    * Render the `Tech Stack` array as colorful UI Chips.
* [ ] **The Action Column**: Create a Dropdown/Select component in each row.
    * Connect it to the `PATCH` API so changing the status updates the DB instantly.
* [ ] **Search & Filtering**: 
    * Add a Global Search Bar to filter the table by Title or Tech keywords.
    * Add "Toggle" filters for Job Type (Remote vs. In-Office).
* [ ] **Visual Feedback**: Add "Success" toasts when a job status is updated to "Applied."

## Phase 4: Automation (Set & Forget)
* [ ] **Background Worker**: Connect the scraper to a task queue (like ARQ or Celery) so the UI doesn't freeze during a sync.
* [ ] **The Mac Scheduler (Cron)**: Set up a system cron job on your MacBook to hit the `/sync` API every morning at 08:00 AM.
* [ ] **Final Polish**: Configure Docker to "Auto-Restart," ensuring the backend is always running when you open your laptop.
