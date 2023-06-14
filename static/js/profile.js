const toggleBtn = document.getElementById("toggle-reminder");
const reminderText = document.getElementById("reminder-status-msg");
let time = 3000;

toggleBtn.addEventListener("click", () => {
  console.log("hellooo");
  reminderText.classList.toggle("reminder-status-msg-show");
  // setTimeout(() => {
  //   reminderText.classList.toggle("reminder-status-msg-show");
  // }, time);
});
