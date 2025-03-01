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
Widget control
"""

import time

from .setting import cfg
from .widget import (
    brake,
    cruise,
    deltabest,
    drs,
    engine,
    flag,
    force,
    fuel,
    gear,
    hybrid,
    instrument,
    p2p,
    pedal,
    pressure,
    radar,
    relative,
    sectors,
    session,
    steering,
    stint,
    suspension,
    temperature,
    timing,
    wear,
    weather,
    wheel
)

WIDGET_PACK = (
    brake,
    cruise,
    deltabest,
    drs,
    engine,
    flag,
    force,
    fuel,
    gear,
    hybrid,
    instrument,
    p2p,
    pedal,
    pressure,
    radar,
    relative,
    sectors,
    session,
    steering,
    stint,
    suspension,
    temperature,
    timing,
    wear,
    weather,
    wheel
)


class WidgetControl:
    """Widget control"""

    def start(self):
        """Start widget"""
        for obj in WIDGET_PACK:
            if cfg.setting_user[obj.WIDGET_NAME]["enable"]:
                # Create widget instance
                setattr(self, f"widget_{obj.WIDGET_NAME}", obj.Draw(cfg))

    @staticmethod
    def close():
        """Close widget"""
        while cfg.active_widget_list:
            for widgets in cfg.active_widget_list:
                widgets.destroy()
                cfg.active_widget_list.remove(widgets)
            time.sleep(0.01)
        print("all widgets closed")

    def toggle(self, name):
        """Toggle widget"""
        for obj in WIDGET_PACK:
            if name == obj.WIDGET_NAME:
                if not cfg.setting_user[obj.WIDGET_NAME]["enable"]:
                    # Create widget instance
                    setattr(self, f"widget_{obj.WIDGET_NAME}", obj.Draw(cfg))
                    # Set True after widget enabled
                    cfg.setting_user[obj.WIDGET_NAME]["enable"] = True
                else:
                    # Get widget instance
                    widget_instance = getattr(self, f"widget_{obj.WIDGET_NAME}")
                    # Set False before widget disabled
                    cfg.setting_user[obj.WIDGET_NAME]["enable"] = False
                    # Remove widget from active list
                    cfg.active_widget_list.remove(widget_instance)
                    # Close widget
                    widget_instance.destroy()
                cfg.save()
                break


wctrl = WidgetControl()
