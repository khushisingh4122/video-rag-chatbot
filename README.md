# 🎥 Video Intelligence Dashboard

## Overview

Video Intelligence Dashboard is a web application that compares YouTube and Instagram videos using publicly available metadata. The platform analyzes video performance based on views, likes, engagement rate, and custom scoring metrics, then generates a comparison report to help users understand which video is performing better.

The project was built to demonstrate full-stack development skills, API integration, data processing, and cloud deployment.

---

## Features

### Video Comparison

* Compare a YouTube video with an Instagram Reel
* Fetch video metadata automatically
* Display video titles, channels, duration, views, and likes

### Performance Analysis

* Calculate engagement rates
* Generate custom performance scores
* Identify the winning video
* Highlight the video with the best engagement

### Dashboard Interface

* Clean and responsive user interface
* Video thumbnails
* Performance comparison cards
* Engagement visualization

### Report Generation

* Generate an analysis summary
* Download comparison results as a report

---

## Technologies Used

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* Python
* FastAPI
* yt-dlp
* Pydantic
* Uvicorn

### Tools & Platforms

* Git
* GitHub
* Render

---

## How It Works

1. The user enters a YouTube URL and an Instagram Reel URL.
2. The frontend sends the URLs to the FastAPI backend.
3. The backend extracts metadata from both videos.
4. Engagement rates and performance scores are calculated.
5. The videos are compared.
6. Results are returned to the frontend and displayed in an easy-to-read dashboard.
7. Users can download the generated report.

---

## Project Structure

```text
video-rag-chatbot/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── video_metadata.py
│   └── other backend files
│
├── frontend/
│   ├── app/
│   ├── public/
│   ├── package.json
│   └── other frontend files
│
└── README.md
```

---

## Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

## Deployment

### Backend Deployment

The backend is deployed on Render and provides a public API endpoint for video analysis.

### Source Code

The complete source code is hosted on GitHub for version control and collaboration.

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Building REST APIs using FastAPI
* Working with React and Next.js
* API integration between frontend and backend
* Data extraction and processing
* Git and GitHub workflow
* Cloud deployment using Render
* Debugging real-world deployment issues

---

## Future Improvements

* AI-powered video recommendations
* Sentiment analysis of video content
* Video transcript processing
* Advanced analytics dashboard
* User authentication
* Historical comparison tracking

---

## Author

**Khush Singh**

Student Developer passionate about AI, software development, and research.
