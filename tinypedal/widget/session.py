#  TinyPedal is an open-source overlay application for racing simulation.
#  Copyright (C) 2022  Xiang
#
#  This file is part of TinyPedal.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Session Widget
"""

import time
import tkinter as tk
import tkinter.font as tkfont

from .. import calculation as calc
from .. import readapi as read_data
from ..base import Widget, MouseEvent

WIDGET_NAME = "session"


class Draw(Widget, MouseEvent):
    """Draw widget"""

    def __init__(self, config):
        # Assign base setting
        Widget.__init__(self, config, WIDGET_NAME)

        # Config size & position
        self.geometry(f"+{self.wcfg['position_x']}+{self.wcfg['position_y']}")

        bar_padx = self.wcfg["font_size"] * self.wcfg["text_padding"]
        bar_gap = self.wcfg["bar_gap"]

        # Config style & variable
        font_session = tkfont.Font(family=self.wcfg["font_name"],
                                   size=-self.wcfg["font_size"],
                                   weight=self.wcfg["font_weight"])

        column_sysc = self.wcfg["column_index_system_clock"]
        column_sest = self.wcfg["column_index_session_timer"]
        column_lapn = self.wcfg["column_index_lapnumber"]
        column_plac = self.wcfg["column_index_place"]

        # Draw label
        bar_style = {"bd":0, "height":1, "padx":bar_padx, "pady":0, "font":font_session}

        if self.wcfg["show_system_clock"]:
            self.bar_clock = tk.Label(self, bar_style, text="CLOCK", width=5,
                                      fg=self.wcfg["font_color_system_clock"],
                                      bg=self.wcfg["bkg_color_system_clock"])
            self.bar_clock.grid(row=0, column=column_sysc, padx=(0, bar_gap), pady=0)

        if self.wcfg["show_session_timer"]:
            self.bar_session = tk.Label(self, bar_style, text="SESSION", width=10,
                                           fg=self.wcfg["font_color_session_timer"],
                                           bg=self.wcfg["bkg_color_session_timer"])
            self.bar_session.grid(row=0, column=column_sest, padx=(0, bar_gap), pady=0)

        if self.wcfg["show_lapnumber"]:
            self.bar_lapnumber = tk.Label(self, bar_style, text="LAPS", width=4,
                                          fg=self.wcfg["font_color_lapnumber"],
                                          bg=self.wcfg["bkg_color_lapnumber"])
            self.bar_lapnumber.grid(row=0, column=column_lapn, padx=(0, bar_gap), pady=0)

        if self.wcfg["show_place"]:
            self.bar_place = tk.Label(self, bar_style, text="PLACE", width=5,
                                      fg=self.wcfg["font_color_place"],
                                      bg=self.wcfg["bkg_color_place"])
            self.bar_place.grid(row=0, column=column_plac, padx=(0, bar_gap), pady=0)

        # Last data
        self.last_clock = None
        self.last_time_left = None
        self.last_lap_into = None
        self.last_plr_place = None

        # Start updating
        self.update_data()

        # Assign mouse event
        MouseEvent.__init__(self)

    def update_data(self):
        """Update when vehicle on track"""
        if read_data.state() and self.wcfg["enable"]:

            # Read session data
            time_left, lap_into, lap_num, lap_total, plr_place = read_data.session()

            # System Clock
            if self.wcfg["show_system_clock"]:
                clock = time.strftime(self.wcfg["system_clock_format"])
                self.update_clock(clock, self.last_clock)
                self.last_clock = clock

            # Session timer
            if self.wcfg["show_session_timer"]:
                self.update_session_timer(time_left, self.last_time_left)
                self.last_time_left = time_left

            # Lap number
            if self.wcfg["show_lapnumber"]:
                self.update_lapnumber(lap_into, self.last_lap_into, lap_num, lap_total)
                self.last_lap_into = lap_into

            # Driver place & total vehicles
            if self.wcfg["show_place"]:
                self.update_place(plr_place, self.last_plr_place)
                self.last_plr_place = plr_place

        # Update rate
        self.after(self.wcfg["update_delay"], self.update_data)

    # GUI update methods
    def update_clock(self, curr, last):
        """System Clock"""
        if curr != last:
            self.bar_clock.config(text=f"{curr}", width=len(curr))

    def update_session_timer(self, curr, last):
        """Session timer"""
        if curr != last:
            self.bar_session.config(text=calc.sec2sessiontime(max(curr, 0)))

    def update_lapnumber(self, curr, last, lap_num, lap_total):
        """Lap number"""
        if curr != last:
            if lap_total > 100000:  # none-lap race type
                lap_num_text = f"{self.wcfg['lapnumber_text']}{lap_num}.{curr:02.0f}"
            else:
                lap_num_text = f"{self.wcfg['lapnumber_text']}{lap_num}.{curr:02.0f}/{lap_total}"

            self.bar_lapnumber.config(text=lap_num_text,
                                      width=len(lap_num_text),
                                      bg=self.maxlap_warning(lap_num - lap_total))

    def update_place(self, curr, last):
        """Driver place & total vehicles"""
        if curr != last:
            self.bar_place.config(text=f"{curr[0]:02.0f}/{curr[1]:02.0f}")

    # Additional methods
    def maxlap_warning(self, lap_diff):
        """Max lap warning"""
        if lap_diff >= -1:
            return self.wcfg["bkg_color_maxlap_warn"]
        return self.wcfg["bkg_color_lapnumber"]
