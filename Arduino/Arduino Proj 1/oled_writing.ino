#include <Wire.h> 
#include <Adafruit_SSD1306.h>
#include <WiFi.h>

#define OLED_ADDR   0x3C
#define OLED_SDA    21
#define OLED_SCL    22

Adafruit_SSD1306 display(OLED_ADDR);

const char* ssid = "Radiohead";
const char* password = "echocharlie";

void setup() {
  Serial.begin(115200);
  
  // init.WiFi And Connect to Radiohead

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("\nConnecting");

  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(100);
    }

  Serial.println("\nConnected to the WiFi network");
  Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());

  // Display Setup

  Wire.begin(OLED_SDA, OLED_SCL);
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  
  // First Display Connection Details

    String a = Serial.readString();
    Serial.print(a);
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0, 0);
    display.println("\nConnected to the WiFi network");
    display.print("Local ESP32 IP: ");
    display.println(WiFi.localIP());
    display.display();

}

void loop() { 
  while (Serial.available() == 0); {}
    String a = Serial.readString();
    Serial.print(a);
    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(WHITE);
    display.setCursor(0, 0);
    display.println(a);
    display.display();
}
