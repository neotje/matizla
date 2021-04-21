var currentOpacity = 1;

function getProgressBar() {
    return document.getElementsByClassName("progress-bar")[0]
}

function hideProgressBar() {

}

function showProgressBar() {}

var animation = anime({
    targets: '.progress-bar',
    opacity: [0, 1],
    duration: 300,
    easing: 'easeInOutQuad'
})

setTimeout(() => {
    console.log("go");
    //animation.reverse();
}, 2000);