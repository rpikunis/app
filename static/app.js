const propertyForm = document.querySelector('#property-form');
const modal = document.getElementById("myModal");
const close = document.getElementsByClassName("close")[0];

propertyForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(event.target);
  const data = Object.fromEntries(formData.entries());
  generateDescription(data);
});

function generateDescription(data) {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/generate-description', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    if (xhr.status === 200) {
      const description = JSON.parse(xhr.responseText).description;
      showModal(description);
    } else {
      console.log('Error generating description');
    }
  };
  xhr.send(JSON.stringify(data));
}

function showModal(description) {
  const descriptionText = document.getElementById("description-text");
  descriptionText.innerHTML = description;
  modal.style.display = "block";

  close.onclick = function() {
    modal.style.display = "none";
  };

  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
}
