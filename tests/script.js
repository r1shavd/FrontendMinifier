// The JavaScript for the frontend handling. Good documentation would be present

/* Handling the modal popup actions :-
First assigning the events to the buttons which contains class name 'modal-show-btn'
*/

// Displaying the modals when the user clicks on the element with the class modal-show-btn
Array.from(document.getElementsByClassName('modal-show-btn')).forEach(function(element, index) {
	// Adding the listening event for each such element btn

	element.addEventListener('click', function(e) {
		// First we get the modal id via the href attribute of the button

		e.preventDefault();
		let modal = document.querySelector(e.target.getAttribute("href"));
		modal.style.display = 'block';
	});
});
// Hiding the modal when the user clicks the close modal btn
Array.from(document.getElementsByClassName('modal-dialog')).forEach(function(element, index) {
	// Iterating through each modal-dialog HTML elements on the page

	if (element.className.includes('alert')) {
		// If the current modal element is actually the alert box, then we skip the process here
		//pass
	} else {
		let modalCloseBtn = element.getElementsByClassName('modal-close-btn')[0];
		modalCloseBtn.addEventListener('click', function(e) {
			e.preventDefault();
			element.style.display = 'none';
		});
	}
});

// Displaying the alert when function is called
let showAlert = (type, title, message) => {
	// The function for the showing of an alert modal on the window of the user

	let alert = document.querySelector('div.modal-dialog.alert');
	let alertBox = alert.getElementsByClassName('alert-box')[0];
	alertBox.classList.remove('success');
	alertBox.classList.remove('error');
	alertBox.classList.add(type);
	alert.getElementsByClassName('head')[0].innerHTML = `${title}<span class="alert-close-btn" onclick="closeAlert(this);">&times;</span>`;
	alert.getElementsByClassName('body')[0].innerHTML = message;
	alert.style.display = 'block';
}
// Closing an alert when the alert-close-btn is clicked
let closeAlert = (element) => {
	// When the user clicks on the close alert box button, then we close the parentNode modal-dialog (in fact removing it from the HTML DOM)

	let alert = document.querySelector('div.modal-dialog.alert');
	alert.style.display = 'none';
}

/* 
Handling the navigation bars functions
*/
// Getting the sidebar menu toggle buttons and assigning them the function for which the sidebar is shown
Array.from(document.getElementsByClassName('menu-toggle-btn')).forEach((element, index) => {
	// Configuring each of the menu toggle bars with the same functions

	let sidebar = document.getElementsByClassName('sidebar')[index];
	element.addEventListener('click', (e) => {
		// When the user clicks on the toggle menu button, we toggle the classname with the active class to display the sidebar on the screen
		
		e.preventDefault();
		sidebar.classList.toggle('active');
		element.classList.toggle('active');
	})
});
// Getting the nav-item and assigning them a link function
Array.from(document.getElementsByClassName('nav-item')).forEach((element, index) => {
	// Setting the same onclick event for all such nav items

	let classList = Array.from(element.classList);
	if (classList.includes('modal-show-btn') || classList.includes('other')) {
		// If the nav-item is a modal show button or has other class in it, then we pass the function

		return false;
	}

	element.addEventListener('click', (e) => {
		// When the user clicks on the nav-item, we redirect the user 

		e.preventDefault();
		try {
			let targetLocation = e.target.getAttribute('href');
			location.href = targetLocation;
		} catch(error) {}
	})
});

// Assigning the onclick visit feature to the link-btn class buttons
/* Make the button in this form
	<button class="btn link-btn" href="/link/to/page">...</button>
   Add the link-btn class to the button tags or anchor tags. The href attribute to the tag and proper target location should be provided.
   No other class should be added except 'btn' and colored-button classes
   */
   Array.from(document.getElementsByClassName('link-btn')).forEach((element, index) => {
	// Assigning the functions to each buttons with the class

	element.addEventListener('click', (e) => {
		// When the user clicks on the button, we redirect the user to the link given in the HREF attribute in the button

		targetLocation = e.target.getAttribute('href');
		location.href = targetLocation;
		return true;
	});

	return true;
});

// Validating the search form but in a try..except.. block for error free execution
try {
	// Getting the search form element from the page
	const searchForm = document.getElementById('search-form');

	// Adding an onsubmit event listener to the search form	
	searchForm.addEventListener('submit', (e) => {
		// Checking the search form when the user clicks submit

		e.preventDefault();
		searchQuery = searchForm.querySelector('input[name="q"]').value.length; // The search query input field's value
		if (searchQuery == 0) {
			// If the user enters the query field as blank

			return false;
		} else {
			// If the user enters atleast something in the query field
			
			searchForm.submit();
			return true;
		}
	});
} catch(error) {/* If BTW the form is currently not displayed at the served HTML page */}

// Assigning the image slider feature to the div with the class name 'image-slider'. Aslo the slider is manual
let image_slide_index = 1;  // Setting the default index to the slide as 0
displaySlides(image_slide_index);  

function nextSlide(n) {  
	// The function for changing the next slides

	displaySlides(image_slide_index += n);  
}  

function currentSlide(n) {  
	// The function for displaying the current slide in the image-slider

	displaySlides(image_slide_index = n);  
}  

function displaySlides(n) {  
	// The function for switching between the slides in the image-slider manual

	try {
		var i;  
		var slides = document.getElementsByClassName("slide");  
		if (n > slides.length) { image_slide_index = 1; }  
		if (n < 1) { image_slide_index = slides.length; }  
		for (i = 0; i < slides.length; i++) {  
			slides[i].style.display = "none";  
		}  
		slides[image_slide_index - 1].style.display = "block"; 
	} catch(error) {}
}

// Getting the CSRF token for the post request per page
let CSRFtoken;
try {
	CSRFtoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
} catch(error) {
	CSRFtoken = undefined;
}