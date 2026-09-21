function toggleMenu() {
    document.getElementById('sidebar').classList.toggle('open');
}

function toggleDescription() {
    document.getElementById('description').classList.toggle('open');
}

document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebar');
    const button = document.querySelector('.button-menu');

    if (!sidebar.contains(event.target) && !button.contains(event.target)) {
        sidebar.classList.remove('open');
    }
});