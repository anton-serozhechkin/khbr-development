if (screen.width <= 1199) {
    let bar = document.getElementById('barsButton')
    let menu = document.getElementById('header-navigation-id')
    let flag = false;
    bar.addEventListener('click', function () {
            if (flag == false) {

                menu.style.opacity = '1'
                menu.style.transition = 'all .2s ease-in-out'
                flag = true
            }
            else {
                menu.style.opacity = '0'
                menu.style.transition = 'all .2s ease-in-out'
                flag = false;
            }
        }
    )}
