// static/js/main.js
// EduCaps Interactive Client Engine

document.addEventListener('DOMContentLoaded', function() {
    console.log('EduCaps client engine loaded.');

    // 1. PWA Service Worker Registration
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js')
                .then(reg => console.log('EduCaps ServiceWorker registered:', reg.scope))
                .catch(err => console.log('EduCaps ServiceWorker registration skipped:', err));
        });
    }

    // 2. Interactive 3D Flip Card System (Keyboard + Click/Touch)
    const flipCards = document.querySelectorAll('.flip-card');
    flipCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Prevent flipping if clicked on a button or link inside
            if (e.target.closest('button') || e.target.closest('a') || e.target.closest('input')) {
                return;
            }
            this.classList.toggle('flipped');
        });

        card.addEventListener('keydown', function(e) {
            if (e.key === ' ' || e.key === 'Enter') {
                e.preventDefault();
                this.classList.toggle('flipped');
            }
        });
    });

    // 3. Capsule Completion Action Handler
    const completeBtn = document.getElementById('complete-btn');
    const feedbackMsg = document.getElementById('completion-feedback');

    if (completeBtn) {
        completeBtn.addEventListener('click', function() {
            const capsuleId = this.dataset.capsuleId;
            const csrfToken = this.dataset.csrfToken;
            
            completeBtn.disabled = true;
            completeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';

            fetch(`/complete_capsule/${capsuleId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    completeBtn.classList.add('completed');
                    completeBtn.innerHTML = '<i class="fas fa-check-circle"></i> Completed &bull; Spaced Review Scheduled';
                    completeBtn.disabled = false;
                    if (feedbackMsg) {
                        feedbackMsg.textContent = 'Progress saved! Capsule added to your spaced repetition queue.';
                    }
                } else {
                    completeBtn.disabled = false;
                    completeBtn.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Try Again';
                    alert('Progress could not be saved. Please try again.');
                }
            })
            .catch(error => {
                console.error('Completion error:', error);
                completeBtn.disabled = false;
                completeBtn.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Try Again';
            });
        });
    }

    // 4. Interactive Quiz Assessment Handler
    const quizForms = document.querySelectorAll('.quiz-options-form');
    quizForms.forEach(form => {
        const questionId = form.dataset.questionId;
        const csrfToken = form.dataset.csrfToken;
        const radioInputs = form.querySelectorAll('input[type="radio"]');
        const questionCard = document.getElementById(`quiz-question-${questionId}`);
        const feedbackBox = questionCard ? questionCard.querySelector('.quiz-feedback-box') : null;
        const hintBox = questionCard ? questionCard.querySelector('.quiz-hint-box') : null;
        const hintBtn = form.querySelector('.btn-hint-quiz');

        // Visual selection indicator
        radioInputs.forEach(input => {
            input.addEventListener('change', () => {
                form.querySelectorAll('.quiz-option-label').forEach(lbl => lbl.classList.remove('selected'));
                input.closest('.quiz-option-label').classList.add('selected');
            });
        });

        // Progressive hint toggle
        if (hintBtn && hintBox) {
            hintBtn.addEventListener('click', () => {
                hintBox.style.display = (hintBox.style.display === 'none' || !hintBox.style.display) ? 'block' : 'none';
                hintBox.innerHTML = `<strong><i class="fas fa-lightbulb"></i> Hint:</strong> ${hintBtn.dataset.hint}`;
            });
        }

        // Quiz answer submission
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const selectedRadio = form.querySelector('input[name="selected_option"]:checked');

            if (!selectedRadio) {
                alert('Please select an option before checking.');
                return;
            }

            const checkBtn = form.querySelector('.btn-check-quiz');
            checkBtn.disabled = true;
            checkBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Checking...';

            const formData = new URLSearchParams();
            formData.append('selected_option', selectedRadio.value);

            fetch(`/quiz/submit/${questionId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: formData.toString()
            })
            .then(res => res.json())
            .then(data => {
                checkBtn.innerHTML = '<i class="fas fa-check-circle"></i> Evaluated';
                if (data.status === 'success' && feedbackBox) {
                    feedbackBox.style.display = 'block';
                    if (data.is_correct) {
                        feedbackBox.className = 'quiz-feedback-box correct-box';
                        feedbackBox.innerHTML = `<strong><i class="fas fa-check-circle"></i> Correct!</strong> ${data.explanation} <br><small><i class="fas fa-calendar-check"></i> SuperMemo SM-2: scheduled for spaced review in ${data.next_review_days} day(s).</small>`;
                        selectedRadio.closest('.quiz-option-label').classList.add('correct');
                    } else {
                        feedbackBox.className = 'quiz-feedback-box incorrect-box';
                        feedbackBox.innerHTML = `<strong><i class="fas fa-times-circle"></i> Not quite!</strong> The correct option was <strong>${data.correct_option}</strong>.<br>${data.explanation}`;
                        selectedRadio.closest('.quiz-option-label').classList.add('incorrect');
                    }

                    // Lock options after evaluation
                    radioInputs.forEach(r => r.disabled = true);
                }
            })
            .catch(err => {
                console.error('Quiz submit error:', err);
                checkBtn.disabled = false;
                checkBtn.innerHTML = '<i class="fas fa-check-circle"></i> Check Answer';
            });
        });
    });

    // 5. Dynamic AI Tutor Question Answering
    const tutorSubmitBtn = document.getElementById('tutor-submit-btn');
    const tutorInput = document.getElementById('tutor-question-input');
    const tutorResponseBox = document.getElementById('tutor-response-box');
    const tutorResponseText = document.getElementById('tutor-response-text');

    if (tutorSubmitBtn && tutorInput) {
        const askTutor = function() {
            const query = tutorInput.value.trim();
            if (!query) {
                tutorInput.focus();
                return;
            }

            const capsuleId = tutorSubmitBtn.dataset.capsuleId;
            const csrfToken = tutorSubmitBtn.dataset.csrfToken;

            tutorSubmitBtn.disabled = true;
            tutorSubmitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Consulting...';

            const formData = new URLSearchParams();
            formData.append('query', query);

            fetch(`/tutor/ask/${capsuleId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: formData.toString()
            })
            .then(res => res.json())
            .then(data => {
                tutorSubmitBtn.disabled = false;
                tutorSubmitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Ask';
                if (data.status === 'success' && tutorResponseBox && tutorResponseText) {
                    tutorResponseBox.style.display = 'block';
                    tutorResponseText.textContent = data.response;
                }
            })
            .catch(err => {
                console.error('Tutor error:', err);
                tutorSubmitBtn.disabled = false;
                tutorSubmitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Ask';
            });
        };

        tutorSubmitBtn.addEventListener('click', askTutor);
        tutorInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                askTutor();
            }
        });
    }

    // 6. Accordion functionality for Subject Library & Course Cards
    const courseAccordionToggles = document.querySelectorAll('.course-accordion-toggle');
    courseAccordionToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            const targetId = this.getAttribute('aria-controls');
            const targetContent = document.getElementById(targetId);

            this.setAttribute('aria-expanded', !isExpanded);
            if (targetContent) {
                if (isExpanded) {
                    targetContent.setAttribute('hidden', '');
                } else {
                    targetContent.removeAttribute('hidden');
                }
            }
        });
    });

    // Auto-expand accordion when URL hash matches #subj-ID
    const handleCourseHashExpansion = function() {
        if (window.location.hash && window.location.hash.startsWith('#subj-')) {
            const targetCard = document.querySelector(window.location.hash);
            if (targetCard) {
                const toggle = targetCard.querySelector('.course-accordion-toggle');
                const targetContent = targetCard.querySelector('.course-collapsible-body');
                if (toggle && targetContent) {
                    toggle.setAttribute('aria-expanded', 'true');
                    targetContent.removeAttribute('hidden');
                    setTimeout(() => {
                        targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }, 150);
                }
            }
        }
    };
    handleCourseHashExpansion();
    window.addEventListener('hashchange', handleCourseHashExpansion);


    // Backward compatibility for any legacy .accordion-header elements
    const legacyAccordionHeaders = document.querySelectorAll('.accordion-header');
    legacyAccordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const accordionContent = header.nextElementSibling;
            if (accordionContent) {
                const isExpanded = header.getAttribute('aria-expanded') === 'true';
                header.setAttribute('aria-expanded', !isExpanded);
                if (!isExpanded) {
                    accordionContent.style.maxHeight = accordionContent.scrollHeight + 'px';
                    accordionContent.style.padding = '0.5rem 0';
                } else {
                    accordionContent.style.maxHeight = '0';
                    accordionContent.style.padding = '0';
                }
            }
        });
    });

    // 7. Authenticated Profile Dropdown Menu Toggle & Outside Dismissal
    const profileDropdownBtn = document.getElementById('profileDropdownBtn');
    const profileDropdownMenu = document.getElementById('profileDropdownMenu');

    if (profileDropdownBtn && profileDropdownMenu) {
        profileDropdownBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            const isOpen = profileDropdownMenu.classList.contains('is-open');
            if (isOpen) {
                profileDropdownMenu.classList.remove('is-open');
                profileDropdownBtn.setAttribute('aria-expanded', 'false');
            } else {
                profileDropdownMenu.classList.add('is-open');
                profileDropdownBtn.setAttribute('aria-expanded', 'true');
            }
        });

        // Close on clicking anywhere outside
        document.addEventListener('click', function(e) {
            if (!profileDropdownBtn.contains(e.target) && !profileDropdownMenu.contains(e.target)) {
                profileDropdownMenu.classList.remove('is-open');
                profileDropdownBtn.setAttribute('aria-expanded', 'false');
            }
        });

        // Close on Escape key press
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && profileDropdownMenu.classList.contains('is-open')) {
                profileDropdownMenu.classList.remove('is-open');
                profileDropdownBtn.setAttribute('aria-expanded', 'false');
                profileDropdownBtn.focus();
            }
        });
    }

    // 8. Mobile Drawer Menu Toggle (Public Navigation)
    const mobileMenuToggleBtn = document.getElementById('mobileMenuToggleBtn');
    const mobileDrawerMenu = document.getElementById('mobileDrawerMenu');

    if (mobileMenuToggleBtn && mobileDrawerMenu) {
        mobileMenuToggleBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            const isOpen = mobileDrawerMenu.classList.contains('is-open');
            if (isOpen) {
                mobileDrawerMenu.classList.remove('is-open');
                mobileMenuToggleBtn.setAttribute('aria-expanded', 'false');
            } else {
                mobileDrawerMenu.classList.add('is-open');
                mobileMenuToggleBtn.setAttribute('aria-expanded', 'true');
            }
        });

        // Close on clicking outside
        document.addEventListener('click', function(e) {
            if (!mobileMenuToggleBtn.contains(e.target) && !mobileDrawerMenu.contains(e.target)) {
                mobileDrawerMenu.classList.remove('is-open');
                mobileMenuToggleBtn.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // 9. Prevent Submitting Empty Search Queries
    const searchForms = document.querySelectorAll('form[role="search"]');
    searchForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const searchInput = form.querySelector('input[type="search"]');
            if (searchInput && !searchInput.value.trim()) {
                e.preventDefault();
                searchInput.focus();
            }
        });
    });

    // 10. Mentor Mode Selection Cards Handler
    const modeCards = document.querySelectorAll('.mode-choice-card');
    if (modeCards.length > 0) {
        modeCards.forEach(card => {
            const radio = card.querySelector('.mode-radio-input');
            card.addEventListener('click', function() {
                modeCards.forEach(c => c.classList.remove('selected'));
                this.classList.add('selected');
                if (radio) {
                    radio.checked = true;
                }
            });
            if (radio) {
                radio.addEventListener('focus', () => card.classList.add('focused'));
                radio.addEventListener('blur', () => card.classList.remove('focused'));
                radio.addEventListener('change', () => {
                    modeCards.forEach(c => c.classList.remove('selected'));
                    if (radio.checked) {
                        card.classList.add('selected');
                    }
                });
            }
        });
    }
});