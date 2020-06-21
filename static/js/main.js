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
function detail_slider() {
    let slider = document.querySelector('.slider-detail')
    if(slider) {
        let count = 4;
        let slideArray = document.getElementsByClassName('slide-detail')
        console.log(slideArray.length)
            jQuery('.slider-detail').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                prevArrow: ('<i class="fa fa-chevron-left" aria-hidden="true">'),
                nextArrow: ('<i class="fa fa-chevron-right" aria-hidden="true">'),
                autoplay: true
            });
    }
}
function currency() {
    let API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
        request = new XMLHttpRequest();
    request.open('GET',API)
    request.responseType = 'json';
    request.send();
    request.onload = function () {
        let currency = request.response;
        console.log(currency)
        let USD = document.getElementById('usd'),
            EURO = document.getElementById('euro'),
            RUR = document.getElementById('rur')
        let currencyUSD = currency[0].buy;
        let currencyUsdSliced = currencyUSD.substr(0,currencyUSD.length - 3)
        let currencyEURO = currency[1].buy;
        let currencyEuroSliced = currencyEURO.substr(0,currencyEURO.length - 3)
        let currencyRUR = currency[2].buy;
        let currencyRurSliced = currencyRUR.substr(0,currencyRUR.length - 3)
        USD.textContent = currencyUsdSliced;
        EURO.textContent = currencyEuroSliced;
        RUR.textContent = currencyRurSliced;
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

$('body').on('click', '.password-control', function(){
    if ($('#password-input').attr('type') == 'password'){
        $(this).addClass('view');
        $('#password-input').attr('type', 'text');
    } else {
        $(this).removeClass('view');
        $('#password-input').attr('type', 'password');
    }
    return false;
});
detail_slider();
poll_slider();
currency()
poll();
poll_statusBar();

