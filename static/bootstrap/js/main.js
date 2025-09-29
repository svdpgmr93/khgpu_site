const menuLink = document.getElementById('#m-link-university')

const univerMenu = document.getElementById('#univer-menu')

function menuOpen() {
    univerMenu.classList.toggle('d-none')
}

menuLink.addEventListener('click', menuOpen)