"""The optional local boot launcher must stay gated and target only Android 5.1 TVs."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ANDROID = "{http://schemas.android.com/apk/res/android}"


class BootLaunchWiringTest(unittest.TestCase):
    def test_receiver_is_private_and_registered_for_boot(self):
        manifest = ET.parse(ROOT / "launcher/app/src/main/AndroidManifest.xml").getroot()
        permissions = {
            element.get(ANDROID + "name")
            for element in manifest.findall("uses-permission")
        }
        self.assertIn("android.permission.RECEIVE_BOOT_COMPLETED", permissions)

        application = manifest.find("application")
        receiver = next(
            element for element in application.findall("receiver")
            if element.get(ANDROID + "name") == ".BootLaunchReceiver"
        )
        self.assertEqual("false", receiver.get(ANDROID + "exported"))
        self.assertEqual("@bool/launch_after_boot", receiver.get(ANDROID + "enabled"))
        actions = {
            element.get(ANDROID + "name")
            for element in receiver.findall("intent-filter/action")
        }
        self.assertEqual({"android.intent.action.BOOT_COMPLETED"}, actions)

    def test_launch_is_off_by_default_and_opted_in_only_for_api_22_builds(self):
        base = ET.parse(ROOT / "launcher/app/src/main/res/values/config.xml").getroot()
        launch_after_boot = next(
            element for element in base.findall("bool")
            if element.get("name") == "launch_after_boot"
        )
        self.assertEqual("false", (launch_after_boot.text or "").strip())

        legacy = ET.parse(ROOT / "launcher/app/src/main/res/values-v22/config.xml").getroot()
        legacy_launch = next(
            element for element in legacy.findall("bool")
            if element.get("name") == "launch_after_boot"
        )
        self.assertEqual("true", (legacy_launch.text or "").strip())


if __name__ == "__main__":
    unittest.main()
