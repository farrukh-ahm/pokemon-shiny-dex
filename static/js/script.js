let navToggle = document.getElementById("nav-toggle")
let navBar = document.getElementsByClassName("nav")


navToggle.addEventListener("click", ()=>{
    for(let nav of navBar){
        nav.classList.toggle("toggle")
    }
})


let message = document.getElementById("message")

setTimeout(()=>{
    message.remove()
}, 3000)



