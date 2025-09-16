from pyenjoy.definition.register_names import *
from pyenjoy.definition.register_values import *
modbus_map = {

    output_phase_a_voltage_n: output_phase_a_voltage,
    output_phase_b_voltage_n: output_phase_b_voltage,
    output_phase_c_voltage_n: output_phase_c_voltage,

    output_phase_a_current_n: output_phase_a_current,
    output_phase_b_current_n: output_phase_b_current,
    output_phase_c_current_n: output_phase_c_current,

    grid_frequency_n: grid_frequency,

    ac_output_total_active_power_n: ac_output_total_active_power,
    dc_total_power_n: dc_total_power,
    dc_total_current_n: dc_total_current,

    battery_voltage_n: battery_voltage,
    battery_current_n: battery_current,

    working_condition_n: working_condition,
    current_charge_discharge_working_mode_n: current_charge_discharge_working_mode,
    grid_connected_off_grid_state_n: grid_connected_off_grid_state,

    dsp_version_major_n: dsp_version_major,
    dsp_version_minor_n: dsp_version_minor,
    dsp_version_patch_n: dsp_version_patch,

    cpld_version_major_n: cpld_version_major,
    cpld_version_minor_n: cpld_version_minor,
    cpld_version_patch_n: cpld_version_patch,

    igbt_temperature_n: igbt_temperature,
    ambient_temperature_n: ambient_temperature,
    inductance_temperature_n: inductance_temperature,

    dc_history_charge_amount_n: dc_history_charge_amount,
    dc_daily_charge_amount_n: dc_daily_charge_amount,
    dc_history_discharge_amount_n: dc_history_discharge_amount,
    dc_daily_discharge_amount_n: dc_daily_discharge_amount,

    ac_history_charge_amount_n: ac_history_charge_amount,
    ac_daily_charge_amount_n: ac_daily_charge_amount,
    ac_history_discharge_amount_n: ac_history_discharge_amount,
    ac_daily_discharge_amount_n: ac_daily_discharge_amount,

    serial_number_n: serial_number,

    set_active_charge_discharge_power_n: set_active_charge_discharge_power,

    off_grid_settings_n: off_grid_settings,
    module_operation_mode_setting_n: module_operation_mode_setting,

    maximum_charge_power_n: maximum_charge_power,
    maximum_discharge_power_n: maximum_discharge_power,

    maximum_battery_charge_current_limit_n: maximum_battery_charge_current_limit,
    maximum_battery_discharge_current_limit_n: maximum_battery_discharge_current_limit,

    battery_temperature_n: battery_temperature,
    battery_soc_n: battery_soc,
    battery_soh_n: battery_soh,

    battery_max_charge_voltage_n: battery_max_charge_voltage,
    battery_max_charge_current_n: battery_max_charge_current,
    battery_max_discharge_voltage_n: battery_max_discharge_voltage,
    battery_max_discharge_current_n: battery_max_discharge_current,

    battery_remain_capacity_n: battery_remain_capacity,
    battery_charge_capacity_n: battery_charge_capacity,
    battery_discharge_capacity_n: battery_discharge_capacity,

    battery_daily_accumulate_charge_capacity_n: battery_daily_accumulate_charge_capacity,
    battery_daily_accumulate_discharge_capacity_n: battery_daily_accumulate_discharge_capacity,

    battery_history_accumulate_charge_capacity_n: battery_history_accumulate_charge_capacity,
    battery_history_accumulate_discharge_capacity_n: battery_history_accumulate_discharge_capacity,

    battery_charge_forbidden_n: battery_charge_forbidden,
    battery_discharge_forbidden_n: battery_discharge_forbidden,

}