"""The hello integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry) -> bool:
    """Set up hello from a config entry."""

    hass.states.set("hello_world.hello", "Hello, world!")

    # Return boolean to indicate that initialization was successful.
    return True
