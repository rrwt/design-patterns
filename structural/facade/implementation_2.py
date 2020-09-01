"""
Facade pattern simplifying interaction with a complex video conversion framework
"""


class AwesomeConverter:
    def __init__(self, source_file: str) -> None:
        self.source_file = source_file
        self.file_name = "".join(self.source_file.split(".")[:-1])


class Ogg(AwesomeConverter):
    def to_mp4(self) -> str:
        return f"{self.file_name}.mp4"

    def to_mpeg(self) -> str:
        return f"{self.file_name}.mpeg"


class MP4(AwesomeConverter):
    def to_mpeg(self) -> str:
        return f"{self.file_name}.mpeg"

    def to_ogg(self) -> str:
        return f"{self.file_name}.ogg"


class MPEG(AwesomeConverter):
    def to_mp4(self) -> str:
        return f"{self.file_name}.mp4"

    def to_ogg(self) -> str:
        return f"{self.file_name}.ogg"


class VideoConverter:
    """
    Facade
    """

    def __init__(self, source_file: str) -> None:
        self._source_format = source_file.split(".")[-1]
        self._source_file = source_file

        if self._source_format == "ogg":
            self._source = Ogg(self._source_file)
        elif self._source_format == "mp4":
            self._source = MP4(self._source_file)
        elif self._source_format == "mpeg":
            self._source = MPEG(self._source_file)
        else:
            raise ValueError(f"Invalid source format {self._source_format}")

    def convert(self, destination_format: str) -> str:
        if destination_format == "ogg":
            return self._source.to_ogg()
        elif destination_format == "mp4":
            return self._source.to_mp4()
        elif destination_format == "mpeg":
            return self._source.to_mpeg()
        else:
            raise ValueError(f"Conversion to {destination_format} is not supported")


if __name__ == "__main__":
    file_name = "my-awesome-youtube-video.ogg"
    print(f"original file: {file_name}")
    vc = VideoConverter(file_name)
    print(f"new file: {vc.convert('mp4')}")
