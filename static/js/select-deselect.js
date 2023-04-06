const checkAll = document.getElementById('chooseArtists');
const checkboxes = document.querySelectorAll('input[type="checkbox"]');


const selectDeselect = document.getElementById('select-deselect');

selectDeselect.addEventListener('click', function() {
  checkAll.checked = !checkAll.checked;
  checkboxes.forEach(function(checkbox) {
    checkbox.checked = checkAll.checked;
  });
});