class FormValidator {
    static init() {
        const forms = document.querySelectorAll('.needs-validation');
        forms.forEach(form => {
            form.addEventListener('submit', this.handleSubmit.bind(this));
            this.addFieldValidation(form);
        });
    }

    static handleSubmit(event) {
        const form = event.target;
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add('was-validated');
    }

    static addFieldValidation(form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', () => this.validateField(input));
            input.addEventListener('input', () => this.validateField(input));
        });
    }

    static validateField(field) {
        const value = field.value.trim();
        const validationRules = field.dataset.validation;
        
        if (validationRules) {
            const rules = JSON.parse(validationRules);
            let isValid = true;
            let errorMessage = '';

            // Custom validation rules
            if (rules.required && !value) {
                isValid = false;
                errorMessage = 'Trường này là bắt buộc';
            }
            
            field.setCustomValidity(isValid ? '' : errorMessage);
            field.reportValidity();
        }
    }
} 