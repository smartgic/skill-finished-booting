# Copyright (C) 2018 zelmon64
# Github - https://github.com/zelmon64

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from mycroft import MycroftSkill
from mycroft.util import play_mp3
import os


class FinishedBootingSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        MycroftSkill.__init__(self)
        self.mp3_file = None

    def initialize(self):
        # Callback when setting changes are detected from home.mycroft.ai
        self.settings_change_callback = self.on_websettings_changed
        self.on_websettings_changed()

    def on_websettings_changed(self):
        self._run()

    def _run(self):
        self.mp3_file = self.settings.get('mp3_file')
        self.add_event("mycroft.skills.initialized", self.handle_boot_finished)
        self.log.debug('add event handle boot finished')
        self.log.debug('mp3 file used: {}'.format(self.mp3_file))

    def handle_boot_finished(self):
        try:
            if self.mp3_file:
                if os.path.isfile(self.mp3_file):
                    play_mp3(self.mp3_file)
            else:
                self.speak_dialog('finished.booting')
            self.log.debug('finished booting')
        except Exception as e:
            self.log.error('unable to handle boot finished notification')
            self.log.debug(e)


def create_skill():
    return FinishedBootingSkill()
