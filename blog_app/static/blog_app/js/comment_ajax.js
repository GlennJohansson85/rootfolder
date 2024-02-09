// blog_app/static/blog_app/js/comment_ajax.js
document.addEventListener("DOMContentLoaded", function () {
    const commentForms = document.querySelectorAll(".commentform");
    
    commentForms.forEach(commentForm => {
        const addCommentBtn = commentForm.querySelector(".add-comment-btn");

        addCommentBtn.addEventListener("click", function (e) {
            e.preventDefault();

            const formData = new FormData(commentForm);  // Pass the form directly

            fetch(commentForm.action, {
                method: "POST",
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Reload the page after successfully adding a comment
                    window.location.reload();
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });
});
