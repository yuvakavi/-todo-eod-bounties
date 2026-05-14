# PULSE — Todo-Eod-Bouties

## Overview

PULSE is an AI-powered workflow automation platform designed to automate daily engineering and intern productivity workflows inside organizations.

The system manages:

- Daily TODO workflows
- End Of Day (EOD) reporting
- AI-based blocker analysis
- Escalation management
- Reward/Bounty automation
- Weekly productivity aggregation
- Scheduler-based automation

PULSE integrates FastAPI, PostgreSQL/Supabase, AI processing, and Slack-style notification workflows into a unified automation platform.

---

## Features

### 1. Todo Workflow
- Create daily tasks
- Assign priorities
- Track completion status
- Store task data in database

### 2. EOD Workflow
- Employees submit daily work reports
- Store completed work and blockers
- Centralized reporting workflow

### 3. AI-Based Blocker Extraction
- AI analyzes blocker statements
- Detects blocker severity
- Identifies escalation owner
- Categorizes blocker types

### 4. Escalation System
- Automatically escalates high-severity blockers
- Generates escalation alerts
- Supports workflow monitoring

### 5. Reward / Bounty System
- Automatically awards points for completed workflows
- Tracks employee productivity rewards
- Supports gamification architecture

### 6. Weekly Aggregation & Reporting
- Generates weekly productivity summaries
- Calculates:
  - Completed tasks
  - Total EOD submissions
  - Reward points

### 7. Scheduler Automation
- Automated daily TODO scheduling
- Automated EOD reminders
- Weekly reporting automation

### 8. AI Integration
- Uses Ollama + Llama3
- Generates intelligent TODO suggestions
- Supports local AI execution

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend API | FastAPI |
| Database | PostgreSQL / Supabase |
| ORM | SQLAlchemy |
| AI Engine | Ollama + Llama3 |
| Scheduler | APScheduler |
| API Docs | Swagger UI |
| Language | Python |

---

## Project Architecture

```
User
  ↓
FastAPI APIs
  ↓
Workflow Services
  ↓
AI Extraction Engine
  ↓
Escalation System
  ↓
Reward System
  ↓
Weekly Aggregation
  ↓
Scheduler Automation
  ↓
Slack / Notification Layer
```

---

## Folder Structure

```
pulse/
├── app/
│   ├── ai_router/
│   ├── models/
│   ├── routes/
│   ├── scheduler/
│   ├── services/
│   ├── slackbot/
│   ├── tools/
│   ├── utils/
│   ├── mock_data/
│   ├── config.py
│   ├── database.py
│   └── main.py
├── requirements.txt
├── run.py
├── README.md
├── .gitignore
└── .env
```

---

## API Modules

### Todo APIs
- Create Todo
- Update Todo
- Fetch Todos

### EOD APIs
- Submit EOD
- Fetch EOD reports

### Slack APIs
- Slack integration status

### AI Router APIs
- AI module status

---

## Database Tables

- users
- todos
- eod_reports
- bounties
- blockers

---

## Scheduler Jobs

| Job | Purpose |
|------|---------|
| Morning TODO Job | Sends daily tasks |
| EOD Reminder | Sends EOD reminder |
| Weekly Summary | Generates productivity report |

---

## AI Workflow Example

```
Employee submits EOD
  ↓
AI extracts blocker
  ↓
Severity analysis
  ↓
Escalation triggered
  ↓
Reward points issued
  ↓
Weekly analytics updated
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```
DATABASE_URL=your_database_url
SLACK_BOT_TOKEN=your_slack_token
```

### 6. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

### 7. Open Swagger Docs

Navigate to: `http://127.0.0.1:8000/docs`

### 8. Running Scheduler

```bash
python -m app.scheduler.scheduler
```

---

## Getting Started

1. Ensure all dependencies are installed
2. Configure your environment variables in `.env`
3. Start the FastAPI server
4. Access the API documentation at the Swagger UI
5. Begin automating your workflows!

---

## License

[Add your license information here]

---

## Support

For issues or questions, please open an issue on the repository.
