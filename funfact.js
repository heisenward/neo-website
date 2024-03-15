document.addEventListener('DOMContentLoaded', function() {
    // List of fun facts
    var funFacts = [
      "Help",
      "HEY!",
      "I walk to Burger King, and then I walk back home from burger king 🔥😔",
      "SCOTLAND FOREVER!",
      "Someone is always watching",
      "I'm just gonna say it, Thundercat is amazing!",
      "L",
      "W",
      "It's a beautiful day outside. Birds are singing, flowers are blooming.",
      "This is one of the many random messages that can appear when you load the page.",
      "Hopes and dreams",
      "Classic",
      "Deltarune",
      "Lancer",
      "Here is my favorite game of all time:",
      "Have you ever seen a cat?",
      "Lucky Charm is the greatest dog ever!",
      "Where am I going?",
      "Thunderstruck",
      "Them Changes",
      "A Fan's Mail",
      "Minecraft",
      "Minceraft",
    ];
  
    // Get a random index from the funFacts array
    var randomIndex = Math.floor(Math.random() * funFacts.length);
  
    // Get the paragraph element to display the fun fact
    var funFactElement = document.getElementById('fun-fact');
  
    // Display the random fun fact
    funFactElement.textContent = funFacts[randomIndex];
  });
  