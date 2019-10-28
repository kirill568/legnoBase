let title = document.title;
console.log(title);

let designers = document.querySelector(".designers");
let builders = document.querySelector(".builders");
let finishers = document.querySelector(".finishers");

switch (title) {
	case 'designers':
		designers.classList.add("underline");
		break;
	case 'builders':
		builders.classList.add("underline");
		break;
	case 'finishers':
		finishers.classList.add("underline");
		break;
}

