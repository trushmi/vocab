"use_strict";

for (const dashboardCard of document.getElementsByClassName("dashboard-card")) {
  const button = dashboardCard.getElementsByClassName("edit-btn")[0];

  button.addEventListener("click", function (event) {
    if (!dashboardCard.classList.contains("editing")) {
      dashboardCard.classList.add("editing");
    } else {
      dashboardCard.classList.remove("editing");
    }
  });
}

const languages = { en: "English", es: "Spanish", other: "other" };
const selectedLanguage = document.getElementById("selected_language");
