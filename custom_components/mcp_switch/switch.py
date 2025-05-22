import logging
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.entity import EntityCategory
from .const import DOMAIN
from .mcp_client import MCPProcess

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = MCPProcess(
        entry.data["xiaozhi_mcp_endpoint"],
        entry.data["ha_mcp_endpoint"],
        entry.data["ha_token"]
    )
    async_add_entities([MCPSwitch(entry.title, coordinator)], True)

class MCPSwitch(SwitchEntity):
    def __init__(self, name, coordinator: MCPProcess):
        self._attr_name = name
        self._coordinator = coordinator
        self._attr_is_on = False

    async def async_turn_on(self, **kwargs):
        await self._coordinator.start()
        self._attr_is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        await self._coordinator.stop()
        self._attr_is_on = False
        self.async_write_ha_state()

    @property
    def is_on(self):
        return self._attr_is_on