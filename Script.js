// Array of quotes
var quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The will to win, the desire to succeed, the urge to reach your full potential... these are the keys that will unlock the door to personal excellence. - Confucius"



  ];
  
  // Function to generate a random quote
  function generateQuote() {
    var randomIndex = Math.floor(Math.random() * quotes.length);
    var quoteElement = document.getElementById("quote");
    quoteElement.textContent = quotes[randomIndex];
  }
  
  // Event listener for the button
  var generateButton = document.getElementById("generateButton");
  generateButton.addEventListener("click", generateQuote);
  