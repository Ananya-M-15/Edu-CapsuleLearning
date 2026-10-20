"""
EduCaps AI Tutor Service
Implements the mode-specific mentors:
- Cappy (Kids Mode): 3D white/navy/lavender robot guide with playful, encouraging explanations and simplified analogies.
- Anaya (Standard Mode): 3D human mentor with long dark-brown hair and lavender blazer offering structured, career-focused learning.

Designed to be deterministic, pedagogically sound, and grounded in capsule curriculum without external paid API dependencies.
"""

from typing import Dict, Any


class MentorPersona:
    def __init__(self, name: str, mode: str, title: str, avatar: str, greeting: str, tone: str):
        self.name = name
        self.mode = mode
        self.title = title
        self.avatar = avatar
        self.greeting = greeting
        self.tone = tone

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'mode': self.mode,
            'title': self.title,
            'avatar': self.avatar,
            'greeting': self.greeting,
            'tone': self.tone,
        }


def get_mentor_persona(mode: str = 'standard') -> MentorPersona:
    if mode == 'kids':
        return MentorPersona(
            name="Cappy",
            mode="kids",
            title="Your 3D Robot Mascot & Learning Guide",
            avatar="images/mentors/cappy.jpg",
            greeting="Beep-boop! Hey there, explorer! I'm Cappy! Let's power up our brains with today's capsule!",
            tone="enthusiastic, playful, simple, and encouraging"
        )
    return MentorPersona(
        name="Anaya",
        mode="standard",
        title="Your Strategic Career & Learning Mentor",
        avatar="images/mentors/anaya.jpg",
        greeting="Hello! I'm Anaya. Let's master focused micro-skills and build lasting competency together.",
        tone="professional, structured, strategic, and empowering"
    )


def explain_capsule(capsule, mode: str = 'standard') -> Dict[str, str]:
    """
    Synthesizes a tailored, grounded explanation from the capsule's front and back content.
    Never invents facts outside the capsule's educational domain.
    """
    title = capsule.title
    front = capsule.front_content
    back = capsule.back_content
    topic_name = capsule.topic.title
    subject_name = capsule.topic.subject.name

    if mode == 'kids':
        return {
            'mentor': 'Cappy',
            'headline': f"Beep-boop! Here is the secret behind {title}:",
            'core_concept': f"Think of {topic_name} like a superpower! {front}",
            'takeaway': f"Remember this golden rule: {back}",
            'cappy_cheer': "Cappy says: You're doing awesome! Give the quiz a try whenever you're ready! ⭐",
        }
    else:
        return {
            'mentor': 'Anaya',
            'headline': f"Strategic Breakdown: {title}",
            'core_concept': f"In the domain of {subject_name} ({topic_name}), the fundamental principle is: {front}",
            'takeaway': f"Key Competency: {back}",
            'anaya_guidance': "Anaya's Guidance: Review this concept deeply and test your retention with the active-recall assessment below.",
        }


def generate_quiz_hint(question, mode: str = 'standard') -> str:
    """
    Returns a progressive hint for the given quiz question.
    """
    if mode == 'kids':
        if question.kids_hint:
            return f"🤖 Cappy's Clue: {question.kids_hint}"
        return f"🤖 Cappy says: Take a peek back at the card! Look closely for keywords related to: '{question.prompt[:35]}'!"
    else:
        return f"💡 Anaya's Socratic Hint: Focus on the primary mechanism in {question.capsule.title}. Which option directly addresses the fundamental rule explained on the reverse card?"


def answer_capsule_query(capsule, query: str, mode: str = 'standard') -> Dict[str, str]:
    """
    Answers a learner question about the current capsule based strictly on the capsule's validated content.
    Avoids hallucinations: gracefully informs the learner when a question falls outside the capsule scope.
    """
    query_clean = (query or '').strip().lower()
    if not query_clean:
        if mode == 'kids':
            return {
                'mentor': 'Cappy',
                'response': "Beep? What would you like to ask about this card, friend? Type your question and I'll help you out! 🤖",
            }
        return {
            'mentor': 'Anaya',
            'response': "Please provide a specific question regarding this lesson, and I'll break it down for you.",
        }

    front = capsule.front_content
    back = capsule.back_content
    combined_content = f"{capsule.title} {front} {back}".lower()

    # Distinguish meaningful query terms from stopwords
    stopwords = {'what', 'why', 'how', 'is', 'are', 'the', 'a', 'an', 'to', 'in', 'on', 'of', 'for', 'about', 'tell', 'me'}
    meaningful_terms = [w.strip("?,.!") for w in query_clean.split() if w.strip("?,.!") not in stopwords and len(w.strip("?,.!")) > 2]

    # Keyword matching against validated capsule content
    matching_keywords = [w for w in meaningful_terms if w in combined_content]

    if matching_keywords:
        if mode == 'kids':
            return {
                'mentor': 'Cappy',
                'response': f"Beep-boop! Great question about {capsule.title}! Here is how it works: {back} Keep exploring!",
            }
        return {
            'mentor': 'Anaya',
            'response': f"Regarding '{query.strip()}': In this lesson on {capsule.topic.title}, the essential concept is: {back}. This is critical because: {front}",
        }
    else:
        if mode == 'kids':
            return {
                'mentor': 'Cappy',
                'response': f"Beep! That's a curious question, but it's not in this capsule yet! Let's focus on mastering: '{capsule.title}' first! 🌟",
            }
        return {
            'mentor': 'Anaya',
            'response': f"That query reaches beyond the scope of this particular capsule ({capsule.title}). To maintain strong retention, focus on mastering the core takeaway: {back}",
        }


def get_dashboard_briefing(user, mode: str = 'standard') -> Dict[str, Any]:
    """
    Generates a mode-tailored daily briefing for the dashboard.
    """
    persona = get_mentor_persona(mode)
    if mode == 'kids':
        message = f"Beep-boop! Welcome back, {user.username}! Every capsule you finish makes your brain stronger! Ready to collect your next badge?"
    else:
        message = f"Welcome back, {user.username}. Consistent daily micro-learning drives long-term career mastery. Let's tackle your highest-priority objective today."

    return {
        'mentor': persona.to_dict(),
        'briefing_text': message,
    }
