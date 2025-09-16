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






# System
serial_number = ModbusRegister(70, 8, 4, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
inverter_model = ModbusRegister(108, 15, 4, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
ems_software_version_code = ModbusRegister(151, 2, 4, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
ems_software_version = ModbusRegister(57, 2, 4, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
dc_software_version_code = ModbusRegister(152, 2, 4, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
dc_software_version = ModbusRegister(62, 2, 4, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
inv_software_version_code = ModbusRegister(154, 2, 4, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
inv_software_version = ModbusRegister(60, 2, 4, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
rated_power_of_inverter = ModbusRegister(83, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

secondary_working_mode_of_system = ModbusRegister(2, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
system_working_state = ModbusRegister(3, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
primary_working_mode_of_system = ModbusRegister(4, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

pv_working_mode = ModbusRegister(10, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
pv_working_state = ModbusRegister(11, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

battery_work_status = ModbusRegister(69, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

dc_operating_status = ModbusRegister(427, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)

# Real time data
inverter_grid_phase_a_voltage = ModbusRegister(410, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
inverter_grid_phase_b_voltage = ModbusRegister(411, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
inverter_grid_phase_c_voltage = ModbusRegister(412, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)

inverter_phase_a_voltage = ModbusRegister(312, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
inverter_phase_b_voltage = ModbusRegister(313, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
inverter_phase_c_voltage = ModbusRegister(314, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)

inverter_phase_a_frequency = ModbusRegister(315, 1, 4, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RO, gain=0.01)
inverter_phase_b_frequency = ModbusRegister(316, 1, 4, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RO, gain=0.01)
inverter_phase_c_frequency = ModbusRegister(317, 1, 4, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RO, gain=0.01)

inverter_phase_a_current = ModbusRegister(318, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)
inverter_phase_b_current = ModbusRegister(319, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)
inverter_phase_c_current = ModbusRegister(320, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)

inverter_phase_a_active_power = ModbusRegister(321, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)
inverter_phase_b_active_power = ModbusRegister(322, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)
inverter_phase_c_active_power = ModbusRegister(323, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)

inverter_total_active_power = ModbusRegister(330, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)

homeload_total_active_power = ModbusRegister(408, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)

pv1_power = ModbusRegister(387, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)
pv2_power = ModbusRegister(390, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)

# Battery
battery_power = ModbusRegister(420, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)
battery_soc = ModbusRegister(422, 1, 4, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RO, gain=1)
battery_voltage = ModbusRegister(429, 1, 4, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
battery_current = ModbusRegister(430, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)

battery_cluster_1_number_of_clusters = ModbusRegister(600, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
battery_cluster_1_number_of_battery_packs = ModbusRegister(607, 1, 4, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RO, gain=1)
battery_cluster_1_average_cell_temperature = ModbusRegister(625, 1, 4, ModbusType.S16, ModbusUnit.CELSIUS, ModbusAccess.RO, gain=0.1)
battery_cluster_1_rated_capacity = ModbusRegister(636, 1, 4, ModbusType.S16, ModbusUnit.NONE, ModbusAccess.RO, gain=0.1)
battery_cluster_1_charging_current_limit = ModbusRegister(638, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)
battery_cluster_1_discharge_current_limit = ModbusRegister(639, 1, 4, ModbusType.S16, ModbusUnit.AMPERE, ModbusAccess.RO, gain=0.1)
battery_cluster_1_charging_power_limit = ModbusRegister(640, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)
battery_cluster_1_discharge_power_limit = ModbusRegister(641, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)
battery_cluster_1_charging_voltage_limit = ModbusRegister(659, 1, 4, ModbusType.S16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
battery_cluster_1_discharge_voltage_limit = ModbusRegister(660, 1, 4, ModbusType.S16, ModbusUnit.VOLT, ModbusAccess.RO, gain=0.1)
battery_cluster_1_rated_power = ModbusRegister(661, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)



# Generation/consumption
daily_pv1_power_generation = ModbusRegister(13, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_pv1_power_generation = ModbusRegister(15, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
daily_pv2_power_generation = ModbusRegister(17, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_pv2_power_generation = ModbusRegister(19, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
daily_pv_power_generation = ModbusRegister(25, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_pv_power_generation = ModbusRegister(27, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)

daily_export_grid_power = ModbusRegister(33, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_export_grid_power = ModbusRegister(35, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)

daily_purchase_grid_power = ModbusRegister(37, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_purchase_grid_power = ModbusRegister(39, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)

daily_consumption_homeload_power = ModbusRegister(41, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_consumption_homeload_power = ModbusRegister(43, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)

daily_battery_charging_power = ModbusRegister(49, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_battery_charging_power = ModbusRegister(51, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)

daily_battery_discharging_power = ModbusRegister(53, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)
total_battery_discharging_power = ModbusRegister(55, 2, 4, ModbusType.U32, ModbusUnit.KWH, ModbusAccess.RO, gain=0.1)

grid_frequency = ModbusRegister(336, 1, 4, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RO, gain=0.01)

total_grid_active_power = ModbusRegister(351, 1, 4, ModbusType.S16, ModbusUnit.WATT, ModbusAccess.RO, gain=1)

# RW
active_power_actual_value_setting = ModbusRegister(5, 1, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=1)
reactive_power_actual_value_setting = ModbusRegister(6, 1, 3, ModbusType.U16, ModbusUnit.VAR, ModbusAccess.RW, gain=1)

system_primary_working_mode_setting = ModbusRegister(2, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
system_secondary_working_mode_setting = ModbusRegister(3, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

battery_charging_power_percentage_limit = ModbusRegister(261, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
battery_discharging_power_percentage_limit = ModbusRegister(262, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
battery_charging_power_limit = ModbusRegister(282, 2, 3, ModbusType.U32, ModbusUnit.WATT, ModbusAccess.RW, gain=1)
battery_discharging_power_limit = ModbusRegister(284, 2, 3, ModbusType.U32, ModbusUnit.WATT, ModbusAccess.RW, gain=1)
battery_charge_cut_off_soc = ModbusRegister(265, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
battery_discharge_cut_off_soc = ModbusRegister(266, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
battery_mains_charging_enabled = ModbusRegister(269, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Frequent reading/writing
hot_system_primary_working_mode_setting = ModbusRegister(930, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
hot_system_secondary_working_mode_setting = ModbusRegister(931, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
hot_active_power_actual_value_setting = ModbusRegister(932, 1, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=1)
hot_battery_charging_power_percentage_limit = ModbusRegister(933, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
hot_battery_discharging_power_percentage_limit = ModbusRegister(934, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
hot_battery_charge_cut_off_soc = ModbusRegister(935, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
hot_battery_discharge_cut_off_soc = ModbusRegister(936, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=1)
