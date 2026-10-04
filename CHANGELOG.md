# Changelog

## Non publié

### Fixes
- Device info: when the bridge is not linked to the stove yet (open-firenet reports a null model and firmware version), the device shows "RIKA Unknown" and "MB ?" instead of "MB None".

## v2.4.0 (2026-09-30)

### Features
- New diagnostic sensors: error code, error sub-code and warning code.
- New air flap sensors (position and target, in %), created only on stoves that report them.
- New option (Settings > Devices & services > Open Firenet > Configure): pick a Home Assistant temperature sensor to show as the climate entity's current temperature, e.g. for a stove without a RIKA room sensor. Display only: the stove keeps regulating on its own sensor; use Home Assistant's Generic Thermostat or an automation to switch it on/off from that sensor.

### Fixes
- Stoves without a RIKA room sensor no longer report 102.4 °C: the room temperature is now unknown.

Requires open-firenet firmware with the new `/api/state` fields (`warning_code`, `air_flaps_percent`, `room_sensor_connected`) for the warning and air flap sensors.
