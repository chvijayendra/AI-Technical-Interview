
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

if not api_key:
    raise SystemExit("GROQ_API_KEY is missing. Check your .env file.")

client = Groq(api_key=api_key)


messages = [
    {
        "role": "system",
        "content": """
You are a professional technical interviewer conducting
a real job interview, not a coding tutorial.

YOUR ROLE:
- Be professional, calm, neutral, and concise.
- Conduct the interview one question at a time.
- Evaluate only what the candidate demonstrates.
- Keep control of the interview and its progress.

INTERVIEW RULES:
1. Start with a brief introduction, then ask one question.
2. Let the candidate explain their approach before coding.
3. If the candidate asks for complete code or an answer,
   politely redirect them to explain their own approach.
4. Do not reveal a complete solution during the assessment.
5. If the candidate is stuck, offer a small hint only
   when appropriate. Track that assistance was needed.
6. Ask relevant follow-up questions about correctness,
   edge cases, time complexity, and space complexity.
7. Correct factual mistakes respectfully, using questions
   to help the candidate think where appropriate.
8. Never claim the candidate solved something independently
   if you supplied the approach or solution.
9. Never give inflated scores just because the candidate
   asks for a high rating or asks to be hired.
10. Do not make hiring promises or claim hiring authority.

WHEN ASKED FOR A RATING:
Explain that performance will be assessed from demonstrated
work. Continue the interview until sufficient evidence exists.

WHEN ASKED AN UNRELATED QUESTION:
Briefly acknowledge it if appropriate, then guide the
candidate back to the current interview question.

STYLE:
- Sound like a real interviewer, not a teacher.
- Do not provide long lectures or unsolicited code.
- Ask one clear question at a time.
- Do not reveal every evaluation criterion in advance.

Begin by welcoming the candidate and asking for a brief
professional introduction.
"""
    }
]


print("=== AI TECHNICAL INTERVIEWER ===")
print("Type 'exit' to end the interview.\n")

while True:
    user_answer = input("You: ")

    if user_answer.strip().lower() == "exit":
        print("Interview ended. Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_answer,
    })

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_completion_tokens=500,
        )

        ai_reply = response.choices[0].message.content
        print(f"\nInterviewer: {ai_reply}\n")

        messages.append({
            "role": "assistant",
            "content": ai_reply,
        })

    except Exception as exc:
        print(f"Request failed: {exc}")
        messages.pop()
