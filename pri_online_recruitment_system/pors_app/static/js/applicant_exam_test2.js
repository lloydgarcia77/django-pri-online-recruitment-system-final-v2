$(document).ready(function (e) {
    const quizContainer = document.getElementById("quiz");
    const resultsContainer = document.getElementById("results");
    const submitButton = document.getElementById("submit");
    const progressOverlayContainer = document.getElementById("progressOverlay");
    const examProgressbarContainer = document.getElementById("examProgressbar");
    let currentSlide = 0;

    const myQuestions = [
        {
            question: "Which is Brittle? ?",
            answers: {
                a: "Glass",
                b: "Sand",
                c: "Cotton",                
                d: "Water"
            },
            correctAnswer: "a"
        },
        {
            question: "If BUTTERFLY can fly, the worm can ?",
            answers: {
                a: "Walk",
                b: "Crawl",
                c: "Run",                
                d: "Stand"
            },
            correctAnswer: "b"
        },
        {
            question: "The opposite of SOFT is ?",
            answers: {
                a: "Hard",
                b: "Mild",
                c: "Smooth",                
                d: "Dusty"
            },
            correctAnswer: "a"
        },
        {
            question: "Which does not belong ?",
            answers: {
                a: "Fork",
                b: "Spoon",
                c: "Saucer",                
                d: "Paper"
            },
            correctAnswer: "d"
        },
        {
            question: "If you will invert NOON, what will be the outcome ?",
            answers: {
                a: "NOW",
                b: "NOON",
                c: "MOON",                
                d: "NOOM"
            },
            correctAnswer: "b"
        },
        {
            question: "The opposite of INFANT is ?",
            answers: {
                a: "Baby",
                b: "Girl",
                c: "Adult",                
                d: "Male"
            },
            correctAnswer: "c"
        },
        {
            question: "Which does not belong ?",
            answers: {
                a: "Sleeping",
                b: "Walking",
                c: "Running",                
                d: "Playing"
            },
            correctAnswer: "a"
        },
        {
            question: "If BIRD is to animal, then MAN is to ?",
            answers: {
                a: "Human",
                b: "Ape",
                c: "Monkey",                
                d: "Fish"
            },
            correctAnswer: "a"
        },
        {
            question: "The LADY is to female, then GENTLEMEN is to ?",
            answers: {
                a: "Bird",
                b: "Shoes",
                c: "Male",                
                d: "Baby"
            },
            correctAnswer: "c"
        },
        {
            question: "The Opposite of BOY ?",
            answers: {
                a: "Male",
                b: "Man",
                c: "Girl",                
                d: "Lady"
            },
            correctAnswer: "c"
        }
         
    ];


    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }

    function buildQuiz() {
        // we'll need a place to store the HTML output
        const output = [];

        // for each question

        myQuestions.forEach((currentQuestion, questionNumber) => {
            // we'll want to store the list of answer choices
            const answers = [];
            // and for each available answer...

            for (letter in currentQuestion.answers) {
                answers.push(
                    `<label>
                        <input type="radio" name="question${questionNumber}" value="${letter}">
                        ${letter} :
                        ${currentQuestion.answers[letter]}
                    </label>`
                );
            }
            // add this question and its answers to the output

            output.push(
                `<div class="slide">
                    <div class="question"> ${currentQuestion.question} </div>
                    <div class="answers"> ${answers.join("")} </div>
                </div>`
            );

            // finally combine our output list into one string of HTML and put it on the page
            quizContainer.innerHTML = output.join("");
        });
    }

    function showResults() {
        // gather answer containers from our quiz
        const answerContainers = quizContainer.querySelectorAll(".answers");

        // keep track of user's answers

        let numCorrect = 0;

        myQuestions.forEach((currentQuestion, questionNumber) => {
            // find selected answer
            const answerContainer = answerContainers[questionNumber];
            const selector = `input[name=question${questionNumber}]:checked`
            const userAnswer = (answerContainer.querySelector(selector) || {}).value;

            // if answer is correct  

            if (userAnswer === currentQuestion.correctAnswer) {
                // add to the number of correct answers
                numCorrect++;

                // color the answers green
                answerContainers[questionNumber].style.color = "lightgreen";
            } else {
                // if answer is wrong or blank
                // color the answers red
                answerContainers[questionNumber].style.color = "red";
            }
            resultsContainer.style.display = 'block'
            resultsContainer.innerHTML = `Score: ${numCorrect*2} out of ${myQuestions.length*2}`;

        });

        // Submit score to back end
        let data = {
            'score': numCorrect,
            'over': myQuestions.length
        }

        // convert to json

        data = JSON.stringify(data);
        // create request to be sent to django backend
        // https://docs.djangoproject.com/en/2.2/ref/csrf/
        const urlAttr = $(this).attr("data-url");
        // show loading before rendering the 5 sec loading
        // $('.news').css('display','none');
        // $('.news').hide();
        // $('.news').show();
        // $('.news').css('display','block');
        progressOverlayContainer.style.display = 'block';
        setTimeout(() => {
            $.ajax({
                headers: { "X-CSRFToken": getCookie("csrftoken") },
                type: 'POST',
                url: urlAttr,
                data: data,
                dataType: 'json',
                success: (data) => {
                    // // https://stackoverflow.com/questions/1865837/whats-the-difference-between-window-location-and-window-location-replace
                    // window.location adds an item to your history in that you can (or should be able to) click "Back" and go back to the current page.
                    // window.location.replace replaces the current history item so you can't go back to it
                    window.location.replace(data.urlAttr);
                    // window.location = data.urlAttr;
                }
            });
        }, 5000);
    }

    // display quiz right away
    buildQuiz();

    // pagination
    const previousButton = document.getElementById("previous");
    const nextButton = document.getElementById("next");
    const slides = document.querySelectorAll(".slide");

    function showSlide(n) {
        slides[currentSlide].classList.remove('active-slide');
        slides[n].classList.add('active-slide');
        currentSlide = n;

        if (currentSlide === 0) {
            previousButton.style.display = 'none';
        } else {
            previousButton.style.display = 'inline-block';
        }

        if (currentSlide === slides.length - 1) {
            nextButton.style.display = 'none';
            submitButton.style.display = 'inline-block';
        } else {
            nextButton.style.display = 'inline-block';
            submitButton.style.display = 'none';
        } 
        // update the progress of the exam
        
        examProgressbarContainer.style.width = `${((currentSlide+1) / myQuestions.length) * 100}%`
        examProgressbarContainer.innerHTML = `${currentSlide+1} out of ${myQuestions.length} Complete (success)`
    }

    showSlide(0);

    function showNextSlide() {
        showSlide(currentSlide + 1);
    }

    function showPreviousSlide() {
        showSlide(currentSlide - 1);
    }

    // toggle buttons

    previousButton.addEventListener("click", showPreviousSlide);
    nextButton.addEventListener("click", showNextSlide);

    // on submit, show results

    submitButton.addEventListener("click", showResults);
    
});