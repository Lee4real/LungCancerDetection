document.querySelector('.logo a').addEventListener('click', function(event) {
    event.preventDefault();
    // Redirect to main page URL
    window.location.href = 'main-page.html'; // Change to your main page URL
});
document.getElementById('imgInput').addEventListener('change', function() {
    previewImage();
});

function previewImage() {
    var fileInput = document.getElementById('imgInput');
    var imagePreview = document.getElementById('imagePreview');

    if (fileInput.files && fileInput.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            imagePreview.src = e.target.result;
        };

        reader.readAsDataURL(fileInput.files[0]); // Convert image to base64 string
    }
}