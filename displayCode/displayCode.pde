int timeDelay = 8000;
int time = 0;
int lastTime = 0; 
int fadeout = 255;
int fadein = -100; 
PFont f;
String tweets[];
final int white = 255;
final int black = 0;

void setup() {
  fullScreen();
  background(152, 152, 152);
  f = createFont("Georgia",36,true);
  tweets = loadStrings("../tweets.txt");
  noCursor();
}

boolean textfadesin = true;
int i = 0;

void draw() {
  background(white);

  if (textfadesin) {
    fill(black, fadein); 
    fadein++;
  } else {
    fill(black, fadeout); 
    fadeout--;
  }

  textFont(f,36);
  rectMode(CENTER);
  textAlign(LEFT);
  text(tweets[i],width/2,height/2,width*0.5,height*0.25);
  
    if (millis() - time >= timeDelay) {
    time = millis();
    textfadesin = !textfadesin;
    fadein = 0;
    fadeout = 255;
    if (textfadesin) {
      i++;
    }
  }
}