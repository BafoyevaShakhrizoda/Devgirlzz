document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.question-card');
    const nextBtn = document.getElementById('next-btn');
    const prevBtn = document.getElementById('prev-btn');
    const submitBtn = document.getElementById('submit-btn');
    const progressBar = document.querySelector('.progress-bar::after');
    const progressText = document.getElementById('progress-text');
    let currentQuestion = 0;
    
    // Initialize progress
    updateProgress();
    
    // Next button click
    nextBtn.addEventListener('click', function() {
        if (validateCurrentQuestion()) {
            questions[currentQuestion].classList.remove('active');
            questions[currentQuestion].classList.add('hidden');
            
            currentQuestion++;
            questions[currentQuestion].classList.remove('hidden');
            questions[currentQuestion].classList.add('active');
            
            updateNavigation();
            updateProgress();
        } else {
            alert('Iltimos, javobni tanlang!');
        }
    });
    
    // Previous button click
    prevBtn.addEventListener('click', function() {
        questions[currentQuestion].classList.remove('active');
        questions[currentQuestion].classList.add('hidden');
        
        currentQuestion--;
        questions[currentQuestion].classList.remove('hidden');
        questions[currentQuestion].classList.add('active');
        
        updateNavigation();
        updateProgress();
    });
    
    // Validate current question has an answer
    function validateCurrentQuestion() {
        const currentQuestionId = questions[currentQuestion].dataset.questionId;
        const selectedOption = document.querySelector(`input[name="question_${currentQuestionId}"]:checked`);
        return selectedOption !== null;
    }
    
    // Update navigation buttons
    function updateNavigation() {
        if (currentQuestion === 0) {
            prevBtn.disabled = true;
        } else {
            prevBtn.disabled = false;
        }
        
        if (currentQuestion === questions.length - 1) {
            nextBtn.classList.add('hidden');
            submitBtn.classList.remove('hidden');
        } else {
            nextBtn.classList.remove('hidden');
            submitBtn.classList.add('hidden');
        }
    }
    
    // Update progress bar and text
    function updateProgress() {
        const progress = ((currentQuestion + 1) / questions.length) * 100;
        document.querySelector('.progress-bar').style.setProperty('--progress', `${progress}%`);
        progressText.textContent = `${currentQuestion + 1}/${questions.length}`;
    }
    
    // Style options on selection
    const options = document.querySelectorAll('.option');
    options.forEach(option => {
        option.addEventListener('click', function() {
            const input = this.querySelector('input');
            input.checked = true;
            
            // Remove selected class from all options
            options.forEach(opt => {
                opt.classList.remove('selected');
            });
            
            // Add selected class to current option
            this.classList.add('selected');
        });
    });
});