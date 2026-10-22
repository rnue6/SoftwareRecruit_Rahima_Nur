#include <Arduino.h>

// store encoder pin numbers and resolution
typedef struct {
    uint8_t cs;
    uint8_t clk;
    uint8_t mosi;
    uint8_t miso;
    uint8_t resolution;
} AMT22;


// initialize Encoder Pins
void AMT22_init(AMT22 *encoder,
                uint8_t csPin,
                uint8_t clkPin,
                uint8_t mosiPin,
                uint8_t misoPin,
                uint8_t resolution)
{
    // set encoder pins and resolution
    encoder->cs = csPin;
    encoder->clk = clkPin;
    encoder->mosi = mosiPin;
    encoder->miso = misoPin;
    encoder->resolution = resolution;

    // configure input and output pins
    pinMode(encoder->cs, OUTPUT);
    pinMode(encoder->clk, OUTPUT);
    pinMode(encoder->mosi, OUTPUT);
    pinMode(encoder->miso, INPUT);

    // set initial pin states
    digitalWrite(encoder->cs, HIGH);
    digitalWrite(encoder->clk, LOW);
    digitalWrite(encoder->mosi, LOW);
}


// Read Encoder Position
uint16_t AMT22_readPosition(AMT22 *encoder)
{
    uint16_t data = 0;

    // start communication with encoder
    digitalWrite(encoder->cs, LOW);
    delayMicroseconds(3);

    // read 16 bits from encoder
    for (uint8_t i = 0; i < 16; i++) {
        digitalWrite(encoder->clk, LOW);
        digitalWrite(encoder->mosi, LOW);
        delayMicroseconds(1);

        digitalWrite(encoder->clk, HIGH);

        // store each incoming bit
        data <<= 1;

        if (digitalRead(encoder->miso) == HIGH) {
            data |= 1;
        }

        delayMicroseconds(1);
    }

    // end communication with encoder
    digitalWrite(encoder->cs, HIGH);
    digitalWrite(encoder->clk, LOW);

    // keep the lower 14 position bits
    data &= 0x3FFF;

    // convert to 12-bit resolution if needed
    if (encoder->resolution == 12) {
        data >>= 2;
    }

    return data;
}

// Convert Position to Angle
float AMT22_readAngle(AMT22 *encoder)
{
    uint16_t position = AMT22_readPosition(encoder);
    uint16_t counts;

    // set total counts per rotation
    if (encoder->resolution == 12) {
        counts = 4096;
    } else {
        counts = 16384;
    }

    // calculate angle in degrees
    return (float)position * 360.0 / counts;
}


// Create Encoder Object
AMT22 jointEncoder;


void setup()
{
    // start serial communication
    Serial.begin(9600);

    // initialize encoder (CS, CLK, MOSI, MISO, resolution)
    AMT22_init(&jointEncoder, 5, 9, 10, 11, 14);
}


void loop()
{
    // read and display joint angle
    float angle = AMT22_readAngle(&jointEncoder);

    Serial.print("Joint angle: ");
    Serial.println(angle);

    // wait before next reading
    delay(100);
}
