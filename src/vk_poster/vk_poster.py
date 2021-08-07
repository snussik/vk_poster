import vk_api
import datetime
from typing import Optional


class VK:
    """VK class to post messages to groups
    """

    def __init__(self, token, v, group_short_name) -> None:
        """VK class initialisation

        Args:
            token (str): Token of VK standalone app
            v (float): VK API version
            group_short_name (str): VK group name
        """
        self.token = token
        self.app = vk_api.VkApi(token=self.token)
        self.upload = vk_api.upload.VkUpload(self.app)
        self.v = v
        self.group_id = - \
            self.app.method("groups.getById", {
                            "group_ids": group_short_name})[0]['id']
        self.body = dict(owner_id=self.group_id, from_group=1, v=self.v)

    def quene_msg(self, msg=None, photo=None, quene_time=356, date:Optional[datetime.datetime]=None) -> int:
        """Posting quened message to VK group

        Args:
            msg (str, optional}: Message thath should be posted. Defaults to None.
            photo (str, optional): Link to photo image file. Defaults to None.
            quene_time (int, optional): Number of day quened for posting. Defaults to 356.

        Raises:
            ValueError: You should provide msg or photo data. If both is None then VK API returns error

        Returns:
            int: If posting was ok - returns post id, otherwise - returns -1
        """

        if msg == photo and msg is None:
            raise ValueError(
                f"Message ({msg}) or attachment ({photo}) should be given")

        message_body = {
            **self.body,
            "publish_date": self.get_time(quene_time,date=date),
        }

        if photo is not None:
            message_body.update({"attachments": self.upload_image(photo)})

        if msg is not None:
            message_body.update({"message": msg})

        result = self.app.method("wall.post", message_body)

        if result.get("post_id"):
            return result["post_id"]
        return -1

    def get_time(self, days: int, date:Optional[datetime.datetime]=None) -> float:
        """Returns date in future x days in unixtimestamp format

        Args:
            days (int): Number of days in future from now
            date (datetime.datetime, optional): Exact daytime. Defaults to None

        Returns:
            float: date in future  in unixtimestamp format
        """
        if date is not None:
            return date.timestamp()

        unix_timestamp = datetime.datetime.now(
            datetime.timezone.utc).timestamp()
        return unix_timestamp + (60 * 60 * 24 * days)

    def upload_image(self, img:str ) -> str:
        """Uploading image to VK group

        Args:
            img (str): Path to image file

        Returns:
            str: Link to image in string format: photo123456_123456. More details: https://vk.com/dev/wall.post?params[owner_id]=5284984&params[friends_only]=0&params[from_group]=0&params[message]=test&params[attachments]=photo&params[signed]=0&params[mark_as_ads]=0&params[close_comments]=0&params[mute_notifications]=0&params[v]=5.131
        """

        photo = self.upload.photo_wall(
            photos=img,
            group_id=-self.group_id,
        )
        vk_photo_url = 'photo{}_{}'.format(
            photo[0]['owner_id'], photo[0]['id'])

        return vk_photo_url
