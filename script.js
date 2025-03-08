// JavaScript code can be added here for interactivity
document.addEventListener('DOMContentLoaded', function() {
    // Example: Add click event to navigation links
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            alert('Navigating to ' + this.textContent);
        });
    });
});
