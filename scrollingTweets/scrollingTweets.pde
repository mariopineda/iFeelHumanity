// Declare global variables
PFont f1; // Font for the "three words"
PFont f2; // Font for the scrolling tweets
int fontSize1 = 40;
int fontSize2 = 30;

String w[];
String tweets[];
final int white = 255;
final int black = 0;
final int grey = 150;
float y; // y coord of scrolling text
float x; // x coord of scrolling text
float dx = 1; // Decrement amount for x coord (= speed of scrolling tweets)
int i = 0; 
int alpha;

void setup() {
  fullScreen();
  //size(1200, 800);
  f1 = createFont("Georgia", fontSize1, true);
  f2 = createFont("Arial", fontSize2, true);
  noCursor();
  frameRate(30);
  
  // Set the coords for the first tweet to be scrolled
  x = width;
  y = (int) random(fontSize2, height-fontSize2);
  
  // Load tweets and randomly select first tweet to scroll
  tweets = loadStrings("../tweets.txt");
  i = (int) random(0, tweets.length); // Pick a random tweet

  // Set a random alpha (transparency) for first scrolling tweet
  alpha = (int) random(25,175);
}
  
void draw() {
  // Load data
  w = loadStrings("../topThreeWords.txt"); // Reloading three words every interation
  // TODO - reload tweet list regulaerly (but not every iteration)
  
  background(white);
  fill(black);
  textFont(f1, fontSize1);
  rectMode(CENTER);
  textAlign(LEFT);
  String txt = "I feel " + w[0] + "\n\nI feel " + w[1] + "\n\nI feel "+ w[2];
  text(txt,width/2,height/3);

  //
  // Scrolling tweets
  //
  fill(150, 150, 150, alpha);
  textFont(f2, fontSize2);
  rectMode(CORNER);
  textAlign(LEFT);
  text(tweets[i],x,y); 
  
  // Decrement x (move scrolling text)
  x = x - dx;
  
  // If x is less than the negative width of the text string, then it is off the screen and its time to set things up for the next tweet to be scrolled
  float tweetWidth = textWidth(tweets[i]);
  if (x < -tweetWidth) {
    x = width; 
    i = (int) random(0, tweets.length); // Pick a random tweet    
    y = (int) random(fontSize2, height-fontSize2); // Pick a random y coord
    alpha = (int) random(25,175);
  }
}