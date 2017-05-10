PFont f;
String w[];
final int white = 255;
final int black = 0;

void setup() {
  fullScreen();
  background(152, 152, 152);
  f = createFont("Georgia",40,true);
  noCursor();
  frameRate(1);
}

void draw() {
  w = loadStrings("../topThreeWords.txt");
  background(white);
  fill(black);
  textFont(f,90);
  //rectMode(CENTER);
  textAlign(LEFT);
  String txt = "I feel " + w[0] + "\n\nI feel " + w[1] + "\n\nI feel "+ w[2];
  text(txt,200, 250);
}