// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed. Running script...');

    // Accordion functionality for the library page
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    if (accordionHeaders.length > 0) {
        console.log('Found accordion headers. Attaching listeners.');
        accordionHeaders.forEach(header => {
            header.addEventListener('click', event => {
                const accordionContent = header.nextElementSibling;
                const isExpanded = header.getAttribute('aria-expanded') === 'true';
                header.setAttribute('aria-expanded', !isExpanded);
                if (!isExpanded) {
                    accordionContent.style.maxHeight = accordionContent.scrollHeight + 'px';
                    accordionContent.style.padding = '0.5rem 0';
                } else {
                    accordionContent.style.maxHeight = '0';
                    accordionContent.style.padding = '0';
                }
            });
        });
    }

    // Completion button handler for the learn page
    const completeBtn = document.getElementById('complete-btn');

    if (completeBtn) {
        completeBtn.addEventListener('click', function() {
            const capsuleId = this.dataset.capsuleId;
            const csrfToken = this.dataset.csrfToken;
            
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
                    window.location.href = '/learn/';
                } else {
                    alert('Request failed. Check console for details.');
                }
            })
            .catch(error => {
                console.error('CRITICAL FETCH ERROR:', error);
                alert('A critical error occurred. Check the console for details.');
            });
        });
    }
});