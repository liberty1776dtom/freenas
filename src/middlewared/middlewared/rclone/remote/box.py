from middlewared.rclone.base import BaseRcloneRemote
from middlewared.schema import Str


class BoxRcloneRemote(BaseRcloneRemote):
    name = "BOX"
    title = "Box"

    rclone_type = "box"

    credentials_schema = [
        Str("token", title="Access Token", required=True),
    ]
