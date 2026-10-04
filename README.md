# EU Junior Developer Job Tracker

A small data project that compares software-job demand across Spain, Germany,
the Netherlands and Belgium. It is deliberately focused on the first question a
junior candidate needs to answer: **which markets and role families have the
most visible demand right now?**

The current version queries the [Adzuna API](https://developer.adzuna.com/),
groups practical search terms into role families, and prints a country-by-role
snapshot. It is an in-progress project: the data-collection layer is built;
persistence, an API and the dashboard are the next milestones.

## What it measures

- Countries: Spain (`es`), Germany (`de`), the Netherlands (`nl`) and Belgium
  (`be`)
- Role families: frontend, backend, full-stack, UX/UI, product/design and
  general software-development searches
- Source: Adzuna job-search counts, collected through its public API

The results are directional, not a claim about the entire labour market.
Search titles differ by country and seniority is not consistently available in
the source, so the project documents those limitations rather than presenting
the counts as precise hiring figures.

## Stack

- Python for data collection
- `requests` for the API client
- FastAPI and pandas planned for the application and data layer
- SQLite planned for local snapshots
- HTML, CSS and vanilla JavaScript planned for the dashboard

## Run the current collector

1. Create an Adzuna developer account and obtain an app ID and key.
2. Create a `.env` file in the project root:

   ```env
   ADZUNA_APP_ID=your_app_id
   ADZUNA_APP_KEY=your_app_key
   ```

3. Install the project dependencies and run:

   ```bash
   python main.py
   ```

The script prints counts in the form `country | role: count`.

## Roadmap

1. Persist collection snapshots in SQLite so trends can be compared over time.
2. Expose the data through a FastAPI service.
3. Build a small, accessible dashboard with country and role comparisons.
4. Improve the search taxonomy and document its bias with real collected data.

## Why this project exists

Most public job-market trackers are US-centric. I built this to practise Python
and backend fundamentals on a question I genuinely need to answer as an EU
junior developer — while being explicit about what the data can and cannot say.
