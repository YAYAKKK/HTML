document.addEventListener('DOMContentLoaded', function () {
    // Fungsi untuk mengubah warna navbar ketika discroll
    window.addEventListener('scroll', function () {
        var navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Fungsi untuk menggulir kartu artikel
    document.getElementById('scroll-left').addEventListener('click', function () {
        document.getElementById('article-container').scrollBy({ left: -300, behavior: 'smooth' });
    });

    document.getElementById('scroll-right').addEventListener('click', function () {
        document.getElementById('article-container').scrollBy({ left: 300, behavior: 'smooth' });
    });
});


    // Delayed removal of the 'visible' class to trigger the transition
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            document.querySelectorAll('section.visible').forEach(function(section) {
                section.classList.remove('visible');
            });
        }, 100);
    });

