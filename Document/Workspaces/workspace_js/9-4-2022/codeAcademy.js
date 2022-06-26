const getUserChoice = function(userInput) {
  
  userInput = userInput.toLowerCase()
  if(userInput != 'scissors' && userInput !='paper' && userInput !='rock'){
    console.log("NOTHING HERE!")
  }else if(userInput == 'rock'){
    let rockOutput = console.log(`Here you are --> ${userInput} [0] | [${getComputerChoice()}] ${determineWinner()}`)
  }else if(userInput == 'paper'){
    let paperOutput = console.log(`Here you are --> ${userInput} [1] | [${getComputerChoice()}]`)
  }else if(userInput == 'scissors'){
    let scissorsOutput = console.log(`Here you are --> ${userInput} [2] | [${getComputerChoice()}]`)
  }else{
    console.log("Something goes wrong!?")
  }
}



let randNumber
const getComputerChoice = function(){
  randNumber = Math.floor(Math.random() * 3);
  return randNumber
}

const determineWinner = (userChoice,computerChoice) =>{
  let outputDM = ""
  if(userChoice == computerChoice) {
    outputDM= "Game tied."
  }
  return outputDM
}



for(i=0;i<5;i++){
  getUserChoice('rock')

  getUserChoice('paper')
  getUserChoice('scissors')
  console.log("---------------------")
}

determineWinner()
// console.log(`Total Rock = ${rNum}`)
// console.log(`Total Paper = ${pNum}`)
// console.log(`Total Scissors = ${sNum}`)

















// const getUserChoice = userInput => userInput.toLowerCase() != 'scissors' && userInput.toLowerCase() != 'paper' && userInput.toLowerCase() != 'rock' ? console.log("nothing here!") : console.log(`here you are --> ${userInput}`);

// getUserChoice('rock')


// const getComputerChoice => 