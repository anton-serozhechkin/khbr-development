function poll() {
    let checkboxArray = document.querySelectorAll('.poll-checkbox'),
        resultButton = document.getElementById('poll_result_button'),
        pollForm = document.getElementById('poll-form'),
        pollResults = document.getElementById('poll-results');
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
function poll_statusBar() {
    let statusBarArray = document.querySelectorAll('.poll_result_statusBar'),
        poll_result_percent = document.querySelectorAll('.poll_result_percent')

        for(let i = 0;i < statusBarArray.length;i++) {
            statusBarArray[i].style.width = poll_result_percent[i].textContent.replace('%','') + '%';
        }

}
poll();
poll_statusBar();
