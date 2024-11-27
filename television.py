class Television:
    """
    The class is a television that has the basic components:
    -Max/Min volume
    -Max/Min channel
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes the television:
        -The power is set to off by default
        -The television is not muted
        -The television's volume is set to minimum
        -The television's channel is set to minimum
        """
        self.__status = False
        self.__muted = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL


    def power(self) -> None:
        """
        Turns the television on and off:
        -If television is on, it will turn off
        -If the television is off, it will turn on
        """
        self.__status = not self.__status


    def mute(self) -> None:
        """
        Mutes or unmutes the television:
        -If the television is muted, the volume is set to the minimum
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume
            else:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME


    def channel_up(self) -> None:
        """
        Moves the channel on the television up:
        -Moves the television up by one
        -If the channel is higher than the max, it is set to the max
        """
        if self.__status:
            self.__channel += 1
        if self.__channel > Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """
         Moves the channel on the television down:
        -Moves the television down by one
        -If the channel is lower than the min, it is set to the min
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        """
        Moves the volume on the television up:
        -If the television is muted, it is unmuted and increased by 1
        -If the volume is lower than the max volume, it will increase by 1
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
                self.__volume += 1
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self) -> None:
        """
        Moves the volume on the television down:
        -If the television is muted, it is unmuted and decreased by 1
        -If the volume is higher than the min volume, it will decrease by 1
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
                self.__volume -= 1 if self.__volume > Television.MIN_VOLUME else self.__volume
            elif self.__muted == False:
                self.__volume -= 1 if self.__volume > Television.MIN_VOLUME else self.__volume


    def __str__(self) -> str:
        """
        Returns the power, channel, and volume of the television
        -This is in the format of Power = [power], Channel = [channel], Volume = [volume]
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'