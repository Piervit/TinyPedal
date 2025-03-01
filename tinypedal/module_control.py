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
Module control
"""

import time

from .setting import cfg
from .realtime_delta import DeltaTime
from .realtime_battery import Battery
from .realtime_fuel import FuelUsage
from .realtime_relative import RelativeInfo
from .overlay_toggle import OverlayLock, OverlayAutoHide


class ModuleControl:
    """Module control"""

    def __init__(self):
        """Widget list"""
        self.delta_time = DeltaTime(cfg)  # delta module
        self.battery_usage = Battery(cfg)  # battery module
        self.fuel_usage = FuelUsage(cfg)  # fuel module
        self.relative_info = RelativeInfo(cfg)  # relative module
        self.overlay_lock = OverlayLock(cfg)  # overlay lock
        self.overlay_hide = OverlayAutoHide(cfg)  # overlay auto hide

    def start(self):
        """Start module"""
        self.delta_time = DeltaTime(cfg)
        self.battery_usage = Battery(cfg)
        self.fuel_usage = FuelUsage(cfg)
        self.relative_info = RelativeInfo(cfg)
        self.overlay_lock = OverlayLock(cfg)
        self.overlay_hide = OverlayAutoHide(cfg)

        if cfg.overlay["delta_module"]:
            self.delta_time.start()
        if cfg.overlay["fuel_module"]:
            self.fuel_usage.start()
        if cfg.overlay["battery_module"]:
            self.battery_usage.start()
        if cfg.overlay["relative_module"]:
            self.relative_info.start()
        self.overlay_hide.start()

    def is_stopped(self):
        """Check is all module stopped"""
        return all((
                    self.delta_time.stopped,
                    self.battery_usage.stopped,
                    self.fuel_usage.stopped,
                    self.relative_info.stopped,
                    self.overlay_hide.stopped
                    ))

    def stop(self):
        """Stop modules"""
        self.delta_time.running = False
        self.battery_usage.running = False
        self.fuel_usage.running = False
        self.relative_info.running = False
        self.overlay_hide.running = False
        while not self.is_stopped():
            time.sleep(0.01)


module = ModuleControl()
