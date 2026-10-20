# EduCaps — Catalogue Audit & Baseline Inventory

**Date of Audit:** October 19, 2026
**Audit Source of Truth:** Local Database (`db.sqlite3`) and Initial Fixture (`learning/fixtures/initial_content.json`)
**Status:** Baseline Established — All 50 Existing Substantive Capsules Preserved

---

## 1. Executive Summary

This audit establishes the baseline catalogue inventory of the EduCaps platform. Prior marketing copy and UI placeholder text indicated "100+ courses," but a rigorous verification of the underlying Django models, database records, and content fixtures confirms that the existing library consists of **5 top-level courses (`Subject` records)**, **5 modules (`Topic` records)**, and **50 individual lessons (`Capsule` records)**.

All 50 capsules contain substantive, hand-crafted educational text structured as two-sided interactive micro-cards (front prompt/story, back lesson/takeaway). No capsules will be deleted, renamed, or modified. This audit documents the current state, identifies subject matter gaps, examines conceptual overlaps, and provides the architectural foundation for expanding to 100+ distinct, high-quality courses.

---

## 2. Source of Truth & Database Verification

The EduCaps content architecture uses a three-tier hierarchy in [`learning/models.py`](file:///d:/Project/EduCaps/learning/models.py):

$$\text{Subject (Course)} \longrightarrow \text{Topic (Module)} \longrightarrow \text{Capsule (Bite-sized Lesson)}$$

| Database Table | Model Class | Database Records | Fixture Records |
| :--- | :--- | :---: | :---: |
| `learning_subject` | [`Subject`](file:///d:/Project/EduCaps/learning/models.py#L11) | **5** | **5** |
| `learning_topic` | [`Topic`](file:///d:/Project/EduCaps/learning/models.py#L22) | **5** | **5** |
| `learning_capsule` | [`Capsule`](file:///d:/Project/EduCaps/learning/models.py#L35) | **50** | **50** |
| `learning_quizquestion` | [`QuizQuestion`](file:///d:/Project/EduCaps/learning/models.py#L122) | 0 (Dynamic) | 0 |
| `learning_userprogress` | [`UserProgress`](file:///d:/Project/EduCaps/learning/models.py#L49) | 13 | 0 (User data excluded) |

Both `db.sqlite3` and `learning/fixtures/initial_content.json` match identically in course, module, and capsule definitions.

---

## 3. Inventory of the Existing 5 Courses

Each of the 5 existing courses currently contains exactly **1 Topic** and **10 Capsules**, designed as a 10-day foundational sprint.

### Course 1: Money Psychology — Master Your Financial Mindset
- **Catalogue Identifier:** `FIN-101`
- **Database PK:** `1`
- **Icon Class:** `fas fa-brain`
- **Description:** *"Learn how your emotions, habits and hidden biases shape your money decisions — and how you can outsmart them."*
- **Audience:** General adult learners, young professionals, and older teenagers developing financial self-awareness.
- **Difficulty:** Beginner.
- **Topic 1 (PK 1):** *The Hidden Side of Money* (Order: 0)
  - **Capsule 1 (Day 1):** *Why Smart People Make Dumb Money Choices* — Cognitive bias, mental accounting, and financial mistakes.
  - **Capsule 2 (Day 2):** *The Latte Lie* — Micro-expenses vs. large structural financial decisions.
  - **Capsule 3 (Day 3):** *The 50/30/20 Rule — Budgeting That Actually Works* — Needs, wants, and savings framework.
  - **Capsule 4 (Day 4):** *The Dopamine Debt* — Emotional spending, retail therapy, and delay tactics.
  - **Capsule 5 (Day 5):** *Financial FOMO* — Social comparison, lifestyle inflation, and peer spending pressure.
  - **Capsule 6 (Day 6):** *Invisible Expenses* — Subscriptions, auto-renewals, and recurring cash leakage.
  - **Capsule 7 (Day 7):** *Money & Identity* — Emotional money scripts inherited from upbringing.
  - **Capsule 8 (Day 8):** *The Magic of Pay Yourself First* — Automating savings before discretionary outflow.
  - **Capsule 9 (Day 9):** *The Fear of Investing* — Risk perception, inflation drag, and long-term compound growth.
  - **Capsule 10 (Day 10):** *Money is a Mirror* — Aligning financial allocation with genuine personal values.

---

### Course 2: Digital Habits & Focus in the Smartphone Age
- **Catalogue Identifier:** `PROD-101`
- **Database PK:** `2`
- **Icon Class:** `fas fa-mobile-alt`
- **Description:** *"Learn how to master your attention, avoid distraction and reclaim your time in a connected world."*
- **Audience:** Students, knowledge workers, and digital citizens struggling with screen addiction and fragmented attention.
- **Difficulty:** Beginner.
- **Topic 2 (PK 2):** *Reclaiming Your Attention* (Order: 0)
  - **Capsule 11 (Day 1):** *The Attention Economy* — How algorithmic notification feeds monetize human focus.
  - **Capsule 12 (Day 2):** *Dopamine Traps* — Variable reward schedules in social media apps.
  - **Capsule 13 (Day 3):** *Deep Work vs Shallow Work* — High-leverage concentrated thinking vs. reactive busywork.
  - **Capsule 14 (Day 4):** *Single-Tasking Power* — The cognitive tax of task-switching and attention residue.
  - **Capsule 15 (Day 5):** *Digital Minimalism* — Decluttering home screens, notifications, and toxic feeds.
  - **Capsule 16 (Day 6):** *The Power of Boredom* — Cultivating cognitive silence to foster creativity.
  - **Capsule 17 (Day 7):** *Attention Rituals* — Morning focus blocks and phone-free launch routines.
  - **Capsule 18 (Day 8):** *Rest-oriented Productivity* — Active cognitive restoration vs. passive screen exhaustion.
  - **Capsule 19 (Day 9):** *Social Media Diet* — Intentional consumption limits and batch processing.
  - **Capsule 20 (Day 10):** *The Attention Dividend* — Long-term compound gains of sustained focus.

---

### Course 3: Emotional Intelligence & Human Behaviour
- **Catalogue Identifier:** `EQ-101`
- **Database PK:** `3`
- **Icon Class:** `fas fa-users`
- **Description:** *"Understand yourself and others better — communicate, lead and connect with more ease."*
- **Audience:** Aspiring leaders, team members, and individuals navigating complex interpersonal dynamics.
- **Difficulty:** Beginner to Intermediate.
- **Topic 3 (PK 3):** *Mastering Emotional Intelligence* (Order: 0)
  - **Capsule 21 (Day 1):** *What Is Emotional Intelligence?* — The 4 pillars: self-awareness, self-management, social awareness, relationship management.
  - **Capsule 22 (Day 2):** *Self-Awareness* — Recognizing physiological emotional triggers in real time.
  - **Capsule 23 (Day 3):** *Self-Management* — The sacred pause between stimulus and response.
  - **Capsule 24 (Day 4):** *Social Awareness* — Reading micro-expressions, body language, and team emotional climate.
  - **Capsule 25 (Day 5):** *Relationship Management* — Building trust, boundary setting, and empathetic alignment.
  - **Capsule 26 (Day 6):** *Handling Conflict* — De-escalating arguments and attacking problems rather than people.
  - **Capsule 27 (Day 7):** *Emotional Resilience* — Cognitive reframing and recovering from setbacks.
  - **Capsule 28 (Day 8):** *The Power of Curiosity* — Replacing defensiveness with open inquiry.
  - **Capsule 29 (Day 9):** *The Mirror Effect* — How personal emotional states unintentionally project onto others.
  - **Capsule 30 (Day 10):** *EQ as Leadership* — Inspiring others through authentic presence and emotional stability.

---

### Course 4: The Art of Speaking & Influence
- **Catalogue Identifier:** `COM-101`
- **Database PK:** `4`
- **Icon Class:** `fas fa-microphone`
- **Description:** *"Learn how to speak powerfully, persuade ethically and express your ideas with confidence."*
- **Audience:** Professionals, students, and speakers delivering presentations, pitches, or meeting updates.
- **Difficulty:** Beginner to Intermediate.
- **Topic 4 (PK 4):** *Speak So Others Listen* (Order: 0)
  - **Capsule 31 (Day 1):** *Why Some Voices Get Heard* — Vocal presence, pacing, and intentional silence.
  - **Capsule 32 (Day 2):** *Storytelling Power* — The narrative arc: character, hurdle, breakthrough, and takeaway.
  - **Capsule 33 (Day 3):** *The Rule of Three* — Cognitive chunking for memorable verbal delivery.
  - **Capsule 34 (Day 4):** *Voice & Body Alignment* — Open posture, eye contact, and grounded breathing.
  - **Capsule 35 (Day 5):** *Asking Great Questions* — Unlocking conversational depth and audience engagement.
  - **Capsule 36 (Day 6):** *Listening to Lead* — Active empathetic listening and reflecting back core points.
  - **Capsule 37 (Day 7):** *Handling Q&A Like a Pro* — Bridging difficult questions with calm structure.
  - **Capsule 38 (Day 8):** *Persuasion with Integrity* — Ethos, pathos, logos without manipulative deception.
  - **Capsule 39 (Day 9):** *Handling Nerves* — Converting adrenaline and stage fright into vocal energy.
  - **Capsule 40 (Day 10):** *One Sentence Summary* — Distilling complex arguments into an unforgettable bottom line.

---

### Course 5: Sustainable Living in Everyday Life
- **Catalogue Identifier:** `SCI-101`
- **Database PK:** `5`
- **Icon Class:** `fas fa-leaf`
- **Description:** *"Simple habits to live greener, save resources and protect our planet — without extremes."*
- **Audience:** Everyday citizens, households, and environmentally conscious learners seeking practical actions.
- **Difficulty:** Beginner.
- **Topic 5 (PK 5):** *Everyday Eco Choices* (Order: 0)
  - **Capsule 41 (Day 1):** *Why Sustainability Matters* — Ecological footprints and small individual multiplier effects.
  - **Capsule 42 (Day 2):** *The 3 R’s Revisited* — Prioritizing Refusal and Reduction over passive Recycling.
  - **Capsule 43 (Day 3):** *Plastic Problem — Simplified* — Single-use plastics, microplastics, and durable swaps.
  - **Capsule 44 (Day 4):** *Energy Savers at Home* — Phantom loads, smart thermostats, and appliance efficiency.
  - **Capsule 45 (Day 5):** *Water Wisdom* — Everyday water conservation in domestic kitchens and bathrooms.
  - **Capsule 46 (Day 6):** *Sustainable Food Choices* — Seasonal produce, food waste minimization, and plant-forward plates.
  - **Capsule 47 (Day 7):** *Conscious Transport* — Active transit, public transit, and route optimization.
  - **Capsule 48 (Day 8):** *Mindful Consumerism* — The 30-day purchase rule and secondhand purchasing.
  - **Capsule 49 (Day 9):** *Waste Segregation & Composting* — Diverting organic matter from methane-producing landfills.
  - **Capsule 50 (Day 10):** *Green Future Vision* — Sustaining long-term eco habits without eco-anxiety.

---

## 4. Subject Coverage Gaps & Taxonomy Deficits

The audit reveals significant domain concentration in the initial 5 courses:

1. **Heavy Concentration in Behavioral Soft Skills**: 4 of the 5 courses (`Money Psychology`, `Digital Habits`, `Emotional Intelligence`, `The Art of Speaking`) center on personal habits, psychological self-regulation, and interpersonal communication.
2. **Complete Absence of Technical & Hard Skills**:
   - **Zero** Programming or Software Development courses.
   - **Zero** Web Development or Engineering courses.
   - **Zero** Artificial Intelligence or Machine Learning literacy courses.
   - **Zero** Data Science, Analytics, or Database courses.
   - **Zero** Computer Science Fundamentals (Data Structures, Algorithms, Networking).
   - **Zero** Cybersecurity, Privacy, or Digital Defense courses.
3. **Absence of Quantitative & Logical Reasoning**:
   - **Zero** Mathematics, Logic, or Algorithmic Problem Solving courses.
4. **Limited Tactical Depth in Existing Domains**:
   - In Finance, `Money Psychology` covers behavioral awareness, but there are no courses on budgeting spreadsheets, index fund investing, debt mechanics, credit scores, or taxation.
   - In Sustainability, `Everyday Eco Choices` covers home habits, but there are no courses on climate science data, renewable energy systems, or circular economy principles.
5. **Absence of Professional & Career Readiness**:
   - No courses covering entrepreneurship, product management, resume/portfolio design, or technical documentation.

---

## 5. Overlap & Differentiation Analysis

To avoid redundant courses in the proposed 100+ catalogue, the existing courses were examined for boundary overlaps:

| Existing Course | Potential Overlap Risk | Clear Boundary Established in Blueprint |
| :--- | :--- | :--- |
| **`FIN-101` Money Psychology** | Could overlap with tactical budgeting (`FIN-102`) or investing (`FIN-103`). | `FIN-101` remains strictly focused on *behavioral finance, emotional spending, and cognitive biases*. Tactical budgeting (`FIN-102`) focuses on tools, zero-based cash flows, and emergency funds. Investing (`FIN-103`) focuses on asset classes, index funds, and portfolio risk. |
| **`PROD-101` Digital Habits & Focus** | Could overlap with general time management (`PROD-102`) or habit science (`PROD-103`). | `PROD-101` focuses specifically on *device use, smartphone notifications, and screen fatigue*. `PROD-102` focuses on calendar architecture and energy cycles. `PROD-103` analyzes cue-routine-reward habit loops. |
| **`COM-101` The Art of Speaking & Influence** | Could overlap with written workplace communication (`COM-102`) or presentation slide design (`COM-105`). | `COM-101` is strictly verbal delivery, voice modulation, and impromptu speaking. Written communication (`COM-102`) addresses asynchronous email, Slack etiquette, and documentation. |
| **`EQ-101` Emotional Intelligence & Human Behaviour** | Could overlap with workplace conflict resolution (`EQ-102`) or leadership (`EQ-106`). | `EQ-101` establishes foundational internal self-regulation and social empathy. `EQ-102` teaches tactical mediation and de-escalation scripts. `EQ-106` teaches managerial influence without authority. |
| **`SCI-101` Sustainable Living in Everyday Life** | Could overlap with climate science (`SCI-102`) or circular economy (`SCI-107`). | `SCI-101` remains an actionable domestic consumer guide. `SCI-102` is an empirical examination of atmospheric science, emissions data, and climate modeling. |

---

## 6. Architectural Scalability Recommendations

1. **Preserve Current Topic/Capsule Schema**: The current Django models [`Subject`](file:///d:/Project/EduCaps/learning/models.py#L11), [`Topic`](file:///d:/Project/EduCaps/learning/models.py#L22), and [`Capsule`](file:///d:/Project/EduCaps/learning/models.py#L35) are completely capable of supporting 100+ courses.
2. **Topic Expansion per Course**: The current courses have 1 topic with 10 capsules. To achieve comprehensive course depth (60 to 100 capsules per course), each course should feature 4 to 6 topics (modules), with 12 to 20 capsules per topic.
3. **Dual-Mode Learner Support**: The [`LearnerProfile`](file:///d:/Project/EduCaps/learning/models.py#L65) model supports `standard` and `kids` modes. The content blueprint provides guidance for adapting adult knowledge worker topics into exploratory Cappy-guided journeys for young learners.
4. **Batch Generation Strategy**: Content authoring should proceed in validated topical sprints (e.g., 5 to 10 courses at a time) rather than unreviewed bulk text generation.
