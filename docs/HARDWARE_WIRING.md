# Hardware Wiring Guide

## Pin Map

### ESP32-NoIR-CAM (GPIO)

| Component | GPIO Pin |
|-----------|----------|
| Camera CS | 4 |
| Camera SCK | 14 |
| Camera MOSI | 13 |
| Camera MISO | 12 |
| Red Filter Servo | 15 |
| Deep-sleep wake | RTC_GPIO0 (GPIO36) |

### NEO-6M GPS → ESP32 (Serial)

| GPS | ESP32 |
|-----|-------|
| TX | GPIO16 (RX2) |
| RX | GPIO17 (TX2) |
| VCC | 3.3V |
| GND | GND |

### Power Distribution

```
11.1V 3S LiPo
    ├── F450 Flight Controller (ESC BEC → 5V)
    ├── ESP32-CAM (5V IN via VIN pin)
    └── NEO-6M (3.3V via regulator)
```

## Wiring Diagram (Text)

```
         ┌──────────────────────────────┐
         │        F450 Frame            │
         │  ┌──────────────────────┐    │
         │  │  KK 2.1.5 / Pixhawk │    │
         │  └──────────┬───────────┘    │
         │             │ 5V BEC         │
         │             ▼                │
         │  ┌──────────────────────┐    │
         │  │   ESP32-NoIR-CAM     │    │
         │  │   GPIO16 ← GPS TX    │    │
         │  │   GPIO17 → GPS RX    │    │
         │  │   GPIO4  ← CAM CS    │    │
         │  │   GPIO15 → Filter    │    │
         │  └──────────────────────┘    │
         │  ┌──────────────────────┐    │
         │  │   ESP32-RGB-CAM      │    │
         │  │   (same wiring,      │    │
         │  │    different UART)   │    │
         │  └──────────────────────┘    │
         └──────────────────────────────┘
```
