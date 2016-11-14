import wordcram.*;

void setup() {
  fullScreen();
  //size(800, 600);
  background(255);
  colorMode(HSB);
  
  new WordCram(this)
      .fromTextFile("../wordList.txt")
      .sizedByWeight(1, 120)
      .withColors(color(30), color(110), color(random(255), 240, 200))
      .angledAt(0)
      .withFont("Copse")
      .drawAll();
}