document.getElementById('imageFile').addEventListener('change', function(event) {
    var output = document.getElementById('outputImage');
    output.innerHTML = '';
    var img = document.createElement('img');
    img.src = URL.createObjectURL(event.target.files[0]);
    output.appendChild(img);
});
