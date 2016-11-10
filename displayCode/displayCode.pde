int timeDelay = 8000;
int time = 0;
int lastTime = 0; 
int fadeout = 255;
int fadein = -100; 
PFont f;

void setup() {
  fullScreen();
  background(152, 152, 152);
  f = createFont("Georgia",36,true);
}

boolean textfadesin = true;

void draw() {
  background(0);
  
  //
  // Load tweets
  //
  String tweets[] = loadStrings("../tweets.txt");
  println("Loading file with " + tweets.length + " tweets");
  for (int i=0; i < tweets.length; i++) {
    println(tweets[i]);
  }

  if (textfadesin) {
    fill(255, fadein); 
    fadein++;
  } else {
    fill(255, fadeout); 
    fadeout--;
  }

  textFont(f,36);
  rectMode(CENTER);
  text(tweets[3],width/2,height/2,700,300);
  
    if (millis() - time >= timeDelay) {
    time = millis();
    textfadesin = !textfadesin;
    fadein = 0;
    fadeout = 255;
  }
}