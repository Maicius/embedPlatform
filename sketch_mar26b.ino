#include <dht11.h>

dht11 DHT11;
#define DHT11PIN 8
#define TRIG_PIN 2
#define ECHO_PIN 3
#define MAX_K 99
#define DEFAULT_COUNT 9

const int pinBuzzer = 7;
const int darkThreshold = 1000;

int darkness = 0;
float dist = 0.0;
float humidity = 0.0;
float temperature = 0.0;
float median_val;
float median_distance;
float distance_list[MAX_K];
float avg_val;
float avg_distance;
float avgDistanceList[MAX_K];

int median = 0;
int length_list;
int k;
float median_filter(float raw_val, int length_list, int k);

int loop_count = 0;

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

void checkDHT() {
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
  Serial.print("light:");
  Serial.println(darkness);

  dist = getDistance();
  if (loop_count > DEFAULT_COUNT) {
    k = loop_count % DEFAULT_COUNT;
    length_list = DEFAULT_COUNT;
  } else {
    length_list = loop_count;
    k = loop_count;
  }
  median_distance = median_filter(dist, length_list, k);
  Serial.print("distance:");
  Serial.println((long)dist);
  if (darkness > darkThreshold) {
    digitalWrite(pinBuzzer, LOW);
  } else {
    digitalWrite(pinBuzzer, HIGH);
  }

  int chk = DHT11.read(DHT11PIN);
  humidity = (float)DHT11.humidity;
  Serial.print("wet:");
  Serial.println(humidity);
  temperature = (float)DHT11.temperature;
  Serial.print("temperature:");
  Serial.println(temperature);
  loop_count++;
  delay(1000);

}

// 中位值滤波
float median_filter(float raw_val, int length_list, int k) {
  avgDistanceList[k] = raw_val;
  float sum = 0;
  for (int i = 0; i < length_list; i++) {
    sum += avgDistanceList[i];
  }
  avg_val = sum / length_list;
  //format_output("均值滤波：", avg_val);
  return avg_val;
}
