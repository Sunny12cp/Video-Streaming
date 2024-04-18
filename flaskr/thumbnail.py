import subprocess


def make_thumbnail(infile, outfile) -> bool:
    returnCode = subprocess.call(
        [
            "ffmpeg",
            "-loglevel",
            "quiet",
            "-i",
            infile,
            "-ss",
            "00:00:00.000",
            "-vframes",
            "1",
            outfile,
        ]
    )

    if returnCode == 0:
        return True
    else:
        return False
