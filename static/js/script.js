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
const addSlug = document.querySelector(".add-slug")
const modal1Open = document.getElementsByClassName("modal1-open")
const delConfirm = document.querySelector(".del-confirm")
const modal1Close = document.getElementsByClassName("modal1-close")

// function openCheck(dialog) {
//     if (dialog.open) {
//       console.log("Dialog open");
//     } else {
//       console.log("Dialog closed");
//     }
//   }

//   document.addEventListener("DOMContentLoaded", openCheck)

for(let modal of modal1Open){
    modal.addEventListener("click", (e)=>{
        let slug = e.target.getAttribute("data-type")
        delModal.showModal();
        addSlug.setAttribute("action", `deletepokemon/${slug}`)
    })
}

for(let modal of modal1Close){
    modal.addEventListener("click", (e)=>{
        addSlug.removeAttribute("action")
        delModal.close()
    })
}


// USER SHINY DELETE MODAL

const deleteModal =  document.querySelector(".user-shiny-delete-modal");
const deleteModalOpen = document.getElementsByClassName("user-shiny-delete-modal-open");
const deleteModalClose = document.querySelector(".user-shiny-delete-modal-close");
const addDeleteSlug = document.querySelector(".delete-slug")
const imageAdd = document.querySelector(".add-image")

for(let btn of deleteModalOpen){
    btn.addEventListener("click", (e)=>{
        console.log("click")
        deleteModal.showModal()
        let slug = e.target.getAttribute("data-type")
        let imageData = e.target.getAttribute("data-image")
        let user = e.target.getAttribute("data-user")
        console.log(user)
        addDeleteSlug.setAttribute("action", `/delete/${user}/${slug}`)
        imageAdd.setAttribute("src", imageData)
        console.log(imageData)
        console.log(slug)

    })
}

deleteModalClose.addEventListener("click", ()=>{
    deleteModal.close()
})