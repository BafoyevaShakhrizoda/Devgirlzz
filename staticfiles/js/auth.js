// Portfolio link toggle
document.addEventListener('DOMContentLoaded', function() {
    const portfolioCheckbox = document.getElementById('has_portfolio');
    const portfolioLinkField = document.querySelector('.portfolio-link');
    
    if (portfolioCheckbox && portfolioLinkField) {
        portfolioCheckbox.addEventListener('change', function() {
            if (this.checked) {
                portfolioLinkField.classList.add('show');
            } else {
                portfolioLinkField.classList.remove('show');
            }
        });
    }
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            let isValid = true;
            
            // Check required fields
            const requiredInputs = this.querySelectorAll('input[required]');
            requiredInputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                }
            });
            
            // Check password match
            const password1 = this.querySelector('#password1');
            const password2 = this.querySelector('#password2');
            
            if (password1 && password2) {
                if (password1.value !== password2.value) {
                    isValid = false;
                    password2.classList.add('error');
                    alert('Parollar mos kelmadi!');
                } else {
                    password2.classList.remove('error');
                }
            }
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
});