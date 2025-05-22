from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, CONF_HA_ENDPOINT, CONF_XIAOZHI_ENDPOINT, CONF_TOKEN

class MCPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="MCP XiaoZhi Bridge", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_XIAOZHI_ENDPOINT): str,
                vol.Required(CONF_HA_ENDPOINT): str,
                vol.Required(CONF_TOKEN): str,
            })
        )