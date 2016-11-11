int timeDelay = 8000;
int time = 0;
int lastTime = 0; 
int fadeout = 255;
int fadein = -100; 
PFont f;
String tweets[];

void setup() {
  fullScreen();
  background(152, 152, 152);
  f = createFont("Georgia",36,true);
  tweets = loadStrings("../tweets.txt");
}

boolean textfadesin = true;
int i = 0;

void draw() {
  background(0);

  if (textfadesin) {
    fill(255, fadein); 
    fadein++;
  } else {
    fill(255, fadeout); 
    fadeout--;
  }

  textFont(f,36);
  rectMode(CENTER);
  text(tweets[i],width/2,height/2,700,300);
  
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