import logging
import dns.resolver
import requests
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

# Константы
PRIMARY_DNS_SERVER = '193.238.131.93'
ALTERNATIVE_DNS_SERVER = '193.238.131.65'
URL = 'http://android-market.eltex.local/balance'
HOSTNAME = 'android-market.eltex.local'


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Настройка платформы сенсора."""
    add_entities([BalanceSensor()], True)


class BalanceSensor(Entity):
    """Представление сенсора баланса."""

    def __init__(self):
        """Инициализация сенсора."""
        self._state = None

    @property
    def name(self):
        """Возвращает имя сенсора."""
        return 'Баланс: Сибирские сети'

    @property
    def state(self):
        """Возвращает состояние сенсора."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Возвращает единицу измерения."""
        return '₽'

    def update(self):
        """Обновление состояния сенсора."""
        try:
            # Использование заданных DNS-серверов для разрешения имени хоста
            resolver = dns.resolver.Resolver()
            resolver.nameservers = [PRIMARY_DNS_SERVER, ALTERNATIVE_DNS_SERVER]
            answers = resolver.resolve(HOSTNAME, 'A')
            ip_address = answers[0].to_text()

            # Создание URL с использованием IP-адреса
            url_with_ip = URL.replace(HOSTNAME, ip_address)

            # Выполнение HTTP запроса
            response = requests.get(url_with_ip, headers={'Host': HOSTNAME})
            self._state = response.text.strip()
        except Exception as e:
            _LOGGER.error("Ошибка при получении данных: %s", e)
            self._state = None
