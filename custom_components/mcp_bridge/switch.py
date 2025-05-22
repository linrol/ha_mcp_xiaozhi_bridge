import logging
from homeassistant.components.switch import SwitchEntity
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
        self._attr_unique_id = "mcp_bridge_switch"

        self._attr_device_info = {
            "identifiers": {(f"{DOMAIN}", "mcp_bridge_device")},
            "name": f"{self._attr_name}",
            "manufacturer": "linrol",
            "model": "MCP Bridge v1.0"
        }
        _LOGGER.debug("初始化设备: %s", self._attr_name)
        _LOGGER.debug("deviceId=%s", self._attr_unique_id)

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