function toggleMenu() {
    var navLinks = document.getElementById('navLinks');
    if (navLinks) {
        navLinks.style.display = (navLinks.style.display === 'block') ? 'none' : 'block';
    }
}