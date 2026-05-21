const cardsArray = [
    "Taj Mahal",
    "Kathak",
    "Diwali",
    "Biryani",
    "Taj Mahal",
    "Kathak",
    "Diwali",
    "Biryani"
];

cardsArray.sort(() => 0.5 - Math.random());

const gameBoard = document.getElementById("gameBoard");

let firstCard = null;
let secondCard = null;

cardsArray.forEach(text => {

    const card = document.createElement("div");
    card.classList.add("card");

    card.dataset.name = text;
    card.innerHTML = "?";

    card.addEventListener("click", () => {

        if(card.innerHTML === "?"){
            card.innerHTML = text;
        }

        if(!firstCard){
            firstCard = card;
        } else {
            secondCard = card;

            if(firstCard.dataset.name === secondCard.dataset.name){

                firstCard = null;
                secondCard = null;

            } else {

                setTimeout(() => {
                    firstCard.innerHTML = "?";
                    secondCard.innerHTML = "?";

                    firstCard = null;
                    secondCard = null;

                }, 1000);
            }
        }
    });

    gameBoard.appendChild(card);
});