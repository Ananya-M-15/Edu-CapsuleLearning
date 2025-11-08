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

    // --- BUTTON DEBUGGING ---
    console.log('Script is now looking for the complete button...');
    const completeBtn = document.getElementById('complete-btn');

    if (completeBtn) {
        // If you see this message, it means the script found the button!
        console.log('SUCCESS: Button found! Attaching click listener.');
        
        completeBtn.addEventListener('click', function() {
            console.log('Button clicked! Starting fetch request...');
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
                console.log('Fetch response received:', data);
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
    } else {
        // If you see this message, the script could NOT find the button.
        console.error('FAILURE: Could not find element with id="complete-btn" on this page.');
    }
});