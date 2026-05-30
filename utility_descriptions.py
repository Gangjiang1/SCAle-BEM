
# =================
# utility code for description generation
# =================

def generate_chilled_water_description(chiller_num, chiller_details):
    description = f"For the chilled water loop in the system, the chilled water is supplied by electric chillers. \n"
    for chiller_id, details in chiller_details.items():
        description += (
            f"Chiller {chiller_id} has a rated capacity of {details['chiller_capacity']} W and a rated COP of {details['chiller_COP']}. \n"
        )
    description += (
            f"The chilled water supply temperature is {details['chilled_water_supply_temperature']} Celsius. "
            f"The design temperature difference (DeltaT) for chilled water is {details['chilled_water_temperature_difference']} Celsius."
            f"The rated efficiency of the pump is {details['pump_efficiency']}, with a rated flow rate of {details['pump_flow']} m3/s, "
            f"a rated pump head of {details['pump_head']} Pa, and a rated power of {details['pump_power']} W. \n"
        )
    return description

def generate_hot_water_description(boiler_num, boiler_details):
    description = ""
    for boiler_id, details in boiler_details.items():
        description += (
            f"Boiler {boiler_id} has a rated capacity of {details['boiler_capacity']} W and a rated efficiency of {details['boiler_efficiency']}. \n"
        )
    description += (
            f"The hot water supply temperature is {details['hot_water_supply_temperature']} Celsius. "
            f"The design temperature difference (DeltaT) for hot water is {details['hot_water_temperature_difference']} Celsius."
            f"The rated efficiency of the pump is {details['pump_efficiency']}, with a rated flow rate of {details['pump_flow']} m3/s, "
            f"a rated pump head of {details['pump_head']} Pa, and a rated power of {details['pump_power']} W. \n"
        )
    description2 = f"For the hot water loop in the system, the hot water is supplied by {details['fuel_type']} boilers. \n" + description
    return description2

def generate_condenser_water_description(tower_num, tower_details):
    description = ""
    for tower_id, details in tower_details.items():
        tower_capacity = details['tower_capacity'] if details['tower_capacity'] else 'Autosize'
        description += (
            f"Cooling tower {tower_id} has a rated capacity of {tower_capacity} W. The rated air flow rate is {details['air_flow']} m3/s, and the rated water flow rate is {details['water_flow']} m3/s. The fan's rated power is {details['fan_power']} W. \n"
        )
    description += (
            f"The rated efficiency of the pump is {details['pump_efficiency']}, with a rated flow rate of {details['pump_flow']} m3/s, "
            f"a rated pump head of {details['pump_head']} Pa, and a rated power of {details['pump_power']} W. \n"
        )
    description2 = f"For the condenser water loop in the system, the condenser water is supplied by cooling towers. \n" + description
    return description2

########
def generate_air_system_fcu_description(unit_details):

    # 显示全部zones
    description = ""
    for unit, details in unit_details.items():  # 遍历 `unit_details` 这个字典
        # zones = ", ".join(details['zones'])
        # Process each zone name: remove 'Thermal ' and convert to lowercase
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        # Join the processed zone names into a single string separated by commas
        zones_str = ', '.join(zones)
        # 使用条件表达式动态生成控制方式描述
        control_description = (
            "variable fan" if details['control'] == "ASHRAE90VariableFan" else
            "cycling fan" if details['control'] == "CyclingFan" else
            "multi speed fan" if details['control'] == "MultiSpeedFan" else
            "variable fan and variable water flow" if details['control'] == "VariableFanVariableFlow" else
            details['control']
        )
        description += (
            f"The HVAC system in this building is fan coil unit, FCU, system, which serves {zones_str}.\n"
            f"The capacity control method of fan coil units, FCUs, is {control_description}.\n"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency of fan coil units, FCUs, is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )
    return description

def generate_air_system_vrf_description(unit_details):

    # 显示全部zones
    description = ""
    for unit, details in unit_details.items():  # 遍历 `unit_details` 这个字典
        # zones = ", ".join(details['zones'])
        # Process each zone name: remove 'Thermal ' and convert to lowercase
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        # Join the processed zone names into a single string separated by commas
        zones_str = ', '.join(zones)
        description += (
            f"The HVAC system in this building is variable refrigerant flow, VRF, system, which serves {zones_str}.\n"
            f"The rated capacity is {details['cooling_capacity']} W for cooling and {details['heating_capacity']} W for heating.\n"
            f"The rated cooling COP is {details['cooling_COP']} and the heating COP is {details['heating_COP']}.\n"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency of fan coil units, FCUs, is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )
    return description

def generate_air_system_vav_description(unit_details):
    description = "The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.\n"

    for unit, details in unit_details.items():
        economizer_type = (
            "It includes an economizer, which operates based on differential dry bulb.\n" if details['economizer'] == "DifferentialDryBulb" else
            "It includes an economizer, which operates based on differential enthalpy.\n" if details['economizer'] == "DifferentialEnthalpy" else
            "" if details['economizer'] == "NoEconomizer" else
            details['economizer']
        )        
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        zones_str = ', '.join(zones)
        description += (
            f"The AHU {unit} serves {zones_str}.\n{economizer_type}"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )
    return description

def generate_air_system_vav_fcu_descriptions(ahu_params, fcu_params):
    """
    根据生成的参数，构造 AHU 与 FCU 的描述文本。
    """
    description1 = "The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.\n"
    # 如果 AHU 有 economizer（且不为 NoEconomizer），则增加描述
    
    economizer_text = (
        "It includes an economizer, which operates based on differential dry bulb.\n" if ahu_params['economizer'] == "DifferentialDryBulb" else
        "It includes an economizer, which operates based on differential enthalpy.\n" if ahu_params['economizer'] == "DifferentialEnthalpy" else
        "" if ahu_params['economizer'] == "NoEconomizer" else
        ahu_params['economizer']
    )
    zones_AHU = [zone.replace('Thermal ', '').lower() for zone in ahu_params['zones']]
    zones_AHU_str = ', '.join(zones_AHU)
    description_AHU = (
        f"The variable air volume, VAV, system serves {zones_AHU_str}.\n"
        f"{economizer_text}"
        f"The supply air temperature for cooling is {ahu_params['cooling_air_supply_temperature']} Celsius, and for heating is {ahu_params['heating_air_supply_temperature']} Celsius.\n"
        f"The outdoor ventilation rate is {ahu_params['ventilation']} ACH.\n"
        f"The fan efficiency is {ahu_params['fan_efficiency']}, the pressure rise is {ahu_params['fan_pressure']} Pa, and the maximum flow rate is {ahu_params['fan_flow']} m3/s.\n"
    )

    # FCU 部分，加入容量控制方式

    zones_FCU = [zone.replace('Thermal ', '').lower() for zone in fcu_params['zones']]
    zones_FCU_str = ', '.join(zones_FCU)
    # 对于 FCU，示例中也包含了 {economizer_type}，但通常 FCU 不具备 economizer，这里为空字符串
    economizer_text_FCU = ""
    control_text_FCU = (
        "variable fan" if fcu_params['control'] == "ASHRAE90VariableFan" else
        "cycling fan" if fcu_params['control'] == "CyclingFan" else
        "multi speed fan" if fcu_params['control'] == "MultiSpeedFan" else
        "variable fan and variable water flow" if fcu_params['control'] == "VariableFanVariableFlow" else
        fcu_params['control']
    )
    description_FCU = (
        f"The fan coil unit, FCU, system serves {zones_FCU_str}.\n"
        f"The capacity control method of fan coil units, FCUs, is {control_text_FCU}.\n"
        f"The supply air temperature for cooling is {fcu_params['cooling_air_supply_temperature']} Celsius, and for heating is {fcu_params['heating_air_supply_temperature']} Celsius.\n"
        f"The outdoor ventilation rate is {fcu_params['ventilation']} ACH.\n"
        f"The fan efficiency of fan coil units, FCUs, is {fcu_params['FCU_fan_efficiency']}, the pressure rise is {fcu_params['FCU_fan_pressure']} Pa, and the maximum flow rate is {fcu_params['FCU_fan_flow']} m3/s.\n"
    )
    description_AHU = description1 + description_AHU
    description = ""
    description += description_AHU + description_FCU
    return description

def generate_air_system_dx_elec_description(unit_details):
    description = "The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.\n"

    for unit, details in unit_details.items():
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        zones_str = ', '.join(zones)
        economizer_type = (
            "It includes an economizer, which operates based on differential dry bulb.\n" if details['economizer'] == "DifferentialDryBulb" else
            "It includes an economizer, which operates based on differential enthalpy.\n" if details['economizer'] == "DifferentialEnthalpy" else
            "" if details['economizer'] == "NoEconomizer" else
            details['economizer']
        )
        description += (
            f"The unit {unit} serves {zones_str}.\n{economizer_type}"
            f"The rated capacity is {details['cooling_capacity']} W for cooling and {details['heating_capacity']} W for heating.\n"
            f"The rated cooling COP is {details['cooling_COP']} and the heating efficiency is {details['heating_efficiency']}.\n"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )
    return description

def generate_air_system_dx_fuel_description(unit_details):
    description = "The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.\n"

    for unit, details in unit_details.items():
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        zones_str = ', '.join(zones)
        fuel_type = (
            "natural gas" if details['fuel_type'] == "NaturalGas" else
            "coal" if details['fuel_type'] == "Coal" else
            details['fuel_type']
        )
        economizer_type = (
            "It includes an economizer, which operates based on differential dry bulb.\n" if details['economizer'] == "DifferentialDryBulb" else
            "It includes an economizer, which operates based on differential enthalpy.\n" if details['economizer'] == "DifferentialEnthalpy" else
            "" if details['economizer'] == "NoEconomizer" else
            details['economizer']
        )
        description += (
            f"The unit {unit} serves {zones_str}.\nThe fuel type is {fuel_type}.\n{economizer_type}"
            f"The rated capacity is {details['cooling_capacity']} W for cooling and {details['heating_capacity']} W for heating.\n"
            f"The rated cooling COP is {details['cooling_COP']} and the heating efficiency is {details['heating_efficiency']}.\n"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )
    return description

def generate_air_system_dx_hp_description(unit_details):
    description = "The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.\n"

    for unit, details in unit_details.items():
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        zones_str = ', '.join(zones)
        economizer_type = (
            "It includes an economizer, which operates based on differential dry bulb.\n" if details['economizer'] == "DifferentialDryBulb" else
            "It includes an economizer, which operates based on differential enthalpy.\n" if details['economizer'] == "DifferentialEnthalpy" else
            "" if details['economizer'] == "NoEconomizer" else
            details['economizer']
        )
        description += (
            f"The unit {unit} serves {zones_str}.\n{economizer_type}"
            f"The rated capacity is {details['cooling_capacity']} W for cooling and {details['heating_capacity']} W for heating.\n"
            f"The rated cooling COP is {details['cooling_COP']} and the heating efficiency is {details['heating_COP']}.\n"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )
    return description

def generate_air_system_doas_fcu_description(unit_details):
    description1 = "The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.\n"
    description3 = ""
    for unit, details in unit_details.items():
        # economizer_type = f"It includes an economizer, which operates based on {details['economizer']}.\n" if details['economizer'] != "NoEconomizer" else ''
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        zones_str = ', '.join(zones)
        control_description = (
            "variable fan" if details['control'] == "ASHRAE90VariableFan" else
            "cycling fan" if details['control'] == "CyclingFan" else
            "multi speed fan" if details['control'] == "MultiSpeedFan" else
            "variable fan and variable water flow" if details['control'] == "VariableFanVariableFlow" else
            details['control']
        )
        economizer_type = (
            "It includes an economizer, which operates based on differential dry bulb.\n" if details['economizer'] == "DifferentialDryBulb" else
            "It includes an economizer, which operates based on differential enthalpy.\n" if details['economizer'] == "DifferentialEnthalpy" else
            "" if details['economizer'] == "NoEconomizer" else
            details['economizer']
        )
        description3 += (
            f"The DOAS {unit} serves {zones_str}.\n{economizer_type}"
            f"The capacity control method of fan coil units, FCUs, is {control_description}.\n"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )

    return description1 + description3

def generate_air_system_doas_vrf_description(unit_details):
    description1 = "The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.\n"
    description3 = ""
    for unit, details in unit_details.items():
        zones = [zone.replace('Thermal ', '').lower() for zone in details['zones']]
        zones_str = ', '.join(zones)
        economizer_type = (
            "It includes an economizer, which operates based on differential dry bulb.\n" if details['economizer'] == "DifferentialDryBulb" else
            "It includes an economizer, which operates based on differential enthalpy.\n" if details['economizer'] == "DifferentialEnthalpy" else
            "" if details['economizer'] == "NoEconomizer" else
            details['economizer']
        )
        description3 += (
            f"The DOAS {unit} serves {zones_str}.\n{economizer_type}"
            f"The supply air temperature for cooling is {details['cooling_air_supply_temperature']} Celsius, and for heating is {details['heating_air_supply_temperature']} Celsius.\n"
            f"The outdoor ventilation rate is {details['ventilation']} ACH.\n"
            f"The fan efficiency is {details['fan_efficiency']}, the pressure rise is {details['fan_pressure']} Pa, and the maximum flow rate is {details['fan_flow']} m3/s.\n"
        )

    description2 = (
        f"The rated capacity of the HVAC system is {details['cooling_capacity']} W for cooling and {details['heating_capacity']} W for heating.\n"
        f"The rated cooling COP of the HVAC system is {details['cooling_COP']} and the heating COP is {details['heating_COP']}.\n"
    )
    return description1 + description2 + description3

##########

def generate_construction_description(wall_material, wall_thickness, wall_insulation, roof_material, roof_thickness, roof_insulation, window_U, window_SHGC):
    description = f"""The wall is made of {wall_material.split()[-1]}, with a thickness of {wall_thickness} meters and the wall insulation is R{wall_insulation.split()[-1]}. The roof is made of {roof_material.split()[-1]}, with a thickness of {roof_thickness} meters and the roof insulation is R{roof_insulation.split()[-1]}. The floor is made of concrete, covered with carpet. The window U-factor is {window_U} W/m2K and the SHGC is {window_SHGC}. \n"""
    return description

def generate_space_description(space_type_num, space_zones, space_details):
    
    description = f"This building have {space_type_num} space types.\n"
    for space_type, zones in space_zones.items():
        zone_list = ", ".join([f"{zone}" for zone in zones])
        description += f"Space type {space_type} is for zone {zone_list}. "

        details = space_details[space_type]
        description += (
            f"For space type {space_type}, "
            f"the people density is {details['people']['m2/person']} m2/person, the lighting density is {details['lighting']['W/m2']} W/m2, and the electric equipment density is {details['electric_equipment']['W/m2']} W/m2. "
            f"The people activity level is {details['activity']['W/person']} W/person. The infiltration rate is {details['infiltration']['ACH']} ACH. "
            f"The occupancy rate is {details['occupancy']['occupied_value']} from {details['occupancy']['occupancy_start']}:00 to {details['occupancy']['occupancy_end']}:00 and {details['occupancy']['unoccupied_value']} in other periods of time. \n"
        )
    return description

def generate_setpoint_description(setpoint_type_num, setpoint_zones, setpoint_details):
    
    # description = f"This building have {setpoint_type_num} setpoint types.\n"
    description =""
    for setpoint_type, zones in setpoint_zones.items():
        zone_list = ", ".join([f"{zone}" for zone in zones])
        description += f"For zone {zone_list}, "

        details = setpoint_details[setpoint_type]
        description += (
            f"the cooling setpoint is {details['cooling_setpoint_occupied']} Celsius during {details['occupied_start']}:00 to {details['occupied_end']}:00, and {details['cooling_setpoint_unoccupied']} Celsius in unoccupied periods. "
            f"The heating setpoint is {details['heating_setpoint_occupied']} Celsius during {details['occupied_start']}:00 to {details['occupied_end']}:00, and {details['heating_setpoint_unoccupied']} Celsius in unoccupied periods. \n"
        )
    return description

def generate_T_multi_flat_description(n, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b, v_x):

    # patch
    v_b=v_b+h_b
    description = f"""Simulate a {n} story T-shaped building."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segment is {h_a} meters long and {h_b} meters wide.
The vertical segment is {v_a} meters long and {v_b} meters wide.
The vertical segment is {v_x:.2f} meters to the edge of the horizontal segment.
The building orientation is {deg:.0f} degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_T_multi_gable_description(n, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b, v_x):

    # patch
    v_b=v_b+h_b
    description = f"""Simulate a {n} story T-shaped building with a gable roof."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segment is {h_a} meters long and {h_b} meters wide.
The vertical segment is {v_a} meters long and {v_b} meters wide.
The vertical segment is {v_x:.2f} meters to the edge of the horizontal segment.
The attic height is {at:.2f} meters.
The building orientation is {deg:.0f} degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_U_multi_flat_description(n, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v1_a, v2_a, h_a, v1_b, v2_b):
    # patch
    v1_b=v1_b+h_b
    v2_b=v2_b+h_b
    
    description = f"""Simulate a {n} story U-shaped building."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segment is {h_a} meters long and {h_b} meters wide.
The left vertical segment is {v1_a} meters long and {v1_b} meters wide.
The right vertical segment is {v2_a} meters long and {v2_b} meters wide.
The building orientation is {deg:.0f} degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_U_multi_gable_description(n, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v1_a, v2_a, h_a, v1_b, v2_b):

    # patch
    v1_b=v1_b+h_b
    v2_b=v2_b+h_b
    

    description = f"""Simulate a {n} story U-shaped building with a gable roof."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segment is {h_a} meters long and {h_b} meters wide.
The left vertical segment is {v1_a} meters long and {v1_b} meters wide.
The right vertical segment is {v2_a} meters long and {v2_b} meters wide.
The attic height is {at:.2f} meters.
The building orientation is {deg:.0f} degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_L_multi_flat_description(n, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b):
    
    # patch
    v_b=v_b+h_b
    description = f"""Simulate a {n} story L-shaped building."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segment is {h_a} meters long and {h_b} meters wide.
The vertical segment is {v_a} meters long and {v_b} meters wide.
The building orientation is {deg:.0f} degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_L_multi_gable_description(n, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b):

    # patch
    v_b=v_b+h_b
    description = f"""Simulate a {n} story L-shaped building with a gable roof."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segment is {h_a} meters long and {h_b} meters wide.
The vertical segment is {v_a} meters long and {v_b} meters wide.
The attic height is {at:.2f} meters.
The building orientation is {deg:.0f} degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_hollow_square_multi_flat_description(n, a, b, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, x, y):

    description = f"""Simulate a {n} story hollow square, courtyard building."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segments are {a:.2f} meters long and {y:.2f} meters wide.
The vertical segments are {x:.2f} meters long and {b:.2f} meters wide.
The building orientation is {deg} degrees to the north.
Each story has 4 thermal zones in each orientation.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_hollow_square_multi_gable_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, x, y):

    description = f"""Simulate a {n} story hollow square, courtyard building with a gable roof."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The horizontal segments are {a:.2f} meters long and {y:.2f} meters wide.
The vertical segments are {x:.2f} meters long and {b:.2f} meters wide.
The attic height is {at:.2f} meters.
The building orientation is {deg} degrees to the north.
Each story has 4 thermal zones in each orientation.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_square_single_flat_description(n, a, b, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e,):

    description = f"""Simulate a {n} story rectengular building that is {a:.2f} meters long, {b:.2f} meters wide."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The building orientation is {deg:.0f} degrees to the north.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_square_single_gable_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e):

    description = f"""Simulate a {n} story rectengular building that is {a:.2f} meters long, {b:.2f} meters wide, with a gable roof"""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The attic height is {at:.2f} meters.
The building orientation is {deg:.0f} degrees to the north.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_square_single_hip_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e):

    description = f"""Simulate a {n} story rectengular building that is {a:.2f} meters long, {b:.2f} meters wide, with a hip roof"""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The attic height is {at:.2f} meters.
The building orientation is {deg:.0f} degrees to the north.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_square_multi_flat_description(n, a, b, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, t):

    description = f"""Simulate a {n} story rectengular building that is {a:.2f} meters long, {b:.2f} meters wide."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The building orientation is {deg:.0f} degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is {t:.2f} meters.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_square_multi_gable_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, t):

    description = f"""Simulate a {n} story rectengular building that is {a:.2f} meters long, {b:.2f} meters wide, with a gable roof."""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The attic height is {at:.2f} meters.
The building orientation is {deg:.0f} degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is {t:.2f} meters.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description

def generate_square_multi_hip_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, t):

    description = f"""Simulate a {n} story rectengular building that is {a:.2f} meters long, {b:.2f} meters wide, with a hip roof"""

    for i in range(n):
        description += f"\nThe height of story {i+1} is {c_values[i]:.2f} meters."

    description += f"""
The attic height is {at:.2f} meters.
The building orientation is {deg:.0f} degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is {t:.2f} meters.
The window-to-wall ratio is {wwr_n:.2f} for the north, {wwr_s:.2f} for the south, {wwr_w:.2f} for the west, and {wwr_e:.2f} for the east."""
    return description