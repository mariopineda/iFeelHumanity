// Set up canvas
PFont f;
void setup() {
  fullScreen();
  background(255, 255, 255); // Background color as rgb values
  f = createFont("Georgia",16,true);
}

void draw() {
  background(255);
  String tweets[] = loadStrings("../tweets.txt");
  println("Loading file with " + tweets.length + " tweets");
  for (int i=0; i < tweets.length; i++) {
    println(tweets[i]);
  }

  textFont(f,36);
  fill(0,0,0);
  rectMode(CENTER);
  text(tweets[3],width/2,height/2,700,300);
}