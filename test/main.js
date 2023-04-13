const snowscraper = document.querySelector(".snowscraper");

const createWord = (text, index) => {
    const letter = document.createElement("span");

    letter.innerHTML = text;

    letter.classList.add("snowscraper-letter");

    letter.style.transitionDelay = `${index * 40}ms`;

    return letter;
}

const addWord = (text, index) => snowscraper.appendChild(createWord(text, index));

const createTitle = text => text.split("").map(addWord);

createTitle("SNOWSCRAPER")
