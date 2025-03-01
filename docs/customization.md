# Customization Guide

TinyPedal offers a wide range of customization, which is currently available by editing `.JSON` setting file with text editor.

Starting from version 1.9.0, TinyPedal comes with a new `Preset Manager` that let user to load or create setting preset. All `.JSON` setting files are located in `TinyPedal\settings` folder. Preset can be switched or created via tray icon menu `Load Preset`, which opens `Preset Manager` window.

Note: for version older than 1.9.0, `.JSON` files are located in TinyPedal root folder.

TinyPedal will auto-save setting when user makes any changes to widget position, or has toggled widget visibility, auto-hide, overlay-lock. Due to this reason, to avoid losing changes, it is recommended to quit APP before editing or saving JSON file. Any changes will only take effect after reloading preset or restarting APP.


## Backup file 
TinyPedal will automatically create a backup file with time stamp suffix if old setting file is invalid, and a new default `.JSON` will be generated.

A newer released version will auto-update old setting and add new setting after loading. It is still recommended to manually create backups before updating.


## Editing Notes
To make changes, editing `values` on the right side of colon.

Do not modify anything (keys) on the left side of colon, any changes to those keys will be reverted back to default setting by APP.

If APP fails to launch after editing `.JSON`, check for typo error or invalid values; or delete `.JSON` to let APP generate a new default file.

If a value is surrounded by quotation marks, make sure not to remove those quotation marks, otherwise may cause error.

Any boolean type value (true or false) will only accept: `true`, which can be substituted with `1`. And `false`, which can be substituted with `0`. All words must be in `lowercase`, otherwise will have no effect.

Color value is in web colors format (hexadecimal color codes), which starts with `#` number sign. Various image editors or online tools can generate those color codes.

If a number (default value) does not contain any decimal place, that means it only accepts `integer`. Make sure not to add any decimal place, otherwise error will occur.


## Common Setting
    enable
This checks whether a widget will be loaded at startup. It can also be accessed and changed from tray icon `Widgets` submenu.

    update_delay
This sets widget refresh rate, value is in milliseconds. A value of `20` means refresh every 20ms, which equals 50fps. Since most data from sharedmemory plugin is capped at 50fps, setting any value less than `10` will not gain any benefit, and could result significant increase of CPU usage.

    position_x, position_y
Defines widget position on screen. Those values will be auto-saved by app, no need to manually set.

    opacity
By default, all widgets have a 90% opacity setting, which equals `0.9` value. Lower value adds more transparency to widget.

    bar_gap
Set gap (screen pixel) between elements in a widget, only accept integer, `1` = 1 pixel.

    font_name
Mono type font is highly recommended. To set custom font, write `full font name` inside quotation marks. If a font name is invalid, a default fallback font will be used by program.

    font_size
Set font size, increase or decrease font size will also apply to widget size. Value only accept `integer`, do not put any decimal place.

    font_weight
Acceptable value: `normal` or `bold` .

    text_padding
Set text edge padding value that multiplies & scales with `font_size`. Default is `0.2` for most widgets.

    font_color
Those are for font color.

    bkg_color
Those are for background color.

    show_caption
Show short caption description besides each info block.

    column_index_*
Set order of each info column(or row). Must keep index number unique to each column, otherwise columns will overlap.


## Overlay
    fixed_position
Check whether widget is locked at startup. This setting can be toggled from tray icon menu. Valid value: `true`, same as `1`. `false`, same as `0`.

    auto_hide
Check whether auto hide is enabled. This setting can be toggled from tray icon menu. Valid value: `true`, same as `1`. `false`, same as `0`.

    delta_module
Enable delta timing module. This module provides timing data for `Delta best` and `Timing` widgets, which returns value 0 if turned off.

    fuel_module
Enable fuel calculation module. This module provides vehicle fuel usage data for `Fuel` and other widgets, which returns nothing if turned off.

    battery_module
Enable battery calculation module. This module provides vehicle battery usage data for `Hybrid` and other widgets, which returns nothing if turned off.

    relative_module
Enable relative calculation module. This module provides vehicle relative data for `Relative` and `Radar` widgets, which returns nothing if turned off.

    hover_color_1, hover_color_2
Define color of hover cover when mouse cursor is above widget (when not locked).

    transparent_color
Define global transparent background color. Default value is `"#000002"`. This setting is meant to be used by none-Windows platform where transparent background color is not supported, and user may customize a substitute color.


## Brake
    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    temp_unit
2 unit types are available: `0` = Celsius, `1` = Fahrenheit

    inner_gap
Set inner gap (screen pixel) of each temperature value, only accept integer, `1` = 1 pixel.

    color_swap_temperature
Swap heat map color between font & background color.

    show_degree_sign
Set `true` to show degree sign for each temperature value.

    leading_zero
Set amount leading zeros for each temperature value. Default is `2`. Minimum value is limited to `1`.

    show_average
Show average brake temperature calculated from a full lap.

    highlight_duration
Set duration (seconds) for highlighting average brake temperature from previous lap after crossing start/finish line. Default value is `5` seconds.


## Cruise
    show_track_clock
Show current in-game clock time of the circuit.

    track_clock_time_scale
Set time multiplier for time-scaled session. Default value is `1`, which matches "Time Scale: Normal" setting in-game.

    track_clock_format
Set track clock format string. To show seconds, add `%S`, such as `"%H:%M:%S %p"`. See [link](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) for full list of format codes.

    show_compass
Show compass directions with three-figure bearings that matches game's cardinal directions.

    show_elevation
Show elevation difference in game's coordinate system.

    elevation_unit
2 unit types are available: `0` = meter, `1` = feet.

    show_odometer
Show odometer that displays total driven distance of local player. 

    odometer_unit
2 unit types are available: `0` = kilometer, `1` = mile.

    meters_driven
This value holds the total distance(meters) that local player has driven. Accept manual editing.


## Deltabest
    layout
2 layouts are available: `0` = delta bar above deltabest text, `1` = delta bar below deltabest text.

    color_swap
Swap time gain & loss color between font & background color.

    show_delta_bar
Show visualized delta bar.

    bar_length_scale, bar_height_scale
Scale delta bar length & height, accepts decimal place.

    bar_display_range
Set max display range (gain or loss) for delta bar, accepts decimal place.


## DRS
    font_color_activated, bkg_color_activated
Set color when DRS is activated by player.

    font_color_allowed, bkg_color_allowed
Set color when DRS is allowed but not yet activated by player.

    font_color_available, bkg_color_available
Set color when DRS is available but current disallowed to use.

    font_color_not_available, bkg_color_not_available
Set color when DRS is unavailable for current track or car.


## Engine
    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_temperature
Show oil & water temperature.

    temp_unit
2 unit types are available: `0` = Celsius, `1` = Fahrenheit

    overheat_threshold_oil, overheat_threshold_water
Set temperature threshold for oil & water overheat color indicator, unit in Celsius.

    warning_color_overheat
Set oil & water overheat color indicator.

    show_turbo_pressure
Show turbo pressure.

    turbo_pressure_unit
3 unit types are available: `0` = bar, `1` = psi, `2` = kPa.

    show_rpm
Show engine RPM.


## Flag
    layout
2 layouts are available: `0` = horizontal layout, `1` = vertical layout.

    show_pit_timer
Show pit timer, and total amount time spent in pit after exit pit.

    pit_time_highlight_duration
Set highlight duration for total amount time spent in pit after exit pit.

    show_low_fuel
Show low fuel indicator when fuel level is below certain amount value.

    low_fuel_for_race_only
Only show low fuel indicator during race session.

    low_fuel_volume_threshold
Set fuel volume threshold to show low fuel indicator when total amount of remaining fuel is equal or less than this value. This value takes consideration from `fuel_unit` setting of Fuel Widget. For example, if `fuel_unit` is set to gallon, then this value should also be set using gallon unit. The purpose of this setting is to limit low fuel warning when racing on lengthy tracks, where fuel tank may only hold for a lap or two. Default value is `20`.

    low_fuel_lap_threshold
Set amount lap threshold to show low fuel indicator when total completable laps of remaining fuel is equal or less than this value. Default value is `2` laps before running out of fuel.

    show_speed_limiter
Show speed limiter indicator.

    speed_limiter_text
Set custom pit speed limiter text which shows when speed limiter is engaged. 

    show_yellow_flag
Show yellow flag indicator of current & next sectors.

    yellow_flag_for_race_only
Only show yellow flag indicator during race session.

    show_blue_flag
Show blue flag indicator with timer.

    blue_flag_for_race_only
Only show blue flag indicator during race session.

    show_startlights
Show race start lights indicator with light frame number for standing-type start.

    red_lights_text
Set custom text for red lights. 

    green_flag_text
Set custom text for green flag. 

    green_flag_duration
Set display duration(seconds) for green flag text before it disappears. Default value is `3`.

    show_start_countdown
Show race start countdown timer for standing-type start. 


## Force
    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_g_force
Show longitudinal & lateral G force with direction indicator.

    show_downforce_ratio
Show front vs rear downforce ratio. 50% means equal downforce; higher than 50% means front has more downforce.


## Fuel
    bkg_color_low_fuel
Set low fuel color indicator, which changes widget background color when there is just 2 laps of fuel left.

    fuel_unit
2 unit types are available: `0` = liters, `1` = gallons. This setting affects all widgets that use fuel data.

    low_fuel_lap_threshold
Set amount lap threshold to show low fuel indicator when total completable laps of remaining fuel is equal or less than this value. Default value is `2` laps before running out of fuel.


## Gear
    layout
2 layouts are available: `0` = horizontal layout, `1` = vertical layout.

    speed_unit
3 unit types are available: `0` = KPH, `1` = MPH, `2` = m/s.

    show_speed_limiter
Show speed limiter indicator.

    speed_limiter_text
Set custom pit speed limiter text which shows when speed limiter is engaged. 

    show_rpm_bar
Show a RPM bar at bottom of gear widget, which moves when RPM reaches range between safe & max RPM.

    rpm_bar_gap
The gap between RPM bar & gear widget, in pixel.

    rpm_bar_height
RPM bar height, in pixel.

    rpm_bar_edge_height
A visible thin edge line, in pixel, set `0` to hide this line.

    rpm_safe_multiplier
This value multiplies max RPM value, which sets a relative safe RPM range for RPM color indicator (changes gear widget background color upon reaching this RPM value).

    rpm_warn_multiplier
This value multiplies max RPM value, which sets a relative near-max RPM range for RPM color indicator.

    neutral_warning_speed_threshold, neutral_warning_time_threshold
Set speed/time threshold value for neutral gear color warning, which activates color warning when speed & time-in-neutral is higher than threshold. Speed unit in meters per second, default value is `28`. Time unit in seconds, default value is `0.3` seconds.

    bkg_color_rpm_over_rev
This sets the color for over-rev and neutral-gear warning indicator.


## Hybrid
    show_battery_charge
Show percentage available battery charge.

    show_battery_drain
Show percentage battery charge drained in current lap.

    show_battery_regen
Show percentage battery charge regenerated in current lap.

    show_boost_motor_temp
Show boost motor temperature with customizable unit & overheating indicator.

    show_boost_water_temp
Show boost motor cooler water temperature with customizable unit & overheating indicator.

    show_boost_motor_rpm
Show boost motor RPM.

    show_boost_motor_torque
Show boost motor torque.

    show_boost_motor_state
Show boost motor activation timer.

    overheat_threshold_motor, overheat_threshold_water
Set temperature threshold for boost motor & water overheat color indicator, unit in Celsius.

    low_battery_threshold
Set percentage threshold for low battery charge warning indicator.

    freeze_duration
Set auto-freeze duration (seconds) for previous lap drained/regenerated battery charge display. Default value is `5` seconds.


## Instrument
    icon_size
Set size of instrument icon in pixel. Minimum value is limited to `16`.

    layout
2 layouts are available: `0` = horizontal layout, `1` = vertical layout.

    warning_color_*
Set warning color for each icon, which shows when conditions are met.

    show_headlights
Show Headlights state.

    show_ignition
Show Ignition & Starter state.

    show_clutch
Show Auto-Clutch state.

    show_wheel_lock
Show Wheel Lock state.

    show_wheel_slip
Show Wheel Slip state.

    wheel_lock_threshold
Set percentage threshold for triggering wheel lock warning under braking. `0.2` means 20% of tyre slip ratio.

    wheel_slip_threshold
Set percentage threshold for triggering wheel slip warning. `0.1` means 10% of tyre slip ratio.

    wheel_radius_front, wheel_radius_rear
Set radius for front and rear wheels, which is used to calculate tyre slip ratio. Manual editing is not required, as this value will be automatically calculated based on a special algorithm after player has completed a full lap, and will be auto-saved to `.JSON` file.

    minimum_speed
Set minimum speed threshold before APP records and calculates wheel radius samples. Default value is `16.5` (m/s),

    minimum_samples
Set minimum number of radius samples that required for calculating average wheel radius. Default value is `400`. Minimum value is limited to `100`.


## P2P
    show_battery_charge
Show percentage available battery charge.

    show_boost_motor_state
Show boost motor activation timer.

    activation_threshold_gear
Set minimum gear threshold for P2P ready indicator.

    activation_threshold_speed
Set minimum speed threshold for P2P ready indicator, unit in KPH.

    minimum_activation_time_delay
Set minimum time delay between each P2P activation, unit in seconds.

    maximum_activation_time_per_lap
Set maximum P2P activation time per lap, unit in seconds.


## Pedal
    bar_length_scale, bar_width_scale
Scale pedal bar length & width, accepts decimal place.

    full_pedal_height
This is the indicator height when pedal reaches 100% travel, value in pixel.

    show_brake_pressure
Show brake pressure changes applied on all wheels, which auto scales with max brake pressure and indicates amount brake released by ABS on all wheels. This option is enabled by default, which replaces game's filtered brake input that cannot show ABS.

    show_ffb_meter
This enables Force Feedback meter.

    ffb_clipping_color
Set Force Feedback clipping color.


## Pressure
    show_tyre_pressure
Show tyre pressure of each wheel.

    tyre_pressure_unit
3 unit types are available: `0` = kPa, `1` = psi, `2` = bar.

    show_tyre_load
This enables tyre Load display.

    show_tyre_load_ratio
Show percentage ratio of tyre load between each and total tyre load. Set `false` to show individual tyre load in Newtons.

    show_brake_pressure
Show percentage brake pressure of each wheel.


## Radar
    radar_radius
Set the radar display area by radius(unit meter). Default value is `25` meters. Minimum value is limited to `5`.

    radar_scale
Sets global scale of radar display. Default value is `0.6`, which is 60% of original size.

    vehicle_length, vehicle_width
Set vehicle overall size (length & width), value in meters.

    bkg_color
Set radar background color. Default value is `"#000002"`, which makes background fully transparent.

    player_color
Set player vehicle color. Default value is `"#000002"`, which makes background fully transparent.

    player_outline_color, player_outline_width
Set outline color & width of player vehicle.

    opponent_color
Set opponent vehicle color.

    opponent_color_laps_ahead, opponent_color_laps_behind
Set color for opponent vehicle that is laps ahead or behind player vehicle.

    auto_hide
Auto hides radar display when no nearby vehicles.

    auto_hide_time_threshold
Set amount time(unit second) before triggering auto hide. Default value is `1` second.

    minimum_auto_hide_distance
Set minimum straight line distance(unit meter) before triggering auto hide. Set `-1` value to auto scale with `radar_radius` value. Default value is `-1`.

    show_center_mark
Show center mark on radar.

    center_mark_radius
Set center mark size by radius(unit meter).

    show_distance_circle
Show distance circles on radar for distance reference.

    distance_circle_1_radius, distance_circle_2_radius
Set circle size by radius(unit meter). Circle will not be displayed if radius is bigger than `radar_radius`.

    additional_vehicles_front, additional_vehicles_behind
Set additional visible vehicles. Each value is limited to a maximum of 60 additional vehicles (for a total of 120 additional vehicles). Default value is `4`.


## Relative
    font_color_laps_ahead, font_color_laps_behind
Set font color for opponent vehicle that is laps ahead or behind player vehicle.

    driver_name_mode
Set driver name display mode. Default value is `0`, which displays driver name. Set to `1` to display vehicle(livery) name. Set to `2` to display both driver name & vehicle name combined.

    bar_driver_name_width
Set drive name display width, value in chars, such as 18 = 18 chars.

    show_laptime
Show driver's last laptime.

    show_class
Show vehicle class categories. Class name & color are fully customizable, by editing `classes.json`.

First, find full class name of a vehicle, this can be done by a few ways:
* Looking at laptime data file located in `deltabest` folder, see `README.txt` in `deltabest` folder.
* Looking at class section of a mod's VEH file in MAS
* Increase `bar_class_name_width` value to reveal full class name.

Then, replace `WriteMatchedNameHere` with the found class name, and change `ReplaceClassNameHere` text to a desired class short name (better keep name less than 4 chars).

Last, set `color code` for the class, save and restart app.

You can add more classes following the JSON format, make sure that second last bracket doesn't have a comma after. Also note that, app will not verify, nor to edit `classes.json` after it was created, so you will have to make sure everything typed in the file is correct.

    bar_class_name_width
Set class name display width, value is in chars, 4 = 4 chars wide.

    bar_time_gap_width
Set time gap display width, value is in chars, 5 = 5 chars wide.

    show_position_in_class
Show driver's position standing in class.

    show_pit_status
Show indicator whether driver is currently in pit.

    pit_status_text
Set custom pit status text which shows when driver is in pit. 

    show_tyre_compound
Show tyre compound index (front/rear).

    tyre_compound_list
Set custom tire compound index letter. One letter corresponds to one compound index. Note: since most vehicle mods don't share a common tire compound types or list order, it is impossible to have a tyre compound letter list that matches every car.

    show_pitstop_count
Show each driver's pitstop count.

    show_pit_request
Show pit request color indicator on pitstop count column.

    show_pit_timer
Show pit timer on last laptime column.

    pit_time_highlight_duration
Set highlight duration for total amount time spent in pit after exit pit.

    hide_vehicle_in_garage_for_race
Hide vehicles that are stored in garage stall during race (for example, DNF or DQ). This option is enabled by default, set to `false` to disable.

    additional_players_front, additional_players_behind
Set additional players shown on relative list. Each value is limited to a maximum of 60 additional players (for a total of 120 additional players). Default value is `0`.


## Sectors
    layout
2 layouts are available: `0` = target & current sectors above deltabest sectors, `1` = deltabest sectors above target & current sectors.

    target_time_mode
Set mode for accumulated target sector time. Set `0` to show theoretical best sector time from session best sectors. Set `1` to show sector time from personal best laptime.

    freeze_duration
Set auto-freeze duration (seconds) for previous sector time display. Default value is `5` seconds.

    always_show_laptime_gap
Set `true` to always show sector/laptime gap bar. Set `false` to show only in freeze duration.

    show_speed
Show speed and session fastest speed.

    speed_unit
3 unit types are available: `0` = KPH, `1` = MPH, `2` = m/s.

    speed_highlight_duration
Set duration (seconds) for highlighting new fastest speed. Default value is `5` seconds.

    show_position_lapnumber
Show local driver position standing & current lap number.

    last_saved_sector_data
Store last auto-saved sector data string of current session, not recommended for manual editing.


## Session
    show_system_clock
Show current system clock time.

    system_clock_format
Set clock format string. To show seconds, add `%S`, such as `"%H:%M:%S %p"`. See [link](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) for full list of format codes.

    show_session_timer
Show session timer, accuracy is limited by 200ms refresh rate of rF2 API.

    show_lapnumber
Show your current lap number & max laps (if available).

    lapnumber_text
Set custom lap number description text. Set `""` to hide text.

    bkg_color_maxlap_warn
Set warning color that shows 1 lap before exceeding max-lap in qualify (or indicates the last lap of a lap-type race).

    show_place
Show your current place against all drivers in a session.


## Steering
    bar_length_scale, bar_height_scale
Scale steering bar length & height, accepts decimal place.

    bar_edge_width
Set left and right edge boundary width.

    show_scale_mark
This enables scale marks on steering bar.

    scale_mark_degree
Set gap between each scale mark in degree. Default is `90` degree. Minimum value is limited to `10` degree.


## Stint
    layout
2 layouts are available: `0` = vertical layout, `1` = reversed vertical layout.

    tyre_compound_list
Set custom tire compound index letter. One letter corresponds to one compound index.

    stint_history_count
Set the number of stint history display. Default is to show `2` most recent stints.

    minimum_stint_threshold_minutes
Set the minimum stint time threshold in minutes for updating stint history. This only affects ESC.


## Suspension
    show_ride_height
Show ride height (millimeter).

    rideheight_offset*
Set ride height offset for bottoming indicator. Value in millimeters, but without decimal place.

    warning_color_bottoming
Set color indicator when car bottoming.

    show_rake_angle
Show rake angle (degree) & rake (millimeter).

    wheelbase
Set wheelbase in millimeters, for used in rake angle calculation.

    warning_color_negative_rake
Set color indicator when negative rake.


## Temperature
    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    temp_unit
2 unit types are available: `0` = Celsius, `1` = Fahrenheit

    inner_gap
Set inner gap (screen pixel) of each temperature value, only accept integer, `1` = 1 pixel.

    color_swap_temperature
Swap heat map color between font & background color.

    ICO_mode
Set full tyre temperature display mode (inner/center/outer). Set `false` to show average temperature instead.

    show_degree_sign
Set `true` to show degree sign for each temperature value.

    leading_zero
Set amount leading zeros for each temperature value. Default is `2`. Minimum value is limited to `1`.

    show_innerlayer
Show tyre inner layer temperature.

    show_tyre_compound
Show tyre compound index (front/rear).

    tyre_compound_list
Set custom tire compound index letter. One letter corresponds to one compound index.


## Timing
    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_session_best
Show current session best laptime from all vehicle classes.

    session_best_from_same_class_only
Show current session best laptime from same vehicle class only.

    show_best
Show personal best laptime.

    show_last
Show personal last laptime.

    show_current
Show personal current laptime.

    show_estimated
Show personal current estimated laptime.

    prefix_*
Set prefix text that displayed beside laptime. Set to `""` to hide prefix text.


## Wear
    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_remaining
Show total remaining tyre in percentage that changes color according to wear.

    show_wear_difference
Show total tyre wear difference of previous lap.

    realtime_wear_difference
Show tyre wear difference of current lap that constantly updated in realtime.

    freeze_duration
Set freeze duration(seconds) for previous lap tyre wear info if `realtime_wear_difference` is enabled.

    show_lifespan
Show estimated tyre lifespan in laps.

    warning_threshold_remaining
Set warning threshold for total remaining tyre in percentage. Default is `30` percent.

    warning_threshold_wear
Set warning threshold for total amount tyre wear of last lap in percentage. Default is `3` percent.

    warning_threshold_laps
Set warning threshold for estimated tyre lifespan in laps. Default is `5` laps.

    font_color_warning
Set warning font color when reaching user defined threshold.


## Weather
    show_percentage_sign
Set `true` to show percentage sign for rain & wetness display.

    show_temperature
Show track & ambient temperature.

    temp_unit
2 unit types are available: `0` = Celsius, `1` = Fahrenheit

    show_rain
Show rain percentage.

    show_wetness
Show surface condition, minimum, maximum, and average wetness.


## Wheel
    show_camber
Show camber (degree).

    show_toe_in
Show toe-in (degree).
