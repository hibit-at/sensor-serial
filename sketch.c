const int photoresistorPin = A0; // フォトレジスタが接続されているアナログピン

void setup() {
  Serial.begin(9600); // シリアル通信の開始
}

void loop() {
  int sensorValue = analogRead(photoresistorPin); // フォトレジスタからの情報を読み取る
  Serial.println(sensorValue); // シリアルモニタに情報を出力
  delay(1000); // 1秒間のディレイ
}