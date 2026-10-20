# EduCaps — 100+ Course Catalogue Blueprint

**Document Version:** 1.0  
**Total Courses Defined:** 105  
**Total Pedagogical Categories:** 14  
**Status:** Fully Articulated Blueprint (Ready for Incremental Authoring & Staged Ingestion)  

---

## 1. Executive Summary & Catalogue Architecture

This document establishes the comprehensive curriculum blueprint for the EduCaps micro-learning platform. Rather than relying on superficial placeholders or generic AI-generated filler, this blueprint defines **105 distinct, substantive course offerings** across 14 foundational disciplines.

Each course is fully specified with:
1. **Unique, stable catalogue identifier** (e.g. `PRG-101`, `WEB-103`).
2. **Clear, distinct title** and **concise description**.
3. **Defined target audience** and **difficulty level** (Beginner, Intermediate, Advanced).
4. **Explicit measurable learning outcomes** (5 concrete competencies per course).
5. **Prerequisites** or clear foundational entry statements.
6. **Suggested topic count** (4–5 modules) and **long-term capsule target** (60–85 bite-sized lessons).
7. **Differentiation statement** explaining how the course uniquely delivers value.
8. **5-stage high-level curriculum progression** from foundations to real-world synthesis.

### Baseline Preservation Notice
The 5 existing database courses ([`FIN-101`](#fin-101-money-psychology--master-your-financial-mindset), [`PROD-101`](#prod-101-digital-habits--focus-in-the-smartphone-age), [`EQ-101`](#eq-101-emotional-intelligence--human-behaviour), [`COM-101`](#com-101-the-art-of-speaking--influence), and [`SCI-101`](#sci-101-sustainable-living-in-everyday-life)) and all 50 of their current substantive lesson capsules are fully preserved and anchored within this expanded master architecture.

---

## 2. Category Distribution & Summary Table

| # | Category Name | Course Count | Target Capsules |
| :-: | :--- | :-: | :-: |
| 1 | Programming & Software Development | **9** | 635 |
| 2 | Web Development & Full-Stack Engineering | **8** | 555 |
| 3 | Artificial Intelligence & Machine Learning | **8** | 535 |
| 4 | Data Science, Analytics & Databases | **8** | 535 |
| 5 | Computer Science Fundamentals & Architecture | **7** | 510 |
| 6 | Cybersecurity, Privacy & Digital Safety | **7** | 470 |
| 7 | Mathematics, Logic & Algorithmic Reasoning | **7** | 475 |
| 8 | Financial Literacy, Economics & Wealth Management | **8** | 515 |
| 9 | Communication, Writing & Public Speaking | **8** | 500 |
| 10 | Emotional Intelligence, Leadership & Psychology | **8** | 495 |
| 11 | Productivity, Focus & Digital Wellbeing | **7** | 430 |
| 12 | Business, Entrepreneurship & Career Readiness | **7** | 465 |
| 13 | Science, Everyday Technology & Sustainability | **7** | 450 |
| 14 | Creative Thinking, Problem Solving & Design | **6** | 390 |
| **Total** | **All Categories Combined** | **105** | **6960** |

---

## 3. Complete Course Catalogue Specifications

### Programming & Software Development

#### 1. `PRG-101`: Python Foundations for Problem Solving
- **Description:** Master core computational logic, Python data structures, and script automation from scratch.
- **Category:** Programming & Software Development
- **Difficulty:** Beginner
- **Target Audience:** Beginner programmers, career switchers, and non-technical professionals seeking script automation.
- **Prerequisites:** None. Suitable for complete beginners.
- **Curriculum Scope:** 5 Topics | Target: 80 Capsules
- **Pedagogical Differentiation:** Focuses on practical problem-solving recipes and execution tracing rather than dry syntax memorization.
- **Learning Outcomes:**
  - Write clean, readable Python code adhering to PEP 8 standards.
  - Manipulate core data types (strings, lists, dictionaries, sets, tuples).
  - Implement control flow logic, loops, and modular functions.
  - Handle file I/O operations and exceptions gracefully.
  - Build automated scripts to solve everyday data and file management tasks.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Variables, data types, and memory models as labeled containers.
  2. **Stage 2 (Core Concepts & Guided Examples):** Control flow: conditional branching and iterative loops.
  3. **Stage 3 (Applied Exercises & Practice):** Functions, parameter passing, return values, and scope.
  4. **Stage 4 (Real-World Scenarios & Projects):** Data structures: list comprehensions and dictionary mappings.
  5. **Stage 5 (Review, Assessment & Mastery):** File handling, exception handling, and modular script project.

---

#### 2. `PRG-102`: JavaScript Core & Modern ES6+
- **Description:** Understand the engine of the web: closures, the event loop, asynchronous promises, and modern ES6+ idioms.
- **Category:** Programming & Software Development
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Web learners and developers wanting a deep conceptual grasp of JavaScript behavior.
- **Prerequisites:** Basic understanding of programming variables or completion of PRG-101.
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Demystifies the JavaScript runtime, asynchronous event loop, and prototype chain rather than just syntax tricks.
- **Learning Outcomes:**
  - Explain scope, execution contexts, hoisting, and lexical closures.
  - Master modern ES6+ features (destructuring, arrow functions, modules).
  - Handle asynchronous operations cleanly using Promises and async/await.
  - Understand the single-threaded event loop and call stack mechanics.
  - Manipulate DOM nodes and manage browser events safely.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Runtime foundations, types, coercion, and variable declarations.
  2. **Stage 2 (Core Concepts & Guided Examples):** Lexical scoping, closure mechanics, and higher-order functions.
  3. **Stage 3 (Applied Exercises & Practice):** Objects, prototypes, ES6 classes, and modern syntax sugar.
  4. **Stage 4 (Real-World Scenarios & Projects):** Asynchronous JavaScript: Callbacks, Promises, and async/await.
  5. **Stage 5 (Review, Assessment & Mastery):** The browser event loop, microtasks, and DOM integration patterns.

---

#### 3. `PRG-103`: Object-Oriented Design & Clean Code
- **Description:** Transform messy procedural scripts into maintainable, modular software using SOLID principles and design patterns.
- **Category:** Programming & Software Development
- **Difficulty:** Intermediate
- **Target Audience:** Developers who know programming syntax and want to write professional, maintainable codebases.
- **Prerequisites:** Familiarity with at least one object-oriented language (Python, Java, C#, or TypeScript).
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Emphasizes composition over inheritance and pragmatic refactoring rather than dogmatic enterprise boilerplate.
- **Learning Outcomes:**
  - Apply the SOLID principles to prevent rigid, fragile code architectures.
  - Identify and refactor common code smells (long methods, god objects, feature envy).
  - Implement essential design patterns (Factory, Strategy, Observer, Decorator).
  - Write self-documenting code with clear variable and function naming.
  - Design cohesive modules with loose coupling.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Clean code fundamentals: naming, function purity, and code smells.
  2. **Stage 2 (Core Concepts & Guided Examples):** Core OOP mechanics: encapsulation, polymorphism, and composition.
  3. **Stage 3 (Applied Exercises & Practice):** SOLID principles decoded with real-world refactoring examples.
  4. **Stage 4 (Real-World Scenarios & Projects):** Behavioral and structural design patterns in daily engineering.
  5. **Stage 5 (Review, Assessment & Mastery):** Architectural modularity: package boundaries and interface segregation.

---

#### 4. `PRG-104`: Rust for Safe & Fast Systems
- **Description:** Learn memory safety without a garbage collector through Rust's ownership, borrowing, and concurrency guarantees.
- **Category:** Programming & Software Development
- **Difficulty:** Intermediate to Advanced
- **Target Audience:** Intermediate developers seeking high-performance systems programming and bulletproof memory safety.
- **Prerequisites:** Experience with C, C++, Python, or Go.
- **Curriculum Scope:** 5 Topics | Target: 85 Capsules
- **Pedagogical Differentiation:** Breaks the notorious Rust learning curve into micro-mental models for the borrow checker.
- **Learning Outcomes:**
  - Explain ownership, moves, borrowing, and lifetime mechanics.
  - Use pattern matching, enums, and Result/Option for exhaustive error handling.
  - Build robust concurrent applications free of data races.
  - Leverage Rust traits and generics for zero-cost abstractions.
  - Create fast CLI tools and safe systems libraries.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Rust syntax, tooling (Cargo), and variable mutability.
  2. **Stage 2 (Core Concepts & Guided Examples):** The ownership model, borrowing rules, and slice references.
  3. **Stage 3 (Applied Exercises & Practice):** Custom types: structs, enums, pattern matching, and error handling.
  4. **Stage 4 (Real-World Scenarios & Projects):** Traits, generics, lifetimes, and zero-cost abstraction design.
  5. **Stage 5 (Review, Assessment & Mastery):** Concurrency primitives, fear-free threads, and smart pointers.

---

#### 5. `PRG-105`: Go for Cloud & Backend Services
- **Description:** Build simple, blazing-fast web APIs and microservices using Go's lightweight concurrency and standard library.
- **Category:** Programming & Software Development
- **Difficulty:** Intermediate
- **Target Audience:** Backend engineers, DevOps professionals, and programmers wanting simplicity and cloud-native velocity.
- **Prerequisites:** Basic understanding of HTTP and programming fundamentals.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on Go's idiomatic simplicity, goroutines, and channels rather than porting OOP habits into Go.
- **Learning Outcomes:**
  - Write idiomatic Go following effective Go conventions.
  - Design lightweight concurrent architectures with goroutines and channels.
  - Build RESTful HTTP microservices using Go's standard net/http package.
  - Manage packages, dependencies, and modules using Go tooling.
  - Structure clean backend services with interfaces and error handling.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Go syntax simplicity: types, structs, pointers, and interfaces.
  2. **Stage 2 (Core Concepts & Guided Examples):** Error handling patterns, defer, panic, and recover.
  3. **Stage 3 (Applied Exercises & Practice):** Concurrency mastery: goroutines, channels, and select blocks.
  4. **Stage 4 (Real-World Scenarios & Projects):** HTTP servers, middleware, routing, and JSON serialization.
  5. **Stage 5 (Review, Assessment & Mastery):** Testing, benchmarking, and building production container binaries.

---

#### 6. `PRG-106`: Automated Testing & Test-Driven Development (TDD)
- **Description:** Write bug-resistant code by mastering unit tests, integration tests, mocks, and the red-green-refactor cycle.
- **Category:** Programming & Software Development
- **Difficulty:** Intermediate
- **Target Audience:** Developers who want to ship code confidently without fearing regressions.
- **Prerequisites:** Basic programming competence in any modern language.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Teaches the testing pyramid and pragmatic test design instead of chasing brittle 100% test coverage metrics.
- **Learning Outcomes:**
  - Implement the Red-Green-Refactor cycle in daily feature authoring.
  - Differentiate unit, integration, end-to-end, and regression testing.
  - Use test doubles (mocks, stubs, fakes, spies) effectively.
  - Write maintainable, readable assertions that serve as living documentation.
  - Integrate automated test runs into CI/CD pipelines.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Why software fails: the cost of bugs and the testing pyramid.
  2. **Stage 2 (Core Concepts & Guided Examples):** Writing solid unit tests: AAA pattern (Arrange, Act, Assert).
  3. **Stage 3 (Applied Exercises & Practice):** Mocks, stubs, and isolating external dependencies.
  4. **Stage 4 (Real-World Scenarios & Projects):** TDD in practice: test-first development and regression prevention.

---

#### 7. `PRG-107`: Git, GitHub & Collaborative Version Control
- **Description:** Master branching, merging, rebasing, pull requests, and resolving complex merge conflicts without panic.
- **Category:** Programming & Software Development
- **Difficulty:** Beginner
- **Target Audience:** Students, self-taught developers, and teams collaborating on software repositories.
- **Prerequisites:** Basic command line navigation helpful but not required.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Explains Git's underlying directed acyclic graph (DAG) data model so commands make intuitive sense.
- **Learning Outcomes:**
  - Navigate Git's internal mental model (blobs, trees, commits, refs).
  - Execute clean branching strategies and merge conflict resolutions.
  - Understand when to merge vs. rebase interactively.
  - Conduct professional code reviews through GitHub pull requests.
  - Rescue lost work using the git reflog and cherry-pick.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Git mental model: snapshots, the working tree, staging, and history.
  2. **Stage 2 (Core Concepts & Guided Examples):** Branching, switching, merging, and conflict resolution tactics.
  3. **Stage 3 (Applied Exercises & Practice):** Remote collaboration: clones, remotes, pushes, pulls, and PR workflows.
  4. **Stage 4 (Real-World Scenarios & Projects):** Advanced recovery: interactive rebase, squashing, stash, and reflog.

---

#### 8. `PRG-108`: Debugging & Code Troubleshooting Strategies
- **Description:** Develop systematic investigative thinking to diagnose and solve baffling software defects faster.
- **Category:** Programming & Software Development
- **Difficulty:** Intermediate
- **Target Audience:** Developers at any level who lose hours to trial-and-error debugging.
- **Prerequisites:** Basic programming experience in any language.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Teaches scientific root-cause elimination and cognitive debugging heuristics rather than random print statement guessing.
- **Learning Outcomes:**
  - Apply the scientific debugging method (Hypothesize, Reproduce, Isolate, Fix, Verify).
  - Use interactive debuggers, conditional breakpoints, and stack traces.
  - Diagnose race conditions, memory leaks, and off-by-one boundary bugs.
  - Read and interpret cryptic compiler errors and stack traces accurately.
  - Write regression tests to ensure fixed bugs never return.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The psychology of debugging: cognitive traps and systematic isolation.
  2. **Stage 2 (Core Concepts & Guided Examples):** Trace tools: debuggers, log levels, inspection, and breakpoints.
  3. **Stage 3 (Applied Exercises & Practice):** Common failure patterns: state corruption, null pointers, race conditions.
  4. **Stage 4 (Real-World Scenarios & Projects):** Writing reproducible bug reports and automated regression guards.

---

#### 9. `PRG-109`: API Design with REST & GraphQL
- **Description:** Design resilient, intuitive, and versioned APIs that client developers love to consume.
- **Category:** Programming & Software Development
- **Difficulty:** Intermediate
- **Target Audience:** Backend and full-stack developers designing web services.
- **Prerequisites:** Understanding of HTTP requests and basic web architectures.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Directly compares RESTful resource design and GraphQL graph query schemas with real-world trade-offs.
- **Learning Outcomes:**
  - Design clean RESTful endpoints using proper HTTP verbs and status codes.
  - Implement pagination, filtering, sorting, and idempotent operations.
  - Define GraphQL schemas, queries, mutations, and resolvers.
  - Manage API versioning, deprecation, and backward compatibility.
  - Implement API authentication, rate limiting, and documentation (OpenAPI).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** HTTP protocol fundamentals: verbs, headers, status codes, and payloads.
  2. **Stage 2 (Core Concepts & Guided Examples):** REST resource modeling: URIs, collections, and relations.
  3. **Stage 3 (Applied Exercises & Practice):** Advanced REST patterns: pagination, caching, idempotency, and HATEOAS.
  4. **Stage 4 (Real-World Scenarios & Projects):** GraphQL paradigm: schema definition language, queries, and resolvers.
  5. **Stage 5 (Review, Assessment & Mastery):** Production API concerns: rate limiting, auth tokens, and OpenAPI docs.

---

### Web Development & Full-Stack Engineering

#### 10. `WEB-101`: HTML5 & Modern Semantic Web Architecture
- **Description:** Construct accessible, SEO-optimized, and standards-compliant web document structures.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Beginner
- **Target Audience:** Aspiring web developers and designers building digital foundations.
- **Prerequisites:** None. Suitable for absolute beginners.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on semantic meaning, accessibility landmarks, and document outline rather than outdated tag lists.
- **Learning Outcomes:**
  - Structure semantic web pages using appropriate HTML5 tags.
  - Build accessible forms with proper validation and labels.
  - Embed responsive images and multimedia with modern attributes.
  - Optimize document head metadata for search engines and social sharing.
  - Ensure document structure complies with accessibility standards.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The web document model, DOM tree, and anatomy of an HTML element.
  2. **Stage 2 (Core Concepts & Guided Examples):** Semantic structure: header, nav, main, article, section, footer.
  3. **Stage 3 (Applied Exercises & Practice):** Interactive forms: inputs, labels, validation, and accessibility.
  4. **Stage 4 (Real-World Scenarios & Projects):** Media embedding, metadata, OpenGraph tags, and SEO foundations.

---

#### 11. `WEB-102`: Modern CSS, Flexbox, Grid & Responsive Systems
- **Description:** Master CSS layout algorithms, responsive design, custom properties, and fluid typography.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Web creators who want to style interfaces without fighting the cascade or relying blindly on frameworks.
- **Prerequisites:** Basic understanding of HTML elements.
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Demystifies the CSS layout engine (box model, stacking context, flex/grid algorithms) instead of trial-and-error styling.
- **Learning Outcomes:**
  - Master the CSS Box Model, specificity calculation, and the cascade.
  - Build 1D layouts with Flexbox and 2D responsive grids with CSS Grid.
  - Implement responsive breakpoints with modern media and container queries.
  - Create reusable design token systems with CSS Custom Properties.
  - Add subtle micro-animations and transitions for polished user experience.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The Cascade, specificity calculations, inheritance, and the box model.
  2. **Stage 2 (Core Concepts & Guided Examples):** Flexbox deep-dive: axes, alignment, wrapping, and flex factors.
  3. **Stage 3 (Applied Exercises & Practice):** CSS Grid: template areas, fractional units, and auto-placement.
  4. **Stage 4 (Real-World Scenarios & Projects):** Responsive engineering: mobile-first design, fluid typography, container queries.
  5. **Stage 5 (Review, Assessment & Mastery):** Modern CSS: variables, color models (HSL, OKLCH), and keyframe animations.

---

#### 12. `WEB-103`: Full-Stack Web Architecture with Django & Python
- **Description:** Build complete, secure, database-backed web applications with Django's MVT pattern, ORM, and template engine.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Intermediate
- **Target Audience:** Developers who know Python and want to engineer robust, full-stack web platforms.
- **Prerequisites:** Python fundamentals (PRG-101) and basic HTML/CSS.
- **Curriculum Scope:** 5 Topics | Target: 85 Capsules
- **Pedagogical Differentiation:** Reflects the exact battle-tested architectural patterns utilized in EduCaps itself.
- **Learning Outcomes:**
  - Understand the Model-View-Template (MVT) architectural pattern.
  - Design database schemas and execute optimized queries using Django ORM.
  - Implement secure authentication, user sessions, and permission checks.
  - Build dynamic views, forms, and template inheritance hierarchies.
  - Deploy Django applications with production settings, static assets, and WSGI.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Django project architecture: settings, apps, URL routing, and WSGI.
  2. **Stage 2 (Core Concepts & Guided Examples):** Models and Django ORM: migrations, relationships, queries, and indexing.
  3. **Stage 3 (Applied Exercises & Practice):** Views and Templates: context passing, template tags, filters, and forms.
  4. **Stage 4 (Real-World Scenarios & Projects):** Authentication, session management, user profiles, and authorization.
  5. **Stage 5 (Review, Assessment & Mastery):** Production hardening: CSRF, security headers, Whitenoise, and deployment.

---

#### 13. `WEB-104`: React & Component-Driven UI Engineering
- **Description:** Construct reactive user interfaces using components, state hooks, props, and declarative rendering.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Intermediate
- **Target Audience:** Frontend developers building modern single-page applications.
- **Prerequisites:** Proficiency in JavaScript (PRG-102) and modern CSS (WEB-102).
- **Curriculum Scope:** 5 Topics | Target: 80 Capsules
- **Pedagogical Differentiation:** Emphasizes the mental model of UI as a pure function of state, avoiding common hook anti-patterns.
- **Learning Outcomes:**
  - Explain JSX, the Virtual DOM, and React's reconciliation algorithm.
  - Manage component state and lifecycle using useState, useEffect, and useRef.
  - Share state across component trees using context and custom hooks.
  - Optimize re-rendering using memoization techniques (useMemo, useCallback).
  - Structure modular, accessible, and testable UI component libraries.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Mental model of React: declarative UI, JSX, and component hierarchies.
  2. **Stage 2 (Core Concepts & Guided Examples):** State and Props: unidirectional data flow and event handling.
  3. **Stage 3 (Applied Exercises & Practice):** Hooks in depth: useState, useEffect lifecycle, refs, and cleanup.
  4. **Stage 4 (Real-World Scenarios & Projects):** State scaling: custom hooks, reducer patterns, and context providers.
  5. **Stage 5 (Review, Assessment & Mastery):** Performance optimization, error boundaries, and component testing.

---

#### 14. `WEB-105`: Node.js & Express Backend Architecture
- **Description:** Build high-throughput web backends, REST APIs, and middleware chains using the Node.js runtime and Express.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Intermediate
- **Target Audience:** Developers who know JavaScript and want to build server-side backends.
- **Prerequisites:** Solid JavaScript foundation (PRG-102).
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on production middleware composition, stream handling, and security hardening.
- **Learning Outcomes:**
  - Understand the Node.js event loop, libuv, and non-blocking I/O.
  - Build RESTful services with Express routing and middleware pipelines.
  - Handle file uploads, streams, and buffer operations efficiently.
  - Implement JWT-based authentication and role-based access control.
  - Structure enterprise Express apps with services, controllers, and repositories.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Node.js architecture: V8, event loop, modules, and process management.
  2. **Stage 2 (Core Concepts & Guided Examples):** Express fundamentals: routing, request/response cycles, and middleware.
  3. **Stage 3 (Applied Exercises & Practice):** Database integration, ORMs/ODMs, and async error handling.
  4. **Stage 4 (Real-World Scenarios & Projects):** Authentication, token verification, and input validation pipelines.
  5. **Stage 5 (Review, Assessment & Mastery):** Logging, environment configuration, clustering, and health checks.

---

#### 15. `WEB-106`: Web Performance Optimization & Core Web Vitals
- **Description:** Speed up web applications by optimizing asset delivery, rendering pipelines, and Google's Core Web Vitals.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Intermediate to Advanced
- **Target Audience:** Frontend engineers, performance engineers, and web developers aiming for sub-second page loads.
- **Prerequisites:** Working knowledge of HTML, CSS, and JavaScript.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Teaches the browser's critical rendering path from network packet to pixel display.
- **Learning Outcomes:**
  - Audit web apps using Lighthouse, Chrome DevTools, and WebPageTest.
  - Optimize Google Core Web Vitals: LCP, INP, and CLS.
  - Minimize critical rendering path blocking: CSS/JS minification, bundling, and deferral.
  - Implement modern image compression (WebP, AVIF) and lazy loading.
  - Leverage HTTP caching, CDNs, and resource hints (preconnect, preload).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The Critical Rendering Path: DNS, TCP, TLS, DOM, CSSOM, Render Tree, Paint.
  2. **Stage 2 (Core Concepts & Guided Examples):** Core Web Vitals deep-dive: Largest Contentful Paint, Interaction to Next Paint, Cumulative Layout Shift.
  3. **Stage 3 (Applied Exercises & Practice):** Asset optimization: images, fonts, JavaScript tree shaking, and code splitting.
  4. **Stage 4 (Real-World Scenarios & Projects):** Network layer: HTTP/2, HTTP/3, CDN caching headers, and service workers.

---

#### 16. `WEB-107`: Progressive Web Apps (PWA) & Offline-First Design
- **Description:** Turn responsive websites into installable, offline-capable mobile and desktop apps with service workers and web manifests.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Intermediate
- **Target Audience:** Web developers building resilient web apps that function seamlessly on flaky network connections.
- **Prerequisites:** Proficiency in JavaScript (PRG-102) and basic web fundamentals.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on battle-tested caching strategies (stale-while-revalidate, network-first) used in real PWA deployments.
- **Learning Outcomes:**
  - Configure a Web App Manifest for mobile and desktop installation.
  - Understand the Service Worker lifecycle (register, install, activate).
  - Implement caching strategies: cache-first, network-first, and stale-while-revalidate.
  - Manage background synchronization and client storage via IndexedDB.
  - Audit and troubleshoot PWAs using browser developer tools.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** PWA architecture: what makes an application progressive and installable.
  2. **Stage 2 (Core Concepts & Guided Examples):** The Service Worker lifecycle: interception, caching, and cache invalidation.
  3. **Stage 3 (Applied Exercises & Practice):** Caching strategies: Stale-While-Revalidate, Cache First, and Network First.
  4. **Stage 4 (Real-World Scenarios & Projects):** Offline state management: IndexedDB, Background Sync, and Push notifications.

---

#### 17. `WEB-108`: Web Accessibility (WCAG 2.2) & Inclusive UX
- **Description:** Design and build web interfaces that everyone can use, including keyboard users and people with visual or motor impairments.
- **Category:** Web Development & Full-Stack Engineering
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Frontend developers, UI/UX designers, and product managers.
- **Prerequisites:** Basic HTML and CSS knowledge.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Prioritizes native semantic HTML before reaching for ARIA, avoiding the 'bad ARIA is worse than no ARIA' trap.
- **Learning Outcomes:**
  - Apply the WCAG 2.2 principles: Perceivable, Operable, Understandable, Robust.
  - Ensure full keyboard navigability and visible focus indicator management.
  - Use ARIA roles, states, and live regions responsibly when HTML alone is insufficient.
  - Validate color contrast ratios and avoid relying on color alone for information.
  - Test web applications using screen readers (NVDA, VoiceOver) and automated linters.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Why accessibility matters: legal, ethical, and universal usability foundations.
  2. **Stage 2 (Core Concepts & Guided Examples):** Keyboard navigation: focus order, skip links, and interactive widgets.
  3. **Stage 3 (Applied Exercises & Practice):** Visual accessibility: color contrast, scalable text, and motion sensitivity.
  4. **Stage 4 (Real-World Scenarios & Projects):** ARIA in practice: labels, expanded states, live regions, and screen reader testing.

---

### Artificial Intelligence & Machine Learning

#### 18. `AI-101`: Everyday AI Literacy: What AI Can and Cannot Do
- **Description:** Demystify modern artificial intelligence, separate marketing hype from technical reality, and navigate the AI era with confidence.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Beginner
- **Target Audience:** General learners, students, professionals, and curious citizens.
- **Prerequisites:** None. Zero technical or mathematical background required.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on technical clarity and debunking myths rather than vendor hype or apocalyptic predictions.
- **Learning Outcomes:**
  - Define AI, Machine Learning, and Deep Learning without technical jargon.
  - Differentiate rule-based systems from statistical pattern-matching systems.
  - Identify real-world limitations: hallucinations, bias, and lack of common sense.
  - Evaluate AI claims critically in news, software, and marketing.
  - Adopt responsible personal productivity habits using generative AI tools.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Demystifying AI: how machines learn from historical examples.
  2. **Stage 2 (Core Concepts & Guided Examples):** From rules to patterns: why computers can now recognize cats and write essays.
  3. **Stage 3 (Applied Exercises & Practice):** The anatomy of an LLM: token prediction, context windows, and hallucinations.
  4. **Stage 4 (Real-World Scenarios & Projects):** AI in society: ethics, copyright, energy usage, and human collaboration.

---

#### 19. `AI-102`: Machine Learning Intuition & Core Algorithms
- **Description:** Build an intuitive mental model of supervised and unsupervised learning algorithms without getting lost in calculus.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Software developers, product managers, and data enthusiasts entering machine learning.
- **Prerequisites:** Basic high school algebra intuition.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Visualizes decision boundaries, loss functions, and optimization geometrically before presenting mathematical formulas.
- **Learning Outcomes:**
  - Differentiate supervised, unsupervised, and reinforcement learning.
  - Understand core algorithms: Linear Regression, Logistic Regression, Decision Trees, K-Means.
  - Explain overfitting, underfitting, and the bias-variance trade-off.
  - Evaluate models using accuracy, precision, recall, F1-score, and ROC curves.
  - Structure clean train/test validation splits to prevent data leakage.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The ML paradigm: features, labels, and finding mathematical mapping functions.
  2. **Stage 2 (Core Concepts & Guided Examples):** Regression and classification: drawing best-fit lines and decision boundaries.
  3. **Stage 3 (Applied Exercises & Practice):** Tree models and ensembles: Random Forests and Gradient Boosting intuition.
  4. **Stage 4 (Real-World Scenarios & Projects):** Unsupervised learning: clustering, dimensionality reduction, and PCA.
  5. **Stage 5 (Review, Assessment & Mastery):** Model evaluation: confusion matrices, cross-validation, and metrics that matter.

---

#### 20. `AI-103`: Deep Learning & Neural Network Foundations
- **Description:** Understand how artificial neurons, layers, activation functions, and backpropagation enable machines to learn complex representations.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Intermediate
- **Target Audience:** Programmers and students wanting to understand the computational engine behind modern AI.
- **Prerequisites:** Basic Python and foundational machine learning intuition (AI-102).
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Deconstructs backpropagation and gradient descent into intuitive step-by-step physical analogies.
- **Learning Outcomes:**
  - Explain the architecture of an artificial neuron: weights, biases, and activations.
  - Trace forward propagation and backpropagation through a network.
  - Select appropriate activation functions (ReLU, Sigmoid, Softmax).
  - Mitigate vanishing gradients and overfitting using Dropout, Batch Normalization, and Adam.
  - Understand the historical shift from shallow perceptrons to deep architectures.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The Perceptron: inputs, weights, thresholds, and linear separability.
  2. **Stage 2 (Core Concepts & Guided Examples):** Multi-layer networks: hidden representations and non-linear activation functions.
  3. **Stage 3 (Applied Exercises & Practice):** How networks learn: loss functions, gradient descent, and backpropagation.
  4. **Stage 4 (Real-World Scenarios & Projects):** Training challenges: learning rates, momentum, vanishing gradients, and regularization.
  5. **Stage 5 (Review, Assessment & Mastery):** From dense networks to specialized architectures (CNNs, RNNs, Transformers).

---

#### 21. `AI-104`: Large Language Models & Prompt Engineering Principles
- **Description:** Master the transformer architecture, self-attention, context windows, and structured prompt engineering methodologies.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Developers, technical writers, and knowledge workers integrating LLMs into software and workflows.
- **Prerequisites:** None. Suitable for curious technical and non-technical learners.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on foundational transformer mechanics (tokens, attention, temperature) and systematic prompting frameworks.
- **Learning Outcomes:**
  - Explain tokenization, embeddings, and self-attention in plain language.
  - Differentiate base models, fine-tuned models, and RLHF alignment.
  - Apply prompting frameworks: Few-Shot, Chain-of-Thought, and Role-Based prompting.
  - Understand context window constraints and retrieval-augmented generation (RAG).
  - Mitigate prompt injection and guard against factual hallucinations.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** How LLMs read: tokens, high-dimensional vector spaces, and embeddings.
  2. **Stage 2 (Core Concepts & Guided Examples):** The Transformer breakthrough: self-attention and predicting next tokens.
  3. **Stage 3 (Applied Exercises & Practice):** From raw text to assistants: pre-training, fine-tuning, and RLHF alignment.
  4. **Stage 4 (Real-World Scenarios & Projects):** Systematic prompt engineering: clear directives, few-shot examples, and chain-of-thought.
  5. **Stage 5 (Review, Assessment & Mastery):** Building with LLMs: temperature, context limits, RAG architectures, and safety.

---

#### 22. `AI-105`: Computer Vision Foundations
- **Description:** Explore how computers process visual data: image filters, convolutional neural networks (CNNs), and object detection.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Intermediate
- **Target Audience:** Developers and AI practitioners interested in visual media and autonomous systems.
- **Prerequisites:** Understanding of neural networks (AI-103) and Python basics.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Focuses on the spatial intuition of convolutions, kernels, and pooling layers.
- **Learning Outcomes:**
  - Represent digital images as numerical matrices and color channels.
  - Apply classical image processing filters (edge detection, blurring, thresholding).
  - Understand Convolutional Neural Networks: kernels, strides, padding, and pooling.
  - Differentiate image classification, object detection, and semantic segmentation.
  - Utilize pre-trained vision models via transfer learning.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Images as numbers: pixel grids, color channels (RGB), and classical matrix filters.
  2. **Stage 2 (Core Concepts & Guided Examples):** Convolutional layers: feature detectors, spatial hierarchies, and pooling operations.
  3. **Stage 3 (Applied Exercises & Practice):** Classic vision architectures: from AlexNet to ResNet and modern Vision Transformers.
  4. **Stage 4 (Real-World Scenarios & Projects):** Real-world vision tasks: object detection (YOLO), segmentation, and transfer learning.

---

#### 23. `AI-106`: Natural Language Processing (NLP) Essentials
- **Description:** Learn how computers process, analyze, and generate human language using statistical and semantic models.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Intermediate
- **Target Audience:** Developers and data scientists building search, sentiment, and text processing pipelines.
- **Prerequisites:** Basic Python and machine learning concepts (AI-102).
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Traces the computational evolution from TF-IDF and word2vec to modern contextual embeddings.
- **Learning Outcomes:**
  - Preprocess text: tokenization, lemmatization, stop words, and regex cleaning.
  - Implement classical feature extraction: Bag-of-Words and TF-IDF.
  - Understand dense word embeddings (Word2Vec) and vector semantic arithmetic.
  - Build sentiment analysis and document classification models.
  - Explain semantic similarity and vector search using cosine distance.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The nature of language: ambiguity, syntax, tokenization, and morphological normalization.
  2. **Stage 2 (Core Concepts & Guided Examples):** Counting words: Bag-of-Words, TF-IDF, and n-grams for classical text mining.
  3. **Stage 3 (Applied Exercises & Practice):** Word embeddings: Word2Vec, GloVe, and high-dimensional semantic spaces.
  4. **Stage 4 (Real-World Scenarios & Projects):** Modern semantic search: cosine similarity, vector databases, and sentence transformers.

---

#### 24. `AI-107`: AI Ethics, Bias & Responsible Machine Intelligence
- **Description:** Examine the societal footprint of AI: algorithmic bias, deepfakes, copyright, surveillance, and responsible deployment.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Product builders, policy thinkers, engineers, and everyday digital citizens.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Presents rigorous, balanced case studies on real-world algorithmic fallout rather than sci-fi panic.
- **Learning Outcomes:**
  - Identify how historical human biases infiltrate training datasets.
  - Evaluate fairness metrics in algorithmic decision-making (hiring, lending, justice).
  - Understand the intellectual property, copyright, and consent dilemmas of generative AI.
  - Analyze the ecological and computational costs of training frontier models.
  - Apply practical checklists for responsible, transparent AI deployment.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Where bias comes from: historical data, unrepresentative sampling, and proxy variables.
  2. **Stage 2 (Core Concepts & Guided Examples):** Algorithmic harms in the wild: facial recognition, lending, and criminal justice audits.
  3. **Stage 3 (Applied Exercises & Practice):** Generative dilemmas: copyright, synthetic media, deepfakes, and identity theft.
  4. **Stage 4 (Real-World Scenarios & Projects):** Responsible AI governance: auditing, explainability, safety guardrails, and transparency.

---

#### 25. `AI-108`: Practical Machine Learning with Scikit-Learn
- **Description:** Write clean, reproducible machine learning code using Python's gold-standard Scikit-Learn library.
- **Category:** Artificial Intelligence & Machine Learning
- **Difficulty:** Intermediate
- **Target Audience:** Programmers who want to train, tune, and evaluate machine learning models in Python.
- **Prerequisites:** Python fundamentals (PRG-101) and ML intuition (AI-102).
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Emphasizes the unified fit/predict/transform API, robust pipelines, and preventing data leakage.
- **Learning Outcomes:**
  - Master the Scikit-Learn estimator, transformer, and predictor API patterns.
  - Build automated data preprocessing and feature scaling pipelines.
  - Tune model hyperparameters using GridSearchCV and RandomizedSearchCV.
  - Prevent data leakage between training and testing datasets.
  - Export and serialize trained models for web application deployment.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The Scikit-Learn philosophy: unified API, datasets, estimators, and predictors.
  2. **Stage 2 (Core Concepts & Guided Examples):** Feature engineering: scalers, one-hot encoders, and column transformers.
  3. **Stage 3 (Applied Exercises & Practice):** Building end-to-end pipelines that eliminate training data leakage.
  4. **Stage 4 (Real-World Scenarios & Projects):** Hyperparameter tuning, cross-validation strategies, and learning curves.
  5. **Stage 5 (Review, Assessment & Mastery):** Model serialization (joblib/pickle) and serving predictions via web APIs.

---

### Data Science, Analytics & Databases

#### 26. `DAT-101`: SQL Essentials & Relational Database Design
- **Description:** Query, join, aggregate, and structure relational databases using standard ANSI SQL.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Data analysts, software engineers, product managers, and business analysts.
- **Prerequisites:** None. Suitable for beginners.
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Teaches the logical query execution order so learners understand why queries work or fail.
- **Learning Outcomes:**
  - Write complex SELECT queries with filtering (WHERE), sorting (ORDER BY), and limits.
  - Aggregate data using GROUP BY and filter groups using HAVING.
  - Master relational joins: INNER, LEFT, RIGHT, FULL OUTER, and CROSS joins.
  - Design normalized relational schemas (1NF, 2NF, 3NF) with primary and foreign keys.
  - Write subqueries, Common Table Expressions (CTEs), and window functions.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Relational data model: tables, rows, columns, keys, and basic SELECT queries.
  2. **Stage 2 (Core Concepts & Guided Examples):** Filtering, text pattern matching (LIKE), NULL handling, and sorting.
  3. **Stage 3 (Applied Exercises & Practice):** Aggregations: COUNT, SUM, AVG, GROUP BY, and HAVING.
  4. **Stage 4 (Real-World Scenarios & Projects):** Relational joins: joining multiple tables without Cartesian accidents.
  5. **Stage 5 (Review, Assessment & Mastery):** Advanced querying: subqueries, CTEs (WITH clauses), and database normalization.

---

#### 27. `DAT-102`: Data Analysis & Manipulation with Python & Pandas
- **Description:** Clean, reshape, slice, and analyze messy tabular data using Python's powerful Pandas library.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Intermediate
- **Target Audience:** Data analysts, scientists, researchers, and Python programmers.
- **Prerequisites:** Python fundamentals (PRG-101).
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Focuses on vectorized operations and chain methods rather than slow, procedural loops.
- **Learning Outcomes:**
  - Master Pandas Series and DataFrames: indexing, slicing, and filtering.
  - Handle missing data (NaNs), duplicates, and incorrect data types.
  - Perform groupby aggregations and multi-level data summaries.
  - Merge, concatenate, and reshape datasets using pivot and melt.
  - Analyze time-series data with date indexing, resample, and rolling windows.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Pandas data structures: Series and DataFrames under the hood.
  2. **Stage 2 (Core Concepts & Guided Examples):** Selecting and filtering: loc, iloc, boolean indexing, and query methods.
  3. **Stage 3 (Applied Exercises & Practice):** Data cleansing: dealing with nulls, string manipulation, and type casting.
  4. **Stage 4 (Real-World Scenarios & Projects):** Groupby operations, pivot tables, and statistical aggregations.
  5. **Stage 5 (Review, Assessment & Mastery):** Merging datasets (merge/join/concat) and time-series analysis.

---

#### 28. `DAT-103`: Data Visualization & Storytelling with Charts
- **Description:** Turn dry rows of numbers into compelling, honest, and persuasive visual narratives.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Data analysts, marketers, executives, and anyone who presents data to decision-makers.
- **Prerequisites:** Basic familiarity with charts (bar, line, scatter).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on human visual perception (pre-attentive attributes, color theory) and avoiding chart clutter.
- **Learning Outcomes:**
  - Select the right chart type for your data relationship (trend, distribution, comparison).
  - Apply pre-attentive visual attributes (color, size, position) to direct audience attention.
  - Eliminate chart junk and maximize the data-ink ratio.
  - Spot and avoid visual distortion tactics (truncated axes, misleading 3D charts).
  - Structure clear visual narratives with actionable headlines and annotations.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The psychology of human vision: pre-attentive attributes and cognitive load.
  2. **Stage 2 (Core Concepts & Guided Examples):** Chart taxonomy: choosing between bars, lines, scatters, histograms, and heatmaps.
  3. **Stage 3 (Applied Exercises & Practice):** Design discipline: decluttering, typography, color harmony, and accessibility.
  4. **Stage 4 (Real-World Scenarios & Projects):** Data storytelling: annotations, framing context, and driving executive decisions.

---

#### 29. `DAT-104`: Statistics for Data Analysts & Decision Makers
- **Description:** Grasp the core statistical concepts needed to interpret data, design A/B tests, and make sound decisions.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Intermediate
- **Target Audience:** Analysts, product managers, marketers, and developers working with quantitative metrics.
- **Prerequisites:** Basic numerical arithmetic and high school math.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on practical interpretation and common statistical traps rather than manual formula calculation.
- **Learning Outcomes:**
  - Distinguish mean, median, mode, variance, and standard deviation.
  - Understand distributions: the Normal distribution, skewness, and outliers.
  - Formulate hypotheses and interpret p-values and confidence intervals.
  - Design and analyze rigorous A/B experiments without sample ratio mismatch.
  - Avoid statistical fallacies (survivorship bias, regression to the mean, Simpson's paradox).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Descriptive statistics: central tendency, dispersion, percentiles, and IQR.
  2. **Stage 2 (Core Concepts & Guided Examples):** Probability distributions: Uniform, Binomial, and Normal curves.
  3. **Stage 3 (Applied Exercises & Practice):** Sampling and the Central Limit Theorem: why sample sizes matter.
  4. **Stage 4 (Real-World Scenarios & Projects):** Inferential statistics: hypothesis testing, null hypothesis, and p-value truth.
  5. **Stage 5 (Review, Assessment & Mastery):** Experimentation in practice: A/B testing design, statistical power, and paradoxes.

---

#### 30. `DAT-105`: NoSQL Databases: MongoDB, Redis & Document Stores
- **Description:** Explore non-relational data modeling: document stores (MongoDB), key-value caches (Redis), and graph databases.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Intermediate
- **Target Audience:** Backend engineers and web developers architecting scalable applications.
- **Prerequisites:** Understanding of relational database basics (DAT-101).
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Directly compares ACID relational consistency with CAP theorem distributed trade-offs.
- **Learning Outcomes:**
  - Understand the CAP theorem and BASE consistency models.
  - Design nested document schemas in MongoDB using embedding vs. referencing.
  - Use Redis for in-memory caching, session storage, and rate limiting.
  - Query unstructured and semi-structured JSON datasets efficiently.
  - Select the appropriate database paradigm (SQL vs. NoSQL) for specific access patterns.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Beyond relational: the rise of NoSQL, the CAP theorem, and eventual consistency.
  2. **Stage 2 (Core Concepts & Guided Examples):** Document databases: MongoDB CRUD operations, indexing, and aggregation pipelines.
  3. **Stage 3 (Applied Exercises & Practice):** Key-value and in-memory caches: Redis data structures (strings, hashes, sets, pub/sub).
  4. **Stage 4 (Real-World Scenarios & Projects):** Polyglot persistence: combining SQL, document, and cache layers in one architecture.

---

#### 31. `DAT-106`: Data Cleaning, Missing Values & Quality Assurance
- **Description:** Master the unglamorous 80% of data work: profiling datasets, detecting anomalies, and repairing dirty data.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Data analysts, business intelligence engineers, and data science students.
- **Prerequisites:** Basic spreadsheet or Pandas knowledge (DAT-102).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Teaches systematic data quality validation frameworks rather than ad-hoc one-off fixes.
- **Learning Outcomes:**
  - Audit datasets for structural errors, type mismatches, and duplicate records.
  - Handle missing data with domain-informed imputation or principled deletion.
  - Standardize text data: whitespace, capitalization, date formats, and encodings (UTF-8).
  - Detect statistical outliers using z-scores and interquartile ranges.
  - Automate data quality validation checks before feeding analytics pipelines.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The cost of dirty data: garbage in, garbage out in business and ML.
  2. **Stage 2 (Core Concepts & Guided Examples):** Missing data taxonomy: MCAR, MAR, and MNAR imputation strategies.
  3. **Stage 3 (Applied Exercises & Practice):** Text and format standardization: dates, timezones, strings, and categorical mapping.
  4. **Stage 4 (Real-World Scenarios & Projects):** Outlier detection, duplicate resolution, and automated schema validation.

---

#### 32. `DAT-107`: Business Intelligence & Dashboard Engineering
- **Description:** Design interactive, performant executive dashboards that monitor business health and guide strategic decisions.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Intermediate
- **Target Audience:** BI developers, business analysts, and operations managers.
- **Prerequisites:** Basic SQL (DAT-101) and visualization principles (DAT-103).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on user-centric dashboard information architecture rather than cramming 50 disconnected charts onto a screen.
- **Learning Outcomes:**
  - Define actionable KPIs (Leading vs. Lagging indicators) aligned with business goals.
  - Architect the '5-second rule' dashboard visual hierarchy.
  - Implement drill-downs, dynamic filtering, and parameterized views.
  - Optimize underlying queries and aggregates for fast dashboard rendering.
  - Establish user feedback loops to maintain dashboard adoption and relevance.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The purpose of BI: connecting business questions to metric definitions.
  2. **Stage 2 (Core Concepts & Guided Examples):** Information hierarchy: summary KPI cards, comparative trends, and granular drill-downs.
  3. **Stage 3 (Applied Exercises & Practice):** Interactive design: global filters, cross-filtering, and responsive layouts.
  4. **Stage 4 (Real-World Scenarios & Projects):** Data refresh schedules, query caching, and dashboard maintenance rituals.

---

#### 33. `DAT-108`: Data Pipelines & ETL Engineering Fundamentals
- **Description:** Understand how data flows from production transactional databases into analytical data warehouses via ETL/ELT pipelines.
- **Category:** Data Science, Analytics & Databases
- **Difficulty:** Intermediate
- **Target Audience:** Aspiring data engineers, software developers, and technical analysts.
- **Prerequisites:** Basic SQL (DAT-101) and programming fundamentals (PRG-101).
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Teaches idempotency, backfilling, and failure recovery as core pipeline design principles.
- **Learning Outcomes:**
  - Differentiate ETL (Extract-Transform-Load) and modern ELT paradigms.
  - Design idempotent pipeline runs that can safely be retried upon failure.
  - Understand batch vs. streaming data ingestion architectures.
  - Model dimensional schemas: Star schema, Snowflake schema, Fact and Dimension tables.
  - Manage workflow orchestration (DAGs) and data quality checkpoints.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The data lifecycle: operational databases vs. analytical warehouses (OLTP vs. OLAP).
  2. **Stage 2 (Core Concepts & Guided Examples):** Extract and Load: change data capture (CDC), batch dumps, and API extraction.
  3. **Stage 3 (Applied Exercises & Practice):** Transform: dimensional modeling, facts, slowly changing dimensions (SCD).
  4. **Stage 4 (Real-World Scenarios & Projects):** Pipeline resilience: idempotency, retries, dead letter queues, and alerts.
  5. **Stage 5 (Review, Assessment & Mastery):** Modern data stack overview: warehouses (Snowflake/BigQuery), dbt, and orchestrators.

---

### Computer Science Fundamentals & Architecture

#### 34. `CS-101`: Data Structures in Daily Programming
- **Description:** Master arrays, linked lists, hash tables, stacks, queues, trees, and graphs, and know exactly when to use each.
- **Category:** Computer Science Fundamentals & Architecture
- **Difficulty:** Intermediate
- **Target Audience:** Programmers preparing for technical interviews or wanting to write high-efficiency code.
- **Prerequisites:** Programming fundamentals in any language (PRG-101 or PRG-102).
- **Curriculum Scope:** 5 Topics | Target: 80 Capsules
- **Pedagogical Differentiation:** Focuses on memory layout and Big-O trade-offs in real production scenarios rather than abstract proofs.
- **Learning Outcomes:**
  - Analyze time and space complexity using Big-O notation.
  - Understand contiguous vs. linked memory layouts (Arrays vs. Linked Lists).
  - Explain hash table internal mechanics, hash functions, and collision handling.
  - Use Stacks and Queues to manage execution state and buffers.
  - Navigate hierarchical structures: Binary Search Trees, Heaps, and Tries.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Big-O notation, asymptotic analysis, and computer memory allocation.
  2. **Stage 2 (Core Concepts & Guided Examples):** Linear structures: dynamic arrays, linked lists, and memory cache locality.
  3. **Stage 3 (Applied Exercises & Practice):** Hash tables: hashing algorithms, bucket collisions, and O(1) lookups.
  4. **Stage 4 (Real-World Scenarios & Projects):** Stacks and Queues: LIFO, FIFO, call stacks, and message queues.
  5. **Stage 5 (Review, Assessment & Mastery):** Trees and Graphs: BSTs, priority queues (heaps), and adjacency representations.

---

#### 35. `CS-102`: Classic Algorithms: Sorting, Searching & Graph Traversal
- **Description:** Learn the algorithmic strategies that power modern computing: divide-and-conquer, dynamic programming, BFS, and DFS.
- **Category:** Computer Science Fundamentals & Architecture
- **Difficulty:** Intermediate to Advanced
- **Target Audience:** Computer science students and software developers building computational problem-solving muscle.
- **Prerequisites:** Data structures knowledge (CS-101).
- **Curriculum Scope:** 5 Topics | Target: 80 Capsules
- **Pedagogical Differentiation:** Builds visual intuition for algorithmic recurrence relations and branch exploration.
- **Learning Outcomes:**
  - Implement and compare sorting algorithms (MergeSort, QuickSort, Timsort).
  - Execute logarithmic binary search on ordered datasets.
  - Traverse networks using Breadth-First Search (BFS) and Depth-First Search (DFS).
  - Solve optimization problems with Greedy algorithms and Dynamic Programming (memoization).
  - Find shortest paths in weighted networks using Dijkstra's algorithm.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Algorithmic paradigms: brute force vs. divide-and-conquer.
  2. **Stage 2 (Core Concepts & Guided Examples):** Searching and sorting: binary search, divide-and-conquer sorts, stability.
  3. **Stage 3 (Applied Exercises & Practice):** Graph traversal: BFS (queue) vs. DFS (stack/recursion) and cycle detection.
  4. **Stage 4 (Real-World Scenarios & Projects):** Shortest paths: Dijkstra and A* pathfinding intuition.
  5. **Stage 5 (Review, Assessment & Mastery):** Dynamic Programming: overlapping subproblems, memoization, and tabulation.

---

#### 36. `CS-103`: Computer Architecture: How Hardware Executes Code
- **Description:** Journey beneath the software abstraction: transistors, logic gates, the CPU fetch-decode-execute cycle, and memory hierarchy.
- **Category:** Computer Science Fundamentals & Architecture
- **Difficulty:** Intermediate
- **Target Audience:** Programmers who want to understand what the physical silicon is actually doing.
- **Prerequisites:** None. General curiosity about computer hardware.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Connects high-level programming language code directly to assembly instructions and silicon gates.
- **Learning Outcomes:**
  - Explain binary representation, two's complement, and floating-point IEEE 754.
  - Trace logic gates (AND, OR, NOT, XOR) and building blocks like ALUs and registers.
  - Walk through the CPU instruction cycle: Fetch, Decode, Execute, Write-back.
  - Understand the memory hierarchy: L1/L2/L3 caches, RAM, SSDs, and latency numbers.
  - Explain how pipelining and branch prediction accelerate execution.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** From electricity to bits: binary, hexadecimal, ASCII, and numbers in silicon.
  2. **Stage 2 (Core Concepts & Guided Examples):** Boolean logic, silicon gates, flip-flops, registers, and the ALU.
  3. **Stage 3 (Applied Exercises & Practice):** The Central Processing Unit: instruction sets, registers, and the clock cycle.
  4. **Stage 4 (Real-World Scenarios & Projects):** The memory hierarchy: cache hits, misses, RAM, and the cost of memory latency.

---

#### 37. `CS-104`: Operating Systems & Process Concurrency
- **Description:** Discover how operating systems manage hardware resources: processes, threads, virtual memory, scheduling, and file systems.
- **Category:** Computer Science Fundamentals & Architecture
- **Difficulty:** Intermediate to Advanced
- **Target Audience:** Developers and engineering students building scalable backend systems.
- **Prerequisites:** Basic programming and computer architecture familiarity (CS-103).
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Demystifies the kernel/user boundary, system calls, and concurrency race conditions.
- **Learning Outcomes:**
  - Differentiate processes (isolated memory) and threads (shared memory).
  - Explain CPU scheduling algorithms and preemption.
  - Understand virtual memory, page tables, TLBs, and swapping.
  - Prevent concurrency hazards: race conditions, deadlocks, and starvation.
  - Use synchronization primitives: mutexes, semaphores, and atomic operations.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The OS role: kernel space, user space, system calls, and hardware abstraction.
  2. **Stage 2 (Core Concepts & Guided Examples):** Processes and Threads: context switches, process control blocks, and memory maps.
  3. **Stage 3 (Applied Exercises & Practice):** Concurrency challenges: critical sections, race conditions, mutexes, and deadlocks.
  4. **Stage 4 (Real-World Scenarios & Projects):** Memory management: virtual addressing, paging, page faults, and cache eviction.
  5. **Stage 5 (Review, Assessment & Mastery):** Storage and I/O: file system structures, inodes, and device controllers.

---

#### 38. `CS-105`: Computer Networking & The Internet Protocol Suite
- **Description:** Understand how data travels across the globe: TCP/IP, UDP, DNS, routing, HTTP, and TLS encryption.
- **Category:** Computer Science Fundamentals & Architecture
- **Difficulty:** Intermediate
- **Target Audience:** Web developers, network engineers, and system administrators.
- **Prerequisites:** None. General web familiarity.
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Uses packet-level mental models and real browser diagnostic traces rather than abstract networking layer memorization.
- **Learning Outcomes:**
  - Navigate the 4-layer TCP/IP model and 7-layer OSI conceptual model.
  - Explain packet routing, IP addressing (IPv4/IPv6), and CIDR subnets.
  - Compare reliable TCP (three-way handshake, congestion control) with fast UDP.
  - Trace a complete DNS resolution and TLS handshake lifecycle.
  - Troubleshoot network connectivity using ping, traceroute, and curl.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The networked world: physical links, packets, routers, and switches.
  2. **Stage 2 (Core Concepts & Guided Examples):** Network layer: IP addresses, subnets, routing tables, and NAT.
  3. **Stage 3 (Applied Exercises & Practice):** Transport layer: TCP reliable streams, flow control, and UDP datagrams.
  4. **Stage 4 (Real-World Scenarios & Projects):** Application layer protocols: DNS, HTTP/1.1, HTTP/2, HTTP/3, and WebSockets.
  5. **Stage 5 (Review, Assessment & Mastery):** Network security: TLS cryptographic handshakes, certificates, and firewalls.

---

#### 39. `CS-106`: Computational Thinking & Algorithmic Problem Solving
- **Description:** Develop the fundamental problem-solving mindset of computer science: decomposition, pattern recognition, abstraction, and algorithms.
- **Category:** Computer Science Fundamentals & Architecture
- **Difficulty:** Beginner
- **Target Audience:** Beginners, kids, educators, and anyone wanting to think more logically and systematically.
- **Prerequisites:** None. Suitable for all ages.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Presents language-agnostic logic puzzles and real-world analogies suitable for both Kids Mode and Standard Mode.
- **Learning Outcomes:**
  - Decompose complex, overwhelming problems into manageable sub-tasks.
  - Recognize recurring patterns across seemingly unrelated domains.
  - Apply abstraction to strip away distracting details and isolate core mechanisms.
  - Design step-by-step algorithms using pseudocode and flowcharts.
  - Test algorithms systematically against extreme edge cases.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The 4 pillars of computational thinking: decomposition, patterns, abstraction, algorithms.
  2. **Stage 2 (Core Concepts & Guided Examples):** Decomposition in action: breaking down complex systems into modular parts.
  3. **Stage 3 (Applied Exercises & Practice):** Pattern recognition: spotting similarities, rules, and mathematical symmetries.
  4. **Stage 4 (Real-World Scenarios & Projects):** Abstraction and algorithm design: creating instructions that never fail.

---

#### 40. `CS-107`: System Design Principles for Scalable Applications
- **Description:** Learn how web giants scale to millions of users: load balancing, horizontal scaling, caching, sharding, and resilience.
- **Category:** Computer Science Fundamentals & Architecture
- **Difficulty:** Intermediate to Advanced
- **Target Audience:** Intermediate to senior developers and system architects.
- **Prerequisites:** Understanding of databases (DAT-101), networking (CS-105), and backend servers (WEB-103/105).
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Focuses on engineering trade-offs (consistency vs. latency) rather than buzzword bingo.
- **Learning Outcomes:**
  - Design horizontally scalable web architectures free of single points of failure.
  - Configure load balancers (Round Robin, Least Connections, IP Hash).
  - Implement multi-tier caching (Client, CDN, Redis) and cache invalidation.
  - Scale databases: read replicas, master-slave replication, and database sharding.
  - Implement asynchronous queues, microservices, and circuit breaker fault tolerance.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Scaling foundations: vertical vs. horizontal scaling, stateless servers, and bottlenecks.
  2. **Stage 2 (Core Concepts & Guided Examples):** Traffic distribution: DNS routing, reverse proxies, and load balancing algorithms.
  3. **Stage 3 (Applied Exercises & Practice):** Caching strategies: CDN edge caching, Redis clusters, and the invalidation challenge.
  4. **Stage 4 (Real-World Scenarios & Projects):** Data tier scalability: read replicas, master-master replication, and sharding strategies.
  5. **Stage 5 (Review, Assessment & Mastery):** Asynchronous resilience: message brokers (Kafka/RabbitMQ), circuit breakers, and SLAs.

---

### Cybersecurity, Privacy & Digital Safety

#### 41. `SEC-101`: Personal Cybersecurity & Digital Defense Essentials
- **Description:** Protect your digital identity, devices, and data from hackers, scammers, phishing, and identity theft.
- **Category:** Cybersecurity, Privacy & Digital Safety
- **Difficulty:** Beginner
- **Target Audience:** Everyone who uses a smartphone, computer, or online account.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Provides actionable, zero-jargon security habits that give 99% protection with minimal friction.
- **Learning Outcomes:**
  - Create uncrackable, unique passwords using modern password managers.
  - Enable and configure robust Multi-Factor Authentication (MFA/2FA) methods.
  - Spot and neutralize sophisticated phishing emails, texts (smishing), and calls.
  - Secure home Wi-Fi networks and practice safe public Wi-Fi habits.
  - Audit personal device permissions and protect mobile hardware from compromise.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The threat landscape: who attacks everyday people and why credential stuffing works.
  2. **Stage 2 (Core Concepts & Guided Examples):** Passwords and Authentication: password managers, passphrases, and 2FA hardware keys.
  3. **Stage 3 (Applied Exercises & Practice):** Social engineering defense: spotting phishing, urgency triggers, and impostor fraud.
  4. **Stage 4 (Real-World Scenarios & Projects):** Device hygiene: OS updates, encrypted backups, screen locks, and Wi-Fi safety.

---

#### 42. `SEC-102`: Web Application Security & OWASP Top 10
- **Description:** Identify, exploit in lab environments, and remediate the most critical web security vulnerabilities.
- **Category:** Cybersecurity, Privacy & Digital Safety
- **Difficulty:** Intermediate
- **Target Audience:** Web developers, software engineers, and aspiring security researchers.
- **Prerequisites:** Web development fundamentals (HTML, JavaScript, basic backend).
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Focuses on root-cause code fixes and secure development lifecycles rather than superficial patching.
- **Learning Outcomes:**
  - Understand and defend against the OWASP Top 10 web vulnerabilities.
  - Prevent SQL Injection through parameterized queries and ORM safety.
  - Defend against Cross-Site Scripting (XSS) with context-aware escaping and Content Security Policy (CSP).
  - Mitigate Cross-Site Request Forgery (CSRF) with anti-forgery tokens and SameSite cookies.
  - Implement secure cryptographic storage for passwords (bcrypt, Argon2).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Security mindset: trust boundaries, attack surfaces, and defense-in-depth.
  2. **Stage 2 (Core Concepts & Guided Examples):** Injection attacks: SQLi, command injection, and parameterized prevention.
  3. **Stage 3 (Applied Exercises & Practice):** Client-side vulnerabilities: Reflected, Stored, and DOM XSS, plus CSP mitigation.
  4. **Stage 4 (Real-World Scenarios & Projects):** Session and authentication flaws: CSRF, broken access control, and cookie flags.
  5. **Stage 5 (Review, Assessment & Mastery):** Security headers, dependency scanning, and automated security testing in CI.

---

#### 43. `SEC-103`: Cryptography Fundamentals: Ciphers, Hashes & Keys
- **Description:** Understand the mathematical pillars of digital trust: symmetric encryption, public-key cryptography, hashing, and digital signatures.
- **Category:** Cybersecurity, Privacy & Digital Safety
- **Difficulty:** Intermediate
- **Target Audience:** Developers, technical enthusiasts, and security students.
- **Prerequisites:** Basic algebra and computer science concepts.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Explains cryptographic mechanisms visually and intuitively without burying learners in number theory.
- **Learning Outcomes:**
  - Differentiate encoding, hashing, symmetric encryption, and asymmetric encryption.
  - Explain cryptographic hash functions (SHA-256) and collision resistance.
  - Understand AES symmetric block ciphers, initialization vectors, and Galois/Counter Mode (GCM).
  - Walk through public-key cryptography (RSA, Elliptic Curves) and key exchange (Diffie-Hellman).
  - Verify digital signatures and Certificate Authorities (PKI).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The goal of cryptography: Confidentiality, Integrity, Authentication, and Non-repudiation.
  2. **Stage 2 (Core Concepts & Guided Examples):** Hashing: one-way functions, checksums, rainbow tables, and salting.
  3. **Stage 3 (Applied Exercises & Practice):** Symmetric encryption: shared secrets, stream ciphers, and AES block modes.
  4. **Stage 4 (Real-World Scenarios & Projects):** Asymmetric encryption: public/private key pairs, RSA, and Diffie-Hellman key exchange.
  5. **Stage 5 (Review, Assessment & Mastery):** Digital signatures, X.509 certificates, and the Public Key Infrastructure (PKI).

---

#### 44. `SEC-104`: Network Security & Firewall Defense
- **Description:** Defend networks against intrusions: packet inspection, firewalls, VPNs, IDS/IPS, and zero-trust architecture.
- **Category:** Cybersecurity, Privacy & Digital Safety
- **Difficulty:** Intermediate
- **Target Audience:** Network administrators, cloud engineers, and IT professionals.
- **Prerequisites:** Computer networking fundamentals (CS-105).
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Focuses on modern Zero-Trust architecture ('never trust, always verify') rather than legacy castle-and-moat models.
- **Learning Outcomes:**
  - Configure stateful inspection firewalls and packet-filtering rules.
  - Differentiate VPN protocols (WireGuard, OpenVPN, IPsec) and their encryption.
  - Understand Intrusion Detection and Prevention Systems (IDS/IPS).
  - Mitigate Distributed Denial of Service (DDoS) attacks with rate limiting and scrubbers.
  - Implement Zero-Trust network segmentation.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Network attack vectors: port scanning, ARP spoofing, man-in-the-middle, and DDoS.
  2. **Stage 2 (Core Concepts & Guided Examples):** Firewalls: packet filtering, stateful inspection, and application-layer gateways.
  3. **Stage 3 (Applied Exercises & Practice):** Secure tunneling: VPN protocols, WireGuard, and encrypted overlays.
  4. **Stage 4 (Real-World Scenarios & Projects):** Zero Trust Architecture: micro-segmentation, identity-aware proxies, and continuous validation.

---

#### 45. `SEC-105`: Ethical Hacking & Defensive Vulnerability Assessment
- **Description:** Learn the methodology of ethical penetration testing to discover and patch vulnerabilities before malicious attackers strike.
- **Category:** Cybersecurity, Privacy & Digital Safety
- **Difficulty:** Intermediate to Advanced
- **Target Audience:** Security practitioners, system administrators, and software engineers.
- **Prerequisites:** Networking (CS-105) and web application fundamentals (SEC-102).
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Strictly defensive and authorized scope; focuses on systematic remediation workflows.
- **Learning Outcomes:**
  - Understand the ethical and legal boundaries of penetration testing and vulnerability disclosure.
  - Conduct reconnaissance and footprinting using passive OSINT and active port scanning.
  - Identify unpatched CVEs and misconfigured network services.
  - Perform vulnerability assessments using automated tools and manual validation.
  - Write clear, actionable remediation reports for software engineering teams.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Ethical boundaries: laws, scope of engagement, rules of engagement, and authorization.
  2. **Stage 2 (Core Concepts & Guided Examples):** Reconnaissance: OSINT, DNS interrogation, and network mapping (Nmap).
  3. **Stage 3 (Applied Exercises & Practice):** Vulnerability discovery: scanning, banner grabbing, and identifying known CVEs.
  4. **Stage 4 (Real-World Scenarios & Projects):** Exploitation verification in controlled sandboxes and privilege escalation concepts.
  5. **Stage 5 (Review, Assessment & Mastery):** Defensive remediation: patch management, configuration hardening, and vulnerability reporting.

---

#### 46. `SEC-106`: Identity & Access Management (OAuth, JWT, 2FA)
- **Description:** Master modern authentication and authorization protocols: OAuth 2.0, OpenID Connect, JSON Web Tokens, and RBAC.
- **Category:** Cybersecurity, Privacy & Digital Safety
- **Difficulty:** Intermediate
- **Target Audience:** Backend developers and full-stack engineers building secure user systems.
- **Prerequisites:** Web API fundamentals (PRG-109) and basic web security.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Clarifies the crucial difference between authentication (who you are) and authorization (what you can do).
- **Learning Outcomes:**
  - Distinguish Authentication (AuthN) from Authorization (AuthZ).
  - Implement OAuth 2.0 grant types (Authorization Code with PKCE).
  - Use OpenID Connect (OIDC) for single sign-on (SSO) identity federation.
  - Structure, sign, verify, and safely store JSON Web Tokens (JWTs).
  - Implement Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Authentication vs. Authorization: sessions, cookies, and tokens.
  2. **Stage 2 (Core Concepts & Guided Examples):** JSON Web Tokens (JWT): structure, signing algorithms, claims, and storage pitfalls.
  3. **Stage 3 (Applied Exercises & Practice):** OAuth 2.0 and OIDC: authorization servers, scopes, tokens, and PKCE.
  4. **Stage 4 (Real-World Scenarios & Projects):** Enterprise access control: RBAC hierarchies, ABAC policies, and session revocation.

---

#### 47. `SEC-107`: Digital Privacy, Data Tracking & Surveillance Protection
- **Description:** Learn how web tracking, behavioral fingerprinting, and data brokers operate, and how to minimize your digital footprint.
- **Category:** Cybersecurity, Privacy & Digital Safety
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Privacy-conscious individuals, journalists, researchers, and everyday citizens.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Provides practical, daily browser and device privacy configurations without demanding that you disconnect entirely from modern life.
- **Learning Outcomes:**
  - Explain how browser fingerprinting, cookies, and tracking pixels follow users across the web.
  - Understand the data broker industry and commercial profiling mechanics.
  - Configure privacy-respecting browsers, DNS over HTTPS, and ad-blocking tools.
  - Manage mobile app telemetry, location permissions, and ad IDs.
  - Understand the principles of legal privacy frameworks like GDPR and CCPA.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The surveillance economy: cookies, trackers, data brokers, and device fingerprinting.
  2. **Stage 2 (Core Concepts & Guided Examples):** Browser defense: content blockers, anti-fingerprinting, and container tabs.
  3. **Stage 3 (Applied Exercises & Practice):** Network privacy: DNS leaks, Encrypted Client Hello, and Tor network intuition.
  4. **Stage 4 (Real-World Scenarios & Projects):** Mobile privacy: permissions, sensor access, background telemetry, and regulatory rights.

---

### Mathematics, Logic & Algorithmic Reasoning

#### 48. `MTH-101`: Mental Math & Practical Numerical Intuition
- **Description:** Overcome math anxiety and develop rapid mental estimation, percentage math, and order-of-magnitude numerical intuition.
- **Category:** Mathematics, Logic & Algorithmic Reasoning
- **Difficulty:** Beginner
- **Target Audience:** Anyone wanting to make fast, accurate calculations in daily life, shopping, and business meetings.
- **Prerequisites:** Basic arithmetic (addition, subtraction, multiplication).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on mental chunking, rounding tricks, and Fermi estimates rather than tedious pencil-and-paper formulas.
- **Learning Outcomes:**
  - Calculate percentages, discounts, and tips in your head in seconds.
  - Use decomposition to multiply two-digit numbers effortlessly.
  - Perform Fermi estimations and order-of-magnitude sanity checks.
  - Spot misleading statistics and impossible numerical claims instantly.
  - Estimate compound growth and doubling times using the Rule of 72.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Mental math foundations: friendly numbers, complement addition, and breaking apart sums.
  2. **Stage 2 (Core Concepts & Guided Examples):** Rapid multiplication: distribution tricks, doubling-and-halving, and squares.
  3. **Stage 3 (Applied Exercises & Practice):** Percentages and proportions: the 10% and 1% method, tips, discounts, and markups.
  4. **Stage 4 (Real-World Scenarios & Projects):** Fermi estimation: solving impossible order-of-magnitude questions with confident intuition.

---

#### 49. `MTH-102`: Discrete Mathematics for Computer Science
- **Description:** Master sets, relations, propositional logic, graph theory, and combinatorics—the mathematical bedrock of software engineering.
- **Category:** Mathematics, Logic & Algorithmic Reasoning
- **Difficulty:** Intermediate
- **Target Audience:** Computer science students and self-taught developers wanting theoretical engineering depth.
- **Prerequisites:** High school algebra.
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Directly links discrete mathematical theorems to actual data structures and algorithmic implementations.
- **Learning Outcomes:**
  - Manipulate mathematical sets, subsets, unions, intersections, and Cartesian products.
  - Evaluate propositional logic expressions and predicate calculus.
  - Understand mathematical induction and recursive proofs.
  - Calculate permutations, combinations, and binomial coefficients.
  - Apply graph theory principles (degrees, paths, cycles, trees) to computational problems.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Set theory: sets, Venn diagrams, power sets, and relations.
  2. **Stage 2 (Core Concepts & Guided Examples):** Formal logic: propositions, truth tables, logical equivalence, and quantifiers.
  3. **Stage 3 (Applied Exercises & Practice):** Proof techniques: direct proof, contradiction, and mathematical induction.
  4. **Stage 4 (Real-World Scenarios & Projects):** Combinatorics: counting principles, permutations, combinations, and the Pigeonhole Principle.
  5. **Stage 5 (Review, Assessment & Mastery):** Graph theory fundamentals: vertices, edges, paths, isomorphism, and Euler circuits.

---

#### 50. `MTH-103`: Probability & Risk in Everyday Decisions
- **Description:** Learn to calculate odds, understand expected value, and make rational bets in an uncertain world.
- **Category:** Mathematics, Logic & Algorithmic Reasoning
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Decision makers, investors, poker players, and everyday critical thinkers.
- **Prerequisites:** Basic arithmetic.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on cognitive probability traps (gambler's fallacy, base rate neglect) and calculating expected value.
- **Learning Outcomes:**
  - Calculate basic and compound probabilities (AND vs. OR rules).
  - Understand conditional probability and apply Bayes' Theorem intuitively.
  - Calculate Expected Value (EV) to determine whether a risk is mathematically favorable.
  - Recognize the Gambler's Fallacy and the Hot Hand illusion.
  - Apply probabilistic thinking to medical tests, insurance policies, and investments.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Probability foundations: sample spaces, independent events, and the law of large numbers.
  2. **Stage 2 (Core Concepts & Guided Examples):** Compound probability: union, intersection, and mutual exclusivity.
  3. **Stage 3 (Applied Exercises & Practice):** Conditional probability and Bayes' Theorem: updating beliefs based on new evidence.
  4. **Stage 4 (Real-World Scenarios & Projects):** Expected value, variance, and the mathematics of insurance and lotteries.
  5. **Stage 5 (Review, Assessment & Mastery):** Cognitive probability fallacies: base rate neglect, clustering illusion, and risk calibration.

---

#### 51. `MTH-104`: Linear Algebra for Machine Learning & Graphics
- **Description:** Understand vectors, matrices, dot products, transformations, and eigenvalues as geometric transformations.
- **Category:** Mathematics, Logic & Algorithmic Reasoning
- **Difficulty:** Intermediate
- **Target Audience:** Aspiring machine learning practitioners, game developers, and graphics programmers.
- **Prerequisites:** High school algebra and coordinate geometry.
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Teaches linear algebra geometrically (spaces stretching, rotating, and projecting) rather than as mechanical matrix arithmetic.
- **Learning Outcomes:**
  - Visualize vectors as arrows and coordinates in multi-dimensional space.
  - Understand dot products (projection/similarity) and cross products (orientation).
  - Interpret matrix multiplication as linear transformations of space.
  - Calculate determinants and understand matrix invertibility.
  - Explain eigenvalues and eigenvectors and their role in Principal Component Analysis (PCA).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Vectors in space: magnitude, direction, vector addition, and linear combinations.
  2. **Stage 2 (Core Concepts & Guided Examples):** Dot products and cosine similarity: measuring alignment in high dimensions.
  3. **Stage 3 (Applied Exercises & Practice):** Matrices as geometric transformations: scaling, rotation, shearing, and the basis vectors.
  4. **Stage 4 (Real-World Scenarios & Projects):** Matrix multiplication, systems of linear equations, and determinants.
  5. **Stage 5 (Review, Assessment & Mastery):** Eigenvalues and Eigenvectors: invariant axes and dimensionality reduction.

---

#### 52. `MTH-105`: Formal Logic, Truth Tables & Fallacy Detection
- **Description:** Sharpen your reasoning: master deductive and inductive logic, construct truth tables, and spot logical fallacies in arguments.
- **Category:** Mathematics, Logic & Algorithmic Reasoning
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Debaters, critical thinkers, law students, and programmers.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Applies formal logic directly to analyzing real-world political speeches, advertisements, and debate transcripts.
- **Learning Outcomes:**
  - Differentiate valid vs. invalid, sound vs. unsound deductive arguments.
  - Construct and evaluate truth tables for complex conditional statements.
  - Identify formal logical fallacies (affirming the consequent, denying the antecedent).
  - Spot informal fallacies (straw man, ad hominem, false dichotomy, slippery slope).
  - Structure clear, logically rigorous arguments in writing and debate.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Argument structure: premises, conclusions, and validity vs. truth.
  2. **Stage 2 (Core Concepts & Guided Examples):** Propositional operators: AND, OR, NOT, IMPLIES, and truth tables.
  3. **Stage 3 (Applied Exercises & Practice):** Formal syllogisms and deductive inference rules (Modus Ponens, Modus Tollens).
  4. **Stage 4 (Real-World Scenarios & Projects):** Informal fallacy field guide: cognitive distortions and emotional debate manipulation.

---

#### 53. `MTH-106`: Game Theory: Strategic Decision Making
- **Description:** Analyze multi-player strategic interactions: the Prisoner's Dilemma, Nash Equilibrium, zero-sum games, and cooperative strategies.
- **Category:** Mathematics, Logic & Algorithmic Reasoning
- **Difficulty:** Intermediate
- **Target Audience:** Business strategists, economists, negotiators, and competitive game players.
- **Prerequisites:** Basic probability and logical reasoning (MTH-103).
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Focuses on the evolution of trust and cooperative strategies (Tit-for-Tat) in repeated human interactions.
- **Learning Outcomes:**
  - Model strategic dilemmas using payoff matrices and decision trees.
  - Identify dominant strategies and calculate the Nash Equilibrium.
  - Analyze the Prisoner's Dilemma and mechanisms for sustaining cooperation.
  - Differentiate zero-sum games from positive-sum collaborative games.
  - Apply signaling, commitment, and deterrence tactics in negotiations.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** What is a game: players, strategies, payoffs, and information rules.
  2. **Stage 2 (Core Concepts & Guided Examples):** The Prisoner's Dilemma: individual rationality vs. collective ruin.
  3. **Stage 3 (Applied Exercises & Practice):** Nash Equilibrium: finding stable outcomes where no player regrets their choice.
  4. **Stage 4 (Real-World Scenarios & Projects):** Repeated games, the evolution of trust (Tit-for-Tat), and credible commitments.

---

#### 54. `MTH-107`: Calculus Intuition for Science and Modeling
- **Description:** Understand differentiation as rate of change and integration as accumulation without drowning in algebraic drill.
- **Category:** Mathematics, Logic & Algorithmic Reasoning
- **Difficulty:** Intermediate
- **Target Audience:** Students and programmers seeking intuitive calculus comprehension for machine learning and physics.
- **Prerequisites:** High school algebra and functions.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Builds geometric, visual intuition for limits, derivatives, and integrals inspired by 3Blue1Brown's pedagogical style.
- **Learning Outcomes:**
  - Explain limits and instantaneous rate of change as slopes of tangent lines.
  - Understand the derivative as a sensitivity measure (how output changes with input).
  - Apply basic differentiation rules (power, product, chain rule) intuitively.
  - Understand the definite integral as the accumulation of infinitely thin slices.
  - Explain the Fundamental Theorem of Calculus linking derivatives and integrals.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The paradox of the instant: speedometers, limits, and zooming in until curves look straight.
  2. **Stage 2 (Core Concepts & Guided Examples):** The Derivative: slopes, tangents, and sensitivity analysis.
  3. **Stage 3 (Applied Exercises & Practice):** Optimization: finding peaks, valleys, and local minima via gradient zeroing.
  4. **Stage 4 (Real-World Scenarios & Projects):** The Integral: area under curves, Riemann sums, and cumulative accumulation.
  5. **Stage 5 (Review, Assessment & Mastery):** The Fundamental Theorem of Calculus and multivariable partial derivatives preview.

---

### Financial Literacy, Economics & Wealth Management

#### 55. `FIN-101`: Money Psychology — Master Your Financial Mindset
- **Description:** Learn how your emotions, habits and hidden biases shape your money decisions — and how you can outsmart them.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Beginner
- **Target Audience:** General adult learners and young professionals seeking emotional and behavioral money clarity.
- **Prerequisites:** None. (Existing EduCaps Subject ID 1).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses strictly on internal behavioral scripts, mental accounting, and emotional triggers rather than financial spreadsheets.
- **Learning Outcomes:**
  - Identify personal money scripts and emotional spending triggers.
  - Differentiate structural wealth decisions from minor micro-expenses.
  - Implement automated savings using the 'Pay Yourself First' principle.
  - Resist social comparison and financial FOMO.
  - Align spending habits with genuine core values.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The hidden psychology of money: biases, dopamine spending, and mental accounting.
  2. **Stage 2 (Core Concepts & Guided Examples):** Social comparison: financial FOMO, lifestyle creep, and identity scripts.
  3. **Stage 3 (Applied Exercises & Practice):** Behavioral guardrails: Pay Yourself First, friction rules, and delayed gratification.
  4. **Stage 4 (Real-World Scenarios & Projects):** Mindset synthesis: aligning capital allocation with life satisfaction.

---

#### 56. `FIN-102`: Practical Budgeting & Cash Flow Management
- **Description:** Design a realistic cash flow system: zero-based budgeting, emergency funds, tracking expenses, and sinking funds.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Beginner
- **Target Audience:** Anyone wanting to gain control of their monthly income and stop living paycheck-to-paycheck.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on sustainable, low-friction budgeting systems (zero-based, 50/30/20) that don't require tracking every single penny manually.
- **Learning Outcomes:**
  - Audit personal cash flow to identify fixed, variable, and discretionary expenses.
  - Implement a zero-based or percentage-based (50/30/20) budget.
  - Build an emergency buffer fund calibrated to household risk.
  - Set up sinking funds to eliminate the shock of irregular, annual expenses.
  - Automate banking workflows between checking, savings, and investment accounts.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Where did the money go: tracking cash flow without shame or burnout.
  2. **Stage 2 (Core Concepts & Guided Examples):** Budget frameworks: Zero-Based Budgeting vs. 50/30/20 vs. Pay-Yourself-First.
  3. **Stage 3 (Applied Exercises & Practice):** The Safety Net: calculating and funding a 3-to-6 month liquid emergency reserve.
  4. **Stage 4 (Real-World Scenarios & Projects):** Sinking funds and banking automation: putting personal finance on autopilot.

---

#### 57. `FIN-103`: Investing Fundamentals: Stocks, Bonds & Index Funds
- **Description:** Learn how the financial markets work: broad index funds, asset allocation, diversification, and long-term compound wealth.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Beginner investors wanting to build long-term wealth without gambling or stock picking.
- **Prerequisites:** Basic cash flow stability and an emergency fund (FIN-102 recommended).
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Advocates the Nobel-prize-winning passive index fund philosophy (Bogleheads approach) over speculative active trading.
- **Learning Outcomes:**
  - Explain what stocks, bonds, mutual funds, and ETFs actually represent.
  - Understand market risk, volatility, and historical asset class returns.
  - Apply modern portfolio theory through broad-market low-cost index funds.
  - Evaluate the destructive impact of high expense ratios and hidden advisory fees.
  - Implement a dollar-cost averaging strategy and avoid the market-timing trap.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Why invest: inflation as an invisible tax and the power of compound interest.
  2. **Stage 2 (Core Concepts & Guided Examples):** Asset classes decoded: what owning a stock vs. holding a bond really means.
  3. **Stage 3 (Applied Exercises & Practice):** The Index Fund revolution: why picking individual stocks fails 90% of pros.
  4. **Stage 4 (Real-World Scenarios & Projects):** Asset allocation, diversification, and rebalancing across life stages.
  5. **Stage 5 (Review, Assessment & Mastery):** Executing the strategy: brokerage accounts, index ETFs, and emotional discipline in bear markets.

---

#### 58. `FIN-104`: Understanding Debt, Credit Scores & Loan Strategy
- **Description:** Master credit score mechanics, conquer high-interest consumer debt, and navigate mortgages and student loans strategically.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Consumers carrying debt or planning major borrowing (mortgages, auto loans, student loans).
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Directly compares mathematical debt elimination (Avalanche) vs. psychological momentum (Snowball) strategies.
- **Learning Outcomes:**
  - Demystify credit scoring algorithms (FICO/VantageScore) and utilization ratios.
  - Compare the Debt Avalanche (highest interest) and Debt Snowball (smallest balance) methods.
  - Understand APR, compound interest drag, and amortization schedules.
  - Distinguish productive low-interest debt from predatory high-interest consumer debt.
  - Evaluate refinancing options and loan consolidation risks.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The mathematics of debt: APR, daily compounding, and minimum payment traps.
  2. **Stage 2 (Core Concepts & Guided Examples):** Credit scores decoded: payment history, credit utilization, and credit age.
  3. **Stage 3 (Applied Exercises & Practice):** Debt elimination playbooks: Snowball vs. Avalanche and negotiating interest rates.
  4. **Stage 4 (Real-World Scenarios & Projects):** Strategic borrowing: fixed vs. adjustable rate mortgages and student loan management.

---

#### 59. `FIN-105`: Everyday Economics: Supply, Demand & Inflation
- **Description:** Understand the economic forces shaping your daily life: supply and demand, central bank interest rates, inflation, and market cycles.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Curious citizens and professionals wanting to understand financial headlines.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Explains macroeconomic mechanisms using clear everyday supermarket and housing examples rather than dry mathematical models.
- **Learning Outcomes:**
  - Explain market equilibrium through supply, demand, and price elasticity.
  - Understand inflation drivers (demand-pull, cost-push) and purchasing power erosion.
  - Explain how central banks use interest rates to control economic cycles.
  - Understand GDP, unemployment metrics, and recession indicators.
  - Evaluate the trade-offs of price controls, tariffs, and government subsidies.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The economic engine: scarcity, opportunity cost, and the invisible hand.
  2. **Stage 2 (Core Concepts & Guided Examples):** Supply and Demand: market equilibrium, price elasticity, and shortages.
  3. **Stage 3 (Applied Exercises & Practice):** Money and Inflation: what causes prices to rise and why deflation is feared.
  4. **Stage 4 (Real-World Scenarios & Projects):** Central banks and monetary policy: interest rates, quantitative easing, and cycles.
  5. **Stage 5 (Review, Assessment & Mastery):** Global trade, currency exchange rates, and macroeconomic indicators.

---

#### 60. `FIN-106`: Retirement Planning & Compound Interest Dynamics
- **Description:** Plan your financial independence: compound growth horizons, tax-advantaged accounts, withdrawal rates, and pension systems.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Intermediate
- **Target Audience:** Adults at any career stage planning for retirement or financial independence (FIRE).
- **Prerequisites:** Investing fundamentals (FIN-103).
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Focuses on safe withdrawal rates (the 4% rule) and sequence of returns risk rather than arbitrary savings targets.
- **Learning Outcomes:**
  - Model retirement needs using target withdrawal rates and the Trinity Study (4% rule).
  - Optimize contributions to tax-advantaged accounts (401k, IRA, Roth equivalents).
  - Understand sequence of returns risk during early retirement years.
  - Calculate your 'Financial Independence Number' based on annual expenditure.
  - Plan health insurance and long-term care contingencies in later life.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The retirement reality check: longevity risk, healthcare, and state pensions.
  2. **Stage 2 (Core Concepts & Guided Examples):** Tax-advantaged vehicles: traditional pre-tax vs. Roth post-tax account mathematics.
  3. **Stage 3 (Applied Exercises & Practice):** Safe withdrawal rates: the 4% rule, dynamic spending, and sequence-of-returns risk.
  4. **Stage 4 (Real-World Scenarios & Projects):** The FIRE movement: milestones to financial independence and lifestyle design.

---

#### 61. `FIN-107`: Tax Fundamentals for Freelancers & Employees
- **Description:** Demystify taxes: marginal tax brackets, deductions vs. credits, self-employment taxes, and legal tax minimization.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Freelancers, gig workers, and salaried professionals seeking tax literacy.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Dispels the dangerous myth that 'moving up a tax bracket reduces your total take-home pay'.
- **Learning Outcomes:**
  - Explain how marginal tax brackets and effective tax rates actually work.
  - Distinguish above-the-line tax deductions from dollar-for-dollar tax credits.
  - Manage quarterly estimated taxes and self-employment deductions for freelancers.
  - Keep clean business expense records to withstand audit scrutiny.
  - Differentiate legal tax avoidance/optimization from illegal tax evasion.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Taxes demystified: marginal brackets, effective rates, and common bracket myths.
  2. **Stage 2 (Core Concepts & Guided Examples):** Deductions vs. Credits: standard deduction, itemizing, and high-value tax credits.
  3. **Stage 3 (Applied Exercises & Practice):** Freelance and self-employment taxes: Schedule C, write-offs, and quarterly estimates.
  4. **Stage 4 (Real-World Scenarios & Projects):** Tax-smart life habits: record keeping, audit hygiene, and year-end planning.

---

#### 62. `FIN-108`: Financial Safety: Scams, Fraud & Risk Prevention
- **Description:** Protect your life savings: detect Ponzi schemes, crypto scams, identity theft, credit card skimming, and social engineering fraud.
- **Category:** Financial Literacy, Economics & Wealth Management
- **Difficulty:** Beginner
- **Target Audience:** Everyone wanting to protect their hard-earned money and help elderly relatives avoid scams.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Analyzes the psychological persuasion techniques (urgency, authority, isolation) scammers use to bypass logic.
- **Learning Outcomes:**
  - Identify the anatomical red flags of Ponzi and pyramid schemes.
  - Recognize modern financial scams: crypto recovery, advance-fee fraud, romance scams.
  - Protect bank accounts with account alerts, credit freezes, and virtual credit cards.
  - Take immediate emergency action if personal financial credentials are compromised.
  - Help vulnerable family members safeguard their retirement savings.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The psychology of the scam: fear, greed, urgency, and artificial authority.
  2. **Stage 2 (Core Concepts & Guided Examples):** Investment scams: guaranteed returns, affinity fraud, and crypto pump-and-dumps.
  3. **Stage 3 (Applied Exercises & Practice):** Direct theft: wire fraud, check fraud, account takeover, and synthetic identity theft.
  4. **Stage 4 (Real-World Scenarios & Projects):** Emergency defense protocol: freezing credit, reporting fraud, and securing compromised accounts.

---

### Communication, Writing & Public Speaking

#### 63. `COM-101`: The Art of Speaking & Influence
- **Description:** Learn how to speak powerfully, persuade ethically and express your ideas with confidence.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Professionals, students, and speakers delivering presentations, pitches, or meeting updates.
- **Prerequisites:** None. (Existing EduCaps Subject ID 4).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on verbal delivery, vocal resonance, the rule of three, and converting nervousness into charisma.
- **Learning Outcomes:**
  - Master vocal presence, pacing, pitch modulation, and strategic pausing.
  - Structure memorable remarks using the Rule of Three.
  - Convert stage fright and adrenaline into engaging vocal energy.
  - Answer challenging audience Q&A with poise and structure.
  - Distill complex arguments into an unforgettable one-sentence takeaway.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Voice and body: posture, diaphragmatic breathing, and intentional pausing.
  2. **Stage 2 (Core Concepts & Guided Examples):** Message architecture: the narrative arc, hooks, and the Rule of Three.
  3. **Stage 3 (Applied Exercises & Practice):** Handling pressure: reframing nerves, executive presence, and spontaneous answers.
  4. **Stage 4 (Real-World Scenarios & Projects):** Ethical influence: combining ethos, pathos, and logos for lasting impact.

---

#### 64. `COM-102`: Clear Writing for the Workplace & Remote Teams
- **Description:** Write crisp emails, clear Slack messages, concise memos, and executive updates that save time and get results.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Knowledge workers, managers, and remote professionals.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on asynchronous reading habits—using the BLUF (Bottom Line Up Front) model to respect busy colleagues' time.
- **Learning Outcomes:**
  - Apply the BLUF (Bottom Line Up Front) framework to all business communications.
  - Eliminate corporate buzzwords, passive voice, and unnecessary filler sentences.
  - Format emails with clear calls-to-action (CTAs) and explicit deadlines.
  - Calibrate tone across asynchronous channels (Slack vs. formal proposal).
  - Write executive summaries that leadership can digest in under 60 seconds.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The reader's reality: cognitive overload and why people skim.
  2. **Stage 2 (Core Concepts & Guided Examples):** Structure first: BLUF, scannable formatting, bullet points, and headers.
  3. **Stage 3 (Applied Exercises & Practice):** Sentence-level craft: cutting dead weight, active voice, and eliminating hedge words.
  4. **Stage 4 (Real-World Scenarios & Projects):** Asynchronous collaboration: meeting-free updates, project briefs, and executive memos.

---

#### 65. `COM-103`: Persuasive Storytelling & Narrative Structure
- **Description:** Hook your audience, build emotional resonance, and drive action using timeless narrative storytelling frameworks.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Intermediate
- **Target Audience:** Marketers, founders pitching investors, leaders, and creative writers.
- **Prerequisites:** Basic communication skills.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Translates Hollywood screenwriting structures (Hero's Journey, 3-Act Structure) into business and product narratives.
- **Learning Outcomes:**
  - Structure presentations around a clear protagonist, conflict, turning point, and resolution.
  - Use sensory details and specific vignettes to make abstract data memorable.
  - Build tension and contrast between 'what is' and 'what could be'.
  - Pitch startups or internal initiatives using the problem-solution-vision narrative.
  - Craft an authentic personal leadership narrative.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Why human brains crave stories: neurochemistry, oxytocin, and memory retention.
  2. **Stage 2 (Core Concepts & Guided Examples):** Classic narrative anatomy: character, desire, obstacle, crisis, and transformation.
  3. **Stage 3 (Applied Exercises & Practice):** The Business Narrative: contrasting pain points with future possibilities.
  4. **Stage 4 (Real-World Scenarios & Projects):** Storycraft in action: crafting origin stories, case study victories, and vision pitches.

---

#### 66. `COM-104`: Active Listening & Non-Defensive Dialogue
- **Description:** Master the rarest conversational superpower: listening to understand rather than listening to reply.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Leaders, managers, team members, and partners navigating difficult conversations.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Teaches psychological reflecting techniques (looping, labeling) from hostage negotiation to disarm defensiveness.
- **Learning Outcomes:**
  - Identify the 4 levels of listening (internal, focused, global, empathetic).
  - Mirror and summarize the speaker's emotional state without agreeing with their premise.
  - Ask open-ended, non-judgmental exploratory questions.
  - Recognize internal defensiveness triggers before interrupting.
  - Create psychological safety in high-stakes one-on-one conversations.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The listening crisis: why most people only reload while the other person speaks.
  2. **Stage 2 (Core Concepts & Guided Examples):** Active listening mechanics: mirroring, paraphrasing, and emotional labeling.
  3. **Stage 3 (Applied Exercises & Practice):** The art of powerful questions: shifting from interrogation to open discovery.
  4. **Stage 4 (Real-World Scenarios & Projects):** Non-defensive composure: staying grounded when hearing criticism or emotional complaints.

---

#### 67. `COM-105`: Presentation Design & Slide Delivery
- **Description:** Design clean, persuasive slides and deliver presentations that captivate audiences without teleprompter reading.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Professionals, students, and executives presenting to clients, boards, or conferences.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Adheres to the 'one idea per slide' principle, banning paragraphs of bullet points and cluttered templates.
- **Learning Outcomes:**
  - Apply the 'One Idea Per Slide' design rule.
  - Design clean slide hierarchies using typography, whitespace, and high-impact imagery.
  - Present complex charts and data tables without overwhelming viewers.
  - Deliver slides seamlessly using speaker notes and audience eye contact.
  - Handle unexpected projector crashes and technical presentation failures.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Slide design philosophy: slides are billboards for your voice, not teleprompter scripts.
  2. **Stage 2 (Core Concepts & Guided Examples):** Visual composition: typography, whitespace, color contrast, and photographic focus.
  3. **Stage 3 (Applied Exercises & Practice):** Data presentation: highlighting the single takeaway in complex charts.
  4. **Stage 4 (Real-World Scenarios & Projects):** Stagecraft: transitions, body positioning, clicking without breaking eye contact.

---

#### 68. `COM-106`: Negotiation Essentials: Reaching Win-Win Outcomes
- **Description:** Negotiate salary, contracts, and everyday agreements with confidence, emotional control, and principled strategy.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Intermediate
- **Target Audience:** Job seekers, freelancers, procurement specialists, and professionals seeking fair value.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Builds on Harvard's 'Getting to Yes' principled negotiation framework rather than adversarial high-pressure haggling.
- **Learning Outcomes:**
  - Separate the people from the problem in high-stakes negotiations.
  - Identify your BATNA (Best Alternative to a Negotiated Agreement) and reservation price.
  - Shift from positional bargaining to interest-based mutual value creation.
  - Anchor negotiations strategically and handle low-ball offers calmly.
  - Negotiate job offers and compensation packages ethically.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Negotiation mindsets: competitive zero-sum haggling vs. principled collaborative value creation.
  2. **Stage 2 (Core Concepts & Guided Examples):** Preparation is power: determining your BATNA, reservation price, and target aspiration.
  3. **Stage 3 (Applied Exercises & Practice):** Tactical execution: anchoring, framing trades, and the power of strategic silence.
  4. **Stage 4 (Real-World Scenarios & Projects):** Overcoming impasses: expanding the pie, package deals, and managing difficult counterparties.
  5. **Stage 5 (Review, Assessment & Mastery):** Career negotiation: handling salary discussions, equity, and workplace benefits.

---

#### 69. `COM-107`: Technical Writing & Documentation for Developers
- **Description:** Write API docs, READMEs, architectural decision records (ADRs), and user guides that developers love reading.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Intermediate
- **Target Audience:** Software engineers, DevOps practitioners, open-source maintainers, and technical writers.
- **Prerequisites:** Basic understanding of code or developer tools.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Applies the Diátaxis documentation framework (Tutorials, How-to Guides, Reference, Explanation).
- **Learning Outcomes:**
  - Apply the Diátaxis framework to organize technical documentation.
  - Write exceptional project README files that onboard developers in under 5 minutes.
  - Document REST and GraphQL APIs with accurate parameter tables and curl examples.
  - Draft Architectural Decision Records (ADRs) to capture context and trade-offs.
  - Maintain living documentation that stays updated as the codebase evolves.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Why technical documentation fails: outdated wikis, cognitive blind spots, and lack of audience empathy.
  2. **Stage 2 (Core Concepts & Guided Examples):** The Diátaxis framework: Tutorials (learning-oriented) vs. How-to (task-oriented).
  3. **Stage 3 (Applied Exercises & Practice):** Reference vs. Explanation: writing clean API specs and architectural context.
  4. **Stage 4 (Real-World Scenarios & Projects):** Living docs: docs-as-code, Markdown linting, and automated documentation workflows.

---

#### 70. `COM-108`: Cross-Cultural Communication & Global Collaboration
- **Description:** Navigate international business cultures, direct vs. indirect feedback styles, and high-context communication.
- **Category:** Communication, Writing & Public Speaking
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Remote workers, international teams, multinational leaders, and global collaborators.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Based on Erin Meyer's Culture Map framework across 8 behavioral communication scales.
- **Learning Outcomes:**
  - Differentiate high-context and low-context communication styles across cultures.
  - Navigate direct vs. indirect negative feedback without causing offense or misunderstanding.
  - Understand cultural attitudes toward hierarchy, authority, and consensus decision-making.
  - Manage time perception differences (linear vs. flexible time) in international project planning.
  - Lead inclusive meetings with non-native language speakers.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The invisible lens of culture: why well-intentioned emails trigger cross-border outrage.
  2. **Stage 2 (Core Concepts & Guided Examples):** Communication styles: low-context explicit clarity vs. high-context nuanced reading between lines.
  3. **Stage 3 (Applied Exercises & Practice):** Feedback and authority: giving critique across egalitarian vs. hierarchical team cultures.
  4. **Stage 4 (Real-World Scenarios & Projects):** Time and trust: task-based vs. relationship-based trust in distributed global teams.

---

### Emotional Intelligence, Leadership & Psychology

#### 71. `EQ-101`: Emotional Intelligence & Human Behaviour
- **Description:** Understand yourself and others better — communicate, lead and connect with more ease.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Aspiring leaders, team members, and individuals navigating complex human dynamics.
- **Prerequisites:** None. (Existing EduCaps Subject ID 3).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on the 4 classic pillars of Goleman's EQ: self-awareness, self-management, social awareness, and relationship management.
- **Learning Outcomes:**
  - Identify physiological and emotional triggers before reacting impulsively.
  - Cultivate the 'sacred pause' between stimulus and response.
  - Read non-verbal cues and assess team emotional climates.
  - Build authentic rapport and set healthy boundaries.
  - Lead others through steady, grounded emotional presence.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Foundations of EQ: the 4 pillars and why emotional competence outperforms raw IQ.
  2. **Stage 2 (Core Concepts & Guided Examples):** Self-Awareness and Self-Regulation: catching the amygdala hijack before exploding.
  3. **Stage 3 (Applied Exercises & Practice):** Social Awareness: empathy, reading rooms, and perspective taking.
  4. **Stage 4 (Real-World Scenarios & Projects):** Relationship Management: setting boundaries, resolving tension, and emotional leadership.

---

#### 72. `EQ-102`: Conflict Resolution & De-escalation Techniques
- **Description:** De-escalate workplace clashes, disarm hostility, and turn heated arguments into productive collaborations.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Intermediate
- **Target Audience:** Managers, customer support leads, team collaborators, and mediators.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Provides verbatim verbal de-escalation scripts and tactical breathing techniques to stay calm under fire.
- **Learning Outcomes:**
  - Identify the root causes of conflict (scarce resources, misaligned values, wounded ego).
  - Apply psychological de-escalation scripts to calm an enraged counterpart.
  - Separate the problem from the person during heated disputes.
  - Use the Thomas-Kilmann Conflict Mode Instrument to select the right approach (Collaborating vs. Compromising).
  - Establish collaborative agreements that prevent future friction.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The anatomy of conflict: why minor disagreements spiral into personal warfare.
  2. **Stage 2 (Core Concepts & Guided Examples):** De-escalation tactics: voice tone, lowering volume, acknowledging feelings, and venting.
  3. **Stage 3 (Applied Exercises & Practice):** Mediation frameworks: problem reframing, finding common ground, and separating interests.
  4. **Stage 4 (Real-World Scenarios & Projects):** Post-conflict repair: rebuilding team trust and establishing working agreements.

---

#### 73. `EQ-103`: Empathy & Perspective Taking in High-Stress Environments
- **Description:** Cultivate genuine cognitive empathy without taking on emotional exhaustion or burning out.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Intermediate
- **Target Audience:** Healthcare workers, managers, educators, customer advocates, and team leaders.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Distinguishes cognitive empathy (understanding another's view) from emotional contagion (absorbing their distress).
- **Learning Outcomes:**
  - Differentiate cognitive empathy, emotional empathy, and compassionate action.
  - Practice perspective-taking exercises to understand seemingly irrational behavior.
  - Protect against compassion fatigue and emotional exhaustion.
  - Validate another person's feelings without agreeing to unrealistic demands.
  - Build empathetic workplace cultures during organizational crises.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The mechanics of empathy: mirror neurons, perspective taking, and cognitive versus emotional empathy.
  2. **Stage 2 (Core Concepts & Guided Examples):** The obstacle of judgment: how ego, exhaustion, and in-group bias kill empathy.
  3. **Stage 3 (Applied Exercises & Practice):** Compassion without burnout: boundaries, emotional differentiation, and active compassion.
  4. **Stage 4 (Real-World Scenarios & Projects):** Leading with empathy in crisis: validating reality while maintaining organizational resolve.

---

#### 74. `EQ-104`: Cognitive Biases: How Our Brains Mislead Us
- **Description:** Examine the systematic errors in human thinking: confirmation bias, anchoring, sunk cost fallacy, and availability heuristic.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Investors, developers, managers, journalists, and everyday critical thinkers.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Grounds behavioral economics (Kahneman & Tversky) in modern daily software, career, and purchasing decisions.
- **Learning Outcomes:**
  - Explain System 1 (fast, intuitive) and System 2 (slow, deliberate) thinking modes.
  - Recognize Confirmation Bias and intentionally seek disconfirming evidence.
  - Break free from the Sunk Cost Fallacy in failing projects or relationships.
  - Neutralize Anchoring and Framing effects in pricing and salary discussions.
  - Implement institutional decision checklists that protect teams from collective bias.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** System 1 and System 2: heuristics as evolutionary shortcuts and their modern blind spots.
  2. **Stage 2 (Core Concepts & Guided Examples):** Confirmation bias and belief perseverance: why smart people cling to wrong ideas.
  3. **Stage 3 (Applied Exercises & Practice):** Value distortions: Sunk Cost, Loss Aversion, and the Endowment Effect.
  4. **Stage 4 (Real-World Scenarios & Projects):** Social biases: In-group favoritism, the Halo Effect, and Fundamental Attribution Error.
  5. **Stage 5 (Review, Assessment & Mastery):** De-biasing strategies: pre-mortems, red-teaming, and structured decision checklists.

---

#### 75. `EQ-105`: Resilience, Burnout Prevention & Stress Regulation
- **Description:** Regulate autonomic nervous system stress, build durable psychological resilience, and recover from professional burnout.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** High-achieving professionals, founders, caregivers, and students facing intense chronic pressure.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Integrates physiological nervous system regulation (polyvagal theory, physiological sigh) with psychological cognitive reframing.
- **Learning Outcomes:**
  - Understand the physiological biology of chronic stress and cortisol elevation.
  - Use breathing protocols (physiological sigh) to down-regulate acute anxiety in 60 seconds.
  - Identify the 3 stages of burnout: emotional exhaustion, cynicism, and reduced efficacy.
  - Reframe catastrophic self-talk using cognitive behavioral therapy (CBT) ABCDE models.
  - Construct an environment that supports sustainable high performance without self-destruction.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The neurobiology of stress: sympathetic fight-or-flight vs. parasympathetic rest-and-digest.
  2. **Stage 2 (Core Concepts & Guided Examples):** Burnout anatomy: identifying the clinical difference between normal fatigue and chronic depletion.
  3. **Stage 3 (Applied Exercises & Practice):** Somatic regulation: breathwork, movement, sleep hygiene, and physiological resets.
  4. **Stage 4 (Real-World Scenarios & Projects):** Cognitive resilience: reframing setbacks, internal locus of control, and realistic optimism.

---

#### 76. `EQ-106`: Modern Leadership: Leading Without Authority
- **Description:** Inspire teams, build alignment, and drive high-impact initiatives even when you have zero official managerial title.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Intermediate
- **Target Audience:** Individual contributors, project leads, product managers, and ambitious team members.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on building social capital, strategic reciprocity, and competence trust rather than relying on top-down authority.
- **Learning Outcomes:**
  - Differentiate positional authority from genuine earned leadership.
  - Build relational capital through competence, dependability, and generosity.
  - Align diverse stakeholders around a shared mission using lateral influence.
  - Conduct productive 1-on-1 alignment discussions across departments.
  - Lead meetings that conclude with clear ownership and enthusiasm.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The new leadership landscape: matrixed teams, remote work, and the death of command-and-control.
  2. **Stage 2 (Core Concepts & Guided Examples):** Currency of influence: competence, character, consistency, and social capital.
  3. **Stage 3 (Applied Exercises & Practice):** Lateral persuasion: understanding other department heads' incentives and KPIs.
  4. **Stage 4 (Real-World Scenarios & Projects):** Mobilizing action: running democratic brainstorms and driving collective consensus.

---

#### 77. `EQ-107`: Team Dynamics & Building Psychological Safety
- **Description:** Foster an environment where team members take risks, speak up about mistakes, and collaborate with fearless trust.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Intermediate
- **Target Audience:** Engineering managers, team leads, Agile coaches, and executives.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Brings Amy Edmondson's Harvard research on psychological safety and Google's Project Aristotle into daily team rituals.
- **Learning Outcomes:**
  - Define psychological safety and measure it on your team.
  - Replace blame-and-shame reactions with blameless post-mortem investigations.
  - Model vulnerability and acknowledge personal gaps as a team leader.
  - Encourage divergent perspectives and productive dissent during brainstorms.
  - Establish team working agreements that prevent toxic passive-aggressive behavior.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** What makes high-performing teams tick: Google's Project Aristotle and Edmondson's research.
  2. **Stage 2 (Core Concepts & Guided Examples):** The fear factor: why smart people stay silent when they spot critical project flaws.
  3. **Stage 3 (Applied Exercises & Practice):** Leader behaviors that build safety: acknowledging fallibility, asking curious questions, responding productively.
  4. **Stage 4 (Real-World Scenarios & Projects):** Team rituals: blameless retrospectives, failure celebrations, and psychological safety check-ins.

---

#### 78. `EQ-108`: Self-Compassion & Overcoming Imposter Syndrome
- **Description:** Silence your toxic inner critic, embrace realistic self-compassion, and overcome feelings of being a fraud.
- **Category:** Emotional Intelligence, Leadership & Psychology
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** High-achievers, junior developers, career switchers, and perfectionists.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Draws on Dr. Kristin Neff's self-compassion empirical research to prove self-kindness drives higher resilience than self-flagellation.
- **Learning Outcomes:**
  - Understand the roots of Imposter Phenomenon and recognize its typical triggers.
  - Differentiate destructive self-criticism from constructive self-compassion.
  - Apply the 3 components of self-compassion (Mindfulness, Common Humanity, Self-Kindness).
  - Keep an objective 'Evidence File' of completed achievements and skills.
  - Embrace the 'beginner's mindset' without shame when tackling novel challenges.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The Imposter trap: feeling like a fraud despite documented success.
  2. **Stage 2 (Core Concepts & Guided Examples):** The myth of self-criticism: why beating yourself up degrades cognitive performance.
  3. **Stage 3 (Applied Exercises & Practice):** The 3 pillars of self-compassion: self-kindness, shared humanity, and mindful acceptance.
  4. **Stage 4 (Real-World Scenarios & Projects):** Rewriting internal narratives: practical habits to celebrate progress and embrace healthy imperfection.

---

### Productivity, Focus & Digital Wellbeing

#### 79. `PROD-101`: Digital Habits & Focus in the Smartphone Age
- **Description:** Learn how to master your attention, avoid distraction and reclaim your time in a connected world.
- **Category:** Productivity, Focus & Digital Wellbeing
- **Difficulty:** Beginner
- **Target Audience:** Students, knowledge workers, and digital citizens struggling with phone screen time.
- **Prerequisites:** None. (Existing EduCaps Subject ID 2).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on device minimalism, the attention economy, and escaping variable reward dopamine loops.
- **Learning Outcomes:**
  - Understand how tech apps monetize attention via intermittent variable rewards.
  - Declutter smartphone notifications, badges, and toxic infinite feeds.
  - Practice single-tasking and avoid attention residue from task switching.
  - Embrace intentional boredom to spark deep creative problem solving.
  - Establish morning and evening phone-free sanctuary rituals.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The Attention Economy: notification feeds, dopamine traps, and attention residue.
  2. **Stage 2 (Core Concepts & Guided Examples):** Deep Work vs. Shallow Work: why distraction destroys high-value output.
  3. **Stage 3 (Applied Exercises & Practice):** Digital Minimalism: notification pruning, grayscale mode, and app audits.
  4. **Stage 4 (Real-World Scenarios & Projects):** Sustainable focus habits: single-tasking rituals, boredom tolerance, and the attention dividend.

---

#### 80. `PROD-102`: Time Architecture & Energy Management
- **Description:** Manage your energy rather than just your time: chronotypes, ultradian rhythms, calendar time-blocking, and boundary defense.
- **Category:** Productivity, Focus & Digital Wellbeing
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Overwhelmed professionals, students, and freelancers managing busy schedules.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Prioritizes biological energy curves (ultradian 90-minute focus cycles) over rigid to-do list packing.
- **Learning Outcomes:**
  - Audit personal chronotype and identify peak daily cognitive energy hours.
  - Implement calendar time-blocking for priority deep-work commitments.
  - Defend schedule boundaries against non-essential meeting creep.
  - Structure intentional recovery breaks following 90-minute ultradian cycles.
  - Eliminate 'calendar confetti' to secure uninterrupted focus blocks.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The energy paradox: why managing minutes fails if your battery is drained.
  2. **Stage 2 (Core Concepts & Guided Examples):** Biological rhythms: chronotypes, circadian peaks, and ultradian 90-minute focus waves.
  3. **Stage 3 (Applied Exercises & Practice):** Calendar architecture: time-blocking, buffer days, and theme days.
  4. **Stage 4 (Real-World Scenarios & Projects):** Defending the calendar: saying no gracefully and auditing recurring commitments.

---

#### 81. `PROD-103`: Habit Formation & Behavioral Change Science
- **Description:** Build atomic habits that stick and dismantle unwanted routines using neuroscience and behavioral design.
- **Category:** Productivity, Focus & Digital Wellbeing
- **Difficulty:** Beginner
- **Target Audience:** Anyone seeking permanent positive lifestyle, fitness, learning, or career habit transformation.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Brings the cue-routine-reward loop and habit-stacking into micro-learning applications.
- **Learning Outcomes:**
  - Explain the neurological Habit Loop: Cue, Craving, Response, and Reward.
  - Apply the 4 Laws of Behavior Change to make good habits inevitable.
  - Implement 'Habit Stacking' by anchoring new habits onto existing routines.
  - Design environmental choice architecture that reduces friction for good habits.
  - Recover gracefully when a habit streak is broken using the 'Never Miss Twice' rule.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The neuroscience of automaticity: basal ganglia wiring and the 4-part habit loop.
  2. **Stage 2 (Core Concepts & Guided Examples):** Making it obvious and attractive: environment design, cues, and temptation bundling.
  3. **Stage 3 (Applied Exercises & Practice):** Making it easy: reducing friction, the 2-minute rule, and habit scaling.
  4. **Stage 4 (Real-World Scenarios & Projects):** Making it satisfying: tracking, accountability, and the 'Never Miss Twice' recovery rule.

---

#### 82. `PROD-104`: Deep Work & Cognitive Ergonomics
- **Description:** Cultivate the rare and valuable ability to focus without distraction on cognitively demanding tasks.
- **Category:** Productivity, Focus & Digital Wellbeing
- **Difficulty:** Intermediate
- **Target Audience:** Knowledge workers, writers, software developers, researchers, and creators.
- **Prerequisites:** Basic focus literacy (PROD-101).
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Operationalizes Cal Newport's Deep Work philosophy with practical workspace and scheduling playbooks.
- **Learning Outcomes:**
  - Differentiate Deep Work from shallow administrative busywork.
  - Select a deep work scheduling philosophy (Bimodal, Rhythmic, Monastic, Journalistic).
  - Construct a physical and digital focus cockpit that eliminates micro-interruptions.
  - Build shutdown rituals that free your mind from work anxiety during evenings.
  - Measure and increase daily deep work capacity over time.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The Deep Work thesis: why focused attention is the superpower of the 21st century.
  2. **Stage 2 (Core Concepts & Guided Examples):** Scheduling philosophies: finding the deep work rhythm that matches your career reality.
  3. **Stage 3 (Applied Exercises & Practice):** The focus ritual: location, environmental design, focus triggers, and warmups.
  4. **Stage 4 (Real-World Scenarios & Projects):** The daily shutdown ritual: offloading open cognitive loops for guilt-free evening rest.

---

#### 83. `PROD-105`: Information Overload: Curation & Personal Knowledge Management
- **Description:** Build a 'Second Brain': capture insights, organize knowledge with the PARA method, and turn reading into output.
- **Category:** Productivity, Focus & Digital Wellbeing
- **Difficulty:** Intermediate
- **Target Audience:** Researchers, students, writers, developers, and information workers.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Implements Tiago Forte's CODE (Capture, Organize, Distill, Express) and PARA (Projects, Areas, Resources, Archives).
- **Learning Outcomes:**
  - Overcome digital hoarding by adopting the CODE knowledge curation pipeline.
  - Organize digital files and notes actionable by project using the PARA method.
  - Practice progressive summarization to distill long articles into executive highlights.
  - Shift focus from passive content consumption to active creative output.
  - Create a resilient personal knowledge repository that compounds over decades.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The digital hoarder's trap: why bookmarking 1,000 articles changes nothing.
  2. **Stage 2 (Core Concepts & Guided Examples):** The CODE framework: Capture what resonates, Organize for action, Distill essence, Express output.
  3. **Stage 3 (Applied Exercises & Practice):** The PARA method: structuring digital life by Projects, Areas, Resources, and Archives.
  4. **Stage 4 (Real-World Scenarios & Projects):** Progressive summarization and knowledge retrieval: turning past reading into instant assets.

---

#### 84. `PROD-106`: Procrastination Decoded: Action Triggers & Momentum
- **Description:** Understand the true emotional roots of procrastination and use behavioral momentum tactics to get started effortlessly.
- **Category:** Productivity, Focus & Digital Wellbeing
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Chronic delayers, perfectionists, students, and workers paralyzed by looming deadlines.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Treats procrastination as an emotional regulation problem (fear of failure, boredom, overwhelm) rather than poor time management.
- **Learning Outcomes:**
  - Deconstruct procrastination into emotional avoidance rather than laziness.
  - Overcome perfectionism paralysis with the 'permission to write junk' heuristic.
  - Use the 5-Minute Rule to shatter task initiation friction.
  - Break monolithic intimidating projects into micro-executable next actions.
  - Eliminate self-blame cycles that perpetuate delayed action.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The psychology of delay: why procrastination is an emotional defense mechanism, not laziness.
  2. **Stage 2 (Core Concepts & Guided Examples):** The perfectionism trap: all-or-nothing thinking, fear of judgment, and avoidance.
  3. **Stage 3 (Applied Exercises & Practice):** Action triggers: the 5-minute rule, micro-stepping, and lowering activation energy.
  4. **Stage 4 (Real-World Scenarios & Projects):** Momentum engineering: harnessing dopamine through visible micro-wins.

---

#### 85. `PROD-107`: Sleep, Rest & Cognitive Recovery for Peak Performance
- **Description:** Unlock the biological foundation of memory and focus: sleep cycles, circadian light, non-sleep deep rest (NSDR), and mental recovery.
- **Category:** Productivity, Focus & Digital Wellbeing
- **Difficulty:** Beginner
- **Target Audience:** Anyone suffering from brain fog, afternoon crashes, and insomnia.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Grounds sleep architecture in peer-reviewed neuroscience (Huberman, Matthew Walker) with practical evening protocols.
- **Learning Outcomes:**
  - Explain sleep architecture: NREM slow-wave sleep, REM dreaming, and memory consolidation.
  - Anchor circadian rhythms using morning sunlight and evening light dimming.
  - Optimize sleep temperature, caffeine cutoff windows, and sleep environment.
  - Practice Non-Sleep Deep Rest (NSDR) or Yoga Nidra for rapid midday cognitive recovery.
  - Establish restorative weekend habits that prevent Monday morning grogginess.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The science of sleep: what the brain does at night (glymphatic wash, memory filing).
  2. **Stage 2 (Core Concepts & Guided Examples):** Circadian biology: photons, melatonin, adenosine accumulation, and caffeine mechanics.
  3. **Stage 3 (Applied Exercises & Practice):** The ultimate sleep environment: darkness, temperature drop, soundscapes, and rituals.
  4. **Stage 4 (Real-World Scenarios & Projects):** Active daytime rest: power naps, NSDR protocols, and cognitive decompression.

---

### Business, Entrepreneurship & Career Readiness

#### 86. `BUS-101`: Startup Fundamentals: From Idea to Customer Discovery
- **Description:** Validate ideas, interview prospective customers without bias, build MVPs, and achieve problem-solution fit.
- **Category:** Business, Entrepreneurship & Career Readiness
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Aspiring entrepreneurs, indie hackers, intrapreneurs, and product creators.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on 'The Mom Test' customer interview methodology to avoid false-positive encouragement.
- **Learning Outcomes:**
  - Evaluate business ideas using problem severity, market size, and founder-market fit.
  - Conduct customer discovery interviews that extract honest historical facts.
  - Define a Minimum Viable Product (MVP) that tests core assumptions with minimal code.
  - Recognize true Problem-Solution fit and Product-Market fit indicators.
  - Pivot product hypotheses based on customer data without emotional attachment.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Idea generation: finding expensive, hair-on-fire problems worth solving.
  2. **Stage 2 (Core Concepts & Guided Examples):** Customer discovery: The Mom Test rules for interviewing without seeking approval.
  3. **Stage 3 (Applied Exercises & Practice):** The MVP mindset: building the simplest artifact to validate demand.
  4. **Stage 4 (Real-World Scenarios & Projects):** Early traction: finding your first 10 paying customers manually.
  5. **Stage 5 (Review, Assessment & Mastery):** Iterating toward Product-Market fit and knowing when to pivot.

---

#### 87. `BUS-102`: Product Management: Defining What to Build and Why
- **Description:** Bridge engineering, design, and business: master PRDs, prioritization matrices (RICE), user stories, and roadmaps.
- **Category:** Business, Entrepreneurship & Career Readiness
- **Difficulty:** Intermediate
- **Target Audience:** Product managers, technical founders, and developers transitioning to product roles.
- **Prerequisites:** Basic understanding of software development workflows.
- **Curriculum Scope:** 5 Topics | Target: 75 Capsules
- **Pedagogical Differentiation:** Prioritizes outcome-focused roadmaps over output-focused feature factory velocity.
- **Learning Outcomes:**
  - Define the product manager's role at the intersection of UX, tech, and business.
  - Draft clear Product Requirement Documents (PRDs) that empower engineering teams.
  - Prioritize feature backlogs using frameworks like RICE, Kano, and Value vs. Effort.
  - Write user stories with unambiguous acceptance criteria.
  - Track product success using North Star metrics and leading indicators.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The PM role: discovery vs. delivery, outcomes over feature outputs.
  2. **Stage 2 (Core Concepts & Guided Examples):** Framing the problem: user personas, journey mapping, and value propositions.
  3. **Stage 3 (Applied Exercises & Practice):** Prioritization science: RICE scoring, MoSCoW, and saying no to executive pet projects.
  4. **Stage 4 (Real-World Scenarios & Projects):** Execution artifacts: writing great PRDs, user stories, and acceptance criteria.
  5. **Stage 5 (Review, Assessment & Mastery):** Product analytics: cohorts, retention curves, funnel drop-offs, and feature adoption.

---

#### 88. `BUS-103`: Customer Research & User Interview Techniques
- **Description:** Uncover what customers truly need through ethnographic observation, usability testing, and qualitative interviews.
- **Category:** Business, Entrepreneurship & Career Readiness
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** UX researchers, product designers, marketers, and startup founders.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on past behavioral evidence over hypothetical future customer promises.
- **Learning Outcomes:**
  - Formulate research plans with specific falsifiable learning goals.
  - Recruit representative users without skewing toward friendly cheerleaders.
  - Ask neutral, open-ended non-leading interview questions.
  - Conduct think-aloud usability testing to spot interface friction points.
  - Synthesize qualitative interview transcripts into actionable thematic affinity maps.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Why qualitative research matters: metrics tell you what; interviews tell you why.
  2. **Stage 2 (Core Concepts & Guided Examples):** The interview craft: building rapport, embracing silence, and probing past behavior.
  3. **Stage 3 (Applied Exercises & Practice):** Usability testing: the think-aloud protocol and watching where users stumble.
  4. **Stage 4 (Real-World Scenarios & Projects):** Synthesis: affinity diagramming, customer journey maps, and presenting insights to teams.

---

#### 89. `BUS-104`: Modern Marketing Fundamentals: Organic, Search & Social
- **Description:** Understand modern growth: SEO mechanics, content marketing, distribution loops, and audience building.
- **Category:** Business, Entrepreneurship & Career Readiness
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Marketers, creators, founders, and small business owners.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on building sustainable distribution flywheels rather than wasting money on random paid ad experiments.
- **Learning Outcomes:**
  - Understand the classic marketing funnel: Awareness, Consideration, Conversion, Retention.
  - Master on-page SEO fundamentals (search intent, keywords, technical health).
  - Create high-value content marketing assets that attract inbound traffic.
  - Build distribution flywheels where customer usage drives organic referrals.
  - Calculate conversion rates across marketing touchpoints.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Marketing foundations: positioning, target audience segmentation, and the value proposition.
  2. **Stage 2 (Core Concepts & Guided Examples):** Search Engine Optimization (SEO): search intent, keywords, authority, and backlinks.
  3. **Stage 3 (Applied Exercises & Practice):** Content and community: creating educational assets that build trust and inbound demand.
  4. **Stage 4 (Real-World Scenarios & Projects):** Social distribution: tailoring narratives to platform algorithms and building an email list.
  5. **Stage 5 (Review, Assessment & Mastery):** Growth flywheels: viral loops, referral mechanisms, and conversion funnel optimization.

---

#### 90. `BUS-105`: Career Navigation: Interviewing, Portfolios & Salary Negotiation
- **Description:** Accelerate your professional trajectory: build standout portfolios, ace behavioral interviews, and negotiate market-rate pay.
- **Category:** Business, Entrepreneurship & Career Readiness
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Job seekers, graduating students, and professionals aiming for career advancement.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Focuses on the hiring manager's perspective: de-risking the hire and demonstrating business impact.
- **Learning Outcomes:**
  - Craft high-signal resumes that pass automated screening and catch recruiter attention.
  - Build project portfolios that highlight real business outcomes and problem solving.
  - Master the STAR method (Situation, Task, Action, Result) for behavioral interviews.
  - Conduct reverse interviews to evaluate company culture and manager competence.
  - Negotiate base salary, equity, bonuses, and remote flexibility professionally.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The hiring manager's mind: how hiring decisions are actually made behind closed doors.
  2. **Stage 2 (Core Concepts & Guided Examples):** High-signal artifacts: modern resume formatting, LinkedIn optimization, and case-study portfolios.
  3. **Stage 3 (Applied Exercises & Practice):** Interview mastery: behavioral storytelling with the STAR method and technical screening poise.
  4. **Stage 4 (Real-World Scenarios & Projects):** Offer evaluation and negotiation: scripts, anchoring, counter-offers, and total compensation math.

---

#### 91. `BUS-106`: Freelancing & Independent Consulting Mastery
- **Description:** Build a thriving independent business: client acquisition, value-based pricing, bulletproof contracts, and pipeline management.
- **Category:** Business, Entrepreneurship & Career Readiness
- **Difficulty:** Intermediate
- **Target Audience:** Freelancers, agency founders, consultants, and developers going solo.
- **Prerequisites:** A marketable technical, creative, or business skill.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Transitions independent professionals from trading hours for money to value-based pricing and recurring retainers.
- **Learning Outcomes:**
  - Define a profitable consulting niche with high willingness-to-pay.
  - Transition from hourly billing to value-based project pricing and retainers.
  - Draft clear client proposals, scopes of work, and protective contracts.
  - Build an inbound client pipeline that prevents the 'feast-and-famine' cycle.
  - Manage client expectations and eliminate scope creep gracefully.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Going independent: choosing a specialized niche and positioning yourself as an expert.
  2. **Stage 2 (Core Concepts & Guided Examples):** Pricing strategies: why hourly billing caps income and how to price on client value.
  3. **Stage 3 (Applied Exercises & Practice):** Client acquisition: warm outreach, case studies, referrals, and inbound content.
  4. **Stage 4 (Real-World Scenarios & Projects):** Operations and protection: contracts, milestone billing, scope creep defense, and retainers.

---

#### 92. `BUS-107`: Financial Metrics for Businesses: CAC, LTV & Unit Economics
- **Description:** Understand how businesses make or lose money: Customer Acquisition Cost, Lifetime Value, Gross Margins, and Churn.
- **Category:** Business, Entrepreneurship & Career Readiness
- **Difficulty:** Intermediate
- **Target Audience:** Startup founders, product managers, investors, and business analysts.
- **Prerequisites:** Basic arithmetic.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on SaaS and digital business unit economics with intuitive cash-multiplier spreadsheets.
- **Learning Outcomes:**
  - Calculate Customer Acquisition Cost (CAC) and Customer Lifetime Value (LTV).
  - Evaluate unit economic health using the LTV:CAC ratio and payback period.
  - Measure customer churn (logo churn vs. net revenue churn).
  - Read Income Statements, Balance Sheets, and Cash Flow Statements.
  - Analyze gross margins and operating leverage in business models.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Unit economics 101: does a single customer make you money or lose you money?
  2. **Stage 2 (Core Concepts & Guided Examples):** Acquisition and Retention metrics: CAC, payback period, churn rate, and expansion revenue.
  3. **Stage 3 (Applied Exercises & Practice):** SaaS metrics deep-dive: MRR, ARR, Net Revenue Retention (NRR), and runway.
  4. **Stage 4 (Real-World Scenarios & Projects):** Financial statements for operators: P&L statements, gross margins, and burn rates.

---

### Science, Everyday Technology & Sustainability

#### 93. `SCI-101`: Sustainable Living in Everyday Life
- **Description:** Simple habits to live greener, save resources and protect our planet — without extremes.
- **Category:** Science, Everyday Technology & Sustainability
- **Difficulty:** Beginner
- **Target Audience:** Everyday citizens, households, and environmentally conscious learners.
- **Prerequisites:** None. (Existing EduCaps Subject ID 5).
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on achievable household eco-habits (food waste, energy savers, transit) without eco-anxiety or moral shaming.
- **Learning Outcomes:**
  - Calculate and reduce personal household ecological and carbon footprints.
  - Apply the 3 R's: prioritizing Refusing and Reducing over passive recycling.
  - Eliminate single-use plastics and microplastic contamination in domestic settings.
  - Optimize home energy and water usage to reduce environmental strain and bills.
  - Adopt sustainable seasonal dietary habits that cut food waste.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Why sustainability matters: ecological footprints and individual leverage.
  2. **Stage 2 (Core Concepts & Guided Examples):** Household resource efficiency: energy, water, heating, and phantom power.
  3. **Stage 3 (Applied Exercises & Practice):** Conscious consumption: single-use plastics, mindful shopping, and sustainable food.
  4. **Stage 4 (Real-World Scenarios & Projects):** Waste management: composting, recycling reality, and sustaining green habits.

---

#### 94. `SCI-102`: Climate Science Essentials: What the Data Shows
- **Description:** Understand atmospheric science, greenhouse gases, historical climate data, feedback loops, and IPCC emissions scenarios.
- **Category:** Science, Everyday Technology & Sustainability
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Citizens, students, policymakers, and professionals seeking empirical climate literacy.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Grounds climate mechanisms directly in empirical temperature records, ice core data, and greenhouse physics without political spin.
- **Learning Outcomes:**
  - Explain the greenhouse effect and how CO2 and methane trap infrared radiation.
  - Read and interpret paleoclimate ice core data and Keeling curve CO2 records.
  - Understand climate feedback loops (albedo effect, permafrost thaw, ocean acidification).
  - Differentiate climate mitigation (reducing emissions) from adaptation (building resilience).
  - Evaluate global decarbonization pathways across energy, industry, and agriculture.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The physical greenhouse effect: solar radiation, infrared absorption, and planetary heat balances.
  2. **Stage 2 (Core Concepts & Guided Examples):** The historical record: ice cores, tree rings, and the Industrial Revolution inflection point.
  3. **Stage 3 (Applied Exercises & Practice):** Systemic climate feedback loops: ice-albedo, ocean currents, and methane tipping points.
  4. **Stage 4 (Real-World Scenarios & Projects):** Impacts: sea level rise, extreme weather events, biodiversity, and ocean acidification.
  5. **Stage 5 (Review, Assessment & Mastery):** The path to Net Zero: mitigation, carbon budgets, adaptation, and renewable transitions.

---

#### 95. `SCI-103`: Renewable Energy Systems: Solar, Wind & Storage
- **Description:** Explore the technological revolution powering the clean energy transition: photovoltaics, wind turbines, grid batteries, and hydrogen.
- **Category:** Science, Everyday Technology & Sustainability
- **Difficulty:** Intermediate
- **Target Audience:** Engineers, investors, environmentalists, and clean-tech enthusiasts.
- **Prerequisites:** Basic high school physics.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Examines the engineering economics (Levelized Cost of Energy - LCOE) and grid storage balancing challenges.
- **Learning Outcomes:**
  - Explain how photovoltaic solar cells convert photons into electrical current.
  - Understand aerodynamic lift and mechanical generation in wind turbines.
  - Analyze grid storage solutions: Lithium-ion, flow batteries, and pumped-storage hydro.
  - Evaluate Levelized Cost of Electricity (LCOE) trends between fossil and clean sources.
  - Understand smart grid modernization and intermittency management.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The global power grid: AC/DC transmission, base load, peaking plants, and the intermittency puzzle.
  2. **Stage 2 (Core Concepts & Guided Examples):** Solar photovoltaics: semiconductor bandgaps, solar panel efficiency, and rooftop systems.
  3. **Stage 3 (Applied Exercises & Practice):** Wind energy: turbine aerodynamics, Betz limit, offshore wind farms, and capacity factors.
  4. **Stage 4 (Real-World Scenarios & Projects):** Energy storage: battery chemistry, pumped hydro, hydrogen carriers, and grid integration.

---

#### 96. `SCI-104`: Everyday Physics: How the Modern World Works
- **Description:** Understand the physical laws shaping daily life: gravity, thermodynamics, electricity, radio waves, and microwave ovens.
- **Category:** Science, Everyday Technology & Sustainability
- **Difficulty:** Beginner
- **Target Audience:** Curious learners of all ages who look at modern technology and wonder 'How does that work?'.
- **Prerequisites:** None. Suitable for both Kids and Standard modes.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Answers concrete everyday questions: why airplanes fly, how microwaves heat food, why the sky is blue, and how GPS works.
- **Learning Outcomes:**
  - Explain Newton's Laws of Motion through cars, sports, and rockets.
  - Understand the laws of thermodynamics: why heat flows from hot to cold and why entropy rises.
  - Explain the electromagnetic spectrum: visible light, radio, Wi-Fi, and X-rays.
  - Understand aerodynamics: Bernoulli's principle, lift, and drag.
  - Explain the everyday physics behind household appliances (refrigerators, induction stoves).
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Forces in motion: inertia, friction, gravity, momentum, and action-reaction pairs.
  2. **Stage 2 (Core Concepts & Guided Examples):** Thermodynamics and heat: conduction, convection, radiation, and refrigeration cycles.
  3. **Stage 3 (Applied Exercises & Practice):** Electricity and magnetism: circuits, electromagnetic induction, motors, and generators.
  4. **Stage 4 (Real-World Scenarios & Projects):** Waves and light: reflection, refraction, optics, radio signals, and why the sky is blue.
  5. **Stage 5 (Review, Assessment & Mastery):** Everyday wonders: the physics of GPS time dilation, flight, and smartphone touchscreens.

---

#### 97. `SCI-105`: Human Biology & Nutrition Literacy
- **Description:** Understand your body: macronutrients, metabolism, the gut microbiome, insulin mechanics, and cardiovascular health.
- **Category:** Science, Everyday Technology & Sustainability
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Anyone wanting to make science-backed nutrition and health choices without falling for fad diets.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Focuses on human physiology and metabolic pathways rather than dogmatic dietary branding or commercial supplement marketing.
- **Learning Outcomes:**
  - Differentiate the metabolic functions of carbohydrates, proteins, and fats.
  - Explain insulin response, blood glucose regulation, and metabolic flexibility.
  - Understand the role of the gut microbiome in digestion, immunity, and mood.
  - Read nutrition food labels critically and identify hidden ultra-processed ingredients.
  - Evaluate cardiovascular health markers (cholesterol, blood pressure) objectively.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The human engine: cellular respiration, ATP generation, and basal metabolic rate.
  2. **Stage 2 (Core Concepts & Guided Examples):** Macronutrients decoded: protein synthesis, carbohydrate glycogen storage, and essential fatty acids.
  3. **Stage 3 (Applied Exercises & Practice):** Hormonal regulation: insulin, glucagon, ghrelin, and leptin hunger cues.
  4. **Stage 4 (Real-World Scenarios & Projects):** Gut health and micronutrients: the microbiome, vitamins, minerals, and whole foods.

---

#### 98. `SCI-106`: Scientific Literacy: Evaluating Claims, Studies & Statistics
- **Description:** Learn to think like a scientist: peer review, p-hacking, randomized controlled trials (RCTs), and spotting bogus health claims.
- **Category:** Science, Everyday Technology & Sustainability
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Critical thinkers, consumers, journalists, and students navigating conflicting health and science news.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Teaches how to read scientific abstracts and detect media sensationalism ('Coffee cures cancer / Coffee causes cancer').
- **Learning Outcomes:**
  - Understand the hierarchy of scientific evidence (case studies vs. RCTs vs. meta-analyses).
  - Differentiate causation from mere statistical correlation.
  - Spot p-hacking, publication bias, and small sample size anomalies in reported studies.
  - Critique sensationalized science headlines using primary study findings.
  - Evaluate conflict-of-interest disclosures and corporate-funded research claims.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The scientific method: hypotheses, falsifiability, and controlled experimentation.
  2. **Stage 2 (Core Concepts & Guided Examples):** The evidence pyramid: from anecdotal opinion to randomized trials and systematic reviews.
  3. **Stage 3 (Applied Exercises & Practice):** Statistical traps in science: p-hacking, correlation vs. causation, and publication bias.
  4. **Stage 4 (Real-World Scenarios & Projects):** The media translation filter: how preliminary mouse studies become sensational headlines.

---

#### 99. `SCI-107`: Circular Economy, Recycling & Waste Reduction
- **Description:** Explore the shift from linear 'take-make-waste' manufacturing to regenerative circular design, repair, and closed-loop material cycles.
- **Category:** Science, Everyday Technology & Sustainability
- **Difficulty:** Intermediate
- **Target Audience:** Designers, business operators, environmentalists, and product creators.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on industrial design and systemic supply chain redesign rather than putting the entire burden on consumer recycling bins.
- **Learning Outcomes:**
  - Differentiate linear economic models from regenerative circular loops.
  - Explain the technical cycle (metals, polymers) vs. biological cycle (compostables).
  - Understand Design for Disassembly and Right-to-Repair principles.
  - Analyze Extended Producer Responsibility (EPR) regulations and corporate take-back schemes.
  - Identify business opportunities in product-as-a-service and refurbishment.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The linear trap: resource extraction, built-in obsolescence, and landfill accumulation.
  2. **Stage 2 (Core Concepts & Guided Examples):** The Circular Butterfly Diagram: biological nutrients vs. technical materials.
  3. **Stage 3 (Applied Exercises & Practice):** Design for disassembly: modular electronics, repairability, and material passports.
  4. **Stage 4 (Real-World Scenarios & Projects):** Business models in circularity: Product-as-a-Service, remanufacturing, and industrial symbiosis.

---

### Creative Thinking, Problem Solving & Design

#### 100. `CRT-101`: Design Thinking: Human-Centered Problem Solving
- **Description:** Solve complex, ambiguous challenges using the 5-stage Stanford d.school Design Thinking framework.
- **Category:** Creative Thinking, Problem Solving & Design
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Designers, product teams, educators, founders, and innovators.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Emphasizes hands-on rapid low-fidelity prototyping and user empathy over polished committee presentations.
- **Learning Outcomes:**
  - Apply the 5 phases of Design Thinking: Empathize, Define, Ideate, Prototype, Test.
  - Synthesize user observations into compelling 'How Might We' (HMW) opportunity statements.
  - Lead divergent brainstorming sessions that generate novel creative possibilities.
  - Build low-fidelity paper and digital prototypes in hours instead of weeks.
  - Conduct user testing sessions to iterate on prototypes based on direct feedback.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** What is Design Thinking: why analytical logic fails for human-centered wicked problems.
  2. **Stage 2 (Core Concepts & Guided Examples):** Phase 1 & 2: Empathizing with users and defining the point-of-view problem statement.
  3. **Stage 3 (Applied Exercises & Practice):** Phase 3: Ideation, divergent thinking, and framing 'How Might We' prompts.
  4. **Stage 4 (Real-World Scenarios & Projects):** Phase 4: Rapid prototyping: paper models, roleplay, and wireframe mockups.
  5. **Stage 5 (Review, Assessment & Mastery):** Phase 5: User testing, feedback integration, and continuous iterative refinement.

---

#### 101. `CRT-102`: First Principles Thinking: Reasoning from the Ground Up
- **Description:** Break down complex problems into fundamental physical truths and reason upward to discover breakthrough innovations.
- **Category:** Creative Thinking, Problem Solving & Design
- **Difficulty:** Intermediate
- **Target Audience:** Entrepreneurs, scientists, engineers, and ambitious problem solvers.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Directly contrasts reasoning by analogy (copying others with slight tweaks) against reasoning from foundational first principles.
- **Learning Outcomes:**
  - Differentiate reasoning by analogy from reasoning by first principles.
  - Use Socratic questioning to strip away untested assumptions and conventions.
  - Boil complex cost or engineering problems down to their fundamental material limits.
  - Reconstruct novel solutions upward from basic components.
  - Apply first-principles thinking to personal career and business dilemmas.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The trap of analogy: why copying industry conventions blinds creators to breakthroughs.
  2. **Stage 2 (Core Concepts & Guided Examples):** The Socratic method: interrogating assumptions, clarifying terms, and seeking proof.
  3. **Stage 3 (Applied Exercises & Practice):** Deconstructing problems to bedrock: physical laws, fundamental materials, and true constraints.
  4. **Stage 4 (Real-World Scenarios & Projects):** Rebuilding from scratch: novel combinations, counter-intuitive designs, and innovation case studies.

---

#### 102. `CRT-103`: Creative Ideation & Divergent Thinking Techniques
- **Description:** Break mental blocks and generate hundreds of novel ideas using SCAMPER, lateral thinking, and constraint inversion.
- **Category:** Creative Thinking, Problem Solving & Design
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Writers, designers, marketers, engineers, and creative thinkers.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Focuses on systematic creative heuristics rather than waiting passively for an unpredictable 'muse' to strike.
- **Learning Outcomes:**
  - Differentiate divergent ideation (generating options) from convergent evaluation (selecting winners).
  - Apply the SCAMPER creative tool (Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse).
  - Use deliberate constraints to unlock breakthrough creative ingenuity.
  - Conduct lateral thinking exercises (random entry, provocative operations).
  - Filter and refine raw brainstormed lists into viable, high-potential concepts.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** The anatomy of creativity: associative memory, neuro-connections, and deferring judgment.
  2. **Stage 2 (Core Concepts & Guided Examples):** Divergence vs. Convergence: why mixing ideation with critique destroys innovation.
  3. **Stage 3 (Applied Exercises & Practice):** The SCAMPER framework in practice: systematic transformation of existing concepts.
  4. **Stage 4 (Real-World Scenarios & Projects):** Constraint manipulation, lateral thinking jumps, and evaluating final concept viability.

---

#### 103. `CRT-104`: User Experience (UX) & User Interface (UI) Design Principles
- **Description:** Design intuitive, delightful digital interfaces: Jakob's Law, Fitts's Law, visual hierarchy, wireframing, and micro-interactions.
- **Category:** Creative Thinking, Problem Solving & Design
- **Difficulty:** Beginner to Intermediate
- **Target Audience:** Developers, aspiring product designers, and web creators.
- **Prerequisites:** None.
- **Curriculum Scope:** 5 Topics | Target: 70 Capsules
- **Pedagogical Differentiation:** Focuses on cognitive usability laws (Nielsen Norman heuristics, psychology of affordances) over trendy visual styling.
- **Learning Outcomes:**
  - Apply fundamental UX laws: Jakob's Law, Fitts's Law, Hick's Law, and Miller's Law.
  - Establish clear visual hierarchy using scale, contrast, proximity, and spacing.
  - Design clear interface affordances, signifiers, and immediate system feedback.
  - Construct low-fidelity wireframes and user flow diagrams.
  - Audit web and mobile screens against Nielsen's 10 Usability Heuristics.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** What makes good design: affordances, signifiers, mental models, and Norman doors.
  2. **Stage 2 (Core Concepts & Guided Examples):** Psychological UX laws: Jakob's law of familiarity, Fitts's law of target sizes, and Hick's law of choices.
  3. **Stage 3 (Applied Exercises & Practice):** UI visual fundamentals: typography scales, spacing grids, color systems, and contrast.
  4. **Stage 4 (Real-World Scenarios & Projects):** Interaction states: hover, focus, active, loading, error, and empty states.
  5. **Stage 5 (Review, Assessment & Mastery):** Usability heuristics: Nielsen's 10 principles and conducting a UX expert audit.

---

#### 104. `CRT-105`: Systems Thinking: Mapping Feedback Loops & Side Effects
- **Description:** Understand complex systems: stocks, flows, reinforcing feedback, balancing feedback, delayed effects, and unintended consequences.
- **Category:** Creative Thinking, Problem Solving & Design
- **Difficulty:** Intermediate
- **Target Audience:** Leaders, policymakers, engineers, software architects, and strategic analysts.
- **Prerequisites:** None.
- **Curriculum Scope:** 4 Topics | Target: 65 Capsules
- **Pedagogical Differentiation:** Brings Donella Meadows' 'Thinking in Systems' concepts to life through real corporate, ecological, and software examples.
- **Learning Outcomes:**
  - Deconstruct systems into stocks, inflows, outflows, and feedback loops.
  - Identify Reinforcing loops (exponential growth/collapse) and Balancing loops (homeostasis).
  - Understand why time delays cause massive overshoot and oscillation in systems.
  - Spot systemic archetypes (Tragedy of the Commons, Shifting the Burden, Fixes that Fail).
  - Identify high-leverage intervention points to transform systemic performance.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Beyond linear cause-and-effect: introducing stocks, flows, and systemic interconnectivity.
  2. **Stage 2 (Core Concepts & Guided Examples):** Feedback dynamics: reinforcing loops (growth engines) and balancing loops (stabilizing limits).
  3. **Stage 3 (Applied Exercises & Practice):** Delays and oscillations: why immediate intuitive fixes frequently worsen systemic problems.
  4. **Stage 4 (Real-World Scenarios & Projects):** Leverage points: Meadows' 12 places to intervene in a system to produce lasting change.

---

#### 105. `CRT-106`: Visual Thinking & Sketch-Noting for Complex Ideas
- **Description:** Synthesize and communicate abstract concepts using simple hand-drawn shapes, arrows, visual metaphors, and layout frameworks.
- **Category:** Creative Thinking, Problem Solving & Design
- **Difficulty:** Beginner
- **Target Audience:** Thinkers, speakers, managers, students, and engineers who struggle to explain ideas with text alone.
- **Prerequisites:** None. Zero artistic drawing talent required.
- **Curriculum Scope:** 4 Topics | Target: 60 Capsules
- **Pedagogical Differentiation:** Teaches functional visual thinking ('drawing to think and communicate') rather than fine art illustration.
- **Learning Outcomes:**
  - Draw the 5 basic visual alphabet shapes (circle, square, triangle, line, dot).
  - Combine visual primitives to represent everyday abstract concepts (lightbulb for ideas, gears for processes).
  - Structure sketch-note layouts: linear, path, radial, and modular container grids.
  - Use visual connectors, arrows, and spatial grouping to illustrate causal relationships.
  - Facilitate live whiteboard sessions that align cross-functional teams.
- **5-Stage Curriculum Progression:**
  1. **Stage 1 (Foundations & Vocabulary):** Visual thinking fundamentals: the basic visual alphabet and overcoming the 'I can't draw' fear.
  2. **Stage 2 (Core Concepts & Guided Examples):** Visual vocabulary: translating abstract words (growth, challenge, connection) into simple icons.
  3. **Stage 3 (Applied Exercises & Practice):** Spatial organization: layouts, visual hierarchy, containers, and color accents.
  4. **Stage 4 (Real-World Scenarios & Projects):** Visual communication in practice: live whiteboarding, sketch-noting meetings, and visual summaries.

---
