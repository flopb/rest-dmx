import usb  # This is pyusb
import copy

class uDMX():
    SingleChannelModeFlag = 1
    MultiChannelModeFlag = 2
    fixtures = {}

    def __init__(self):
        self.vid = 0x16c0
        self.pid = 0x05dc
        self.dev = None
        self.channel_mode = "single"  # single = 1 or multi = 2

        self.dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
        if self.dev is None:
            raise ResourceWarning("uDMX device was not found")

        self.bmRequestType = usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE | usb.util.CTRL_OUT

        self.initFixtures()

    def initFixtures(self):

        self.addFixture("fog", 1, 1, {"1": 0})
        self.addFixture("uv", 2, 8, {"1": 0, "2": 255, "3": 255, "4": 255, "5": 0, "6": 0, "7": 0})
        self.addFixture("rgb1", 49, 56, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0})
        self.addFixture("rgb2", 17, 24, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 255, "7": 0, "8": 0})
        self.addFixture("rgb3", 65, 72, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 255, "7": 255, "8": 255})
        self.addFixture("rgb4", 9, 16, {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0})
        self.addFixture("rgb5", 33, 40, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 0, "6": 255, "7": 0, "8": 0})
        self.addFixture("rgb6", 25, 32, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 0, "7": 0, "8": 0})
        self.addFixture("rgb8", 41, 48, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 255, "7": 255, "8": 255})
        self.addFixture("rgb7", 57, 64, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 255, "7": 255, "8": 255})

    def resetFixtures(self):
        self.initFixtures()
        self.update()

    def addFixture(self, name, ch_start, ch_end, default_values=[]):
        self.fixtures[name] = {}
        i = 1
        self.fixtures[name]["channels"] = {}
        for value in range(ch_start, (ch_end + 1)):
            self.fixtures[name]["channels"][i] = default_values[str(i)] if i <= len(default_values) else 0
            i = i + 1

        self.fixtures[name]["start_channel"] = ch_start
        self.fixtures[name]["end_channel"] = ch_end
        self.update()

    def get_all_fixtures(self):
        all_fixtures = []
        for fixture in self.fixtures:
            all_fixtures.append(fixture)

        return all_fixtures

    def get_snapshot(self):
        all_fixtures = {}
        for fixture in self.fixtures:
            all_fixtures[fixture] = copy.deepcopy(self.fixtures[fixture]["channels"])

        return all_fixtures

    def restore_snapshot(self, snapshot):
        for fixture in snapshot:
            self.setFixtureValues(fixture, snapshot[fixture])
        self.update()

    def setFixtureValues(self, fixture, values):
        for value in values:
            self.fixtures[fixture]["channels"][int(value)] = values[value]

    def getFixtureValues(self, fixture):
        return self.fixtures[fixture]["channels"]

    def update(self, fixtures = []):
        for fixture in self.fixtures:
            if len(fixtures) == 0 or fixture in fixtures:
                #print("Fixture: ", fixture)
                #print("Start-Channel: ", self.fixtures[fixture]["start_channel"])
                #print("Channels: ", self.fixtures[fixture]["channels"])
                #print("Values: ", list(self.fixtures[fixture]["channels"].values()))
                self.setDMX(self.fixtures[fixture]["start_channel"], list(self.fixtures[fixture]["channels"].values()))

    def setDMX(self, channel, value):
        channel = channel - 1
        if type(value) is int:
            n = self.dev.ctrl_transfer(self.bmRequestType, self.SingleChannelModeFlag, wValue=value, wIndex=channel,
                                       data_or_wLength=1)
        elif type(value) is list:
            channel_values = bytearray(value)
            n = self.dev.ctrl_transfer(self.bmRequestType, self.MultiChannelModeFlag, wValue=len(channel_values), wIndex=channel, data_or_wLength=channel_values)
        else:
            raise ValueError("The value can be an integer or a list.")