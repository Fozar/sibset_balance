# Интеграция Home Assistant для баланса "Сибсети"

Эта интеграция позволяет получать текущий баланс счёта интернет-провайдера "Сибсети" в Home Assistant.

## Описание

Интеграция использует нестандартные DNS-серверы провайдера для доступа к внутреннему ресурсу, где публикуется информация о балансе. Данные о балансе представлены в виде простого числа на веб-странице. Запрос должен происходить вашего IP адреса, который ассоциируется у провайдера с лицевым счетом.

## Установка

1. Скопируйте папку `my_balance_sensor` в директорию `custom_components` вашего Home Assistant.
2. Перезагрузите Home Assistant.

## Конфигурация

Добавьте следующие строки в файл `configuration.yaml`:

```yaml
sensor:
  - platform: my_balance_sensor
    scan_interval: 3600  # Интервал обновления в секундах
