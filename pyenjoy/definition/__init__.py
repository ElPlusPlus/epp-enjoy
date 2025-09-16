from pyenjoy.definition.register_names import *
from pyenjoy.definition.register_values import *
modbus_map = {
    serial_number_n: serial_number,
    inverter_model_n: inverter_model,
    ems_software_version_code_n: ems_software_version_code,
    ems_software_version_n: ems_software_version,
    dc_software_version_code_n: dc_software_version_code,
    dc_software_version_n: dc_software_version,
    inv_software_version_code_n: inv_software_version_code,
    inv_software_version_n: inv_software_version,
    rated_power_of_inverter_n: rated_power_of_inverter,

    secondary_working_mode_of_system_n: secondary_working_mode_of_system,
    system_working_state_n: system_working_state,
    primary_working_mode_of_system_n: primary_working_mode_of_system,

    pv_working_mode_n: pv_working_mode,
    pv_working_state_n: pv_working_state,

    battery_work_status_n: battery_work_status,

    dc_operating_status_n: dc_operating_status,

    # Real time data
    inverter_grid_phase_a_voltage_n: inverter_grid_phase_a_voltage,
    inverter_grid_phase_b_voltage_n: inverter_grid_phase_b_voltage,
    inverter_grid_phase_c_voltage_n: inverter_grid_phase_c_voltage,

    inverter_phase_a_voltage_n: inverter_phase_a_voltage,
    inverter_phase_b_voltage_n: inverter_phase_b_voltage,
    inverter_phase_c_voltage_n: inverter_phase_c_voltage,

    inverter_phase_a_frequency_n: inverter_phase_a_frequency,
    inverter_phase_b_frequency_n: inverter_phase_b_frequency,
    inverter_phase_c_frequency_n: inverter_phase_c_frequency,

    inverter_phase_a_current_n: inverter_phase_a_current,
    inverter_phase_b_current_n: inverter_phase_b_current,
    inverter_phase_c_current_n: inverter_phase_c_current,

    inverter_phase_a_active_power_n: inverter_phase_a_active_power,
    inverter_phase_b_active_power_n: inverter_phase_b_active_power,
    inverter_phase_c_active_power_n: inverter_phase_c_active_power,

    inverter_total_active_power_n: inverter_total_active_power,

    homeload_total_active_power_n: homeload_total_active_power,

    pv1_power_n: pv1_power,
    pv2_power_n: pv2_power,

    # Battery
    battery_power_n: battery_power,
    battery_soc_n: battery_soc,
    battery_voltage_n: battery_voltage,
    battery_current_n: battery_current,

    battery_cluster_1_number_of_clusters_n: battery_cluster_1_number_of_clusters,
    battery_cluster_1_number_of_battery_packs_n: battery_cluster_1_number_of_battery_packs,
    battery_cluster_1_average_cell_temperature_n: battery_cluster_1_average_cell_temperature,
    battery_cluster_1_rated_capacity_n: battery_cluster_1_rated_capacity,
    battery_cluster_1_charging_current_limit_n: battery_cluster_1_charging_current_limit,
    battery_cluster_1_discharge_current_limit_n: battery_cluster_1_discharge_current_limit,
    battery_cluster_1_charging_power_limit_n: battery_cluster_1_charging_power_limit,
    battery_cluster_1_discharge_power_limit_n: battery_cluster_1_discharge_power_limit,
    battery_cluster_1_charging_voltage_limit_n: battery_cluster_1_charging_voltage_limit,
    battery_cluster_1_discharge_voltage_limit_n: battery_cluster_1_discharge_voltage_limit,
    battery_cluster_1_rated_power_n: battery_cluster_1_rated_power,



    # Generation/consumption
    daily_pv1_power_generation_n: daily_pv1_power_generation,
    total_pv1_power_generation_n: total_pv1_power_generation,
    daily_pv2_power_generation_n: daily_pv2_power_generation,
    total_pv2_power_generation_n: total_pv2_power_generation,
    daily_pv_power_generation_n: daily_pv_power_generation,
    total_pv_power_generation_n: total_pv_power_generation,

    daily_export_grid_power_n: daily_export_grid_power,
    total_export_grid_power_n: total_export_grid_power,

    daily_purchase_grid_power_n: daily_purchase_grid_power,
    total_purchase_grid_power_n: total_purchase_grid_power,

    daily_consumption_homeload_power_n: daily_consumption_homeload_power,
    total_consumption_homeload_power_n: total_consumption_homeload_power,

    daily_battery_charging_power_n: daily_battery_charging_power,
    total_battery_charging_power_n: total_battery_charging_power,

    daily_battery_discharging_power_n: daily_battery_discharging_power,
    total_battery_discharging_power_n: total_battery_discharging_power,

    grid_frequency_n: grid_frequency,

    total_grid_active_power_n: total_grid_active_power,

    active_power_actual_value_setting_n: active_power_actual_value_setting,
    reactive_power_actual_value_setting_n: reactive_power_actual_value_setting,

    system_primary_working_mode_setting_n: system_primary_working_mode_setting,
    system_secondary_working_mode_setting_n: system_secondary_working_mode_setting,

    battery_charging_power_percentage_limit_n: battery_charging_power_percentage_limit,
    battery_discharging_power_percentage_limit_n: battery_discharging_power_percentage_limit,
    battery_charging_power_limit_n: battery_charging_power_limit,
    battery_discharging_power_limit_n: battery_discharging_power_limit,
    battery_charge_cut_off_soc_n: battery_charge_cut_off_soc,
    battery_discharge_cut_off_soc_n: battery_discharge_cut_off_soc,
    battery_mains_charging_enabled_n: battery_mains_charging_enabled,

    hot_system_primary_working_mode_setting_n: hot_system_primary_working_mode_setting,
    hot_system_secondary_working_mode_setting_n: hot_system_secondary_working_mode_setting,
    hot_active_power_actual_value_setting_n: hot_active_power_actual_value_setting,
    hot_battery_charging_power_percentage_limit_n: hot_battery_charging_power_percentage_limit,
    hot_battery_discharging_power_percentage_limit_n: hot_battery_discharging_power_percentage_limit,
    hot_battery_charge_cut_off_soc_n: hot_battery_charge_cut_off_soc,
    hot_battery_discharge_cut_off_soc_n: hot_battery_discharge_cut_off_soc,
}