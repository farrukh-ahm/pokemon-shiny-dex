let navToggle = document.getElementById("nav-toggle")
let navBar = document.getElementsByClassName("nav")


navToggle.addEventListener("click", ()=>{
    for(let nav of navBar){
        nav.classList.toggle("toggle")
    }
})