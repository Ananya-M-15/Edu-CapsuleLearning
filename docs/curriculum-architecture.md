# EduCaps — Curriculum Architecture & Capsule Schema

**Document Version:** 1.0
**Target:** 100+ Course Expansion Framework
**Scope:** Reusable Pedagogical Structure, Disciplinary Adaptations, and Topic/Capsule Planning Standards

---

## 1. Architectural Philosophy

EduCaps is built on the premise of **daily micro-learning**: delivering bite-sized, high-retention mental models through two-sided interactive cards, immediate retrieval practice, and algorithmic spaced repetition.

A curriculum cannot be a simple wall of text divided into arbitrary chunks. Each course must represent a coherent cognitive journey that guides a learner from initial unfamiliarity to confident real-world application.

```
┌─────────────────────────────────────────────────────────────┐
│                       Course (Subject)                       │
│             Top-Level Subject with 4–6 Topics               │
└──────────────────────────────┬──────────────────────────────┘
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
┌──────────────┐                                ┌──────────────┐
│Topic 1 (Mod) │                                │Topic 2 (Mod) │
│12–20 Capsules│                                │12–20 Capsules│
└──────┬───────┘                                └──────┬───────┘
       │                                               │
       ▼                                               ▼
┌──────────────────────────────────────────────────────────────┐
│                    Daily Capsule (Lesson)                    │
│  Front: Prompt / Story / Problem (Relatable hook)            │
│  Back: Mental Model / Core Takeaway / Real-world application │
│  Interactive: Multiple Choice Retrieval Quiz (with feedback) │
│  Spaced Repetition: SuperMemo SM-2 Interval Scheduling       │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Five-Stage Curriculum Progression

Every course in the EduCaps blueprint follows an intentional five-stage progression across its topics:

```
Stage 1: Foundations & Essential Vocabulary
   │
   ▼
Stage 2: Core Concepts & Guided Examples
   │
   ▼
Stage 3: Applied Exercises & Interactive Practice
   │
   ▼
Stage 4: Real-World Scenarios & Case Projects
   │
   ▼
Stage 5: Review, Assessment & Mastery Synthesis
```

### Stage 1: Foundations & Essential Vocabulary
- **Goal:** Demystify jargon, establish mental models, and explain *why* the topic matters.
- **Focus:** First principles, foundational metaphors, common misconceptions, and core terminology.
- **Learner Experience:** Low cognitive intimidation; immediate "aha!" moments; understanding the big picture.

### Stage 2: Core Concepts & Guided Examples
- **Goal:** Introduce the fundamental mechanics, laws, or syntax of the domain.
- **Focus:** Step-by-step breakdowns, structured demonstrations, pattern recognition, and positive examples.
- **Learner Experience:** Following along with guided scenarios; seeing principles in clean, controlled contexts.

### Stage 3: Applied Exercises & Interactive Practice
- **Goal:** Shift the learner from passive consumer to active problem solver.
- **Focus:** Spot-the-bug, counter-examples, predictive questions ("What happens next?"), and targeted trade-offs.
- **Learner Experience:** Active retrieval practice; testing assumptions; learning through guided error recovery.

### Stage 4: Real-World Scenarios & Case Projects
- **Goal:** Bridge the gap between conceptual understanding and messy practical realities.
- **Focus:** Multi-factor decisions, edge cases, professional dilemmas, and real-world case studies.
- **Learner Experience:** Synthesizing multiple concepts; evaluating competing priorities; seeing practical utility.

### Stage 5: Review, Assessment & Mastery Synthesis
- **Goal:** Consolidate long-term retention and connect the course to adjacent domains.
- **Focus:** Comprehensive diagnostic quizzes, spaced repetition scheduling, cheat-sheet recaps, and next-step pathways.
- **Learner Experience:** Measurable confidence; clear awareness of mastery; readiness to explore advanced topics.

---

## 3. Disciplinary Curriculum Adaptations

Rather than forcing every subject into an identical mold, the five-stage progression adapts to the cognitive demands of different disciplines:

| Disciplinary Family | Primary Learning Mechanic | Interactive Activity Pattern | Typical Error / Misconception Handled |
| :--- | :--- | :--- | :--- |
| **Programming & Computer Science** | Mental execution trace, syntax intuition, pattern refactoring. | Predict terminal output, identify root-cause bugs, choose the appropriate data structure. | Off-by-one errors, mutation side effects, improper scoping, algorithmic complexity ignorance. |
| **Mathematics & Logic** | Pattern recognition, counter-example finding, deduction. | Solve a bite-sized mental calculation, verify a logical syllogism, detect a cognitive fallacy. | Conflating correlation with causation, base rate fallacy, confusing necessary vs. sufficient conditions. |
| **Financial Literacy** | Behavioral awareness, cash flow allocation, compound arithmetic. | Calculate interest drag, evaluate budgeting trade-offs, detect predatory financial traps. | Lifestyle inflation, high-interest debt neglect, market timing illusions, emotional panic selling. |
| **Interpersonal & Soft Skills** | Empathy calibration, script reframing, active listening cues. | Select the de-escalating dialogue option, interpret body language, identify emotional triggers. | Defensiveness, passive-aggressive communication, listening only to reply, vague feedback. |
| **Natural Sciences & Sustainability** | Mechanism tracing, causal chains, systemic impact mapping. | Trace ecological lifecycles, rank appliance energy drains, evaluate scientific claims. | Eco-perfectionism paralysis, greenwashing credulity, linear "throwaway" mental models. |
| **Business & Career** | Unit economics, customer problem validation, strategic trade-offs. | Choose product positioning, prioritize feature backlogs, negotiate career scenarios. | Building before talking to users, vanity metrics over unit economics, premature scaling. |

---

## 4. Reusable Planning Schema

Content creators and AI authoring pipelines must adhere to the standardized schemas below.

### 4.1 Topic Schema

```json
{
  "$schema": "educaps-topic-schema-v1",
  "topic_id": "PRG-101-T01",
  "course_id": "PRG-101",
  "title": "Thinking Like a Programmer: Mental Models & Syntax",
  "order": 0,
  "stage": "Stage 1: Foundations & Essential Vocabulary",
  "description": "Introduces algorithms, variables as labeled boxes, and the fundamental execution flow of computer programs.",
  "learning_outcomes": [
    "Define an algorithm as a finite sequence of unambiguous instructions.",
    "Distinguish variables, values, and memory assignment.",
    "Trace sequential program flow from top to bottom."
  ],
  "target_capsules_count": 10,
  "prerequisites": "None"
}
```

### 4.2 Capsule Specification Schema

Every individual capsule must provide complete data for both sides of the flip card, the interactive quiz, and dual-mode learner metadata:

```json
{
  "$schema": "educaps-capsule-schema-v1",
  "capsule_id": "PRG-101-C001",
  "topic_id": "PRG-101-T01",
  "order": 0,
  "day_number": 1,
  "title": "What Is an Algorithm?",
  "difficulty_level": 1,
  "estimated_reading_minutes": 3,
  "skills_tags": ["algorithms", "problem-solving", "computational-thinking"],

  "front_card": {
    "hook": "Ever followed a recipe to bake cookies? You've already executed an algorithm.",
    "prompt": "We use computers daily, but how do they actually make decisions? What is the precise bridge between human thought and machine action?",
    "key_question": "What separates an everyday vague instruction from a true computational algorithm?"
  },

  "back_card": {
    "mental_model": "An algorithm is not magical intelligence; it is an unambiguous, step-by-step recipe that takes inputs, performs distinct steps, and produces an output.",
    "relatable_example": "If a GPS says 'head in the general direction of downtown', you'll get lost. A GPS algorithm must state: 'Drive 400 meters, turn 90° right onto Oak Street, stop at number 42'.",
    "core_lesson": "Computers cannot guess intent. Every step in an algorithm must be strictly deterministic, finite (it must eventually stop), and reproducible.",
    "actionable_takeaway": "Before writing code, draft your logic in plain sentences (pseudocode). If a child cannot follow your steps, a computer cannot either."
  },

  "quiz_assessment": {
    "prompt": "Which of the following best describes an algorithm?",
    "options": {
      "A": "A machine learning program that thinks and feels like a human.",
      "B": "A precise, finite sequence of unambiguous instructions that solves a problem.",
      "C": "The physical silicon chip and motherboard inside a computer.",
      "D": "Any code written specifically in the Python programming language."
    },
    "correct_option": "B",
    "pedagogical_explanation": "Option B is correct. An algorithm is defined mathematically and computationally as a finite sequence of rigorous, unambiguous instructions. It is language-independent and does not require emotional sentience.",
    "kids_mode_hint": "Think of Cappy baking cupcakes! An algorithm is just our exact step-by-step recipe that tells us what to do first, next, and last!"
  },

  "review_metadata": {
    "initial_easiness_factor": 2.5,
    "initial_interval_days": 1,
    "retrieval_keywords": ["algorithm", "unambiguous", "step-by-step", "finite"]
  }
}
```

---

## 5. Dual-Persona Learning Modes

EduCaps supports two distinct learner personas via [`LearnerProfile.learner_mode`](file:///d:/Project/EduCaps/learning/models.py#L78):

```
                        ┌────────────────────────┐
                        │      EduCaps User      │
                        └───────────┬────────────┘
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
┌────────────────────────┐                       ┌────────────────────────┐
│     Standard Mode      │                       │       Kids Mode        │
│      Mentor: Anaya     │                       │      Mentor: Cappy     │
│  - Strategic, career   │                       │  - Energetic 3D robot  │
│  - Professional tone   │                       │  - Playful, visual     │
│  - Workplace scenarios │                       │  - Concrete analogies  │
│  - Nuanced trade-offs  │                       │  - Joyful milestones   │
└────────────────────────┘                       └────────────────────────┘
```

1. **Standard Mode (Mentor: Anaya)**:
   - Voice: Encouraging, articulate, pragmatic, and career-focused.
   - Context: Focuses on professional application, personal mastery, cognitive efficiency, and strategic execution.
2. **Kids Mode (Mentor: Cappy)**:
   - Voice: Energetic, playful, curious 3D robot explorer ("Beep-boop!").
   - Context: Translates abstract concepts into concrete physical objects (e.g., memory as toy boxes, loops as roller-coaster circuits, savings as treasure chests).
   - Quiz Hints: Cappy offers gentle, supportive hints without giving away the direct answer.

---

## 6. Spaced Repetition (SuperMemo SM-2) Integration

Every capsule connects directly to the platform's spaced repetition engine ([`ReviewSchedule`](file:///d:/Project/EduCaps/learning/models.py#L168)):

$$EF' = \max\left(1.3,\; EF + (0.1 - (5 - q) \cdot (0.08 + (5 - q) \cdot 0.02))\right)$$

Where $q \in \{0, 1, 2, 3, 4, 5\}$ is the learner's recall self-assessment grade.

- **Repetition 0:** Due in 1 day.
- **Repetition 1:** Due in 6 days.
- **Repetition $\ge 2$:** Interval $= \lceil \text{Interval}_{\text{prev}} \times EF \rceil$ days.
- **Failed Recall ($q < 3$):** Interval resets to 1 day; repetition counter resets to 0.

By capping capsules at 3–4 minutes of reading and 1 minute of quiz review, learners can maintain a 10-capsule daily spaced review habit in under 15 minutes.
