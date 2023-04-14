const checkAll = document.getElementById('chooseArtists');
const checkboxes = document.querySelectorAll('input[type="checkbox"]');

const images = document.getElementsByClassName('image');

const selectDeselect = document.getElementById('select-deselect');





selectDeselect.addEventListener('click', function() {
  checkAll.checked = !checkAll.checked;

  for (var i = 0; i < images.length; i++) {
    selectImage(images[i], checkAll.checked
      );
  }

});

const submitButton = document.querySelector('input[type="submit"]');

function enableSubmit(){
  submitButton.disabled = !document.querySelector('input[type="checkbox"]:checked');
}



// Add onclick event listener to each image element
for (var i = 0; i < images.length; i++) {
  images[i].addEventListener("click", function() {
 
   selectImage(this);

});
}


function selectImage(element,override)
{   
    toOverride = typeof override === 'undefined' ? false : true;


    var checkbox = element.querySelector('input[type="checkbox"]');
    checkbox.checked = !checkbox.checked;

    if (toOverride){
      checkbox.checked = override;
    }
    // Add or remove the "selected" class based on the checkbox state
    if (checkbox.checked || toOverride && override) {
      element.classList.add("selected");
    } else {
      element.classList.remove("selected");
    }

    enableSubmit();

}


const slider = document.querySelector('.range-slider__slider');
const value = document.querySelector('.range-slider__value');

  slider.addEventListener('input', function() {
    value.value = slider.value;
  });