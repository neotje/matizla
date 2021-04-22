var progress = 0;
var animation = anime({
    targets: '.progress-bar',
    opacity: [0, 1],
    marginTop: ["0px", "48px"],
    duration: 300,
    easing: 'easeInOutQuad'
});
animation.pause();

function getProgressBar() {
    return document.getElementsByClassName("progress-bar")[0]
}

function hideProgressBar() {
    animation.direction = 'reverse'
    animation.play()
}

function showProgressBar() {
    progress = 0
    animation.direction = 'normal'
    animation.play()
}

function fadeOut() {
    anime({
        targets: 'body',
        opacity: [1, 0],
        duration: 1000,
        easing: 'easeInOutQuad',
        complete: (anim) => {
            pywebview.api.hideWindow("load")
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

setInterval(() => {
    anime({
        targets: '.progress',
        width: `${progress * 100}%`,
        duration: 100,
        easing: 'easeInOutQuad'
    })
}, 100)

fadeIn()