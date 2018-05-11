
/**
 * 
 * @param menuElement
 * @returns
 */
function toggleMenus(menuElement, id) {
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