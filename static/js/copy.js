/* Copies the short link to the Clipbaord */
function copy_function() {
  var text = document.getElementById("demo").textContent
  console.log(text)
  navigator.clipboard.writeText(text)
}