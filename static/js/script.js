// NAVIGATION BURGER

let navToggle = document.getElementById("nav-toggle")
let navBar = document.getElementsByClassName("nav")

navToggle.addEventListener("click", ()=>{
    for(let nav of navBar){
        nav.classList.toggle("toggle")
        console.log("click")
    }
})


// MESSAGE TIMEOUT

let message = document.getElementById("message")

setTimeout(()=>{
    message.remove()
}, 3000)


// DELETE MODAL FOR ADMIN

const delModal = document.querySelector(".modal1")
console.log(delModal)
const addSlug = document.querySelector(".add-slug")
const modal1Open = document.getElementsByClassName("modal1-open")
const delConfirm = document.querySelector(".del-confirm")
const modal1Close = document.getElementsByClassName("modal1-close")

function openCheck(dialog) {
    if (dialog.open) {
      console.log("Dialog open");
    } else {
      console.log("Dialog closed");
    }
  }

  document.addEventListener("DOMContentLoaded", openCheck)

for(let modal of modal1Open){
    modal.addEventListener("click", (e)=>{
        let slug = e.target.getAttribute("data-type")
        addSlug.setAttribute("action", `{% url 'deletepokemon' pokemon.${slug} %}`)
        delModal.showModal();
    })
}

for(let modal of modal1Close){
    modal.addEventListener("click", (e)=>{
        addSlug.removeAttribute("action")
        delModal.close()
    })
}