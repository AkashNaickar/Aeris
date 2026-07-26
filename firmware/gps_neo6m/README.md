# NEO-6M GPS Module

## Wiring

| GPS Module | ESP32-CAM |
|------------|-----------|
| VCC        | 3.3V      |
| GND        | GND       |
| TX         | GPIO16    |
| RX         | GPIO17    |

## Protocol

- Baud rate: 9600
- NMEA sentences: $GPGGA, $GPRMC
- Update rate: 1 Hz

The GPS is read by the ESP32-CAM _before_ each photo capture. Coordinates are embedded in the filename: `capture_<timestamp>_<lat>_<lng>.jpg`

## Cold Start Time

~30 seconds — plan demo accordingly. Keep drone powered on the ground until the GPS fix LED stops blinking.
