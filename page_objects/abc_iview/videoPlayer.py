import logging
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from page_objects.abc_iview.base_ui import BaseUI
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadProperties


class VideoPlayerScreen(BaseUI):
    if ReadProperties.get_platform_name() == 'ios':
        close_btn = (AppiumBy.ACCESSIBILITY_ID, "closeButton")
        video_title = (AppiumBy.ACCESSIBILITY_ID, "videoTitle")
        rewind_30s_btn = (AppiumBy.ACCESSIBILITY_ID, 'rewind30Button')
        play_pause_btn = (AppiumBy.ACCESSIBILITY_ID, 'playPauseButton')
        caption_btn = (AppiumBy.ACCESSIBILITY_ID, 'captionsButton')
        elapsed_time = (AppiumBy.ACCESSIBILITY_ID, 'elapsedTime')
        duration_ele = (AppiumBy.ACCESSIBILITY_ID, "duration")
        scrubber_btn = (AppiumBy.ACCESSIBILITY_ID, 'scrubber')
        autoplay_title = (AppiumBy.ACCESSIBILITY_ID, 'remainingTimeTitle')
        autoplay_btn = (AppiumBy.ACCESSIBILITY_ID, 'autoplayButton')
        next_video_title = (AppiumBy.ACCESSIBILITY_ID, 'next_video_title')
        autoplay_close_btn = (AppiumBy.ACCESSIBILITY_ID, 'autoPlayCloseButton')
    else:
        close_btn = (AppiumBy.ACCESSIBILITY_ID, "Exit Player")
        video_title = (AppiumBy.ID, 'au.net.abc.iview:id/playerEpisodeDetails')
        android_play_btn = (AppiumBy.ACCESSIBILITY_ID, 'Play')
        android_pause_btn = (AppiumBy.ACCESSIBILITY_ID, 'Pause')
        caption_btn = (AppiumBy.ACCESSIBILITY_ID, 'Closed Captions')
        elapsed_time = (AppiumBy.ID, 'au.net.abc.iview:id/exo_position')
        duration_ele = (AppiumBy.ID, 'au.net.abc.iview:id/exo_duration')
        scrubber_btn = (AppiumBy.ID, 'au.net.abc.iview:id/exo_progress')
        autoplay_title = (AppiumBy.ID, 'au.net.abc.iview:id/autoplay_title')
        autoplay_btn = (AppiumBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView')
        next_video_title = (AppiumBy.ID, 'au.net.abc.iview:id/autoplay_desc')
        autoplay_close_btn = (AppiumBy.ID, 'au.net.abc.iview:id/autoplay_close')

    def __init__(self, app):
        super().__init__(app)

    def click_on_close_btn(self):
        self.click(locator=self.close_btn)

    @staticmethod
    def get_starting_pos():
        value = 70
        if ReadProperties.get_platform_name() == 'Android':
            value = 238
        return value

    @staticmethod
    def get_ending_pos():
        value = 333
        if ReadProperties.get_platform_name() == 'Android':
            value = 866
        return value

    @staticmethod
    def get_at_25_pos():
        value = 125
        if ReadProperties.get_platform_name() == 'Android':
            value = 380
        return value

    @staticmethod
    def get_at_50_pos():
        value = 198
        if ReadProperties.get_platform_name() == 'Android':
            value = 545
        return value

    @staticmethod
    def get_at_75_pos():
        value = 272
        if ReadProperties.get_platform_name() == 'Android':
            value = 740
        return value

    @staticmethod
    def get_at_95_pos():
        value = 320
        if ReadProperties.get_platform_name() == 'Android':
            value = 850
        return value

    @staticmethod
    def set_player_y_pos():
        """
        Set the position of y coordinate base on device type
        """
        log = LogGen.loggen()
        device = ReadProperties.get_device_name()
        try:
            match device:
                case 'iPhone 14 Pro Simulator':
                    y_pos = 790
                    log.info(f"Setting y_pos as {device}: {y_pos}")
                    return y_pos
                case 'Pixel_5_API_33':
                    y_pos = 2181
                    log.info(f"Setting y_pos as {device}: {y_pos}")
                    return y_pos
        except Exception as error:
            Exception("Unable to set y coordinate, check device name or case statement", error)

    @staticmethod
    def get_profile_name():
        return "VideoTest"

    def get_profile_icon(self):
        name = self.get_profile_name()
        if ReadProperties.get_platform_name() == 'ios':
            video_test_profile_icon = (AppiumBy.XPATH, f'//*[contains(@name,"{name}")]')
        else:
            pass
        return video_test_profile_icon

    """
    VERIFY KEYWORDS -
    For any methods that involves with validating if visible, or equals, any validation methods.
    """

    def verify_video_title_is_displayed(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wait_for_player(seconds=1)
            self.wake_player()
            return self.is_visible(self.video_title)
        else:
            self.wait_visible(self.video_title)
            return self.is_visible(self.video_title)

    def verify_close_btn_is_displayed(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wait_for_player(seconds=1)
            self.wake_player()
            return self.is_visible(self.close_btn)
        else:
            self.wait_visible(self.close_btn)
            return self.is_visible(self.close_btn)

    def verify_rewind_30s_btn(self):
        self.wait_visible(self.rewind_30s_btn)
        return self.is_visible(self.rewind_30s_btn)

    def verify_play_pause_btn(self):
        self.wait_visible(self.play_pause_btn)
        return self.is_visible(self.play_pause_btn)

    def verify_caption_btn(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wait_for_player(seconds=1)
            self.wake_player()
            return self.is_visible(self.caption_btn)
        else:
            self.wait_visible(self.caption_btn)
            return self.is_visible(self.caption_btn)

    def verify_elapsed_time(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wait_for_player(seconds=1)
            self.wake_player()
            return self.is_visible(self.elapsed_time)
        else:
            self.wait_visible(self.elapsed_time)
            return self.is_visible(self.elapsed_time)

    def verify_android_play_btn(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wake_player()
            return self.is_visible(self.android_play_btn)
        else:
            self.logger.warning("verify_pause_btn is for Android only, this method is being called in a non-android "
                                "test")

    def verify_android_pause_btn(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wait_for_player(seconds=1)
            self.wake_player()
            return self.is_visible(self.android_pause_btn)
        else:
            self.logger.warning("verify_pause_btn is for Android only, this method is being called in a non-android "
                                "test")

    def verify_duration_ele(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wait_for_player(seconds=1)
            self.wake_player()
            return self.is_visible(self.duration_ele)
        else:
            self.wait_visible(self.duration_ele)
            return self.is_visible(self.duration_ele)

    def verify_scrubber_btn(self):
        if ReadProperties.get_platform_name() == 'Android':
            self.wait_for_player(seconds=1)
            self.wake_player()
            return self.is_visible(self.scrubber_btn)
        else:
            self.wait_visible(self.scrubber_btn)
            return self.is_visible(self.scrubber_btn)

    def verify_autoplay_title(self):
        self.wait_visible(self.autoplay_title)
        return self.is_visible(self.autoplay_title)

    def verify_autoplay_btn(self):
        self.wait_visible(self.autoplay_btn)
        return self.is_visible(self.autoplay_btn)

    def verify_next_video_title(self):
        self.wait_visible(self.next_video_title)
        return self.is_visible(self.next_video_title)

    def verify_autoplay_close_btn(self):
        self.wait_visible(self.autoplay_close_btn)
        return self.is_visible(self.autoplay_close_btn)

    """
    INTERACTION KEYWORDS -
    For any onscreen movement manipulation, clicking, tapping, swiping methods
    """

    def wait_for_player(self, seconds: int = 21):
        """
        Wait for the preroll video the ends, usually a preroll will only last 15 seconds, plus classification 5 seconds.
        Adding one second for safety
        :param seconds:
        :return: None
        """
        sleep(seconds)

    def wake_player(self):
        """
        Tap on the screen to reveal player controls.
        This is a tap on the center of the screen method.
        :return:
        """
        self.utils.tap_center()

    def tap_pause_play_btn(self):
        """
        Uses the utility click method to tap on the player/pause button, they both share the same locator
        :return:
        """
        self.click(self.play_pause_btn)

    def tap_android_play_btn(self):
        self.click(self.android_play_btn)

    def tap_android_pause_btn(self):
        self.click(self.android_pause_btn)

    def perform_seek(self, seek_to: int, seek_from: int, resume_after_seek: bool = False, ):
        """
        Seeks the progress by using the seek_to and seek_from value from PlayerSeekPos class,
        to prevent scrubber from moving, this method pauses the video first, then perform.
        By default the method will not unpause the player, because this will make the controls to become hidden.
        :param seek_from:
        :param seek_to:
        :param resume_after_seek: True or False
        :return: None
        """
        # Press pause to stop the video from playing before seeking
        if ReadProperties.get_platform_name() == 'Android':
            if not self.verify_android_pause_btn():
                self.wait_for_player(seconds=2)
                self.wake_player()
                self.tap_android_pause_btn()
            else:
                self.tap_android_pause_btn()
        else:
            self.tap_pause_play_btn()

        self.seek_progress_to_point(seek_from=seek_from, seek_to=seek_to, seek_speed=150)
        if resume_after_seek is True:
            if ReadProperties.get_platform_name() == 'ios':
                self.tap_pause_play_btn()
            else:
                if not self.verify_android_play_btn():
                    self.wake_player()
                    self.tap_android_play_btn()
                else:
                    self.tap_android_play_btn()

    def get_current_duration(self):
        """
        Get the current duration base on the value of 'elapsed_time' and returns it in seconds (int)
        :return:
        """
        if ReadProperties.get_platform_name() == 'ios':
            current_duration_value = self.utils.get_attribute(self.elapsed_time, 'value')
            current_duration_text = self.convert_timestamp_str_to_seconds(value=current_duration_value)
            current_duration_num = int(current_duration_text)
            return current_duration_num
        else:
            if not self.verify_duration_ele():
                self.wake_player()
            current_duration_value = self.utils.get_attribute(self.elapsed_time, 'text')
            return current_duration_value

    @staticmethod
    def convert_timestamp_str_to_seconds(value: str):
        """
        Converts the iOS player timestamp into seconds, it first convert hours, then minutes, then seconds,
        finally adding all together before returning
        :param value: usually the player elasped_time value
        :return: total_in_seconds
        """
        cut_words_sep = ","
        cut_words = value.split(cut_words_sep, 1)[1]

        hour_sep = "hour"
        minutes_sep = "minutes"
        seconds_sep = "seconds"

        seconds_in_hours = 0
        seconds_in_minutes = 0
        total_seconds = 0
        if hour_sep in value:
            hours_num = cut_words.split(hour_sep, 1)[0]
            hours_to_min = int(hours_num) * 60
            seconds_in_hours = hours_to_min * 60
        if minutes_sep in value:
            if hour_sep in value:
                mins = cut_words.split(minutes_sep, 1)[0]
                mins_num = mins.split(hour_sep, 1)[1]
                seconds_in_minutes = int(mins_num) * 60
            else:
                mins = cut_words.split(minutes_sep, 1)[0]
                seconds_in_minutes = int(mins) * 60
        if seconds_sep in value:
            if minutes_sep in value:
                seconds = cut_words.split(seconds_sep, 1)[0]
                print(seconds)
                seconds_num = seconds.split(minutes_sep, 1)[1]
                total_seconds = int(seconds_num)
            else:
                seconds = cut_words.split(seconds_sep, 1)[0]
                total_seconds = int(seconds)

        total_in_seconds = seconds_in_hours + seconds_in_minutes + total_seconds
        return total_in_seconds

    def seek_progress_to_point(self, seek_from: int, seek_to: int, seek_speed=250):
        """
        Move the scrubber to the seek_point location, the method will locate the scrubber before seeking.
        max_seekbar_pos is a constant variable base on the device dimension (example: iPhone 8 is 375)
        off_set is the off set area between the player progress bar and the edge of the screen,
        also base on device dimension

        :param seek_from:
        :param seek_to:
        :param seek_speed: int
        :return:
        """
        y_coordinate = self.set_player_y_pos()
        start_seek_btn_x_y = {"x": seek_from, "y": y_coordinate}
        end_seek_btn_x_y = {"x": seek_to, "y": y_coordinate}
        LogGen.loggen().info(f"Seeking with these value, {start_seek_btn_x_y}  ///and/// {end_seek_btn_x_y}")
        self.utils.Swipe_by_coord(start_x=start_seek_btn_x_y["x"], start_y=start_seek_btn_x_y["y"],
                                  end_x=end_seek_btn_x_y["x"], end_y=end_seek_btn_x_y["y"], velocity=seek_speed
                                  )
