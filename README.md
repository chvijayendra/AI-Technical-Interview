# AI Technical Interviewer

**An AI-powered platform designed to simulate structured, professional technical interviews.**

The AI Technical Interviewer aims to recreate the experience of a real technical interview through structured questioning, adaptive follow-ups, coding assessments, and evidence-based evaluation.

The long-term vision is a professional, video-call-style interview environment where candidates interact with an AI interviewer through voice and video, discuss their projects, solve coding problems, and receive a structured assessment of their demonstrated technical abilities.

> **Project Status:** Early-stage prototype. The current implementation supports terminal-based text interviews through the Groq API. Real-time voice, video, automated code execution, and the graphical interview room are planned capabilities.

---

## Overview

Unlike a general-purpose coding assistant, this project is designed to keep the AI focused on the role of a professional technical interviewer.

The interviewer should assess how a candidate approaches a problem, explains technical decisions, handles edge cases, analyzes complexity, and responds to follow-up questions. It should not automatically reveal complete solutions or reward candidates for work supplied by the AI.

The project is being developed incrementally, starting with the core interview workflow before introducing real-time communication and a dedicated frontend.

## Product Vision

- **Professional AI Interviewer** — Maintains a formal, focused, and structured interview environment.
- **Structured Interview Workflow** — Progresses through introductions, project discussions, coding questions, technical follow-ups, and final evaluation.
- **Adaptive Questioning** — Generates relevant follow-up questions based on the candidate's responses and demonstrated understanding.
- **Problem-Solving Assessment** — Evaluates algorithmic reasoning, correctness, time and space complexity, and edge-case handling.
- **Assistance Awareness** — Distinguishes independent solutions from work completed with hints or substantial guidance.
- **Project-Based Interviews** — Explores project architecture, technology choices, implementation details, and individual contributions.
- **Coding Assessment** — Plans to integrate code execution and test cases to verify correctness independently of the language model's judgment.
- **Evidence-Based Evaluation** — Produces structured feedback based on observed performance rather than unsupported scores or hiring claims.
- **Real-Time Interview Room** — A planned video-call-style interface with voice interaction, interview controls, and an integrated coding workspace.

## Planned Interview Workflow

| Stage | Description |
|---|---|
| 1. Introduction | Welcome the candidate and establish the interview context. |
| 2. Project Discussion | Explore relevant projects, technical decisions, architecture, and personal contributions. |
| 3. Problem Solving | Present a coding problem and ask the candidate to explain their approach. |
| 4. Implementation | Assess the candidate's code, reasoning, complexity, and handling of edge cases. |
| 5. Technical Follow-Ups | Probe deeper into the candidate's understanding and design decisions. |
| 6. Evaluation | Summarize demonstrated strengths, weaknesses, and areas for improvement. |

The intended assessment process accounts for assistance provided during the interview and avoids treating AI-generated solutions as evidence of independent candidate ability.

## Current Implementation

The initial prototype establishes the basic AI interaction and interview behavior.

- Python-based terminal interface.
- Groq API integration using the Groq Python SDK.
- Environment-based API configuration using `python-dotenv`.
- Multi-turn text conversation with conversation history.
- System instructions defining the interviewer's role and expected behavior.
- Experimental interview-stage progression.
- Basic API error handling and session termination.

The current stage-management logic is experimental and requires further testing for consistent behavior.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Groq API | Access to the language model |
| Groq Python SDK | API communication |
| `python-dotenv` | Environment configuration |
| Git and GitHub | Version control and source hosting |

Additional technologies will be introduced as the project evolves to support a backend API, real-time audio/video communication, isolated code execution, and a frontend interface.

## Getting Started

### Prerequisites

- Python installed on your system.
- A Groq API key.
- Git installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/chvijayendra/AI-Technical-Interview.git
cd AI-Technical-Interview
```

### 2. Create a Virtual Environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, allow activation scripts for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install groq python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Replace the placeholder with your own API key. Ensure the selected model is available to your Groq account.

**Security:** Never commit your `.env` file or expose your API key in a public repository.

### 5. Run the Prototype

```bash
python test_groq.py
```

The program starts a terminal-based interview session. Enter your responses when prompted and type `exit` to end the session.

## Design Principles

- **Interview, Not Tutoring:** Prioritize evaluating candidate reasoning over supplying complete solutions.
- **Structured Progression:** Keep the interview focused and follow defined stages.
- **Evidence Over Assumptions:** Base assessments on observed responses and verified code results where available.
- **Consistent Evaluation:** Account for hints, assistance, and the source of the candidate's solution.
- **Professional Interaction:** Maintain a neutral, respectful, and focused interview environment.
- **Responsible Assessment:** Protect candidate information and avoid unsupported conclusions about competence or personality.

## Roadmap

- [x] Initial Python terminal prototype
- [x] Groq API integration
- [x] Multi-turn text conversation
- [x] Initial interviewer instructions and experimental stage management
- [ ] More reliable interview-state management
- [ ] Structured assessment criteria and evaluation reports
- [ ] Automated code execution and test-case validation
- [ ] Résumé and project-context integration
- [ ] Backend API
- [ ] Professional frontend and coding workspace
- [ ] Real-time voice interaction
- [ ] Video-call-style interview experience

## Privacy and Responsible Use

The planned platform may process candidate speech, video, project information, and interview responses. Such features will require appropriate consent, secure handling of personal data, and clear disclosure of how information is used.

Evaluation should prioritize job-relevant evidence, including technical reasoning, code, and demonstrated understanding. Facial expressions or inferred emotions should not be treated as reliable measures of technical competence.

The system is intended to support structured assessment, not independently make final hiring decisions.

## Current Limitations

The current prototype does not yet include:

- A graphical interview room or video-call interface.
- Live microphone, speech, or video processing.
- Automated execution of submitted C++ code.
- Automated résumé or GitHub repository ingestion.
- Persistent interview records or database-backed assessments.
- A validated, production-ready hiring evaluation system.

These capabilities represent future development goals rather than completed features.

## Author

**Ch Vijayendra**

GitHub: [@chvijayendra](https://github.com/chvijayendra)

**Repository:** [AI-Technical-Interview](https://github.com/chvijayendra/AI-Technical-Interview)

---

*Building toward a more structured, interactive, and evidence-based technical interview experience.*
