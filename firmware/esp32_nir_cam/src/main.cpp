#include <esp_camera.h>
#include <WiFi.h>
#include <SD_MMC.h>
#include <TinyGPS++.h>
#include "config.h"

TinyGPSPlus gps;
HardwareSerial gpsSerial(2);

static camera_config_t camera_config = {
    .pin_pwdn = -1,
    .pin_reset = -1,
    .pin_xclk = GPIO_NUM_4,
    .pin_sscb_sda = GPIO_NUM_18,
    .pin_sscb_scl = GPIO_NUM_23,
    .pin_d7 = GPIO_NUM_36,
    .pin_d6 = GPIO_NUM_37,
    .pin_d5 = GPIO_NUM_38,
    .pin_d4 = GPIO_NUM_39,
    .pin_d3 = GPIO_NUM_35,
    .pin_d2 = GPIO_NUM_34,
    .pin_d1 = GPIO_NUM_5,
    .pin_d0 = GPIO_NUM_13,
    .pin_vsync = GPIO_NUM_25,
    .pin_href = GPIO_NUM_26,
    .pin_pclk = GPIO_NUM_27,
    .xclk_freq_hz = 20000000,
    .ledc_timer = LEDC_TIMER_0,
    .ledc_channel = LEDC_CHANNEL_0,
    .pixel_format = PIXFORMAT_JPEG,
    .frame_size = FRAMESIZE_SVGA,
    .jpeg_quality = 12,
    .fb_count = 1,
};

void setup() {
    Serial.begin(115200);
    gpsSerial.begin(9600, SERIAL_8N1, GPIO_NUM_16, GPIO_NUM_17);

    if (!SD_MMC.begin()) {
        Serial.println("SD Card mount failed");
        esp_deep_sleep_start();
    }

    camera_config.ledc_channel = LEDC_CHANNEL_0;
    esp_err_t err = esp_camera_init(&camera_config);
    if (err != ESP_OK) {
        Serial.printf("Camera init failed: 0x%x", err);
        esp_deep_sleep_start();
    }

    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb) {
        Serial.println("Camera capture failed");
        esp_deep_sleep_start();
    }

    while (gpsSerial.available() && gps.encode(gpsSerial.read())) {}

    char filename[64];
    snprintf(filename, sizeof(filename), "/capture_%ld_%.6f_%.6f.jpg",
             millis(), gps.location.lat(), gps.location.lng());

    File file = SD_MMC.open(filename, FILE_WRITE);
    file.write(fb->buf, fb->len);
    file.close();
    esp_camera_fb_return(fb);

    WiFi.softAP(AP_SSID, AP_PASS);
    esp_deep_sleep(5 * 1000000);
}

void loop() {}
