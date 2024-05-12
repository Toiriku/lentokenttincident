

const Context = {
  BEGINNING: 'beginning',
  TRAVEL: 'travel',
  ARRIVAL: 'arrival',
  ENCOUNTER_BUM: 'encounter_bum',
  GAMBLE: 'gamble',
  BLACKJACK: 'blackjack'
};
const Actions = {
  [Context.BEGINNING]: ['Game start'],
  [Context.TRAVEL]: ['Explore X', 'Explore Y', 'Explore Z', 'Explore W'],
  [Context.ARRIVAL]: ['Start Encounter'],
  [Context.ENCOUNTER_BUM]: ['Gamble', 'Trade', 'Information Gathering', 'Move On'],
  [Context.GAMBLE]: ['Start Blackjack', 'fuck go back'],
  [Context.BLACKJACK]: ['Commit tax fraud', 'bet more money']
};

let currentContext = null;

function startEncounter(context) {
  currentContext = context;
  updateActions();
  writing(`Action: ${Description(context)}`);
}



function handleAction(action) {
  console.log(`Handling action: ${action}`);

  switch (currentContext) {
    case Context.BEGINNING:
      startEncounter(Context.TRAVEL);
      writing(`Starting travel: ${currentContext}`);
      break;
    case Context.TRAVEL:
      writing(`You traveled to ${action}`);
      startEncounter(Context.ARRIVAL);
      break;
    case Context.ARRIVAL:
      startEncounter(Context.ENCOUNTER_BUM);
      break;
    case Context.GAMBLE:
      startEncounter(Context.GAMBLE)
      fetch('/play_game', {method: 'POST'})
      break;
    default:
      break;
  }
}




// Nettisivun nappulan päivitys
function updateActions() {
  const actionBox = document.getElementById('actionBox');
  actionBox.innerHTML = ''; // Clear previous actions

  const actions = Actions[currentContext];
  actions.forEach(action => {
    addActionButton(action);
  });
}

function addActionButton(action) {
  const actionBox = document.getElementById('actionBox');
  const button = document.createElement('button');
  button.textContent = action;
  button.addEventListener('click', () => handleAction(action));
  actionBox.appendChild(button);
}

function writing(teksti) {
  const dialogBox = document.getElementById('dialogBox');
  dialogBox.innerHTML += `<p>${teksti}</p>`;
}

function Description(context) {
  switch (context) {
    case Context.BEGINNING:
      return 'Beginning...';
    case Context.ENCOUNTER_BUM:
      return 'Interact with the bum';
    case Context.TRAVEL:
      return 'Traveling: What location will you explore?';
    case Context.ARRIVAL:
      return 'Arrived at a new location';
    case Context.GAMBLE:
      return 'choice: gamble';
    case Context.BLACKJACK:
      return 'Starting Blackjack';
    default:
      return 'b';
  }
}

// Add event listener to the Travel button after DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
  startEncounter(Context.BEGINNING);
});