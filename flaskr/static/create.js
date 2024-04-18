const fake_upload = document.getElementById("fake-upload");
const real_upload = document.getElementById("upload");

fake_upload.addEventListener("click", () => {
  let clickEvent = document.createEvent('MouseEvents');
  clickEvent.initMouseEvent('click', true, true, window, 0, 0, 0, 0, 0, false,
                            false, false, false, 0, null);
  real_upload.dispatchEvent(clickEvent);
});

function displayName() {
  let p = document.getElementById("filename");
  p.innerHTML = real_upload.value.split("\\").pop();
  p.style["display"] = "block";
}
