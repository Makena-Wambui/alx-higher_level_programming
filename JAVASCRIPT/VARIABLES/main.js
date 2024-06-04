const button = document.querySelector("#Button_A");
const heading = document.querySelector("#Heading_A");

button.onclick = () => {
	const name = prompt("What is your name?");
	alert(`Hello ${name}!`);
	heading.textContent = `Welcome, ${name}.`;
}
