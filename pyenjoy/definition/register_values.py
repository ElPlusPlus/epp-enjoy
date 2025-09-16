from pyenjoy.definition.models import ModbusRegister, ModbusType, ModbusUnit, ModbusAccess


output_phase_a_voltage = ModbusRegister(0x6023, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
output_phase_b_voltage = ModbusRegister(0x6024, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
output_phase_c_voltage = ModbusRegister(0x6025, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)

output_phase_a_current = ModbusRegister(0x6026, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)
output_phase_b_current = ModbusRegister(0x6027, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)
output_phase_c_current = ModbusRegister(0x6028, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)

grid_frequency = ModbusRegister(0x602C, 1, 4, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RO, gain=0.01)

ac_output_total_active_power = ModbusRegister(0x6039, 1, 4, ModbusType.S16, ModbusUnit.KILO_WATT, ModbusAccess.RO, gain=0.1)
dc_total_power = ModbusRegister(0x6055, 1, 4, ModbusType.S16, ModbusUnit.KILO_WATT, ModbusAccess.RO, gain=0.1)
dc_total_current = ModbusRegister(0x6056, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)


battery_voltage = ModbusRegister(0x6053, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
battery_current = ModbusRegister(0x6034, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)

working_condition = ModbusRegister(0x6057, 1, 4, ModbusType.E16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
current_charge_discharge_working_mode = ModbusRegister(0x605B, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
grid_connected_off_grid_state = ModbusRegister(0x605C, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

dsp_version_major = ModbusRegister(0x6000, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
dsp_version_minor = ModbusRegister(0x6001, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
dsp_version_patch = ModbusRegister(0x6002, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

cpld_version_major = ModbusRegister(0x6003, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
cpld_version_minor = ModbusRegister(0x6004, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
cpld_version_patch = ModbusRegister(0x6005, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)


igbt_temperature = ModbusRegister(0x6058, 1, 4, ModbusType.S16, ModbusUnit.CELSIUS, ModbusAccess.RO, gain=0.1)
ambient_temperature = ModbusRegister(0x6059, 1, 4, ModbusType.S16, ModbusUnit.CELSIUS, ModbusAccess.RO, gain=0.1)
inductance_temperature = ModbusRegister(0x605A, 1, 4, ModbusType.S16, ModbusUnit.CELSIUS, ModbusAccess.RO, gain=0.1)

dc_history_charge_amount = ModbusRegister(0x6010, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)
dc_daily_charge_amount = ModbusRegister(0x6012, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)
dc_history_discharge_amount = ModbusRegister(0x6014, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)
dc_daily_discharge_amount = ModbusRegister(0x6016, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)

ac_history_charge_amount = ModbusRegister(0x6018, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)
ac_daily_charge_amount = ModbusRegister(0x601A, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)
ac_history_discharge_amount = ModbusRegister(0x601C, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)
ac_daily_discharge_amount = ModbusRegister(0x601E, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)

serial_number = ModbusRegister(0x6070, 16, 4, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

set_active_charge_discharge_power = ModbusRegister(0x0D57, 1, 3, ModbusType.S16, ModbusUnit.KILO_WATT, ModbusAccess.RW, gain=0.1)

off_grid_settings = ModbusRegister(0x5066, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
module_operation_mode_setting = ModbusRegister(0x501B, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

maximum_charge_power = ModbusRegister(0x5078, 1, 3, ModbusType.U16, ModbusUnit.KILO_WATT, ModbusAccess.RW, gain=0.1)
maximum_discharge_power = ModbusRegister(0x5079, 1, 3, ModbusType.U16, ModbusUnit.KILO_WATT, ModbusAccess.RW, gain=0.1)

maximum_battery_charge_current_limit = ModbusRegister(0x163F, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, ModbusAccess.RW, gain=0.1)
maximum_battery_discharge_current_limit = ModbusRegister(0x1640, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, ModbusAccess.RW, gain=0.1)

battery_temperature = ModbusRegister(0x1106, 1, 4, ModbusType.U16, ModbusUnit.CELSIUS, ModbusAccess.RO, gain=0.1)
battery_soc = ModbusRegister(0x1107, 1, 4, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RO, gain=1)
battery_soh = ModbusRegister(0x1120, 1, 4, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RO, gain=1)

battery_max_charge_voltage = ModbusRegister(0x1109, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
battery_max_charge_current = ModbusRegister(0x110A, 2, 4, ModbusType.U32, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.01)
battery_max_discharge_voltage = ModbusRegister(0x110C, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
battery_max_discharge_current = ModbusRegister(0x110D, 2, 4, ModbusType.U32, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.01)

battery_remain_capacity = ModbusRegister(0x1121, 2, 4, ModbusType.U32, ModbusUnit.WH, ModbusAccess.RO, gain=1)
battery_charge_capacity = ModbusRegister(0x1123, 2, 4, ModbusType.U32, ModbusUnit.WH, ModbusAccess.RO, gain=1)
battery_discharge_capacity = ModbusRegister(0x1125, 2, 4, ModbusType.U32, ModbusUnit.WH, ModbusAccess.RO, gain=1)

battery_daily_accumulate_charge_capacity = ModbusRegister(0x1127, 2, 4, ModbusType.U32, ModbusUnit.WH, ModbusAccess.RO, gain=1)
battery_daily_accumulate_discharge_capacity = ModbusRegister(0x1129, 2, 4, ModbusType.U32, ModbusUnit.WH, ModbusAccess.RO, gain=1)

battery_history_accumulate_charge_capacity = ModbusRegister(0x112B, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)
battery_history_accumulate_discharge_capacity = ModbusRegister(0x112D, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=1)

battery_charge_forbidden = ModbusRegister(0x1138, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
battery_discharge_forbidden = ModbusRegister(0x1139, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
