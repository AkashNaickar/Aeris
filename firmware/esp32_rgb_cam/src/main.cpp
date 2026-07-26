#include <esp_camera.h>
#include <WiFi.h>
#include <SD_MMC.h>

static camera_config_t camera_config = {
    .pin_pwdn = 32,
    .pin_reset = -1,
    .pin_xclk = 0,
    .pin_sscb_sda = 26,
    .pin_sscb_scl = 27,
    .pin_d7 = 35,
    .pin_d6 = 34,
    .pin_d5 = 39,
    .pin_d4 = 36,
    .pin_d3 = 21,
    .pin_d2 = 19,
    .pin_d1 = 18,
    .pin_d0 = 5,
    .pin_vsync = 25,
    .pin_href = 23,
    .pin_pclk = 22,
    .xclk_freq_hz = 20000000,
    .ledc_timer = LEDC_TIMER_0,
    .ledc_channel = LEDC_CHANNEL_0,
    .pixel_format = PIXFORMAT_JPEG,
    .frame_size = FRAMESIZE_UXGA,
    .jpeg_quality = 10,
    .fb_count = 1,
};

void setup() {
    Serial.begin(115200);
    SD_MMC.begin();

    esp_camera_init(&camera_config);
    camera_fb_t *fb = esp_camera_fb_get();

    char filename[64];
    snprintf(filename, 64, "/rgb_%lu.jpg", millis());
    File file = SD_MMC.open(filename, FILE_WRITE);
    file.write(fb->buf, fb->len);
    file.close();
    esp_camera_fb_return(fb);

    WiFi.softAP("Aeris-RGB", "aeris2026");
    esp_deep_sleep(5 * 1000000);
}

void loop() {}
