if (sessionStorage.getItem("logginView") == "active") {
	initToggleMenus(document.getElementById("loggin-button"),
			"loggin-container");
} else {
	sessionStorage.setItem("logginView", "inactive")
}
/**
 * 
 * @param menuElement
 * @returns
 */
function toggleMenus(menuElement, id) {
	menuElement.classList.toggle("toggle");
	var element = document.getElementById(id);
	element.classList.toggle("toggle");
	if (id == "loggin-container") {
		if (sessionStorage.getItem("logginView") == "active") {
			sessionStorage.setItem("logginView", "inactive")
		} else {
			sessionStorage.setItem("logginView", "active")
		}
	}
}
function initToggleMenus(menuElement, id) {
	menuElement.classList.toggle("toggle");
	var element = document.getElementById(id);
	element.classList.toggle("toggle");
}
function toggleForm(hideId, showId) {
	var hideElement = document.getElementById(hideId);
	hideElement.style.display = "inline"
	var showElement = document.getElementById(showId);
	showElement.style.display = "none"
}