#include <dht11.h>

dht11 DHT11;
#define DHT11PIN 8
#define TRIG_PIN 2
#define ECHO_PIN 3

const int pinBuzzer = 7;
const int darkThreshold = 1000;

int darkness = 0;
float dist = 0.0;
float humidity=0.0;
float temperature=0.0;

float getDistance() {
  float cm;
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  cm = pulseIn(ECHO_PIN, HIGH) / 58.82; //算成厘米
  cm = (int(cm * 100.0)) / 100.0; //保留两位小数
  return cm;
}

void checkDHT(){
  int chk = DHT11.read(DHT11PIN);
  // 测试 DHT 是否正确连接
  Serial.print("Read sensor: ");
  switch (chk)
  {
    case DHTLIB_OK: 
    Serial.println("OK"); 
    break;
    case DHTLIB_ERROR_CHECKSUM: 
    Serial.println("Checksum error"); 
    break;
    case DHTLIB_ERROR_TIMEOUT: 
    Serial.println("Time out error"); 
    break;
    default: 
    Serial.println("Unknown error"); 
    break;
  }
}

void setup() {
  Serial.begin(9600);
//  Serial.println("DHT11 TEST PROGRAM");
//  Serial.print("LIBRARY");
  // 输出 DHT 库的版本号
//  Serial.println(DHT11LIB_VERSION);
//  Serial.println();
  pinMode(pinBuzzer, OUTPUT);
  
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  
}

void loop() {
  darkness = analogRead(A0);
  Serial.print("darkness:");
  Serial.println(darkness);

  dist = getDistance();
  Serial.print("distance:");  
  Serial.println(dist);
  
  if (darkness > darkThreshold) {
    digitalWrite(pinBuzzer, LOW);
  } else {
    digitalWrite(pinBuzzer, HIGH);
  }
  
  int chk = DHT11.read(DHT11PIN);
  humidity=(float)DHT11.humidity;
  Serial.print("humidity (%): ");
  Serial.println(humidity);
  temperature=(float)DHT11.temperature;
  Serial.print("Temperature °C): ");
  Serial.println(temperature);

  delay(2000);
}
