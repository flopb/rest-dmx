import usb  # This is pyusb


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
        self.addFixture("rgb1", 1, 8, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 255, "7": 255, "8": 255})
        self.addFixture("rgb2", 9, 16, {"1": 0, "2": 0, "3": 0, "4": 255, "5": 255, "6": 255, "7": 255, "8": 255})

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

    def setFixtureValues(self, fixture, values):
        for value in values:
            self.fixtures[fixture]["channels"][int(value)] = values[value]

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