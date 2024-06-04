/*
 * let us add an image chager.
 * We will use jS and DOM AP1 features,
 * to alternate the display of one of two images.
 *
 * First, we store a reference to img element in var myImage.
 * Then we make the onclick event handler property equal to an
 * anonymous function.
 *
 * So every time the image is clicked:
 * 	the value of the image's src attribute is retrieved.
 * 	We then use a conditional to check if the src value is
 * 	equal to the path of the original image.
 * 	If it is, the src value is changed to the path of the second image.
 * 	Hence the other image is loaded inside the img element.
 * 	If it is not, meaning the image must have been already changed,
 * 	the src value is swapped back to the original image path.
 */
 	
const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/firefox-icon.png") {
    myImage.setAttribute("src", "images/image.png");
  } else {
    myImage.setAttribute("src", "images/firefox-icon.png");
  }
};

const myButton = document.querySelector("button");
const myHeading = document.querySelector("h1");

function setUserName () {
	/*
	 * This function contains the function prompt().
	 * It displays a dialog box similar to alert().
	 * It asks the user to enter data, storing it in a var,
	 * after user clicks OK.
	 * The API localStorage is called.
	 * Allows us to store data in the browser and retrieve it later.
	 * Then we use localStorage's setItem() to create and store a data item called name.
	 * We set the value of name to the myName.
	 * To avoid null or blank user name, add a conditional in the code like this.
	 */
	const myName = prompt("Please enter your name");

	if (!myName) {
		// run the function again from the start.
		setUserName();
	} else {
	localStorage.setItem("name", myName);
	myHeading.textContent = `Welcome to MDN, ${myName}!`;
	}
}

/*
 * We use the negation operator to check whether the name data exists.
 * If not setUserName function runs to create it.
 * If it exists because a user set it during a previous visit,
 * then it is retrieved using getItem().
 */
if (!localStorage.getItem("name")) {
	setUserName();
} else {
	const storedName = localStorage.getItem("name");
	myHeading.textContent = `Welcome to MDN, ${storedName}!`;
}

/*
 * Let us put the onClick event handler on the button.
 * When clicked, the function runs.
 * This will allow the user to enter a different name when the button is clicked.
 */
myButton.onclick = () => {
	setUserName();
}
