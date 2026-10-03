# Smart Pantry

> Your Intelligent Kitchen Management System — track your inventory, discover recipes from what you already have, and never let food go to waste.

<p>
  <img src="https://img.shields.io/badge/Hackathon-AI%20Web%20Hackathon%202025-blueviolet?style=for-the-badge" alt="AI Web Hackathon 2025" />
  <img src="https://img.shields.io/badge/🏆%20Position-Runner--Up-silver?style=for-the-badge" alt="Runner-Up" />
  <img src="https://img.shields.io/badge/Event-ITEC-orange?style=for-the-badge" alt="ITEC" />
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-backend-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/HTML5-frontend-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-styling-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Google%20Sheets-database-34A853?style=flat-square&logo=googlesheets&logoColor=white" alt="Google Sheets" />
  <img src="https://img.shields.io/badge/Spoonacular-API-FF6B6B?style=flat-square" alt="Spoonacular API" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License MIT" />
</p>

---

## Table of Contents

- [About the Project](#about-the-project)
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration & Security](#configuration--security)
- [Contributing](#contributing)
- [License](#license)

---

## About the Project

**Smart Pantry** was built for the **AI Web Hackathon 2025**, held under **ITEC (Information Technology Competition and Exhibition)** — the flagship tech event of the **Department of Computer Science at the University of Engineering and Technology (UET), Lahore**.

In this **24-hour AI Web Hackathon**, Smart Pantry secured the **🥈 Runner-Up position**.

---

## Overview

Smart Pantry is a lightweight kitchen management web app that helps you stay on top of your groceries. It keeps a live record of your pantry, warns you about items that are about to expire, and recommends recipes you can cook using the ingredients you already have — cutting down food waste and taking the guesswork out of meal planning.

---

## Features

- **Inventory Management** — Add, view, and remove pantry items (name, quantity, and expiration date).
- **Expiration Tracking** — Automatically flags items as `Fresh`, `Expiring Soon` (within 3 days), or `Expired`.
- **Smart Notifications** — Surfaces items expiring within the next 3 days so nothing gets forgotten.
- **Recipe Recommendations** — Suggests recipes based on your current ingredients via the Spoonacular API.
- **Live Dashboard** — Home page with at-a-glance stats for inventory, recipes, and notifications.
- **Cloud-Backed Storage** — Uses Google Sheets as a simple, accessible data store.

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript (Fetch API) |
| **Backend** | Python, Flask, Flask-CORS |
| **Database** | Google Sheets (via `gspread` + `oauth2client`) |
| **External API** | [Spoonacular](https://spoonacular.com/food-api) (recipe recommendations) |

---

## Project Structure

```
AI_Web_Hackathon_WH0040/
├── app.py              # Flask backend (REST API + Google Sheets integration)
├── home.html           # Dashboard with live stats
├── inventory.html      # Add / view / remove pantry items
├── recipes.html        # Recipe recommendations
├── notifications.html  # Expiring-items alerts
├── styles.css          # Shared styling
└── credentials.json    # Google service account credentials (not committed)
```

---

## API Reference

The Flask backend exposes the following endpoints (base URL `http://127.0.0.1:5000`):

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/items` | Returns all pantry items. |
| `POST` | `/add-item` | Adds an item. Body: `{ "name", "quantity", "expiration_date" }`. |
| `DELETE` | `/remove-item/<name>` | Removes an item by name. |
| `GET` | `/get-recipes` | Returns recipes based on current pantry ingredients. |
| `GET` | `/expiring-items` | Returns items expiring within the next 3 days. |

---

## Getting Started

### Prerequisites

- Python 3.x
- A Google Cloud **service account** with the Google Sheets & Drive APIs enabled
- A free [Spoonacular API key](https://spoonacular.com/food-api)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Muhammad-Umair-Tech/AI_Web_Hackathon_WH0040
   cd AI_Web_Hackathon_WH0040
   ```

2. **Install dependencies**
   ```bash
   pip install flask flask-cors gspread oauth2client requests
   ```

3. **Set up Google Sheets access**
   - Create a service account in Google Cloud and download its `credentials.json`.
   - Place `credentials.json` in the project root.
   - Create a Google Sheet with the header row: `name | quantity | expiration_date`.
   - Share the sheet with the service account email, then copy the Sheet ID into the `SHEET_ID` variable in `app.py`.

4. **Add your Spoonacular API key**
   - Set the `API_KEY` variable in `app.py` to your Spoonacular key.

5. **Run the backend**
   ```bash
   python app.py
   ```
   The server starts at `http://127.0.0.1:5000`.

6. **Open the frontend**
   - Open `home.html` in your browser (or serve the files with any static server).

> **Note:** Expiration dates must be in `YYYY-MM-DD` format to be parsed correctly.

---

## Configuration & Security

- `credentials.json` and your Spoonacular `API_KEY` are secrets — **do not commit them**. Add `credentials.json` to your `.gitignore`.
- For production, prefer loading the Sheet ID, API key, and credentials path from environment variables rather than hardcoding them in `app.py`.

---

## Contributing

This project was built in a 24-hour hackathon sprint. Issues and pull requests are welcome if you'd like to extend it.

---

<p align="center">
  Built with ❤️ and determination at the <strong>AI Web Hackathon 2025</strong> · ITEC · UET Lahore
</p>
