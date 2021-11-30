#include <WiFi.h>

// colocamos los datos de nuestra red
const char* ssid     = "Anastasia";
const char* password = "Mabe2402";

const IPAddress serverIP(192,168,18,2); // La dirección que desea visitar
uint16_t serverPort = 8881;         // Número de puerto del servidor

WiFiClient client; // Declarar un objeto cliente para conectarse al servidor

// Define Trig and Echo pin:
#define trigPin 2
#define echoPin 4

// Define variables:
long duration;
int distance;
int level;

void setup()
{
    // Define inputs and outputs
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    Serial.begin(115200);
    Serial.println();

    WiFi.mode(WIFI_STA);
    WiFi.setSleep(false); 
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(10000);
        Serial.println("Intentando conectar a la red Wi-Fi ...");
        WiFi.begin(ssid, password);
    }
    Serial.println("Conectado a Wi-Fi exitosamente");
    Serial.print("Direccion IP asignada:");
    Serial.println(WiFi.localIP());
}

void loop()
{   
    Serial.println("Intentando conectar al servidor");
    if (client.connect(serverIP, serverPort)) // Intenta acceder a la dirección de destino
    {
        Serial.println("Conexion exitosa");
    }
    else
    {
        Serial.println("Acceso fallido");
        client.stop(); // Cerrar el cliente
    }
    if (client.connected()) // Si está conectado
        {
            // Clear the trigPin by setting it LOW:
            digitalWrite(trigPin, LOW);
            
            delayMicroseconds(5);
          
           // Trigger the sensor by setting the trigPin high for 10 microseconds:
            digitalWrite(trigPin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trigPin, LOW);
            
            // Leer el echoPin. pulseIn() retorna la duracion en microsegundos:
            duration = pulseIn(echoPin, HIGH);
            
            // Calcular el nivel
            distance = duration*0.034/2;
            level = 1040-distance;
            Serial.println(level);
            client.print(level);  
            client.stop();// Enviar datos al servidor
        }
    delay(10000);
}
