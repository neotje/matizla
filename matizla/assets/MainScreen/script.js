function fadeOut() {
    anime({
        targets: 'body',
        opacity: [1, 0],
        duration: 1000,
        easing: 'easeInOutQuad',
        complete: (anim) => {
            pywebview.api.showWindow("load")
        }
    })
}

function fadeIn() {
    anime({
        targets: 'body',
        opacity: [0, 1],
        duration: 1000,
        easing: 'easeInOutQuad'
    })
}