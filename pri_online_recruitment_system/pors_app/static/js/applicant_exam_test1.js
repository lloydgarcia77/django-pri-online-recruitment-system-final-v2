// https://www.sitepoint.com/simple-javascript-quiz/
$(document).ready(function (e) {
    const quizContainer = document.getElementById("quiz");
    const resultsContainer = document.getElementById("results"); 
    const submitButton = document.getElementById("submit");
    const progressOverlayContainer = document.getElementById("progressOverlay");
    const examProgressbarContainer = document.getElementById("examProgressbar");

    let currentSlide = 0;


    const myQuestions = [
        {
            question: "(Find the sum) 1.25 + .02 + 3.12 ?",
            answers: {
                a: "4.39",
                b: "0.439",
                c: "43.9",                
                d: "0.043"
            },
            correctAnswer: "a"
        },
        {
            question: "(Find the sum) 213 + 260 + .25 ?",
            answers: {
                a: "473.25",
                b: "4733.5",
                c: "4.73",                
                d: "0.04733"
            },
            correctAnswer: "a"
        },
        {
            question: "(Find the sum) 98 + 24 + 45 ?",
            answers: {
                a: "165",
                b: "162",
                c: "167",                
                d: "160"
            },
            correctAnswer: "c"
        },
        {
            question: "(Find the sum) 33 + 333 + 222 ?",
            answers: {
                a: "388",
                b: "588",
                c: "488",                
                d: "888"
            },
            correctAnswer: "b"
        },
        {
            question: "(Find the sum) .001 + .01 + 1.000 ?",
            answers: {
                a: "1.01",
                b: "0.01",
                c: "0.001",                
                d: "1.011"
            },
            correctAnswer: "d"
        },
        {
            question: "(Find the sum) 66 + 1.66 + .066 ?",
            answers: {
                a: "6.726",
                b: "67.726",
                c: "677.2",                
                d: "6.766"
            },
            correctAnswer: "b"
        } ,
        {
            question: "(Find the difference) 367 - .367 ?",
            answers: {
                a: "366.633",
                b: "3666.33",
                c: "3.666",                
                d: "3.666"
            },
            correctAnswer: "a"
        }, 
        {
            question: "(Find the difference) 1234 - 134 ?",
            answers: {
                a: "1200",
                b: "1100",
                c: "1000",                
                d: "1500"
            },
            correctAnswer: "b"
        }, 
        {
            question: "(Find the difference) 10,213 - 887 ?",
            answers: {
                a: "9325",
                b: "9326",
                c: "3.666",                
                d: "3.666"
            },
            correctAnswer: "b"
        }, 
        {
            question: "(Find the difference) 888 - 1.88 ?",
            answers: {
                a: "8861.2",
                b: "88.61",
                c: "0.444",                
                d: "886.12"
            },
            correctAnswer: "d"
        }, 
        {
            question: "(Find the difference) 657 - 222 ?",
            answers: {
                a: "435",
                b: "445",
                c: "32.67",                
                d: "415"
            },
            correctAnswer: "a"
        }, 
        {
            question: "(Find the difference) 1345 - 111.34 ?",
            answers: {
                a: "1233",
                b: "123.33",
                c: "13.5",                
                d: "1233.66"
            },
            correctAnswer: "d"
        }, 
        {
            question: "(Find the product) 55 X 22 ?",
            answers: {
                a: "1200",
                b: "1210",
                c: "1010",                
                d: "1212"
            },
            correctAnswer: "b"
        },
        {
            question: "(Find the product)  96 X 16 ?",
            answers: {
                a: "1336",
                b: "1635",
                c: "1566",                
                d: "1536"
            },
            correctAnswer: "d"
        }, 
        {
            question: "(Find the product) 34 X 1.3 ?",
            answers: {
                a: "444.2",
                b: "44.2",
                c: "1.442",                
                d: "4.222"
            },
            correctAnswer: "b"
        }, 
        {
            question: "(Find the product) 1 X .44 ?",
            answers: {
                a: "0.44",
                b: "0.044",
                c: "0.444",                
                d: "1.44"
            },
            correctAnswer: "a"
        }, 
        {
            question: "(Find the product) 33 X .99 ?",
            answers: {
                a: "3.267",
                b: "326.7",
                c: "32.67",                
                d: "3267"
            },
            correctAnswer: "c"
        }, 
        {
            question: "(Find the product) 1.23 X 11 ?",
            answers: {
                a: "13.53",
                b: "1.35",
                c: "13.5",                
                d: "135"
            },
            correctAnswer: "a"
        },        
        {
            question: "(Find the percentage) 5% of 25 ?",
            answers: {
                a: "12.5",
                b: "12.52",
                c: "125.5",                
                d: "1.25"
            },
            correctAnswer: "a"
        },
        {
            question: "(Find the percentage) 75% of 200 ?",
            answers: {
                a: "100",
                b: "125",
                c: "105",                
                d: "150"
            },
            correctAnswer: "d"
        }, 
        {
            question: "(Find the percentage) 3% of 10 ?",
            answers: {
                a: "0.3",
                b: "0.03",
                c: "3",                
                d: "0.003"
            },
            correctAnswer: "a"
        }, 
        {
            question: "(Find the percentage) 12% of 100 ?",
            answers: {
                a: "12",
                b: "1.2",
                c: "12.5",                
                d: "0.0125"
            },
            correctAnswer: "a"
        }, 
        {
            question: "(Find the percentage) 85% of 300 ?",
            answers: {
                a: "522",
                b: "525",
                c: "255",                
                d: "225"
            },
            correctAnswer: "c"
        }, 
        {
            question: "(Find the percentage) 40% of 980 ?",
            answers: {
                a: "3920",
                b: "39",
                c: "392",                
                d: "0.392"
            },
            correctAnswer: "c"
        }, 
        {
            question: "(Find the percentage) 85% of 10,000 ?",
            answers: {
                a: "8500",
                b: "850",
                c: "85",                
                d: "8.5"
            },
            correctAnswer: "a"
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
        const urlAttr =$(this).attr("data-url"); 
        // show loading before rendering the 5 sec loading
        // $('.news').css('display','none');
        // $('.news').hide();
        // $('.news').show();
        // $('.news').css('display','block');
        progressOverlayContainer.style.display = 'block';
        setTimeout(() =>{
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

    // slide function

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