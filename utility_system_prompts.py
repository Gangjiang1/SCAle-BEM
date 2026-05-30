
# =================
# prompts for geometry, info, air, and water, and reflective verification agents
# =================

geo_system_prompt = """
Understand the user's building design intent and below output requirements, automatically select the most appropriate template below based on the user's design specifications and output the filled template with your automated values in {}.
Available Templates:
• From the 14 template functions listed below, select one that best matches the user's design specifications.
• Strictly follow the chosen template and below requirement: Only replace the {} placeholders with values that satisfy the user's requirements. Do not output {}. Do not modify any other word of the template. Do not output initial template.
(1)
generate_hollow_square_multi_flat_description(n, a, b, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, x, y):
• This function generates a hollow square, multi-story building geometry, representing a building with an internal courtyard.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 m high, and the top story is 3.5 m high.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{x}: Length of the vertical segment defining the courtyard cut, must be less than 30% of the horizontal segment length {a}.
{y}: Width of the horizontal segment defining the courtyard cut, must be less than 30% of the vertical segment width {b}.
(2)
generate_hollow_square_multi_gable_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, x, y):
• This function generates a hollow square, multi-story building geometry with a gable attic roof, representing a building with an internal courtyard.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{at}: Height of the building attic.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{x}: Length of the vertical segment defining the courtyard cut, must be less than 30% of the horizontal segment length {a}.
{y}: Width of the horizontal segment defining the courtyard cut, must be less than 30% of the vertical segment width {b}.
(3)
generate_L_multi_flat_description(n, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b):
• This function generates a L-shape, multi-story building geometry.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{h_b}: Horizontal segment width.
{v_a}: Vertical segment length.
{h_a}: Horizontal segment length, must be at least 1 meter greater than the vertical segment length {v_a}.
{v_b}: Vertical segment width, must be at least 1 meter greater than the horizontal segment width {h_b}.
(4)
generate_L_multi_gable_description(n, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b):
• This function generates a L-shape, multi-story building geometry with a gable attic roof.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{at}: Height of the building attic.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{h_b}: Horizontal segment width.
{v_a}: Vertical segment length.
{h_a}: Horizontal segment length, must be at least 1 meter greater than the vertical segment length {v_a}.
{v_b}: Vertical segment width, must be at least 1 meter greater than the horizontal segment width {h_b}.
(5)
generate_square_multi_flat_description(n, a, b, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, t):
• This function generates a square shape, multi-story building geometry.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{t}: The depth of the exterior thermal zone, must be less than both the building length {a} and the building width {b}.
(6)
generate_square_multi_gable_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, t):
• This function generates a square shape, multi-story building geometry with a gable attic roof.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{deg}: Building orientation in degrees relative to true north.
{at}: Height of the building attic.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{t}: The depth of the exterior thermal zone, must be less than both the building length {a} and the building width {b}.
(7)
generate_square_multi_hip_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, t):
• This function generates a square shape, multi-story building geometry with a hip attic roof.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{at}: Height of the building attic.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{t}: The depth of the exterior thermal zone, must be less than both the building length {a} and the building width {b}.
(8)
generate_square_single_flat_description(n, a, b, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e,):
• This function generates a square shape (single zone for each story) building geometry.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
(9)
generate_square_single_gable_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e):
• This function generates a square shape (single zone for each story) building geometry with a gable attic roof.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{at}: Height of the building attic.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
(10)
generate_square_single_hip_description(n, a, b, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e):
• This function generates a square shape (single zone for each story) building geometry with a hip attic roof.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{a}: Overall building length (horizontal segment length).
{b}: Overall building width (vertical segment width).
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{at}: Height of the building attic.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
(11)
generate_T_multi_flat_description(n, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b, v_x):
• This function generates a T-shape, multi-story building geometry.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{h_b}: Horizontal segment width
{v_a}: Vertical segment length
{h_a}: Horizontal segment length, must be at least 1 meter greater than the vertical segment length {v_a}.
{v_b}: Vertical segment width, must be at least 1 meter greater than the horizontal segment width {h_b}
{v_x}: The distance from the vertical segment to the edge of the horizontal segment
(12)
generate_T_multi_gable_description(n, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v_a, h_a, v_b, v_x):
• This function generates a T-shape, multi-story building geometry with a gable attic roof.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{at}: Height of the building attic.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{h_b}: Horizontal segment width
{v_a}: Vertical segment length
{h_a}: Horizontal segment length, must be at least 1 meter greater than the vertical segment length {v_a}.
{v_b}: Vertical segment width, must be at least 1 meter greater than the horizontal segment width {h_b}
{v_x}: The distance from the vertical segment to the edge of the horizontal segment
(13)
generate_U_multi_flat_description(n, c_values, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v1_a, v2_a, h_a, v1_b, v2_b):
• This function generates a U-shape, multi-story building geometry.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{h_b}: Width of the horizontal segment.
{v1_a}: Length of the left vertical segment.
{v2_a}: Length of the right vertical segment.
{h_a}: Length of the horizontal segment. {h_a} must be greater than the sum of left and right vertical segment lengths, i.e., {h_a} > {v1_a} + {v2_a}.
{v1_b}: Width of the left vertical segment.
{v2_b}: Width of the right vertical segment.
(14)
generate_U_multi_gable_description(n, c_values, at, deg, wwr_n, wwr_s, wwr_w, wwr_e, h_b, v1_a, v2_a, h_a, v1_b, v2_b):
• This function generates a U-shape, multi-story building geometry with a gable attic roof.
• Parameter Explanation and Geometric Constraint:
{n}: Number of stories.
{c_values}: A list specifying the floor-to-floor height of each level. For example: c_values = [3.0, 3.0, 3.0, 3.0, 3.5], indicates that the first four stories are 3.0 meter high, and the top story is 3.5 meter high.
{at}: Height of the building attic.
{deg}: Building orientation in degrees relative to true north.
{wwr_n}: Window-to-wall ratio on the north façade.
{wwr_s}: Window-to-wall ratio on the south façade.
{wwr_w}: Window-to-wall ratio on the west façade.
{wwr_e}: Window-to-wall ratio on the east façade.
{h_b}: Width of the horizontal segment.
{v1_a}: Length of the left vertical segment.
{v2_a}: Length of the right vertical segment.
{h_a}: Length of the horizontal segment. {h_a} must be greater than the sum of left and right vertical segment lengths, i.e., {h_a} > {v1_a} + {v2_a}.
{v1_b}: Width of the left vertical segment.
{v2_b}: Width of the right vertical segment.
Output Format:
(only print one of the most relevant function template based on the user's description with your own judement, with all {} placeholders replaced by specific values derived from the user's input.)
"""

info_system_prompt = """
Understand the user's building design intent and below output requirements, automatically select the most appropriate template below based on the user's design specifications and output the filled template with your automated values in {}.
Available Template:
• Use the 3 functions listed below as the template.
• Strictly follow the template and below requirement: Only replace the {} placeholders with values that satisfy the user's requirements. Do not output {}. Do not modify any other word of the template. Do not output initial template.
generate_construction_description('wall_material', wall_thickness, 'wall_insulation', 'roof_material', roof_thickness, 'roof_insulation', window_U, window_SHGC)
generate_space_description(space_type_num, space_zones, space_details)
generate_setpoint_description(setpoint_type_num, setpoint_zones, setpoint_details)
• This 3 function generates building information with constructions, space types, and setpoints.
• Parameter Explanation and Geometric Constraint:
{wall_material}: Must be selected only from the following options: 'wall concrete', 'wall brick', 'wall wood', 'wall gypsum', 'wall metal', 'wall rammed earth'.
{wall_thickness}: Wall thickness in meters.
{wall_insulation}: Must be selected only from the following format: 'Wall Insulation [18-44]'.
{roof_material}: must be selected only from the following options: 'roof concrete', 'roof brick', 'roof wood', 'roof gypsum', 'roof metal', 'roof rammed earth'.
{roof_thickness}: Roof thickness in meters.
{roof_insulation}: Must be selected only from the following format: 'Roof Insulation [18-44]'.
{window_U}: Window U-factor in W/m2K.
{window_SHGC}: Window Solar Heat Gain Coefficient (SHGC).
{space_type_num}: An integer indicating the total number of distinct space types in the building.
{space_zones}: A dictionary mapping each space type to a list of zone names.
Example:
{1:
['1', '2', '3'], (Note that the string "Thermal Zone xx" should not be retained here.)
2: ... (If appropriate or user input mentioned.)
}
(All space-type zone counts combined must equal the computed <Total_Thermal_Zones> below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangular/Square building: Thermal_Zones_per_Story = 5
)
{space_details}: A dictionary containing detailed internal load and operational parameters for each space type, including:
• People density (m²/person)
• Lighting power density (W/m²)
• Electric equipment power density (W/m²)
• Occupant activity level (W/person)
• Infiltration rate (Air Changes per Hour, ACH)
• Occupancy schedule, including:
• Occupancy start and end time
• Occupied value and Unoccupied value. Must be greater than or equal to 0 and less than or equal to 1.
Example:
{1:
{'zones': ['Thermal Zone 1', 'Thermal Zone 2', 'Thermal Zone 3'], (Note that the string "Thermal Zone xx" should be retained here.)
'lighting': {'W/m2': 13.8},
'people': {'m2/person': 10.5},
'occupancy': {'occupancy_start': 8, 'occupancy_end': 18, 'occupied_value': 0.8, 'unoccupied_value': 0.1},
'electric_equipment': {'W/m2': 26.0},
'activity': {'W/person': 120},
'infiltration': {'ACH': 1.6}},
2: ... (If appropriate or user input mentioned.)
}
(All space-type zone counts combined must equal the computed <Total_Thermal_Zones> below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangular/Square building: Thermal_Zones_per_Story = 5
)
{setpoint_type_num}: An integer indicating the number of distinct setpoint schedule types.
{setpoint_zones}: A dictionary mapping each setpoint type to a list of zone names where the setpoint schedule applies.
Example:
{1:
['1', '2', '3'], (Note that the string "Thermal Zone xx" should not be retained here.)
2: ... (If appropriate or user input mentioned.)
}
(All setpoint-type zone counts combined must equal the computed <Total_Thermal_Zones> below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangular/Square building: Thermal_Zones_per_Story = 5
)
{setpoint_details}: A dictionary containing thermal comfort settings for each setpoint type, including:
• Cooling setpoint (occupied) in °C
• Cooling setpoint (unoccupied) in °C
• Heating setpoint (occupied) in °C
• Heating setpoint (unoccupied) in °C
• Occupied period start and end time (hour of day)
During both occupancy and unoccupancy periods, the cooling setpoint must be at least 1 Celsius higher than the heating setpoint.
Example:
{1:
{'zones': ['Thermal Zone 1', 'Thermal Zone 2', 'Thermal Zone 3'], (Note that the string "Thermal Zone xx" should be retained here.)
'cooling_setpoint_occupied': 25.4,
'heating_setpoint_occupied': 21.3,
'cooling_setpoint_unoccupied': 28.8,
'heating_setpoint_unoccupied': 23.8,
'occupied_start': 5,
'occupied_end': 23}
2: ... (If appropriate or user input mentioned.)
}
(All setpoint-type zone counts combined must equal the computed <Total_Thermal_Zones> below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangular/Square building: Thermal_Zones_per_Story = 5
)
Thermal Zone Rules:
The total number of thermal zones must be consistent with both the building shape and the number of stories.
Each building shape has a fixed number of thermal zones per story:
L-shaped building has 2 thermal zones for each story.
T-shaped building has 2 thermal zones for each story.
U-shaped building has 3 thermal zones for each story.
Rectengular building has 5 thermal zones for each story.
Hollow square (courtyard) building has 4 thermal zones for each story.
Total Thermal Zone Formula:
Total Thermal Zones = Thermal Zones per Story × Number of Stories
Examples:
• L-shaped building
Total thermal zones = 2 × number_of_stories
• T-shaped building
Total thermal zones = 2 × number_of_stories
• U-shaped building
Total thermal zones = 3 × number_of_stories (not 4)
• Rectangular building
Total thermal zones = 5 × number_of_stories
• Hollow square (courtyard) building
Total thermal zones = 4 × number_of_stories
Output Format:
(only print the 3 template based on the user's description with your own judement, with all {} placeholders replaced by specific values derived from the user's input.)
"""

air_system_prompt = """
Understand the user's building design intent and below output requirements, automatically select the most appropriate template below based on the user's design specifications and output the filled template with your automated values in {}.
Available Templates:
• From the 9 template functions listed below, select one that best matches the user's design specifications.
• Strictly follow the chosen template and below requirement: Only replace the {} placeholders with values that satisfy the user's requirements. Do not output {}. Do not modify any other word of the template. Do not output initial template.
• If the user does not specify an air-conditioning or air system, directly use: (1)generate_air_system_dx_elec_description(unit_details)
Thermal Zone Rules:
The total number of thermal zones must be consistent with both the building shape and the number of stories.
Each building shape has a fixed number of thermal zones per story:
L-shaped building has 2 thermal zones for each story.
T-shaped building has 2 thermal zones for each story.
U-shaped building has 3 thermal zones for each story.
Rectengular building has 5 thermal zones for each story.
Hollow square (courtyard) building has 4 thermal zones for each story.
Total Thermal Zone Formula:
Total Thermal Zones = Thermal Zones per Story × Number of Stories
Examples:
• L-shaped building
Total thermal zones = 2 × number_of_stories
• T-shaped building
Total thermal zones = 2 × number_of_stories
• U-shaped building
Total thermal zones = 3 × number_of_stories (not 4)
• Rectangular building
Total thermal zones = 5 × number_of_stories
• Hollow square (courtyard) building
Total thermal zones = 4 × number_of_stories
(1)
generate_air_system_dx_elec_description(unit_details)
Example:
{1:
{ "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.
 "fuel_type ":  "electric ", (Possible values: only  "electric ")
 "cooling_COP ": 4.2,
 "heating_efficiency ": 0.88,
 "cooling_capacity ":  "Autosize ", (Can be Autosize)
 "heating_capacity ":  "Autosize ", (Can be Autosize)
 "economizer ":  "NoEconomizer ", (Possible values: 1. DifferentialDryBulb: Economizer operates based on outdoor vs. return air dry-bulb temperature. 2. DifferentialEnthalpy: Economizer operates based on outdoor  vs. return air enthalpy. 3. NoEconomizer: No economizer is used.)
 "cooling_air_supply_temperature ": 13.5,
 "heating_air_supply_temperature ": 45.0,
 "ventilation ": 1.2,
 "fan_efficiency ": 0.72,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900},
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed  <Total_Thermal_Zones > below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For  T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangula r/Square building: Thermal_Zones_per_Story = 5
)
(2)
generate_air_system_dx_fuel_description(unit_details)
Example:
{1:
{ "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.
 "fuel_type ":  "NaturalGas ", (Possible values: 1.  "NaturalGas " 2.  "Coal ")
 "cooling_COP ": 3.8,
 "heating_efficiency ": 0.82,
 "cooling_capacity ":  "Autosize ", (Can be Autosize)
 "heating_capacity ":  "Autosize ", (Can be Autosize)
 "economizer ":  "NoEconomizer ", (Possible values: 1. DifferentialDryBulb: Economizer operates based on outdoor vs. return air dry-bulb temperature. 2. DifferentialEnthalpy: Economizer operates based on outdoor  vs. return air enthalpy. 3. NoEconomizer: No economizer is used.)
 "cooling_air_supply_temperature ": 14.0,
 "heating_air_supply_temperature ": 45.0,
 "ventilation ": 1.2,
 "fan_efficiency ": 0.75,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900},
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed  <Total_Thermal_Zones > below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For  T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangula r/Square building: Thermal_Zones_per_Story = 5
)
(3)
generate_air_system_dx_hp_description(unit_details)
Example:
{1:
{ "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.
 "fuel_type ":  "heat_pump ", (Possible values: only  "heat_pump ")
 "cooling_COP ": 3.45,
 "heating_COP ": 3.80,
 "cooling_capacity ":  "Autosize ", (Can be Autosize)
 "heating_capacity ":  "Autosize ", (Can be Autosize)
 "economizer ":  "NoEconomizer ", (Possible values: 1. DifferentialDryBulb: Economizer operates based on outdoor vs. return air dry-bulb temperature. 2. DifferentialEnthalpy: Economizer operates based on outdoor  vs. return air enthalpy. 3. NoEconomizer: No economizer is used.)
 "cooling_air_supply_temperature ": 14.0,
 "heating_air_supply_temperature ": 45.0,
 "ventilation ": 1.2,
 "fan_efficiency ": 0.75,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900},
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed  <Total_Thermal_Zones > below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For  T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangula r/Square building: Thermal_Zones_per_Story = 5
)
(4)
generate_air_system_fcu_description(unit_details)
{unit_details}: A dictionary that stores all air-system-related parameters.
•  Key (1): Air system ID (each key represents one unit).
• Value: A dictionary describing the properties of that unit.
Example:
{1:
{'zones': ['Thermal Zone 1', 'Thermal Zone 2', 'Thermal Zone 3', ...], (A list of thermal zones served by the fan coil unit. Note that the string "Thermal Zone xx" should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.)
'control': 'CyclingFan', (Defines how the fan coil unit controls air delivery. Possible values: 1. ASHRAE90VariableFan → Variable-speed fan compliant with ASHRAE 90.1. 2. CyclingFan → Fan cycles on/off with load. 3. MultiSpeedFan → Fan operates at discrete speed levels. 4. VariableFanVariableFlow → Both fan speed and water flow are modulated.)
'cooling_air_supply_temperature': 13.5, (Supply air temperature during cooling (°C).)
'heating_air_supply_temperature': 48.0, (Supply air temperature during heating (°C).)
'ventilation': 1.85, (Outdoor air ventilation rate in air changes per hour (ACH).)
'fan_efficiency': 0.82, (Fan efficiency.)
'fan_flow': 'Autosize', (Fan air flow rate (m³/s).)
'fan_pressure': 1200} (Fan pressure rise in Pascals (Pa).)
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed <Total_Thermal_Zones> below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangular/Square building: Thermal_Zones_per_Story = 5
)
(5)
generate_air_system_vrf_description(unit_details)
{unit_details}: A dictionary that stores all air-system-related parameters.
• Key (1): Air system ID (each key represents one unit).
• Value: A dictionary describing the properties of that unit.
Example:
{1:
{ "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.)
 "cooling_COP ": 4.2, (Coefficient of Performance for cooling.)
 "heating_COP ": 4.5, (Coefficient of Performance for heating.)
 "cooling_capacity ":  "Autosize ", (Rated cooling capacity in watts (W). Can be Autosize)
 "heating_capacity ":  "Autosize ", (Rated heating capacity in watts (W). Can be Autosize)
 "cooling_air_supply_temperature ": 14.0, (Cooling supply air temperature (°C))
 "heating_air_supply_temperature ": 45.0, (Heating supply air temperature (°C))
 "ventilation ": 1.2, (Outdoor ventilation rate (ACH))
 "fan_efficiency ": 0.75, (Fan efficiency)
 "fan_flow ":  "Autosize ", (fan airflow rate (m³/s). Can be Autosize)
 "fan_pressure ": 800 (Fan pressure rise (Pa))}
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed  <Total_Thermal_Zones > below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For  T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangula r/Square building: Thermal_Zones_per_Story = 5
)
(6)
generate_air_system_vav_description(unit_details)
{unit_details}: A dictionary that stores all air-system-related parameters.
• Key (1): Air system ID (each key represents one unit).
• Value: A dictionary describing the properties of that unit.
Example:
{1:
{ "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.)
 "economizer ":  "NoEconomizer ", (Possible values: 1.  "DifferentialDryBulb " 2.  "DifferentialEnthalpy " 3.  "NoEconomizer ")
 "cooling_air_supply_temperature ": 13.0,
 "heating_air_supply_temperature ": 45.0,
 "ventilation ": 1.20,
 "fan_efficiency ": 0.75,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900},
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed  <Total_Thermal_Zones > below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For  T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangula r/Square building: Thermal_Zones_per_Story = 5
)
(7)
generate_air_system_vav_fcu_description(ahu_params, fcu_params)
{ahu_params}: A dictionary that stores all VAV and AHU related parameters.
Example:
{
 "unit ":  "AirDistributionUnit ",
 "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.)
 "control ":  "CyclingFan ", (should be consistent with the values in the {ahu_params}. Possible values: 1. CyclingFan: Fan cycles on/off based on load. 2. MultiSpeedFan: Fan operates at discrete speed leve ls. 3. ASHRAE90VariableFan: Variable-speed fan compliant with ASHRAE 90.1. 4. VariableFanVariableFlow: Both fan speed and water flow are modulated.)
 "economizer ":  "NoEconomizer ", (Possible values: 1. DifferentialDryBulb: Economizer operates based on outdoor vs. return air dry-bulb temperature. 2. DifferentialEnthalpy: Economizer operates based on outdoor  vs. return air enthalpy. 3. NoEconomizer: No economizer is used.)
 "cooling_air_supply_temperature ": 13.5,
 "heating_air_supply_temperature ": 45.0,
 "ventilation ": 1.2,
 "FCU_fan_efficiency ": 0.76, (Here below are the relevant FCU parameters, which should be consistent with the values in the following {fcu_params})
 "FCU_fan_flow ":  "Autosize ", (Can be Autosize)
 "FCU_fan_pressure ": 600,
 "fan_efficiency ": 0.9,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900,
}
{fcu_params}: A dictionary that stores all FCU related parameters.
Example:
{
 "unit ":  "FourPipeFanCoil ",
 "zones ": [ "Thermal Zone 4 ",  "Thermal Zone 5 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.)
 "economizer ":  "NoEconomizer ", (should be consistent with the values in the {ahu_params})
 "control ":  "CyclingFan ", (Possible values: 1. CyclingFan: Fan cycles on/off based on load. 2. MultiSpeedFan: Fan operates at discrete speed levels. 3. ASHRAE90VariableFan: Variable-speed fan compliant w ith ASHRAE 90.1. 4. VariableFanVariableFlow: Both fan speed and water flow are modulated.)
 "cooling_air_supply_temperature ": 14.0,
 "heating_air_supply_temperature ": 42.0,
 "ventilation ": 0.8,
 "FCU_fan_efficiency ": 0.76,
 "FCU_fan_flow ":  "Autosize ", (Can be Autosize)
 "FCU_fan_pressure ": 600,
 "fan_efficiency ": 0.9,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900,
}
(8)
generate_air_system_doas_fcu_description(unit_details)
Example:
{1:
{ "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.
 "control ":  "CyclingFan ", (Possible values: 1. CyclingFan: Fan cycles on/off based on load. 2. MultiSpeedFan: Fan operates at discrete speed levels. 3. ASHRAE90VariableFan: Variable-speed fan compliant w ith ASHRAE 90.1. 4. VariableFanVariableFlow: Both fan speed and water flow are modulated.)
 "economizer ":  "NoEconomizer ", (Possible values: 1. DifferentialDryBulb: Economizer operates based on outdoor vs. return air dry-bulb temperature. 2. DifferentialEnthalpy: Economizer operates based on outdoor  vs. return air enthalpy. 3. NoEconomizer: No economizer is used.)
 "cooling_air_supply_temperature ": 14.5,
 "heating_air_supply_temperature ": 42.0,
 "ventilation ": 1.2,
 "fan_efficiency ": 0.75,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900},
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed  <Total_Thermal_Zones > below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For  T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangula r/Square building: Thermal_Zones_per_Story = 5
)
(9)
generate_air_system_doas_vrf_description(unit_details)
Example:
{1:
{ "zones ": [ "Thermal Zone 1 ",  "Thermal Zone 2 ", ...], (A list of thermal zones served by the unit. Note that the string  "Thermal Zone xx " should be retained here. The number of zones in the list must not exceed the previously computed Total Thermal Zones.
 "economizer ":  "NoEconomizer ", (Possible values: 1. DifferentialDryBulb: Economizer operates based on outdoor vs. return air dry-bulb temperature. 2. DifferentialEnthalpy: Economizer operates based on outdoor  vs. return air enthalpy. 3. NoEconomizer: No economizer is used.)
 "cooling_air_supply_temperature ": 14.0,
 "heating_air_supply_temperature ": 45.0,
 "ventilation ": 1.2,
 "fan_efficiency ": 0.75,
 "fan_flow ":  "Autosize ", (Can be Autosize)
 "fan_pressure ": 900,
 "cooling_COP ": 4.8,
 "heating_COP ": 4.5,
 "cooling_capacity ":  "Autosize ", (Can be Autosize)
 "heating_capacity ":  "Autosize "}, (Can be Autosize)
2: ... (If appropriate or user input mentioned.)
}
(All zone counts combined must equal the computed  <Total_Thermal_Zones > below based on the building shape and number of stories.
Total_Thermal_Zones = Thermal_Zones_per_Story × Number of Stories
For L-shaped building: Thermal_Zones_per_Story = 2
For  T-shaped building: Thermal_Zones_per_Story = 2
For U-shaped building: Thermal_Zones_per_Story = 3
For Hollow square (courtyard) building: Thermal_Zones_per_Story = 4
For Rectangula r/Square building: Thermal_Zones_per_Story = 5
)
Output Format Requirement:
You must output exactly one template — the most relevant one.
• The output must contain:
• The function name
• All required arguments/fields for that function
• All {} placeholders must be fully replaced with concrete values inferred from the user's description, using your own judgment.
• Do NOT output the template number (e.g., do not write"Template 1", "(x)", etc.).
• Do not include any explanations, comments, or additional text.
• The final output completed template must be directly executable as a function call.
"""

water_system_prompt = """
Understand the user's building design intent and below output requirements, automatically select the most appropriate template below based on the user's design specifications and output the filled template with your automated values in {}.
Determine Whether Need Water System:
A water system should be generated only if the user's input explicitly mentions VAV or FCU included HVAC systems.
Otherwise, output an empty string "" and do not generate any water system content.
Available Template:
• Use the 3 functions listed below as the template.
• Strictly follow the template and below requirement: Only replace the {} placeholders with values that satisfy the user's requirements. Do not output {}. Do not modify any other word of the template. Do not output initial template.
generate_chilled_water_description(chiller_num, chiller_details)
generate_hot_water_description(boiler_num, boiler_details)
generate_condenser_water_description(tower_num, tower_details)
• This 3 function generates building information with chilled water, hot water, and condenser water information.
• Parameter Explanation and Constraint:
{chiller_num}: The number of chillers in the chilled water system.
{chiller_details}: A dictionary containing detailed information for each chiller.
Example:
{1:
{ "chiller_capacity ":  "Autosize ", (Can be Autosize)
 "chiller_COP ": 5.8,
 "chilled_water_supply_temperature ": 6.0, (only one loop, below parameters should be consistent with the values in the other chillers)
 "chilled_water_temperature_difference ": 6.5,
 "pump_efficiency ": 0.82,
 "pump_flow ":  "Autosize ", (Can be Autosize)
 "pump_head ": 245000,
 "pump_power ":  "Autosize "}, (Can be Autosize)
2: ...（Second chiller with a similar structure, if appropriate or user input mentioned.)
}
{boiler_num}: The number of boilers in the hot water system.
{boiler_details}: A dictionary containing detailed information for each boiler.
Example:
{1:
{ "boiler_capacity ":  "Autosize ", (Can be Autosize)
 "boiler_efficiency ": 0.82,
 "hot_water_supply_temperature ": 65.0, (only one loop, below parameters should be consistent with the values in the other boilers)
 "hot_water_temperature_difference ": 10.0,
 "pump_efficiency ": 0.85,
 "pump_flow ":  "Autosize ", (Can be Autosize)
 "pump_head ": 245000,
 "pump_power ":  "Autosize ", (Can be Autosize)
 "fuel_type ":  "NaturalGas "}, (Possible values:  "NaturalGas ",  "Coal ", or  "Electricity ")
2: ... (Second boiler with a similar structure, if appropriate or user input mentioned.)
}
{tower_num}: The number of cooling towers in the condenser water system.
{tower_details}: A dictionary containing detailed information for each cooling tower.
Example:
{1:
{ "tower_capacity ": 850000, (Can not be Autosize, must be assigned)
 "air_flow ":  "Autosize ", (Can be Autosize) (Only one loop, below parameters should be consistent with the values in the other cooling towers)
 "water_flow ":  "Autosize ", (Can be Autosize)
 "fan_power ":  "Autosize ", (Can be Autosize)
 "pump_efficiency ": 0.82,
 "pump_flow ":  "Autosize ", (Can be Autosize)
 "pump_head ": 245000,
 "pump_power ":  "Autosize "}, (Can be Autosize)
2: ... (Second cooling tower with a similar structure, if appropriate or user input mentioned.)
}
Output Format Requirement:
You must output the 3 function templates based on the user's description with your own judement.
• The output must contain:
• The 3 function name
• All required arguments/fields for that function
• All {} placeholders must be fully replaced with concrete values inferred from the user's description, using your own judgment.
• Do NOT output the template number (e.g., do not write"Template 1", "(x)", etc.).
• Do not include any explanations, comments, or additional text.
• The final output completed template must be directly executable as a function call.
"""

verification_system_prompt = """
You are a verification agent. Your task is to check if the generated code satisfies all constraints.

Check the following:
1. **Geometric Constraints**: 
   - For L-shaped building: {h_a} Horizontal segment length must be greater than {v_a} Vertical segment length
   - For T-shaped building: {h_a} Horizontal segment length must be greater than {v_a} Vertical segment length
   - For U-shaped building: {h_a} Length of the horizontal segment must be greater than {v1_a} Length of the left vertical segment + {v2_a} Length of the right vertical segment
   - For Courtyard building: {x} Length of the vertical segment must be less than {a} Overall building length, {y} Width of the horizontal segment must be less than {b} Overall building width

2. **Thermal Zone Consistency**:
   - Total zones = Zones_per_story × Number_of_stories
   - L-shaped building: 2 zones/story
   - T-shaped building: 2 zones/story
   - U-shaped building: 3 zones/story
   - Courtyard building: 4 zones/story
   - Rectangle building: 5 zones/story

3. **Parameter Validity**:
   - All numeric values must be positive
   - WWR must be between 0 and 1

Output Format:
- If valid: "VERIFICATION_PASSED"
- If invalid: "VERIFICATION_FAILED: [reason]" followed by suggested corrections
"""