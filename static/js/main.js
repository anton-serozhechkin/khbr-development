function poll_slider() {
    let slider = document.querySelector('.slider')
    if(slider) {
        let count = 4;
        let slideArray = document.getElementsByClassName('index-poll-box')
        console.log(slideArray.length)
        if (slideArray.length < 4) {

        } else {
            if (screen.width < 1000) {
                count = 1;
            }

            jQuery('.slider').slick({
                slidesToShow: count,
                slidesToScroll: 1,
                prevArrow: $(''),
                nextArrow: $(''),
                autoplay: true

            });
        }
    }
}
function poll() {
    let checkboxArray = document.querySelectorAll('.poll-checkbox'),
        resultButton = document.getElementById('poll_result_button'),
        pollForm = document.getElementById('poll-form'),
        pollResults = document.getElementById('poll-results');
    if(checkboxArray) {

        for(let i = 0; i < checkboxArray.length;i++) {
            checkboxArray[i].addEventListener('click',function () {
                if(this.checked) {
                    resultButton.style.display = 'block';
                }
            })
        }
        resultButton.addEventListener('click',function () {
            event.preventDefault()
            pollForm.style.display = 'none'
            pollResults.style.display = 'block'
        })

    }
}
function poll_statusBar() {
    let statusBarArray = document.querySelectorAll('.poll_result_statusBar'),
        poll_result_percent = document.querySelectorAll('.poll_result_percent')
    if(statusBarArray) {

        for(let i = 0;i < statusBarArray.length;i++) {
            statusBarArray[i].style.width = poll_result_percent[i].textContent.replace('%','') + '%';
        }
    }

}
poll_slider();

poll();
poll_statusBar();

