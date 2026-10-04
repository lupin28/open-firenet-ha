"""A bridge not linked to its stove yet reports a null model and firmware version (open-firenet >= 3.2.1)."""

from __future__ import annotations

from homeassistant.const import CONF_HOST, CONF_SCAN_INTERVAL
from homeassistant.helpers import device_registry as dr
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.open_firenet.const import DOMAIN


async def test_setup_with_null_stove_identity(hass, bridge):
    bridge.state["stove"].update(
        {"model": None, "model_name": None, "mainboard_version": None, "firmware_build": None}
    )
    entry = MockConfigEntry(domain=DOMAIN, data={CONF_HOST: bridge.host, CONF_SCAN_INTERVAL: 300})
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    devices = dr.async_entries_for_config_entry(dr.async_get(hass), entry.entry_id)
    assert devices
    assert devices[0].model == "RIKA Unknown"
    assert devices[0].sw_version.endswith("(MB ?)")
