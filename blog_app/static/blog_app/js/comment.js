// ======================================
//                                    COMMENT.JS
// ======================================-->
document.addEventListener("DOMContentLoaded", function () {
    var commentForm = document.querySelector('.commentForm');
    if (commentForm) {
        commentForm.addEventListener("submit", function (event) {
            event.preventDefault();

            // Serialize the form data
            var formData = new FormData(commentForm);

            // Send the AJAX request
            fetch(commentForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',  // Identify the request as AJAX
                    'X-CSRFToken': getCookie('csrftoken')   // Include CSRF token
                },
            })
                .then(response => response.json())
                .then(data => {
                    // Update the comments section with the new comment
                    var commentsSection = document.querySelector('.comments-display');
                    if (commentsSection) {
                        commentsSection.innerHTML = data.html;
                    }
                })
                .catch(error => console.error('Error submitting comment:', error));
        });
    }
});

// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
